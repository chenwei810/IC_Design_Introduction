# 附錄 D　Verilog 速查

本附錄整理書中用到的 Verilog 語法，方便閱讀第 4～8 章與 `practice/` 的程式碼時查詢。完整的語法請見 IEEE 1800 標準。範例裡的註解使用英文，和練習檔一致。

---

## 模組與埠

```verilog
module mac (
    input  wire               clk,
    input  wire signed [7:0]  a,      // 8-bit signed input
    output reg  signed [23:0] acc     // assigned inside an always block
);
    // the circuit goes here
endmodule
```

| 寫法 | 意思 |
|---|---|
| `input`、`output`、`inout` | 埠的方向 |
| `wire` | 連線，由 `assign` 或其他模組的輸出驅動 |
| `reg` | 在 `always` 區塊裡被指定的訊號，不一定會變成正反器 |
| `[7:0]` | 位元寬度，這裡是 8 個位元，最高位元是 7 |
| `signed` | 當成有號數（二補數）解讀，見第 3、6 章 |

## 數值的寫法

| 寫法 | 意思 |
|---|---|
| `8'd42` | 8 位元、十進位的 42 |
| `8'hFF` | 8 位元、十六進位的 FF |
| `4'b1010` | 4 位元、二進位的 1010 |
| `24'sd0` | 24 位元、有號、十進位的 0 |
| `1'bx` | 未知值，只在模擬時出現 |
| `$signed(x)` | 把 `x` 當成有號數，可以合成 |

## 運算子

```verilog
a + b    a - b    a * b          // arithmetic
a & b    a | b    a ^ b    ~a    // bitwise AND, OR, XOR, NOT
a && b   a || b   !a             // logical AND, OR, NOT
a == b   a != b   a < b          // comparison
a << 2   a >> 2   a >>> 2        // shifts; >>> keeps the sign of a signed value
c ? a : b                        // a if c is 1, otherwise b
{a, b}   {4{a}}                  // concatenation and repetition
x[23:16] x[8*i +: 8]             // a fixed slice, and 8 bits starting at bit 8*i
```

運算式裡只要有一個運算元是無號數，整個運算式就會變成無號運算（第 6 章）。

## 描述電路的三種寫法

```verilog
assign y2 = sel ? a : b;                        // combinational: continuous assignment

always @(*) begin                               // combinational: use =
    y = b;                                      // a default value first: no latch
    if (sel) y = a;
end

always @(posedge clk or negedge rst_n) begin    // flip-flops: use <=
    if (!rst_n) q <= 1'b0;
    else        q <= d;
end
```

## 條件與選擇

```verilog
always @(*) begin
    case (state)
        IDLE:    next = start ? LOAD : IDLE;
        LOAD:    next = COMPUTE;
        COMPUTE: next = done ? DONE : COMPUTE;
        default: next = IDLE;                   // always cover every case
    endcase
end
```

## 參數與重複的電路

```verilog
parameter LAT = 1;                              // can be overridden: iverilog -P tb.LAT=2
localparam signed [24:0] MAX = 25'sd8388607;    // a constant inside the module

genvar i;
generate
    for (i = 0; i < 8; i = i + 1) begin : lane
        mac u_mac (.clk(clk), .rst_n(rst_n), .clr(clr), .en(en),
                   .a(act[8*i +: 8]), .b(wgt), .acc(acc[24*i +: 24]));
    end
endgenerate
```

`generate` 裡的 `for` 不是「執行很多次」，而是把電路複製很多份（第 4 章）。

## Testbench 專用的寫法

下面這些寫法只在模擬時有意義，不能合成成 ASIC 的電路。

| 寫法 | 用途 |
|---|---|
| `` `timescale 1ns / 1ps `` | 時間的單位與精確度 |
| `#1` | 等待一段時間 |
| `initial begin ... end` | 模擬開始時執行一次 |
| `@(negedge clk)` | 等到時脈的下降緣 |
| `$display("acc = %0d", acc)` | 印出訊息 |
| `$fopen`、`$fscanf`、`$fclose` | 讀寫檔案，例如讀入向量檔 |
| `$dumpfile`、`$dumpvars` | 記錄波形，存成 VCD 檔 |
| `$value$plusargs`、`$test$plusargs` | 讀取執行時的選項，例如 `+vec=` |
| `$finish` | 結束模擬 |

## 常見錯誤

| 錯誤 | 結果 | 相關章節 |
|---|---|---|
| 有號數忘了宣告 `signed` | 負數被當成很大的正數 | 3、6 |
| 有號數和無號數混在同一個運算式 | 整個運算式變成無號運算 | 6 |
| 組合邏輯的 `if`、`case` 沒寫完整 | 長出閂鎖器 | 4 |
| 正反器用 `=`，或組合邏輯用 `<=` | 模擬和合成的結果不一致 | 4 |
| 結果的位元寬度不夠 | 高位元被截掉，或溢位繞回 | 3、15 |
| 跨時脈域的訊號直接使用 | 亞穩態造成偶發的錯誤 | 5 |
| 用 `/` 或 `%` 做一般的除法 | 合成出又大又慢的除法器 | 7 |

---

[← 附錄 C 延伸閱讀](further-reading.md) ｜ [目錄](../README.md) ｜ [回到起點：第 0 章 IC 設計全景 →](../0-before-you-start/00-overview/README.md)
