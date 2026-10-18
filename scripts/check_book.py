#!/usr/bin/env python3
"""檢查全書的連結、章節結構、提示框格式、本書特色區塊與用語。

Check the whole book for broken links, chapter structure, box format,
the book's own blocks and wording.

用法 / Usage:
    python3 scripts/check_book.py

發現錯誤時回傳 1，只有警告時回傳 0。
Exits with 1 if any error is found; warnings alone exit with 0.

連到還沒翻譯的語言版本（en/、ja/、ko/）的連結只算警告，翻譯完成後就會消失。
Links to language versions that are not translated yet only produce warnings.

如果《半導體製造概論》或《Git 概論》的 repo 放在這個 repo 旁邊（同一層資料夾），
指向它們的連結也會一併檢查。
If the sibling repositories of the series sit next to this one, links into
them are checked too.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
SOURCE_LANG = "zh-TW"
TRANSLATION_LANGS = {"en", "ja", "ko"}
SKIP_DIRS = {".git", "node_modules", "templates", "practice"}
SERIES_OWNER = "chenwei810"
SERIES_REPOS = {"Semiconductor_Manufacturing_Introduction", "Git_Introduction"}
HANDS_ON_CHAPTERS = {4, 6, 7, 8, 15}
MAX_VERILOG_LINES = 15
MAX_LINES = {"normal": 170, "hands_on": 220}

LINK_RE = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
IMG_TAG_RE = re.compile(r"<img\b[^>]*\bsrc=\"([^\"]+)\"", re.IGNORECASE)
INLINE_CODE_RE = re.compile(r"`[^`]*`")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})(\w*)")
GITHUB_ROUTE_RE = re.compile(r"^(\.\./)+(issues|pulls|discussions|wiki|releases|actions)(/|$)")
CHAPTER_RE = re.compile(r"^([a-z]{2,3}(?:-[A-Za-z0-9]+)?)/\d-[a-z0-9-]+/(\d{2})-[a-z0-9-]+/README\.md$")
ALERT_RE = re.compile(r"^\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*$")
LIST_ITEM_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+")
SERIES_LINK_RE = re.compile(
    r"https://github\.com/" + SERIES_OWNER + r"/(" + "|".join(SERIES_REPOS) + r")/blob/main/([^)\s#]+)"
)

# 各語言的章節必備元素與標籤 / Required parts and labels of a chapter, per language.
RULES = {
    "zh-TW": {
        "title": "# 第 {n} 章　",
        "position": "> 📍 **設計位置**",
        "position_fields": ["前一站：", "**本章：", "下一站："],
        "abstraction": "🪜 抽象層級：",
        "levels": "規格 ▸ RTL ▸ 網表 ▸ 佈局 ▸ GDS ▸ 晶片",
        "term": "**📖 名詞｜",
        "term_fields": ["定義", "現場用法", "相關名詞", "常見混淆"],
        "knowhow": "**🔧 Know-how｜",
        "knowhow_fields": ["情境", "做法", "為什麼", "沒做會怎樣"],
        "software": "**💻 軟體對照｜",
        "software_fields": ["像什麼", "不一樣的地方", "所以要注意"],
        "deep_dive": "<summary>🔍 深入一點：",
        "hands_on": "## 🧪 跟著做：",
        "end": ["## 本章重點", "## 延伸閱讀"],
        "nav": "[目錄](../../README.md)",
    },
    "en": {
        "title": "# Chapter {n}: ",
        "position": "> 📍 **Where the design is**",
        "position_fields": ["Previous stop:", "**This chapter:", "Next stop:"],
        "abstraction": "🪜 Abstraction level: ",
        "levels": "Spec ▸ RTL ▸ Netlist ▸ Layout ▸ GDS ▸ Chip",
        "term": "**📖 Term | ",
        "term_fields": ["Definition", "On the job", "Related terms", "Common confusion"],
        "knowhow": "**🔧 Know-how | ",
        "knowhow_fields": ["Situation", "Practice", "Why", "If you skip it"],
        "software": "**💻 Software analogy | ",
        "software_fields": ["Like", "Unlike", "Watch out"],
        "deep_dive": "<summary>🔍 Going deeper: ",
        "hands_on": "## 🧪 Try it: ",
        "end": ["## Key takeaways", "## Further reading"],
        "nav": "[Contents](../../README.md)",
    },
    "ja": {
        "title": "# 第 {n} 章　",
        "position": "> 📍 **設計の現在地**",
        "position_fields": ["前の工程：", "**この章：", "次の工程："],
        "abstraction": "🪜 抽象度：",
        "levels": "仕様 ▸ RTL ▸ ネットリスト ▸ レイアウト ▸ GDS ▸ チップ",
        "term": "**📖 用語｜",
        "term_fields": ["定義", "現場での使い方", "関連用語", "よくある混同"],
        "knowhow": "**🔧 ノウハウ｜",
        "knowhow_fields": ["状況", "やり方", "理由", "やらないとどうなる"],
        "software": "**💻 ソフトウェアとの対比｜",
        "software_fields": ["似ている点", "違う点", "だから注意"],
        "deep_dive": "<summary>🔍 もう一歩深く：",
        "hands_on": "## 🧪 やってみよう：",
        "end": ["## この章のポイント", "## 参考文献"],
        "nav": "[目次](../../README.md)",
    },
    "ko": {
        "title": "# 제{n}장 ",
        "position": "> 📍 **설계의 현재 위치**",
        "position_fields": ["이전 단계:", "**이 장:", "다음 단계:"],
        "abstraction": "🪜 추상화 수준: ",
        "levels": "사양 ▸ RTL ▸ 네트리스트 ▸ 레이아웃 ▸ GDS ▸ 칩",
        "term": "**📖 용어｜",
        "term_fields": ["정의", "현장에서는", "관련 용어", "흔한 혼동"],
        "knowhow": "**🔧 노하우｜",
        "knowhow_fields": ["상황", "방법", "이유", "안 하면 어떻게 되나"],
        "software": "**💻 소프트웨어와 비교｜",
        "software_fields": ["닮은 점", "다른 점", "그래서 주의할 점"],
        "deep_dive": "<summary>🔍 조금 더 깊이: ",
        "hands_on": "## 🧪 따라 해 보기: ",
        "end": ["## 이 장의 핵심", "## 참고 자료"],
        "nav": "[목차](../../README.md)",
    },
}

# 台灣用語檢查：常見的非台灣用語（只發出警告）。
# Terminology check for the Traditional Chinese text (warnings only).
DISCOURAGED_TERMS = {
    "流片": "下線",
    "版圖": "佈局",
    "布局": "擺置或佈局",
    "布線": "繞線",
    "布圖規劃": "平面規劃",
    "仿真": "模擬",
    "時鐘": "時脈",
    "觸發器": "正反器",
    "鎖存器": "閂鎖器",
    "寄存器": "暫存器",
    "多路選擇器": "多工器",
    "流水線": "管線",
    "有符號": "有號",
    "無符號": "無號",
    "溢出": "溢位",
    "總線": "匯流排",
    "模塊": "模組",
    "IP 核": "矽智財",
    "標準單元": "標準元件",
    "串擾": "串音",
    "工藝": "製程",
    "光刻": "微影",
    "晶體管": "電晶體",
    "芯片": "晶片",
    "比特": "位元",
    "默認": "預設",
    "缺省": "預設",
    "文件夾": "資料夾",
    "倉庫": "儲存庫",
    "源代碼": "原始碼",
    "寫代碼": "寫程式",
    "信息": "訊息",
    "用戶": "使用者",
    "數據": "資料",
    "服務器": "伺服器",
    "視頻": "影片",
    "創建": "建立",
    "運行": "執行",
    "屏幕": "螢幕",
    "界面": "介面",
    "調試": "除錯",
    "軟件": "軟體",
    "硬件": "硬體",
    "固件": "韌體",
    "接口": "介面",
    "內存": "記憶體",
    "網絡": "網路",
    "質量": "品質",
    "硅": "矽",
}

# 合法的台灣用法，出現時不要誤報 / Valid Taiwanese phrases that contain a discouraged term.
ALLOWED_PHRASES: dict[str, list[str]] = {}

# 常見的簡體字（只發出警告）。只收錄在台灣的繁體中文裡幾乎不會出現的字。
# Common Simplified Chinese characters (warnings only).
SIMPLIFIED_CHARS = set(
    "们这个为与说时过发现会对产业电导体层门线术设计础规质检测试结构样书读写图标题录页问错误单联关开"
    "经语译视频网络专务简态选择应运动输环节约织组济阶处获辆军伤长东乐车马鸟鱼龙风飞广庆库张弹强归"
    "忆怀总战户挂损换摄数断无旧显晓暂杂权条来极构枪树桥档梦检楼汉汤沟没泪泽洁浅测济浓润涨渐温湿满滤"
    "灭灯灵灾炉炼烂烦烧热爱牵状独狮猎猪献环现画畅疗盐监盖盘矿码砖确碍礼祸离种积称税稳穷窃竞笔筑签"
    "简类粮紧纠红级纪纤纯纳纵纷纸纹纺纽练细终绍结绕绘给络绝统继绩续维综绿缓编缘缩缴罗罚职肃肠肤肿胀"
    "胆脑脚脱脸舰艺芜苍苏药获营虑虚补装见观规视览觉触计订认讨让训议讯记讲许论访证评识诉词试话询该详"
    "误请诸读课谁调谈谢贝负贡财责败货贩购贯费资赋赏赔赚赛赞赢赶趋跃践轨转轮软轰轻载较辅辉输边达迁迟"
    "适选递逻遗邮释钉钟钢钱铁铜铝铭银链销锁锅锋锡键镜闭闯闲间闻阀阅队阳阴阵际陆陈险随隐难静顶项顺须"
    "顾领颗颜额饭馆驱驶驾验骑鲜鸡麦黄齐齿龄掺杂兴举义乐习书买乱亏亚亲亿仅从仓优伟传伤价众优员"
    "储锁综钟闩压滞缘"
)


def iter_markdown_files() -> list[Path]:
    files = []
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        files.append(path)
    return files


def strip_code(lines: list[str]) -> list[str]:
    """把程式碼區塊與行內程式碼換成空白，保留行號。"""
    out, fence = [], None
    for line in lines:
        match = FENCE_RE.match(line)
        if match:
            mark = match.group(1)
            if fence is None:
                fence = mark
                out.append("")
                continue
            if mark[0] == fence[0] and len(mark) >= len(fence) and line.strip() == mark:
                fence = None
                out.append("")
                continue
        out.append("" if fence else INLINE_CODE_RE.sub("", line))
    return out


def code_blocks(lines: list[str]) -> list[tuple[int, str, list[str]]]:
    """回傳 (起始行號, 語言, 內容行) / (start line, language, body lines)."""
    blocks, fence, lang, start, body = [], None, "", 0, []
    for no, line in enumerate(lines, 1):
        match = FENCE_RE.match(line)
        if fence is None and match:
            fence, lang, start, body = match.group(1), match.group(2), no, []
        elif fence is not None and line.strip() == fence:
            blocks.append((start, lang, body))
            fence = None
        elif fence is not None:
            body.append(line)
    return blocks


def lang_of(path: Path) -> str | None:
    first = path.relative_to(ROOT).parts[0]
    return first if first in RULES else None


def check_links(path: Path, lines: list[str], errors: list[str], warnings: list[str]) -> None:
    rel = path.relative_to(ROOT).as_posix()
    lang = lang_of(path)
    for no, line in enumerate(lines, 1):
        targets = LINK_RE.findall(line) + IMG_TAG_RE.findall(line)
        for target in targets:
            series = SERIES_LINK_RE.match(target)
            if series:
                repo, inner = series.group(1), unquote(series.group(2))
                target_lang = inner.split("/", 1)[0]
                if lang and target_lang in RULES and target_lang != lang:
                    errors.append(f"{rel}:{no}: 系列書連結的語言不一致 series link points to {target_lang}/ -> {target}")
                sibling = ROOT.parent / repo
                if sibling.is_dir() and not (sibling / inner).exists():
                    errors.append(f"{rel}:{no}: 系列書連結失效 broken series link -> {target}")
                continue
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE) or target.startswith("#"):
                continue
            if GITHUB_ROUTE_RE.match(target):
                continue
            clean = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not clean:
                continue
            resolved = (path.parent / clean).resolve()
            if resolved.exists():
                continue
            try:
                top = resolved.relative_to(ROOT).parts[0]
            except ValueError:
                top = ""
            if top in TRANSLATION_LANGS:
                warnings.append(f"{rel}:{no}: 翻譯尚未完成 translation not available yet -> {target}")
            else:
                errors.append(f"{rel}:{no}: 連結失效 broken link -> {target}")


def check_boxes(path: Path, lines: list[str], errors: list[str]) -> None:
    """引用區塊裡連續兩行一般文字，在 GitHub 上會被合併成同一段。"""
    rel = path.relative_to(ROOT).as_posix()
    prev_text = False
    for no, line in enumerate(lines, 1):
        if not line.startswith(">"):
            prev_text = False
            continue
        content = re.sub(r"^>\s?", "", line)
        if content.strip() == "" or LIST_ITEM_RE.match(content):
            prev_text = False
            continue
        if content.startswith("[!"):
            if not ALERT_RE.match(content.strip()):
                errors.append(f"{rel}:{no}: 不支援的提示框類型 unsupported alert type -> {content.strip()}")
            prev_text = False
            continue
        if prev_text:
            errors.append(
                f"{rel}:{no}: 引用區塊中連續兩行文字會被合併，請改用清單或空行 "
                f"consecutive lines in a blockquote will be merged"
            )
        prev_text = True


def check_details(path: Path, lines: list[str], errors: list[str], label: str | None) -> None:
    """「深入一點」區塊：summary 之後與 </details> 之前都要空一行，GitHub 才會把內容當成 Markdown。"""
    rel = path.relative_to(ROOT).as_posix()
    opened = None
    for no, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped == "<details>":
            if opened is not None:
                errors.append(f"{rel}:{no}: <details> 沒有關閉 unclosed <details>")
            opened = no
            nxt = lines[no] if no < len(lines) else ""
            if not nxt.strip().startswith("<summary>") or not nxt.strip().endswith("</summary>"):
                errors.append(f"{rel}:{no + 1}: <details> 下一行要是一行完整的 <summary> one-line <summary> expected")
            elif label and not nxt.strip().startswith(label):
                errors.append(f"{rel}:{no + 1}: 標題應以「{label}」開頭 summary should start with \"{label}\"")
            if no + 1 < len(lines) and lines[no + 1].strip() != "":
                errors.append(f"{rel}:{no + 2}: </summary> 之後要空一行 blank line needed after </summary>")
        elif stripped == "</details>":
            if opened is None:
                errors.append(f"{rel}:{no}: 多出來的 </details> stray </details>")
            elif lines[no - 2].strip() != "":
                errors.append(f"{rel}:{no}: </details> 之前要空一行 blank line needed before </details>")
            opened = None
    if opened is not None:
        errors.append(f"{rel}:{opened}: <details> 沒有關閉 unclosed <details>")


def chapter_info(path: Path) -> tuple[str, int] | None:
    match = CHAPTER_RE.match(path.relative_to(ROOT).as_posix())
    if not match:
        return None
    return match.group(1), int(match.group(2))


def box_bodies(lines: list[str], header: str) -> list[tuple[int, str]]:
    """回傳以 header 開頭的引用區塊（行號, 內容）。"""
    found = []
    for no, line in enumerate(lines, 1):
        if line.startswith("> ") and header in line:
            body = []
            for nxt in lines[no:]:
                if not nxt.startswith(">"):
                    break
                body.append(nxt)
            found.append((no, "\n".join(body)))
    return found


def check_chapter(path: Path, text: str, errors: list[str], warnings: list[str]) -> None:
    rel = path.relative_to(ROOT).as_posix()
    info = chapter_info(path)
    if info is None:
        return
    lang, number = info
    rules = RULES.get(lang)
    if rules is None:
        if "](../../README.md)" not in text:
            errors.append(f"{rel}: missing navigation link to ../../README.md")
        return
    raw = text.splitlines()
    lines = strip_code(raw)

    title = rules["title"].format(n=number)
    first_heading = next((l for l in raw if l.startswith("# ")), "")
    if not first_heading.startswith(title):
        errors.append(f"{rel}: 標題應以「{title}」開頭 title should start with \"{title}\"")

    # 📍 位置框 / position box
    pos = box_bodies(lines, rules["position"].removeprefix("> "))
    if len(pos) != 1:
        errors.append(f"{rel}: 需要一個位置框 exactly one position box expected ({rules['position']})")
    else:
        for field in rules["position_fields"]:
            if field not in pos[0][1]:
                errors.append(f"{rel}:{pos[0][0]}: 位置框缺少「{field}」 position box missing field")

    # 🪜 抽象層級 / abstraction level
    abst = [l for l in lines if l.startswith(rules["abstraction"])]
    if len(abst) != 1:
        errors.append(f"{rel}: 需要一行抽象層級 exactly one abstraction line expected ({rules['abstraction']})")
    else:
        line = abst[0][len(rules["abstraction"]):]
        if line.replace("**", "") != rules["levels"]:
            errors.append(f"{rel}: 抽象層級的寫法不對 abstraction line should read \"{rules['levels']}\"")
        if "**" not in line:
            errors.append(f"{rel}: 抽象層級要把本章的層級加粗 bold the level of this chapter")

    # 📖 🔧 💻 提示框 / boxes
    for key, fields_key, low, high, kind in (
        ("term", "term_fields", 2, 4, "📖"),
        ("knowhow", "knowhow_fields", 2, 4, "🔧"),
        ("software", "software_fields", 1, 1, "💻"),
    ):
        boxes = box_bodies(lines, rules[key])
        if not low <= len(boxes) <= high:
            target = warnings if kind != "💻" else errors
            target.append(f"{rel}: {kind} 框有 {len(boxes)} 個，建議 {low}～{high} 個 {kind} boxes: {len(boxes)}, expected {low}-{high}")
        for no, body in boxes:
            for field in rules[fields_key]:
                if f"**{field}**" not in body:
                    errors.append(f"{rel}:{no}: {kind} 框缺少「{field}」 box missing field \"{field}\"")
            prev = lines[no - 2] if no >= 2 else ""
            if not ALERT_RE.match(prev.removeprefix("> ").strip()):
                errors.append(f"{rel}:{no}: {kind} 框上一行要是提示框標記 alert marker expected above the box")

    # 🔍 深入一點 / deep dives
    dives = sum(1 for l in lines if l.strip() == "<details>")
    if dives > 2:
        warnings.append(f"{rel}: 「深入一點」有 {dives} 個，建議最多 2 個 {dives} deep dives, at most 2 expected")

    # 🧪 跟著做 / hands-on
    has_hands_on = any(l.startswith(rules["hands_on"]) for l in lines)
    if number in HANDS_ON_CHAPTERS and not has_hands_on:
        errors.append(f"{rel}: 缺少「{rules['hands_on']}」 missing hands-on section")
    if number not in HANDS_ON_CHAPTERS and has_hands_on:
        errors.append(f"{rel}: 這一章不應該有跟著做 no hands-on section in this chapter")

    # 結尾 / end sections and navigation
    for marker in rules["end"] + [rules["nav"]]:
        if marker not in text:
            errors.append(f"{rel}: 缺少「{marker}」 missing section")

    # Verilog 片段長度 / Verilog snippet length
    for start, block_lang, body in code_blocks(raw):
        if block_lang == "verilog" and len(body) > MAX_VERILOG_LINES:
            errors.append(f"{rel}:{start}: Verilog 片段 {len(body)} 行，上限 {MAX_VERILOG_LINES} 行 Verilog snippet too long")

    # 章節長度（只看原文）/ chapter length, original only
    if lang == SOURCE_LANG:
        limit = MAX_LINES["hands_on" if number in HANDS_ON_CHAPTERS else "normal"]
        if len(raw) > limit:
            warnings.append(f"{rel}: 共 {len(raw)} 行，建議 {limit} 行以內 {len(raw)} lines, about {limit} expected")


def check_language(path: Path, lines: list[str], warnings: list[str]) -> None:
    """只檢查繁體中文原文與根目錄的專案文件。"""
    rel = path.relative_to(ROOT)
    first = rel.parts[0]
    if rel.as_posix() in {"STYLE_GUIDE.md", "README.md", "PLAN.md"}:
        return
    if len(rel.parts) > 1 and first != SOURCE_LANG and re.match(r"^[a-z]{2,3}(-[A-Za-z0-9]+)?$", first):
        return
    for no, line in enumerate(lines, 1):
        for term, preferred in DISCOURAGED_TERMS.items():
            cleaned = line
            for phrase in ALLOWED_PHRASES.get(term, []):
                cleaned = cleaned.replace(phrase, "")
            if term in cleaned:
                warnings.append(f"{rel.as_posix()}:{no}: 建議用「{preferred}」取代「{term}」")
        found = sorted({ch for ch in line if ch in SIMPLIFIED_CHARS})
        if found:
            warnings.append(f"{rel.as_posix()}:{no}: 可能是簡體字 possible Simplified Chinese -> {''.join(found)}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    files = iter_markdown_files()
    for path in files:
        text = path.read_text(encoding="utf-8")
        lines = strip_code(text.splitlines())
        info = chapter_info(path)
        label = RULES.get(info[0], {}).get("deep_dive") if info else None
        check_links(path, lines, errors, warnings)
        check_boxes(path, lines, errors)
        check_details(path, lines, errors, label)
        check_chapter(path, text, errors, warnings)
        check_language(path, lines, warnings)

    pending = sum(1 for w in warnings if "translation not available yet" in w)
    for message in warnings:
        if "translation not available yet" not in message:
            print(f"WARNING {message}")
    for message in errors:
        print(f"ERROR   {message}")
    if pending:
        print(f"\n有 {pending} 個連結指向尚未翻譯的語言版本。{pending} links point to translations that are not available yet.")
    print(f"\n檢查了 {len(files)} 個檔案：{len(errors)} 個錯誤，{len(warnings) - pending} 個警告。")
    print(f"Checked {len(files)} files: {len(errors)} errors, {len(warnings) - pending} warnings.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
