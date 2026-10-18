# 寫作規範 / Style Guide

這份規範讓全書的風格保持一致，也讓之後的翻譯更容易。修改或新增內容之前，請先讀一遍。第 1～8 節是繁體中文原文的規範，第 9 節是英文版的規範，第 10 節是日文版與韓文版的格式。

這本書屬於 Introduction 系列，共通的骨架與語氣和[《半導體製造概論》](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction)一致；第 5 節最後的四種區塊，是這本書自己的特色。

Sections 1–8 cover the Traditional Chinese original. Section 9 covers the English version. Section 10 covers Japanese and Korean.

---

## 1. 讀者與深度

- **讀者**：理工背景、但不是 IC 設計專業的人，以及準備進入 IC 設計業的新人。
- **三種讀法**：零基礎的讀者讀正文就夠了；電機、資工系學生可以展開「🔍 深入一點」；軟體與韌體工程師可以特別留意「💻 軟體對照」。
- **深度**：停在「流程、原理、為什麼」。讀完一章，讀者要能說出這一步在做什麼、為什麼要這樣做、做壞了會怎樣。
- **公式**：原則上不寫。數位邏輯與電路學最基本的式子可以用，例如「時脈週期要大於路徑延遲的總和」「動態功耗和電壓的平方成正比」，但一定先用比喻講，再給式子。
- **長度**：一般章節約 150～170 行；有「🧪 跟著做」的章節約 220 行以內。基準是[《半導體製造概論》第 4 章](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/zh-TW/2-process-modules/04-lithography/README.md)。

---

## 2. 用語

### 使用台灣的繁體中文用語

| 使用 | 不使用 |
|---|---|
| 晶片 | 芯片 |
| 下線 | 流片 |
| 佈局 | 版圖 |
| 擺置、繞線 | 布局、布線 |
| 平面規劃 | 布圖規劃 |
| 合成 | 綜合 |
| 模擬 | 仿真 |
| 時脈 | 時鐘 |
| 正反器 | 觸發器 |
| 閂鎖器 | 鎖存器 |
| 暫存器 | 寄存器 |
| 多工器 | 多路選擇器 |
| 管線 | 流水線 |
| 有號數、無號數 | 有符號數、無符號數 |
| 溢位 | 溢出 |
| 匯流排 | 總線 |
| 模組 | 模塊 |
| 矽智財 | IP 核 |
| 標準元件 | 標準單元 |
| 萃取 | 提取 |
| 串音 | 串擾 |
| 程式、程式碼 | 程序、代碼 |
| 軟體、硬體、韌體 | 軟件、硬件、固件 |
| 位元 | 比特 |
| 介面 | 接口 |
| 品質 | 質量 |
| 網路 | 網絡 |
| 預設 | 默認 |
| 資料 | 數據（指 data 時） |

### 術語

- 第一次出現時，寫成「中文（English，縮寫）」，例如「靜態時序分析（Static Timing Analysis，STA）」。
- 之後使用 IC 設計現場實際的說法。現場習慣直接講英文的（例如 RTL、STA、setup、hold、ECO、DRC），就直接使用英文。
- 用詞以[附錄 A 術語總表](zh-TW/appendix/glossary.md)為準。新增術語時，請一併更新術語總表。和《半導體製造概論》重疊的術語（例如光罩、晶粒、電遷移、晶片版本），用詞要和那本書一致。

---

## 3. 排版

- 中文與英文、數字之間加一個半形空格，例如「500 MHz 的時脈」「8 位元的輸入」。
- 數字與單位之間加空格，例如「2 ns」「64 KB」「28 nm」；百分比不加空格，例如「100%」。
- 中文使用全形標點；引號使用「」，引號中再引用使用『』。
- 範圍使用全形波浪號，例如「第 10～13 章」。
- 描述一連串步驟時，先用一行粗體的箭頭流程，例如 **RTL → 合成 → 擺置 → 繞線**，再用編號清單逐步說明。
- 程式碼、檔名、模組名稱與指令用行內程式碼，例如 `mac.v`、`tiny_npu`。

---

## 4. 章節結構

每一章依照以下順序撰寫，可以直接複製[章節範本](templates/chapter-template.md)開始（英文版使用 [chapter-template.en.md](templates/chapter-template.en.md)）：

