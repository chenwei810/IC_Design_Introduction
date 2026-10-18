<!-- source: zh-TW/appendix/verilog-quick-reference.md | sha: 2d8e9f0de079 -->

# 付録 D　Verilog クイックリファレンス

この付録では、本書で使う Verilog の文法をまとめます。第 4～8 章や `practice/` のコードを読むときに引いてください。完全な文法は IEEE 1800 規格を参照してください。例の中のコメントは、練習ファイルと同じく英語です。

---

## モジュールとポート

```verilog
module mac (
    input  wire               clk,
    input  wire signed [7:0]  a,      // 8-bit signed input
    output reg  signed [23:0] acc     // assigned inside an always block
);
    // the circuit goes here
endmodule
```

| 書き方 | 意味 |
|---|---|
| `input`、`output`、`inout` | ポートの向き |
| `wire` | 接続。`assign` やほかのモジュールの出力で駆動される |
| `reg` | `always` ブロックの中で代入される信号。必ずしもフリップフロップになるとは限らない |
| `[7:0]` | ビット幅。ここでは 8 ビットで、最上位ビットは 7 |
| `signed` | 符号付きの数（2 の補数）として読む。第 3、6 章を参照 |

## 数値の書き方

| 書き方 | 意味 |
|---|---|
| `8'd42` | 8 ビット、10 進数の 42 |
| `8'hFF` | 8 ビット、16 進数の FF |
| `4'b1010` | 4 ビット、2 進数の 1010 |
| `24'sd0` | 24 ビット、符号付き、10 進数の 0 |
| `1'bx` | 不定値。シミュレーションでだけ現れる |
| `$signed(x)` | `x` を符号付きの数として扱う。合成できる |

## 演算子

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

式の中にオペランドが一つでも符号なしのものがあれば、式全体が符号なしの演算になります（第 6 章）。

## 回路を記述する三つの書き方

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

## 条件と選択

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

## パラメータと繰り返しの回路

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

`generate` の中の `for` は「何回も実行する」のではなく、回路を何組も複製します（第 4 章）。

## テストベンチ専用の書き方

次の書き方はシミュレーションでだけ意味を持ち、ASIC の回路には合成できません。

| 書き方 | 用途 |
|---|---|
| `` `timescale 1ns / 1ps `` | 時間の単位と精度 |
| `#1` | 一定の時間待つ |
| `initial begin ... end` | シミュレーションの開始時に 1 回実行する |
| `@(negedge clk)` | クロックの立ち下がりエッジまで待つ |
| `$display("acc = %0d", acc)` | メッセージを表示する |
| `$fopen`、`$fscanf`、`$fclose` | ファイルを読み書きする。ベクタファイルの読み込みなど |
| `$dumpfile`、`$dumpvars` | 波形を記録し、VCD ファイルに保存する |
| `$value$plusargs`、`$test$plusargs` | 実行時のオプションを読む。`+vec=` など |
| `$finish` | シミュレーションを終える |

## よくある誤り

| 誤り | 結果 | 関連する章 |
|---|---|---|
| 符号付きの数に `signed` を宣言し忘れる | 負の数がとても大きな正の数として読まれる | 3、6 |
| 符号付きと符号なしの数を同じ式に混ぜる | 式全体が符号なしの演算になる | 6 |
| 組み合わせ回路の `if` や `case` を書ききらない | ラッチができる | 4 |
| フリップフロップに `=` を、組み合わせ回路に `<=` を使う | シミュレーションと論理合成の結果が食い違う | 4 |
| 結果のビット幅が足りない | 上位ビットが切り捨てられる。またはオーバーフローしてラップアラウンドする | 3、15 |
| クロックドメインをまたぐ信号をそのまま使う | メタステーブルでときどき誤りが起きる | 5 |
| ふつうの割り算に `/` や `%` を使う | 大きくて遅い除算器が合成される | 7 |

---

[← 付録 C　参考文献](further-reading.md) ｜ [目次](../README.md) ｜ [出発点に戻る：第 0 章　IC 設計の全体像 →](../0-before-you-start/00-overview/README.md)
