# 翻譯指南 / Translation Guide

## For translators

Thank you for helping bring this book to more readers!

### How the languages are organized

```text
README.md        multilingual landing page with the language selector
zh-TW/           Traditional Chinese, the original
en/              English
ja/              Japanese
ko/              Korean
<code>/          any new language, with exactly the same structure
images/          figures shared by every language
practice/        the practice files (Verilog, testbench, reference model), shared by every language
```

- **Source of truth.** `zh-TW/` is the original. Every other language folder mirrors it file by file, with the same folder names and file names.
- **Language codes.** Use BCP 47 codes such as `es`, `de`, `fr` or `vi`.
- **Links stay the same.** Every language folder sits at the same depth, so links between chapters and links to `../../../images/` and `../../../practice/` work unchanged in every language.
- **Links to other books in the series.** Point them to the same language. An English chapter links to `.../Semiconductor_Manufacturing_Introduction/blob/main/en/...`, a Japanese chapter to `.../ja/...`. `scripts/check_book.py` reports a link that points to another language.
- **Claim first.** Open an issue with the "Translation" template to claim a language or a chapter, so that no two people translate the same file.
- **Translate from either version.** You may translate from the Chinese original or from the English version, but check technical details against the original.
- **Terminology.** Follow [Appendix A: Glossary](en/appendix/glossary.md). Add a column for your language to the glossary first, then translate the chapters.
- **Machine translation** is fine for a first draft, but every file must be reviewed by a person who knows the language and the subject well.
- **Keep these exactly as they are.** Verilog code, commands, file names, module and signal names, and tool output stay unchanged, because readers will see them that way on screen. Code comments are already in English. In Mermaid diagrams, translate the labels.
- **Keep the structure.** Keep every box, every `<details>` block (with a blank line after `</summary>` and before `</details>`), every table row and every list item. The labels for each language are in sections 9 and 10 of the [style guide](STYLE_GUIDE.md).
- **Do not translate `practice/`.** Every language shares the same practice files.

### Source markers

Every translated file starts with a marker that records a fingerprint of the original at the time of translation:

```markdown
<!-- source: zh-TW/2-front-end/04-rtl-and-verilog/README.md | sha: 1a2b3c4d5e6f -->
```

When you finish translating or syncing a file, update its fingerprint:

```bash
python3 scripts/check_translations.py --stamp ja/2-front-end/04-rtl-and-verilog/README.md
```

If the original changes later, the fingerprint no longer matches and the file is reported as outdated:

```bash
python3 scripts/check_translations.py ja
```

Use `git log -p -- zh-TW/<file>` to see what changed in the original, update the translation, and stamp it again.

### Structure check

The structure check compares each translated file with the original: headings, boxes, `<details>` blocks, table rows, list items, links, emoji markers and figure placeholders must match, and every code block except Mermaid diagrams must be identical.

```bash
python3 scripts/check_translations.py --structure ja --strict
```

### Adding a new language