1. **標題**：`# 第 N 章　主題：副標題`（「章」後面是一個全形空格）
2. **📍 設計位置**
3. **🪜 抽象層級**：位置框下方一行
4. **本文**：依內容分節，大致依照「為什麼需要 → 原理 → 流程 → 關鍵指標 → 常見問題」的順序。
5. **📖 名詞框、🔧 Know-how 框**：放在相關段落的後面。每章各約 2～4 個。
6. **💻 軟體對照**：每章一個，放在最適合對照的段落後面。
7. **🔍 深入一點**：每章 0～2 個，放在相關段落後面。
8. **🧪 跟著做**：只在第 4、6、7、8、15 章，放在「本章重點」之前。
9. **本章重點**：3～5 點。
10. **延伸閱讀**：2～3 項公開資料。和《半導體製造概論》相關的章節，可以列為其中一項。
11. **導覽列**：上一章、目錄、下一章。

---

## 5. 提示框與區塊

### 📍 設計位置

```markdown
> 📍 **設計位置**
>
> - 前一站：……
> - **本章：……**
> - 下一站：……
```

位置框描述主角（`tiny_npu` 這顆晶片與其中的 `mac`）現在走到哪裡。各章的位置要和實際流程的先後一致。

### 📖 名詞框

```markdown
> [!NOTE]
> **📖 名詞｜中文（English，縮寫）**
>
> - **定義**：一句話說明它是什麼。
> - **現場用法**：在 IC 設計現場實際怎麼說，最好附一句例句。
> - **相關名詞**：二到四個相關的術語。
> - **常見混淆**：最容易和什麼搞混，差別在哪裡。
```

### 🔧 Know-how 框

```markdown
> [!TIP]
> **🔧 Know-how｜用一句話點出重點**
>
> - **情境**：在什麼情況下會遇到。
> - **做法**：現場怎麼做。
> - **為什麼**：背後的原因。
> - **沒做會怎樣**：後果是什麼。
> - **相關章節**：[第 N 章 標題](相對路徑)
```

「沒做會怎樣」是 Know-how 框最重要的一欄。設計流程的規則大多是從出事學來的，讀者理解了後果，才記得住規則。

> [!IMPORTANT]
> 框裡的每個欄位都要寫成清單項目，也就是每一行都以 `> -` 開頭。GitHub 顯示 `.md` 檔案時，不會把單一換行顯示成換行；如果不用清單，所有欄位會擠成同一段。

Know-how 只寫業界通用的做法與原則，不寫任何公司的實際參數、內部流程或設計資料。

### 🪜 抽象層級（本書特色）

位置框下方空一行，寫一行抽象層級，把本章所在的層級加粗：

```markdown
🪜 抽象層級：規格 ▸ **RTL** ▸ 網表 ▸ 佈局 ▸ GDS ▸ 晶片
```

一章橫跨兩層時，兩層一起加粗，例如第 7 章的 `規格 ▸ **RTL ▸ 網表** ▸ 佈局 ▸ GDS ▸ 晶片`。

### 💻 軟體對照（本書特色）

```markdown
> [!IMPORTANT]
> **💻 軟體對照｜用一句話點出對照**
>
> - **像什麼**：在軟體開發裡對應的概念。
> - **不一樣的地方**：硬體和軟體真正不同的地方。
> - **所以要注意**：軟體背景的人最容易犯的錯。
```

「不一樣的地方」是這個框的重點。只寫相像之處，會讓讀者帶著錯誤的直覺進入硬體設計。

### 🔍 深入一點（本書特色）

```markdown
<details>
<summary>🔍 深入一點：標題</summary>

內容。寫給電機、資工系學生，跳過不影響閱讀正文。

</details>
```

`<summary>` 後面和 `</details>` 前面都要空一行，GitHub 才會把內容當成 Markdown 顯示。

### 🧪 跟著做（本書特色）

```markdown
## 🧪 跟著做：標題

在 `practice/` 資料夾裡執行：

（指令放在 bash 程式碼區塊，輸出放在 text 程式碼區塊）
```

- 只示範步驟，不出題目。
- 使用開源工具 Icarus Verilog 與 Yosys，安裝方式寫在 [practice/README.md](practice/README.md)。
- 書中的每一段輸出，都必須是實際執行的結果。修改練習檔或輸出之後，執行 `bash practice/run_all.sh` 確認書中的輸出仍然正確。
- 書中的輸出來自 Icarus Verilog 12.0 與 Yosys 0.33。換了版本，第 7、8 章的元件數量與邏輯深度可能略有不同。

