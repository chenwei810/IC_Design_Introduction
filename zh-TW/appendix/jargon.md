# 附錄 B　設計現場行話

IC 設計團隊的日常溝通，常常是中文夾雜英文，例如「這條 path 的 slack 爆了，中間切一刀吧」。剛加入團隊的人第一次聽到，常常一頭霧水。

本附錄收錄 IC 設計現場常聽到的說法，並附上例句。各公司、各團隊的習慣用語不完全相同，這裡整理的是普遍的講法。正式的術語定義請見[附錄 A 術語總表](glossary.md)。

---

## 流程與時程

| 行話 | 意思 | 例句 |
|---|---|---|
| spec | 規格書 | 「spec 寫的是飽和，RTL 怎麼做成繞回？」 |
| freeze | 凍結，之後不能隨意修改 | 「RTL freeze 之後，任何修改都要走 ECO。」 |
| 下線、tape-out | 把設計交給晶圓廠 | 「下個月就要下線了，這週把 signoff 收一收。」 |
| shuttle | MPW 的班次 | 「趕不上這班 shuttle，就要再等兩個月。」 |
| signoff | 簽核，某一項檢查正式通過 | 「DRC 已經 signoff 了，剩下 IR。」 |
| 打回前段 | 問題大到要回頭改 RTL | 「差了這麼多，只能打回前段改架構。」 |

## 前段設計

| 行話 | 意思 | 例句 |
|---|---|---|
| instantiate、instance | 放一個模組的實例；實例本身 | 「頂層 instantiate 了 64 個 `mac`。」 |
| lint 一下 | 跑 Lint 檢查寫法 | 「送合成之前，先 lint 一下。」 |
| 長出 latch | 合成時意外產生閂鎖器 | 「`case` 沒寫 `default`，長出一顆 latch。」 |
| 被 optimize 掉 | 被合成工具刪掉 | 「這個 register 被 optimize 掉了，你的輸出沒接。」 |
| 過 CDC | 跨時脈域的訊號經過同步器處理 | 「`START` 是從匯流排側來的，要過 CDC。」 |
| meta | 亞穩態 | 「第一級 flop 可能 meta，不要直接拿去用。」 |

## 驗證

| 行話 | 意思 | 例句 |
|---|---|---|
| TB | Testbench | 「TB 先接起來，跑個 smoke test。」 |
| smoke test | 最基本、跑最快的測試，確認沒有大問題 | 「smoke test 都過不了，先別跑 regression。」 |
| golden、golden model | 參考模型 | 「RTL 跟 golden 對不起來。」 |
| 跑 regression | 跑回歸測試 | 「今晚的 regression 掛了三個。」 |
| 掛了 | 測試失敗 | 「seed 7 那個掛了，我來看。」 |
| seed | 亂數種子 | 「把 seed 給我，我重跑一次。」 |
| cover 到 | 覆蓋率有量到 | 「溢位這個 case 沒有 cover 到。」 |
| dump 波形 | 把模擬的波形存下來除錯 | 「dump 波形出來看就知道了。」 |
| corner case | 很少發生的邊界情況 | 「`LEN` 是 0 的 corner case 有測嗎？」 |

## 時序與後段

| 行話 | 意思 | 例句 |
|---|---|---|
| 收 timing | 把時序違規修到沒有 | 「後段還在收 timing，網表先不要動。」 |
| violation | 違規 | 「setup 還有兩百條 violation。」 |
| slack 爆了 | slack 是負的，而且差很多 | 「這條 slack 爆了 0.3 ns。」 |
| 切一刀 | 插入一級管線 | 「乘法加加法太長，中間切一刀。」 |
| 補 hold buffer | 插入延遲緩衝器修 hold | 「CTS 完再來補 hold buffer。」 |
| P&R、APR | 擺置與繞線 | 「這一版 P&R 跑了一整晚。」 |
| 塞爆 | 擁塞到繞不過去 | 「MAC 陣列旁邊塞爆了。」 |
| 抽 RC | 寄生萃取 | 「抽完 RC，timing 又掉了。」 |
| clean | 檢查完全沒有違規 | 「LVS 終於 clean 了。」 |
| waive 掉 | 列入豁免 | 「`LEN` 在 `START` 之前就固定了，這條 CDC 可以 waive 掉。」 |

## 晶片回來之後

| 行話 | 意思 | 例句 |
|---|---|---|
| 樣品回來了 | 第一批晶片送回實驗室 | 「樣品下週回來，板子要先準備好。」 |
| 點亮 | 第一次通電，確認基本功能 | 「第一天就點亮了，PLL 有 lock。」 |
| 跑 shmoo | 量測電壓與頻率的工作範圍 | 「先跑 shmoo，看低電壓的邊界在哪裡。」 |
| 繞過、workaround | 用韌體或軟體避開硬體的錯誤 | 「這版先用韌體繞過，A1 再修。」 |
| metal fix | 只改金屬層的修正 | 「這個 bug 走 metal fix 就好，不用全部重下。」 |
| full respin | 從底層開始重做所有光罩 | 「要改到電晶體那幾層，只能 full respin 了。」 |
| A0、A1、B0 | 晶片版本 | 「A2 如果還要修，只要換三層金屬光罩。」 |

---

[← 附錄 A 術語總表](glossary.md) ｜ [目錄](../README.md) ｜ [附錄 C 延伸閱讀 →](further-reading.md)
