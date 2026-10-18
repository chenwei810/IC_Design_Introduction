# 第 8 章　靜態時序分析：每一條路徑都要趕得上

> 📍 **設計位置**
>
> - 前一站：邏輯合成，`mac` 變成了 865 個元件
> - **本章：檢查 `mac` 在 500 MHz 下趕不趕得上，並插入一級管線**
> - 下一站：可測試性設計，讓工廠測得出壞掉的晶片

🪜 抽象層級：規格 ▸ RTL ▸ **網表** ▸ 佈局 ▸ GDS ▸ 晶片

---

## 接力賽：資料要在下一聲哨響前抵達

每個時脈邊緣，正反器送出資料。資料穿過一串組合邏輯，必須在下一個時脈邊緣之前抵達下一個正反器。這很像接力賽：每一棒都要在哨音響起前，把棒子交到下一位跑者手上。

交棒還有兩個規矩：

- **Setup**：時脈邊緣之前，資料要先穩定一小段時間，正反器才拍得清楚。
- **Hold**：時脈邊緣之後，資料還要保持不變一小段時間，不能太快被下一筆資料蓋掉。

所以 setup 的要求可以寫成：**時脈週期 ≥ 正反器的輸出延遲 ＋ 組合邏輯的延遲 ＋ setup 時間**。

![時序圖：時脈上升緣前後，各有一段資料必須保持穩定的時間](../../../images/08-setup-hold.svg)

*圖說：上方是時脈，下方是資料。① 時脈的上升緣；② setup 時間；③ hold 時間；④ 資料保持穩定的期間，必須完整蓋住 ② 和 ③；⑤ 資料改變的時刻，只能落在 ② 和 ③ 之外。*

> [!NOTE]
> **📖 名詞｜Setup 與 Hold**
>
> - **定義**：setup time 是時脈邊緣之前資料必須穩定的時間；hold time 是時脈邊緣之後資料必須保持不變的時間。
> - **現場用法**：「setup 不過可以降頻，hold 不過晶片就不能用了。」
> - **相關名詞**：slack、關鍵路徑、時脈偏移
> - **常見混淆**：setup 違規和時脈頻率有關，降低頻率就能解決；hold 違規和頻率無關，降頻也救不回來。

---

## 靜態：不用輸入的時序分析

模擬需要輸入，而且不可能測遍每一條路徑。**靜態時序分析**（Static Timing Analysis，STA）換了一種做法：它不跑任何輸入，而是查元件庫裡每個元件的延遲，再估算每段導線的延遲，把晶片裡每一條路徑的延遲一條一條加起來。

一顆晶片有數百萬條甚至數十億條路徑，STA 可以在幾小時內全部檢查完。

> [!NOTE]
> **📖 名詞｜靜態時序分析（Static Timing Analysis，STA）**
>
> - **定義**：不需要測試輸入，逐條計算每一條路徑的延遲，檢查是否滿足 setup 與 hold 的方法。
> - **現場用法**：「STA 跑完了，WNS 還有 -0.12 ns」「這條要在 STA 裡設成 false path」。
> - **相關名詞**：slack、WNS、TNS、時序限制
> - **常見混淆**：STA 只管時序，不管功能。邏輯寫錯了，STA 照樣可以全部通過。

---

## Slack：還剩多少時間

每條路徑都有一個「最晚必須抵達的時間」和「實際抵達的時間」，兩者相減就是 **slack**：

- slack 是正的：資料提早到了，還有餘裕。
- slack 是負的：資料遲到，這條路徑違規了。

slack 最差的那條路徑叫做**關鍵路徑**（Critical Path），它決定晶片能跑多快。報告裡最常看的兩個數字是**最差負 slack**（Worst Negative Slack，WNS）和**總負 slack**（Total Negative Slack，TNS）：WNS 說明最糟的路徑差多少，TNS 說明問題有多普遍。

---

## 製程角落：最慢的晶片也要趕得上

同一個設計做出來的晶片，速度不會完全一樣。製程有變異，電壓會下降，溫度也會變化。所以 STA 不是只算一次，而是在好幾種極端條件下各算一次，這些條件叫做**製程角落**：

- **setup** 通常在最慢的角落檢查：電晶體偏慢、電壓偏低、溫度偏高。
- **hold** 通常在最快的角落檢查：電晶體偏快、電壓偏高、溫度偏低。