1. Copy the `en/` folder to a new folder named with your language code, for example `es/`.
2. Translate the files. Keep all box formats (`> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `<details>`), emoji, list structure and links.
3. Add the labels for your language to `RULES` in `scripts/check_book.py` and to section 10 of the style guide.
4. Stamp the files you have finished with `--stamp`, and run the structure check.
5. Add your language to the language selector at the top of the root `README.md` and to the language bar of every existing `README.md` home page, and add a column for it in the contents table.
6. Open a pull request with a commit message starting with `i18n(<code>):`.

---

## 中文說明

### 資料夾的安排

```text
README.md        多語言並列的首頁，提供語言選擇
zh-TW/           繁體中文，原文
en/              英文
ja/              日文
ko/              韓文
<語言代碼>/       之後新增的語言，結構完全相同
images/          所有語言共用的圖片
practice/        練習檔（Verilog、Testbench、參考模型），所有語言共用
```

- **原文**：`zh-TW/` 是原文，也是所有翻譯的依據。其他語言的資料夾和原文一一對應，資料夾名稱與檔名完全相同。
- **語言代碼**：使用 BCP 47 代碼，例如 `es`、`de`、`fr`、`vi`。
- **連結不用改**：所有語言的資料夾都在同一層，所以章節之間的連結、指向 `../../../images/` 與 `../../../practice/` 的路徑，在每個語言裡都一樣。
- **系列其他書的連結**：要連到同一種語言。英文章節連到 `.../Semiconductor_Manufacturing_Introduction/blob/main/en/...`，日文章節連到 `.../ja/...`。連錯語言時，`scripts/check_book.py` 會報錯。
- **先認領**：開始翻譯前，請先開 Issue（使用「翻譯」範本）認領語言或章節，避免重複翻譯。
- **翻譯來源**：可以從中文原文或英文版翻譯，但技術細節請以中文原文為準。
- **術語**：以[附錄 A 術語總表](zh-TW/appendix/glossary.md)為準。先在術語總表加上該語言的欄位，把術語的譯法定下來，再開始翻譯內文。
- **機器翻譯**：可以用來產生初稿，但每個檔案都必須經過熟悉該語言與 IC 設計的人校對。
- **保持原樣的東西**：Verilog 程式碼、指令、檔名、模組與訊號名稱，以及工具的輸出，都保持原樣，因為讀者在畫面上看到的就是這樣。程式碼的註解本來就是英文。Mermaid 圖裡的文字要翻譯。
- **保留結構**：每個提示框、每個 `<details>` 區塊（`</summary>` 之後與 `</details>` 之前各空一行）、每一列表格與每一個清單項目都要保留。各語言的標籤寫在[寫作規範](STYLE_GUIDE.md)第 9、10 節。
- **不翻譯 `practice/`**：所有語言共用同一套練習檔。

### 來源標記

每個翻譯檔的第一行都有來源標記，記錄翻譯時原文的「指紋」：

```markdown
<!-- source: zh-TW/2-front-end/04-rtl-and-verilog/README.md | sha: 1a2b3c4d5e6f -->
```

翻譯或同步完一個檔案之後，更新它的指紋：

```bash
python3 scripts/check_translations.py --stamp en/2-front-end/04-rtl-and-verilog/README.md
```

之後只要原文被修改，指紋就會對不上，這個檔案會被列為「過期」：

```bash
python3 scripts/check_translations.py en
```

| 狀態 | 意思 | 怎麼處理 |
|---|---|---|
| 過期 | 原文在翻譯之後又被修改過 | 用 `git log -p -- zh-TW/<檔案>` 查看原文改了什麼，同步翻譯後再執行 `--stamp` |
| 尚未蓋上指紋 | 翻譯完成，但還沒有記錄指紋 | 執行 `--stamp` |
| 缺少 | 原文有、但還沒有翻譯 | 可以認領翻譯 |
| 孤立 | 翻譯有、但原文已經不存在 | 確認原文是否改名或刪除 |

### 結構比對

結構比對會拿每個翻譯檔和原文比較：標題、提示框、`<details>`、表格列數、清單項目、連結、emoji 標記與待補圖片的數量都要相同；除了 Mermaid 圖以外，每個程式碼區塊都要一字不差。

```bash
python3 scripts/check_translations.py --structure ja --strict
```

### 修改中文原文時

修改 `zh-TW/` 的內容之後，對應的翻譯會自動被列為過期。如果只是修正錯字、不影響意思，可以直接對翻譯檔執行 `--stamp`，表示翻譯不需要更新。Commit 訊息的格式請見[貢獻指南](CONTRIBUTING.md)。

### 新增一個語言

1. 把 `en/` 資料夾複製一份，改名為該語言的代碼，例如 `es/`。
2. 翻譯內文，保留所有提示框格式（`> [!NOTE]`、`> [!TIP]`、`> [!IMPORTANT]`、`<details>`）、emoji、清單結構與連結。
3. 在 `scripts/check_book.py` 的 `RULES` 與寫作規範第 10 節，加上該語言的標籤。
4. 翻譯完成的檔案執行 `--stamp`，並跑一次結構比對。
5. 在根目錄 `README.md` 最上方的語言選擇、以及各語言首頁 `README.md` 的語言列加上該語言，並在目錄表格加上一欄。
6. 送出 Pull Request，commit 訊息以 `i18n(<語言代碼>):` 開頭。