### 程式片段

- Verilog 片段每段 15 行以內，放在 `verilog` 程式碼區塊。`scripts/check_book.py` 會檢查這個上限。
- 程式碼裡的註解使用英文，讓所有語言版本可以共用同一段程式碼。

---

## 6. 圖片

- 優先使用 SVG；照片或截圖使用 PNG。
- **圖上不放文字**。需要標示時使用數字編號，在圖下方的說明文字解釋，讓所有語言版本可以共用同一張圖。
- 檔名格式為「章節編號-描述」，例如 `08-setup-hold.svg`，統一放在根目錄的 `images/` 資料夾，所有語言共用。
- 只能使用自己繪製或授權相容的圖片，不可以直接使用書籍、論文、公司網站或 EDA 工具畫面的圖。
- 還沒畫好的圖，先用註解標出位置和內容，例如 `<!-- 圖：時脈樹示意 -->`。執行 `python3 scripts/list_figures.py` 可以列出所有待補的圖。
- 流程圖與方塊圖可以用 Mermaid 繪製，GitHub 會直接顯示，文字也能跟著內文一起翻譯。

圖片的寫法：

```markdown
![替代文字，描述圖片內容](../../../images/08-setup-hold.svg)

*圖說：說明圖中每個編號代表什麼。*
```

---

## 7. 內容原則

- 以流程為主軸，不以公司為主角；不寫特定公司的產品名稱、商標與 EDA 工具名稱。
- 例外：「🧪 跟著做」使用的開源工具（Icarus Verilog、Yosys、GTKWave）可以寫出名稱，但只寫在跟著做、附錄、首頁的練習檔說明，以及 `practice/` 的說明文件裡，正文不寫。產業標準與檔案格式（例如 Verilog、SystemVerilog、UVM、GDSII、OASIS、Liberty、SDC、LEF／DEF、SPEF）不算產品名稱。`practice/README.md` 的安裝說明，也可以寫作業系統與套件管理工具的名稱。
- 引用論文時，不寫和特定公司綁在一起的研討會名稱，只寫作者、篇名與年份。
- 只寫公開資料與業界通用的知識，不寫任何公司的機密，也不寫任何晶圓廠 PDK 裡的實際數值。
- 數字使用量級或概略值，例如「數十億個電晶體」「數百萬美元」。書中 `tiny_npu` 的規格是虛構的教學例子。
- 會隨時間改變的資訊，例如最先進製程的光罩費用，寫成「2020 年代中期」這類較大的範圍，必要時註明「截至某年」。
- 句子盡量短，一句話說一件事。避免雙關、俚語和只有特定地區讀者才懂的梗，翻譯會比較順利。

---

## 8. 連結

- 書內一律使用相對路徑。
- 章節之間的引用寫成 `[第 N 章 標題](../../資料夾/章節資料夾/README.md)`。
- 引用《半導體製造概論》時使用完整網址，寫成 `《半導體製造概論》[第 N 章 標題](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/zh-TW/...)`，各語言版本連到對應語言的資料夾。
- 引用系列的其他書（例如《Git 概論》）也一樣使用完整網址。這些書的 repo 放在這個 repo 旁邊時，`scripts/check_book.py` 也會檢查這些連結，並確認各語言版本連到同一種語言。
- 新增、移動或改名檔案之後，執行 `python3 scripts/check_book.py`，確認沒有失效的連結。

---

## 9. English version

The English version in `en/` is a translation of the Traditional Chinese original in `zh-TW/`. It follows the same structure, depth and principles as sections 1–8.

### Language

- Use American English spelling, such as "color" and "analyze."
- Write short, plain sentences. Prefer everyday words over academic ones.
- Use the terms in [Appendix A: Glossary](en/appendix/glossary.md). Spell out a term with its abbreviation the first time it appears in a chapter, for example "static timing analysis (STA)," and then use the form engineers actually say.
- In the "On the job" field, write how English-speaking chip designers would really say it, not a word-for-word translation of the Chinese. When a Taiwanese expression is useful to know, add it in parentheses, as with 下線 for tape-out.
- Use a space between numbers and units, such as "2 ns" and "64 KB."
- Use an en dash for ranges, such as "Chapters 10–13."

