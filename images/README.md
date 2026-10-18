# 圖片 / Images

全書共用的圖片都放在這個資料夾。中文版、英文版和之後的每一種語言都使用同一套圖片，所以**圖上不放文字**；需要標示時使用數字編號，在各語言的圖說中解釋。

All images are shared by every language version, so **images contain no text**. Use numbers as labels and explain them in the caption of each language.

---

## 規範 / Guidelines

| 項目 Item | 規則 Rule |
|---|---|
| 格式 Format | 優先使用 SVG / SVG preferred |
| 截圖 Screenshots | 不放任何 EDA 工具的截圖，改畫簡化的示意圖 / No screenshots of EDA tools; draw simplified diagrams instead |
| 檔名 File name | 「章節編號-描述」，例如 `08-setup-hold.svg` / chapter number and description |
| 文字 Text | 圖上不放文字，只用數字編號 / No text in images, numbers only |
| 顏色 Color | 使用淺色底卡，在 GitHub 的淺色與深色主題下都看得清楚；不要只靠紅綠色區分 / Use a light card background so the figure reads in both light and dark themes; never rely on red versus green alone |
| 授權 License | 只能使用自己繪製或授權相容的圖片，不可以使用書籍、論文、公司網站或 EDA 工具畫面的圖 / Only images you drew yourself or that have a compatible license |

從章節引用圖片的寫法（每種語言的路徑都一樣） / Referencing an image from a chapter (the path is the same in every language):

```markdown
![替代文字 / alt text](../../../images/08-setup-hold.svg)

*圖說：① ……；② ……。*
```

---

## 已完成的圖 / Finished images

| 檔案 File | 用在哪裡 Used in |
|---|---|
| `cover.svg` | 首頁封面：晶片的平面規劃，被標示出來的是本書的主角 `mac` / Cover on the home pages: a chip floorplan, with the book's `mac` highlighted |
| `social-preview.png` | GitHub 社群預覽圖，在 Settings → General → Social preview 上傳。只用於社群分享，所以含有文字 / GitHub social preview, uploaded under Settings → General → Social preview. It contains text because it is only used for sharing |
| `02-cmos-inverter.svg` | 第 2 章，CMOS 反相器 / Chapter 2, a CMOS inverter |
| `08-setup-hold.svg` | 第 8 章，setup 與 hold 的時間窗 / Chapter 8, the setup and hold window |
| `10-floorplan.svg` | 第 10 章，`tiny_npu` 的平面規劃 / Chapter 10, the floorplan of `tiny_npu` |

流程圖、方塊圖和狀態圖都用 Mermaid 直接寫在章節裡，不另外存成圖片，文字也能跟著內文一起翻譯。

Flowcharts, block diagrams and state diagrams are written in the chapters with Mermaid, not stored as images, so their labels are translated with the text.

---

## 待補的圖 / Figures to draw

目前沒有待補的圖。新增圖片時，先在章節裡用 `<!-- 圖：… -->` 標出位置（英文版是 `<!-- Figure: … -->`），再用下面的指令列出清單。

There are no figures left to draw. When you plan a new figure, mark it with `<!-- 圖：… -->` (`<!-- Figure: … -->` in English) and list the placeholders with:

```bash
python3 scripts/list_figures.py --markdown
```