較新的製程在低電壓時，還有一個反直覺的現象：低溫時電路反而變慢，叫做**溫度反轉**（Temperature Inversion）。28 nm 等級的 `tiny_npu` 也要考慮它。所以要檢查的角落比直覺想到的更多。同一顆晶片上不同位置的差異，則用**晶片上變異**（On-Chip Variation，OCV）的方式另外加上餘裕。

> [!NOTE]
> **📖 名詞｜製程角落（Process Corner）**
>
> - **定義**：由製程、電壓、溫度（PVT）的極端值組合出來的分析條件。
> - **現場用法**：用兩個字母表示 NMOS 和 PMOS 的快慢，例如「SS corner 的 setup 不過」「FF corner 查 hold」。
> - **相關名詞**：PVT、OCV、多模式多角落分析（MCMM）
> - **常見混淆**：corner 不是晶圓上的角落，而是製程、電壓和溫度組合出來的極端情況。

<details>
<summary>🔍 深入一點：為什麼 hold 和時脈頻率無關</summary>

setup 比較的是：這一拍送出的資料，能不能在**下一個**時脈邊緣之前到達。中間隔了一整個週期，所以週期變長，setup 就變得容易滿足。

hold 比較的是：這一拍送出的新資料，會不會太快抵達，在**同一個**時脈邊緣把下一個正反器還沒拍穩的舊資料蓋掉。送出和接收發生在同一個邊緣，算式裡根本沒有週期這一項。

所以 hold 違規主要靠加長資料路徑來修，例如插入延遲用的緩衝器。晶片做出來之後，只有改變電壓或溫度能稍微影響它，幾乎沒有補救的辦法。

</details>

---

## mac 趕不上：插一級管線

`mac` 的關鍵路徑，從輸入 `a`、`b` 出發，經過乘法器和加法器，抵達累加器的正反器。在 `tiny_npu` 裡，`a`、`b` 是 SRAM 每一拍送出的資料，也來自正反器。合成後，這條路徑最長有 32 級邏輯閘。如果每一級平均 70 ps，光邏輯就要 2.24 ns，已經超過 500 MHz 的 2 ns 週期。

修法是在乘法器和加法器之間插入一排正反器，把一條長路徑切成兩段，叫做**管線**（Pipeline）。這是 `rtl/mac_ch08.v` 的第一段：

```verilog
    // Stage 1: multiply, and delay the control signals to match.
    reg signed [15:0] prod;
    reg               clr_d, en_d;
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            prod  <= 16'sd0;
            clr_d <= 1'b0;
            en_d  <= 1'b0;
        end else begin
            prod  <= a * b;
            clr_d <= clr;
            en_d  <= en;
        end
    end
```

第二段再把 `prod` 加進累加器。最長的路徑從 32 級降到 24 級，現在最長的是乘法器那一段，加法器接回累加器的那一圈短得多。代價是多了 18 個正反器（16 位元的乘積，加上兩個跟著延遲一拍的控制訊號），而且結果晚一拍才出來，也就是**延遲拍數**（Latency）從 1 拍變成 2 拍。每一拍仍然完成一次乘加，所以**吞吐量**（Throughput）沒有變。

> [!IMPORTANT]
> **💻 軟體對照｜管線就像 CPU 的指令管線，但沒有人幫你處理延遲**
>
> - **像什麼**：CPU 把一道指令拆成好幾個階段，像生產線一樣同時處理好幾道指令。
> - **不一樣的地方**：在 RTL 裡插一級管線，所有依賴「幾拍後出結果」的地方都要跟著改：控制電路要多等一拍、Testbench 要晚一拍比對，韌體的假設也可能要更新。沒有任何東西會自動幫你調整。
> - **所以要注意**：改了管線深度，就要找出所有依賴它的地方，並重跑驗證。跟著做會看到，沒改 Testbench 會發生什麼事。

---

## 時序收斂

把所有違規修到 slack 都不是負的，叫做**時序收斂**（Timing Closure）。常見的手段有：改 RTL 架構或插管線、把元件換成驅動能力更大的、把關鍵路徑上的元件換成低 Vt 的；hold 違規則插入延遲用的緩衝器。

合成後的 STA 只能估計導線的延遲。第 12 章接上真正的導線之後，還要用萃取出來的數值再做一次。

