#!/usr/bin/env python3
"""檢查翻譯是否和繁體中文原文同步。

Check whether translations are in sync with the Traditional Chinese original.

每個翻譯檔的第一行都有來源標記，記錄翻譯時原文的指紋（SHA-256 的前 12 碼）：
Every translated file starts with a source marker that records a fingerprint
(the first 12 hex digits of SHA-256) of the original at translation time:

    <!-- source: zh-TW/2-front-end/04-rtl-and-verilog/README.md | sha: 1a2b3c4d5e6f -->

原文之後只要被修改，指紋就會不同，這個檔案就會被列為「過期」。
If the original changes later, the fingerprint no longer matches and the file
is reported as outdated.

用法 / Usage:
    python3 scripts/check_translations.py              # 檢查所有語言 / all languages
    python3 scripts/check_translations.py en           # 只檢查英文 / English only
    python3 scripts/check_translations.py en --strict  # 有問題時回傳 1 / exit 1 on problems
    python3 scripts/check_translations.py --structure  # 和原文做結構比對 / compare structure with the original

    # 同步完翻譯之後，更新標記中的指紋 / after syncing a translation, update its fingerprint
    python3 scripts/check_translations.py --stamp en/2-front-end/04-rtl-and-verilog/README.md
    python3 scripts/check_translations.py --stamp en   # 整個語言 / a whole language
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE_LANG = "zh-TW"
LANG_DIR_RE = re.compile(r"^[a-z]{2,3}(-[A-Za-z0-9]+)?$")
MARKER_RE = re.compile(r"<!--\s*source:\s*(\S+)\s*\|\s*sha:\s*([0-9a-f]+|pending)\s*-->")


def fingerprint(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(data).hexdigest()[:12]


def source_files() -> list[str]:
    base = ROOT / SOURCE_LANG
    return sorted(p.relative_to(base).as_posix() for p in base.rglob("*.md"))


def languages() -> list[str]:
    return sorted(
        p.name for p in ROOT.iterdir()
        if p.is_dir() and LANG_DIR_RE.match(p.name) and p.name != SOURCE_LANG
    )


def check_language(lang: str, sources: list[str]) -> int:
    base = ROOT / lang
    outdated, pending, invalid, missing = [], [], [], []

    for rel in sources:
        target = base / rel
        if not target.exists():
            missing.append(rel)
            continue
        match = MARKER_RE.search(target.read_text(encoding="utf-8")[:500])
        expected_source = f"{SOURCE_LANG}/{rel}"
        if not match or match.group(1) != expected_source:
            invalid.append(rel)
        elif match.group(2) == "pending":
            pending.append(rel)
        elif match.group(2) != fingerprint(ROOT / expected_source):
            outdated.append(rel)

    orphaned = []
    if base.exists():
        known = set(sources)
        orphaned = [
            p.relative_to(base).as_posix() for p in sorted(base.rglob("*.md"))
            if p.relative_to(base).as_posix() not in known
        ]

    done = len(sources) - len(missing)
    synced = done - len(outdated) - len(pending) - len(invalid)
    print(f"\n## {lang}：已翻譯 {done}/{len(sources)}，已同步 {synced}  "
          f"(translated {done}/{len(sources)}, in sync {synced})")

    def show(title: str, items: list[str], hint: str = "") -> None:
        if not items:
            return
        print(f"\n{title}（{len(items)}）：")
        for rel in items:
            print(f"  - {lang}/{rel}")
        if hint:
            print(f"  {hint}")

    show("過期 Outdated", outdated,
         f"用 git log -p -- {SOURCE_LANG}/<檔案> 查看原文改了什麼，同步後執行 --stamp。 "
         f"Use git log -p on the original to see what changed, then run --stamp.")
    show("尚未蓋上指紋 Not stamped yet", pending, "翻譯完成後執行 --stamp。 Run --stamp when done.")
    show("來源標記錯誤 Missing or invalid source marker", invalid)
    show("孤立 Orphaned (original no longer exists)", orphaned)
    show("缺少 Missing", missing)
    return len(outdated) + len(pending) + len(invalid) + len(orphaned) + len(missing)


FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})(\w*)")
EMOJI = ["📍", "🪜", "📖", "🔧", "💻", "🔍", "🧪", "⚠️"]


def skeleton(path: Path) -> dict:
    """抓出一個檔案的結構：標題、提示框、表格、清單、連結與程式碼區塊。
    Extract the structure of a file: headings, boxes, tables, lists, links and code."""
    info = {"headings": [], "alerts": [], "details": 0, "table_rows": 0, "list_items": 0,
            "links": 0, "figures": 0, "emoji": {}, "code": [], "mermaid": 0}
    fence, lang, body = None, "", []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = FENCE_RE.match(line)
        if fence is None and match:
            fence, lang, body = match.group(1), match.group(2), []
            continue
        if fence is not None:
            if line.strip() == fence:
                if lang == "mermaid":
                    info["mermaid"] += 1
                else:
                    info["code"].append("\n".join(body))
                fence = None
            else:
                body.append(line)
            continue
        stripped = re.sub(r"^(>\s?)+", "", line)
        heading = re.match(r"^(#{1,6})\s", line)
        if heading:
            info["headings"].append(len(heading.group(1)))
        alert = re.match(r"^\[!(\w+)\]", stripped.strip())
        if alert:
            info["alerts"].append(alert.group(1))
        if line.strip() == "<details>":
            info["details"] += 1
        if line.startswith("|"):
            info["table_rows"] += 1
        if re.match(r"^\s*([-*+]|\d+\.)\s", stripped):
            info["list_items"] += 1
        info["links"] += len(re.findall(r"\]\(", line))
        if re.search(r"<!--\s*(圖|Figure|図|그림)[：:]", line):
            info["figures"] += 1
        for mark in EMOJI:
            if mark in line:
                info["emoji"][mark] = info["emoji"].get(mark, 0) + line.count(mark)
    return info


def compare_structure(langs: list[str]) -> int:
    problems = 0
    for rel in source_files():
        src = skeleton(ROOT / SOURCE_LANG / rel)
        for lang in langs:
            target = ROOT / lang / rel
            if not target.exists():
                continue
            dst = skeleton(target)
            diffs = []
            for key in ("headings", "alerts", "details", "table_rows", "list_items",
                        "links", "figures", "emoji", "mermaid"):
                if src[key] != dst[key]:
                    diffs.append(f"{key}: {src[key]} != {dst[key]}")
            if len(src["code"]) != len(dst["code"]):
                diffs.append(f"code blocks: {len(src['code'])} != {len(dst['code'])}")
            else:
                for i, (a, b) in enumerate(zip(src["code"], dst["code"]), 1):
                    if a != b:
                        diffs.append(f"code block {i} differs from the original")
            if diffs:
                problems += 1
                print(f"\n{lang}/{rel}")
                for d in diffs:
                    print(f"  - {d}")
    print(f"\n結構不一致的檔案：{problems} 個。Files whose structure differs: {problems}.")
    return problems


def stamp(targets: list[str]) -> int:
    files: list[Path] = []
    for item in targets:
        path = (ROOT / item).resolve()
        files.extend(sorted(path.rglob("*.md")) if path.is_dir() else [path])

    count = 0
    for path in files:
        rel = path.relative_to(ROOT)
        lang, inner = rel.parts[0], Path(*rel.parts[1:]).as_posix()
        source = ROOT / SOURCE_LANG / inner
        if lang == SOURCE_LANG or not source.exists():
            print(f"跳過 skip: {rel.as_posix()}")
            continue
        marker = f"<!-- source: {SOURCE_LANG}/{inner} | sha: {fingerprint(source)} -->"
        text = path.read_text(encoding="utf-8")
        if MARKER_RE.search(text[:500]):
            text = MARKER_RE.sub(marker, text, count=1)
        else:
            text = marker + "\n\n" + text
        path.write_text(text, encoding="utf-8")
        count += 1
    print(f"已更新 {count} 個檔案的指紋。Stamped {count} files.")
    return 0


def main() -> int:
    args = sys.argv[1:]
    if "--stamp" in args:
        targets = [a for a in args if a != "--stamp"]
        if not targets:
            print("請指定語言或檔案。Please give a language or a file.")
            return 1
        return stamp(targets)

    strict = "--strict" in args
    if "--structure" in args:
        langs = [a for a in args if not a.startswith("--")] or languages()
        problems = compare_structure(langs)
        return 1 if strict and problems else 0
    langs = [a for a in args if not a.startswith("--")] or languages()
    if not langs:
        print("目前還沒有任何翻譯。No translations yet.")
        return 0

    sources = source_files()
    problems = sum(check_language(lang, sources) for lang in langs)
    return 1 if strict and problems else 0


if __name__ == "__main__":
    sys.exit(main())
