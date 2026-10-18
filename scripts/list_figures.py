#!/usr/bin/env python3
"""列出所有待補的圖。

List every figure placeholder in the book, written as:

    <!-- 圖：描述這張圖要畫什麼 -->

用法 / Usage:
    python3 scripts/list_figures.py              # 純文字清單 / plain list
    python3 scripts/list_figures.py --markdown   # Markdown 待辦清單 / Markdown checklist
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "zh-TW"  # 圖片待辦以繁體中文原文為準 / the original is the reference
PLACEHOLDER_RE = re.compile(r"<!--\s*圖[：:]\s*(.+?)\s*-->")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def main() -> int:
    markdown = "--markdown" in sys.argv[1:]
    found = []
    for path in sorted(SOURCE_DIR.rglob("*.md")):
        rel = path.relative_to(ROOT)
        in_fence = False
        for no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            match = PLACEHOLDER_RE.search(INLINE_CODE_RE.sub("", line))
            if match:
                found.append((rel.as_posix(), no, match.group(1)))

    for rel, no, description in found:
        if markdown:
            print(f"- [ ] `{rel}`：{description}")
        else:
            print(f"{rel}:{no}  {description}")

    print(f"\n共 {len(found)} 張待補的圖。{len(found)} figure placeholders.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
