# 工具腳本 / Scripts

這些腳本只需要 Python 3，不需要安裝任何套件。請在專案根目錄執行。

These scripts only need Python 3. Run them from the repository root.

| 腳本 Script | 用途 Purpose |
|---|---|
| `python3 scripts/check_book.py` | 檢查連結、章節結構、提示框格式、本書特色區塊、Verilog 片段長度與用語。GitHub 會在每次 push 和 Pull Request 時自動執行。 Checks links, chapter structure, box format, the book's own blocks, Verilog snippet length and wording. Runs automatically on GitHub. |
| `python3 scripts/check_translations.py [語言代碼]` | 找出過期、缺少或孤立的翻譯檔。 Finds outdated, missing or orphaned translations. |
| `python3 scripts/check_translations.py --stamp <檔案或語言>` | 翻譯或同步完成後，更新來源標記中的指紋。 Updates the fingerprint in the source marker after translating or syncing. |
| `python3 scripts/check_translations.py --structure [語言代碼]` | 和原文做結構比對：標題、提示框、表格、清單、連結與程式碼區塊。 Compares the structure of each translation with the original: headings, boxes, tables, lists, links and code blocks. |
| `python3 scripts/list_figures.py [--markdown]` | 列出中文原文中所有待補的圖。 Lists all figure placeholders in the original. |
| `bash practice/run_all.sh` | 重跑所有「跟著做」，和書中的輸出比對。需要 Icarus Verilog 與 Yosys。 Re-runs every Try-it section and compares the output with the book. Needs Icarus Verilog and Yosys. |

`check_book.py` 也會檢查連到系列其他書的連結：把《半導體製造概論》或《Git 概論》的 repo 放在這個 repo 旁邊（同一層資料夾），就會一併確認這些連結的檔案存在，並且連到同一種語言。

`check_book.py` also checks links to the other books in the series. If their repositories sit next to this one, it confirms that each linked file exists and is in the same language.
