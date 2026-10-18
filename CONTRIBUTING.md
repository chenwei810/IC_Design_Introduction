# 貢獻指南 / Contributing Guide

[English](#english) ｜ [繁體中文](#繁體中文)

---

## English

Thank you for helping make this book better! Fixing a typo, clarifying a paragraph, drawing a figure, checking a Try-it step or translating a chapter are all very welcome.

### What you can contribute

| Type | Examples | How |
|---|---|---|
| Errata | Typos, technical errors, outdated information | Open an issue, or send a pull request directly |
| Try-it problems | A Try-it step that does not give the output the book shows | Open an issue with your tool versions, the commands you ran and the output you got |
| Content suggestions | A paragraph that is unclear, a new term box, know-how box or deep dive | Open an issue to discuss first |
| Figures | Draw the figures marked as placeholders in the chapters | See [images/README.md](images/README.md) |
| Translations | Translate the book into another language | See [TRANSLATIONS.md](TRANSLATIONS.md) |

### Content principles

This is a public introduction, so everything in it must be shareable. Please **do not** submit:

- Confidential information of any company, such as internal flows, design data or internal documents.
- Any real data from a foundry's process design kit (PDK) or standard cell library, such as design rules, cell timing or device models.
- Names of commercial EDA tools, or screenshots of any EDA tool. The open-source tools used in the Try-it sections (Icarus Verilog, Yosys, GTKWave) are the only exception.
- Names of specific companies' products, or advertising.
- Images or text you do not have the rights to.

For technical corrections, please include public references, or the output you actually got.

### Which version to edit

The Traditional Chinese text in `zh-TW/` is the original. Content changes should be made there first, and the translations in `en/`, `ja/` and `ko/` should then be synced. If you only read English, Japanese or Korean, you are still welcome to fix that version or open an issue in English; a maintainer will take care of the Chinese side.

### Sending a pull request

1. Fork the repository and create a branch, for example `fix/ch08-typo`.
2. Make your changes, following the [style guide](STYLE_GUIDE.md).
3. Run the checks locally:

   ```bash
   python3 scripts/check_book.py
   python3 scripts/check_translations.py
   ```

4. If you changed a Try-it section or anything in `practice/`, run `bash practice/run_all.sh`. It re-runs every Try-it section and compares the output with the book. After an intended change, update the saved outputs with `bash practice/run_all.sh --update` and update the book to match.
5. Write the commit message in the format below, open a pull request, and fill in the checklist.

One pull request should do one thing. It makes reviews much faster.

### Commit message format

Because the book is maintained in several languages, the commit message should tell translators at a glance whether a change needs to be translated:

| Prefix | Use | Needs translation sync? |
|---|---|---|
| `content:` | Changes the meaning of the text, such as fixing a technical error or adding a paragraph | Yes |
| `fix:` | Typos, punctuation or formatting that do not change the meaning | Usually no |
| `practice:` | Changes to the practice files | Check the Try-it sections |
| `figure:` | Adds or changes figures | Figures are shared, but captions may need translating |
| `i18n(<code>):` | Translation work, for example `i18n(en):` | — |
| `docs:` | Project documents such as the README or this guide | Sometimes |
| `chore:` | Scripts, settings, GitHub workflows | No |

### Editor setup

We recommend VS Code. The `.vscode/extensions.json` file lists recommended extensions, including one for Verilog, and VS Code will offer to install them when you open the project.

The boxes use GitHub's alert syntax (`> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`), and the deep dives use `<details>`. Some editors may not preview them correctly; what you see on GitHub is what counts.

### License and code of conduct

By contributing, you agree that your contribution is released under the project's [CC BY-NC-SA 4.0](LICENSE) license. Please follow the [code of conduct](CODE_OF_CONDUCT.md) when taking part in this project.

---

## 繁體中文

感謝你願意讓這本書變得更好！不論是修正一個錯字、補充一段說明、畫一張圖、檢查一個「跟著做」的步驟，還是翻譯一整章，都非常歡迎。

### 可以貢獻什麼

| 類型 | 例子 | 方式 |
|---|---|---|
| 勘誤 | 錯字、技術錯誤、過時的資訊 | 開 Issue，或直接送 Pull Request |
| 跟著做跑不出來 | 照著「跟著做」的步驟，卻得到和書上不同的輸出 | 開 Issue，附上工具版本、你執行的指令和得到的輸出 |
| 內容建議 | 某段說明不夠清楚、想新增名詞框、Know-how 框或深入一點 | 先開 Issue 討論 |
| 圖片 | 繪製章節中標記為「圖：」的待補圖片 | 參考 [images/README.md](images/README.md) |
| 翻譯 | 把這本書翻譯成其他語言 | 參考 [TRANSLATIONS.md](TRANSLATIONS.md) |

### 內容原則

這是一本公開的概論，所有內容都必須能夠公開分享。請**不要**提交：

- 任何公司的機密資訊，例如內部流程、設計資料或內部文件。
- 任何晶圓廠製程設計套件（PDK）或標準元件庫裡的真實資料，例如設計規則、元件時序或元件模型。
- 商用 EDA 工具的名稱，或任何 EDA 工具的截圖。唯一的例外是「跟著做」使用的開源工具（Icarus Verilog、Yosys、GTKWave）。
- 特定公司的產品名稱，或廣告。
- 未經授權的圖片或文字。

修正技術內容時，請附上公開的參考資料，或你實際執行得到的結果。

### 要改哪一個版本

`zh-TW/` 的繁體中文是原文。內容的修改請先改中文原文，再同步 `en/`、`ja/`、`ko/` 等翻譯。只修改某個翻譯版本、或用英文開 Issue 也非常歡迎，維護者會負責同步中文。

### 送出 Pull Request

1. Fork 本專案，建立新的分支，例如 `fix/ch08-typo`。
2. 修改內容，並遵守[寫作規範](STYLE_GUIDE.md)。
3. 在本機執行檢查：

   ```bash
   python3 scripts/check_book.py
   python3 scripts/check_translations.py
   ```

4. 如果修改了「跟著做」或 `practice/` 裡的任何東西，請執行 `bash practice/run_all.sh`。它會重跑每一章的「跟著做」，並和書上的輸出比對。確定要改變輸出時，用 `bash practice/run_all.sh --update` 更新存檔，並把書上的輸出改成一樣。
5. 依照下方的格式撰寫 commit 訊息，送出 Pull Request，並填寫範本中的檢查清單。

一個 Pull Request 最好只處理一件事，審查起來會快很多。

### Commit 訊息格式

這本書有多種語言的版本，所以 commit 訊息要讓譯者一眼看出「這次的修改需不需要同步翻譯」：

| 前綴 | 用途 | 譯者需要同步嗎 |
|---|---|---|
| `content:` | 改變內文的意思，例如修正技術錯誤、新增段落 | 需要 |
| `fix:` | 錯字、標點、格式，不改變意思 | 通常不需要 |
| `practice:` | 修改練習檔 | 檢查各章的「跟著做」 |
| `figure:` | 新增或修改圖片 | 圖片共用，但圖說可能需要翻譯 |
| `i18n(<語言代碼>):` | 翻譯相關，例如 `i18n(en):` | — |
| `docs:` | 專案文件，例如 README 或本指南 | 視情況 |
| `chore:` | 腳本、設定、GitHub workflow | 不需要 |

例如：

```text
content: 第 8 章補充 hold 違規的修法
fix: 第 12 章錯字
practice: 參考模型加上新的測試
i18n(en): sync chapter 8
```

### 編輯環境

建議使用 VS Code。專案中的 `.vscode/extensions.json` 列出了建議安裝的擴充套件，其中包括 Verilog 的語法支援，開啟專案時 VS Code 會提示你安裝。

提示框使用 GitHub 的提示框語法（`> [!NOTE]`、`> [!TIP]`、`> [!IMPORTANT]`），深入一點使用 `<details>`。部分編輯器的預覽可能無法正確顯示，請以 GitHub 網頁上的顯示結果為準。

### 授權與行為準則

送出貢獻，即表示你同意你的貢獻以本專案的 [CC BY-NC-SA 4.0](LICENSE) 授權釋出。參與本專案時，請遵守[行為準則](CODE_OF_CONDUCT.md)。