### Chapter structure

- Title: `# Chapter N: Topic — Subtitle`
- 📍 **Where the design is**, with "Previous stop," "**This chapter**" and "Next stop"
- `🪜 Abstraction level: Spec ▸ **RTL** ▸ Netlist ▸ Layout ▸ GDS ▸ Chip`
- `## Key takeaways` (3–5 points) and `## Further reading`
- `## 🧪 Try it: ...` in Chapters 4, 6, 7, 8 and 15
- Navigation bar: `[← Chapter N-1: Title](...) | [Contents](../../README.md) | [Chapter N+1: Title →](...)`
- Figure placeholders: `<!-- Figure: description -->`

### Boxes

```markdown
> [!NOTE]
> **📖 Term | English term (中文術語)**
>
> - **Definition**: One sentence that says what it is.
> - **On the job**: How designers say it, ideally with an example sentence.
> - **Related terms**: Two to four related terms.
> - **Common confusion**: What it is most often confused with, and the difference.
```

```markdown
> [!TIP]
> **🔧 Know-how | One sentence that states the point**
>
> - **Situation**: When you run into it.
> - **Practice**: What design teams do.
> - **Why**: The reason behind it.
> - **If you skip it**: What goes wrong.
> - **Related chapters**: [Chapter N: Title](relative/path/README.md)
```

```markdown
> [!IMPORTANT]
> **💻 Software analogy | One sentence that states the comparison**
>
> - **Like**: The matching idea in software.
> - **Unlike**: Where hardware really differs.
> - **Watch out**: The mistake people with a software background make most often.
```

```markdown
<details>
<summary>🔍 Going deeper: Title</summary>

Content.

</details>
```

As in the Chinese version, every field must be a list item, because GitHub does not render a single line break as a new line in `.md` files.

---

## 10. Japanese and Korean versions

The Japanese (`ja/`) and Korean (`ko/`) versions follow the same structure as the English version. Only the labels differ. `scripts/check_book.py` checks these labels.

| Element | 日本語 (`ja/`) | 한국어 (`ko/`) |
|---|---|---|
| Title | `# 第 N 章　トピック：サブタイトル` | `# 제N장 주제: 부제` |
| Where the design is | 📍 **設計の現在地**（前の工程／**この章**／次の工程） | 📍 **설계의 현재 위치**（이전 단계／**이 장**／다음 단계） |
| Abstraction level | `🪜 抽象度：仕様 ▸ **RTL** ▸ ネットリスト ▸ レイアウト ▸ GDS ▸ チップ` | `🪜 추상화 수준: 사양 ▸ **RTL** ▸ 네트리스트 ▸ 레이아웃 ▸ GDS ▸ 칩` |
| Term box | `**📖 用語｜用語（中文）**`: 定義／現場での使い方／関連用語／よくある混同 | `**📖 용어｜용어（中文）**`: 정의／현장에서는／관련 용어／흔한 혼동 |
| Know-how box | `**🔧 ノウハウ｜要点**`: 状況／やり方／理由／やらないとどうなる／関連する章 | `**🔧 노하우｜요점**`: 상황／방법／이유／안 하면 어떻게 되나／관련 장 |
| Software analogy | `**💻 ソフトウェアとの対比｜要点**`: 似ている点／違う点／だから注意 | `**💻 소프트웨어와 비교｜요점**`: 닮은 점／다른 점／그래서 주의할 점 |
| Going deeper | `🔍 もう一歩深く：タイトル` | `🔍 조금 더 깊이: 제목` |
| Try it | `## 🧪 やってみよう：タイトル` | `## 🧪 따라 해 보기: 제목` |
| End sections | `## この章のポイント`, `## 参考文献` | `## 이 장의 핵심`, `## 참고 자료` |
| Navigation | `[← 第 N 章　タイトル](...) ｜ [目次](../../README.md) ｜ [第 N 章　タイトル →](...)` | `[← 제N장 제목](...) ｜ [목차](../../README.md) ｜ [제N장 제목 →](...)` |
| Style | Prose in です・ます; boxes in plain だ・である | Prose in 합니다체; boxes in plain ~다 |

Use the terms in each language's glossary ([日本語](ja/appendix/glossary.md), [한국어](ko/appendix/glossary.md)).