> [!TIP]
> **🔧 Know-how｜大的時序問題，要在 RTL 階段解決**
>
> - **情境**：合成後的 STA 顯示，關鍵路徑差了好幾百皮秒。
> - **做法**：回到 RTL 改架構或插管線；合成階段就預留一部分週期，當作之後導線延遲的餘裕。
> - **為什麼**：後段工具擅長修小的違規，例如調整元件大小和位置；差太多的路徑，只能靠改邏輯結構。
> - **沒做會怎樣**：後段花了好幾週反覆嘗試，最後還是得回頭改 RTL，時程全部往後延。
> - **相關章節**：[第 12 章 繞線與寄生效應](../../3-physical-design/12-routing-and-parasitics/README.md)

> [!TIP]
> **🔧 Know-how｜hold 違規一定要在下線前全部清掉**
>
> - **情境**：下線前，有幾條 hold 違規只差一點點，有人提議先不管。
> - **做法**：每一個角落的 hold 都要修到沒有違規，不能抱著「回來再降頻」的想法。
> - **為什麼**：setup 不夠可以降頻使用；hold 和頻率無關，降頻也沒有用。
> - **沒做會怎樣**：晶片回來後，不管跑多慢都會出錯，只能重做光罩。
> - **相關章節**：[第 13 章 簽核](../../3-physical-design/13-signoff/README.md)

---

## 🧪 跟著做：比較邏輯深度，並驗證管線

這個練習沒有接上真正元件庫的延遲資料，所以這裡用**邏輯深度**（路徑上經過幾級邏輯閘）代替延遲。在 `practice/` 資料夾裡，比較管線前後的最長路徑：

```bash
yosys -q -p "read_verilog rtl/mac_ch06.v; synth -top mac; tee -o /dev/stdout ltp -noff" | grep Longest
yosys -q -p "read_verilog rtl/mac_ch08.v; synth -top mac; tee -o /dev/stdout ltp -noff" | grep Longest
```

```text
Longest topological path in mac (length=32):
Longest topological path in mac (length=24):
```

換用其他版本的 Yosys，邏輯深度可能略有不同。接著，用第 6 章的 Testbench 測試管線版的 `mac`：

```bash
iverilog -o sim rtl/mac_ch08.v tb/tb_mac.v
vvp sim +vec=vectors/random.txt
```

```text
MISMATCH at line 2: a = -127, b = -49, expected 6223, got 0
MISMATCH at line 3: a = 80, b = 50, expected 10223, got 6223
MISMATCH at line 4: a = -12, b = -73, expected 11099, got 10223
FAIL: 188 of 208 checks failed
```

`mac` 沒有算錯：第 3 行拿到的 6,223，正是第 2 行的答案。結果晚了一拍，Testbench 卻還在原來的時間比對。告訴 Testbench 延遲變成 2 拍，再跑一次：

```bash
iverilog -P tb.LAT=2 -o sim rtl/mac_ch08.v tb/tb_mac.v
vvp sim +vec=vectors/random.txt
```

```text
PASS: 208 of 208 checks passed
```

這個管線版，就是之後要拿去下線的版本。

---

## 本章重點

1. 資料必須在下一個時脈邊緣前抵達，並滿足 setup 與 hold；週期要大於路徑上的延遲總和。
2. STA 不需要輸入，逐條計算每一條路徑的 slack，並在多個製程角落下檢查。
3. setup 違規可以降頻解決，hold 違規和頻率無關，下線前一定要清掉。
4. `mac` 在 500 MHz 下路徑太長，插入一級管線後，邏輯深度從 32 級降到 24 級，結果晚一拍出來。
5. 管線深度改變後，所有依賴延遲的地方都要跟著修改並重新驗證。

---

## 延伸閱讀

- J. Bhasker、Rakesh Chadha，《Static Timing Analysis for Nanometer Designs: A Practical Approach》
- Neil H. E. Weste、David Money Harris，《CMOS VLSI Design: A Circuits and Systems Perspective》第四版，第 10 章

---

[← 上一章：第 7 章 邏輯合成](../07-logic-synthesis/README.md) ｜ [目錄](../../README.md) ｜ [下一章：第 9 章 可測試性設計 →](../09-design-for-test/README.md)
