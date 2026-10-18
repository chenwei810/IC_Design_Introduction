<!-- source: zh-TW/appendix/verilog-quick-reference.md | sha: 2d8e9f0de079 -->

# 부록 D Verilog 빠른 참조

이 부록에서는 책에서 쓰는 Verilog 문법을 정리합니다. 제4～8장과 `practice/`의 코드를 읽을 때 찾아보세요. 전체 문법은 IEEE 1800 표준을 참고하세요. 예제의 주석은 실습 파일과 마찬가지로 영어입니다.

---

## 모듈과 포트

```verilog
module mac (
    input  wire               clk,
    input  wire signed [7:0]  a,      // 8-bit signed input
    output reg  signed [23:0] acc     // assigned inside an always block
);
    // the circuit goes here
endmodule
```

| 작성법 | 뜻 |
|---|---|
| `input`, `output`, `inout` | 포트의 방향 |
| `wire` | 연결. `assign`이나 다른 모듈의 출력이 구동한다 |
| `reg` | `always` 블록 안에서 대입되는 신호. 꼭 플립플롭이 되는 것은 아니다 |
| `[7:0]` | 비트 폭. 여기서는 8비트이고, 최상위 비트는 7이다 |
| `signed` | 부호 있는 수(2의 보수)로 읽는다. 제3, 6장 참고 |

## 수 쓰는 법

| 작성법 | 뜻 |
|---|---|
| `8'd42` | 8비트, 10진수 42 |
| `8'hFF` | 8비트, 16진수 FF |
| `4'b1010` | 4비트, 2진수 1010 |
| `24'sd0` | 24비트, 부호 있는 10진수 0 |
| `1'bx` | 알 수 없는 값. 시뮬레이션에서만 나타난다 |
| `$signed(x)` | `x`를 부호 있는 수로 다룬다. 합성할 수 있다 |

## 연산자

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

식 안에 부호 없는 피연산자가 하나라도 있으면 식 전체가 부호 없는 연산이 됩니다(제6장).

## 회로를 기술하는 세 가지 작성법

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

## 조건과 선택

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

## 파라미터와 반복되는 회로

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

`generate` 안의 `for`는 '여러 번 실행하는' 것이 아니라, 회로를 여러 벌 복제합니다(제4장).

## 테스트벤치 전용 작성법

다음 작성법은 시뮬레이션에서만 의미가 있으며, ASIC 회로로 합성할 수 없습니다.

| 작성법 | 용도 |
|---|---|
| `` `timescale 1ns / 1ps `` | 시간의 단위와 정밀도 |
| `#1` | 일정 시간 기다린다 |
| `initial begin ... end` | 시뮬레이션이 시작될 때 한 번 실행한다 |
| `@(negedge clk)` | 클록의 하강 에지까지 기다린다 |
| `$display("acc = %0d", acc)` | 메시지를 출력한다 |
| `$fopen`, `$fscanf`, `$fclose` | 파일을 읽고 쓴다. 벡터 파일 읽기 등 |
| `$dumpfile`, `$dumpvars` | 파형을 기록해 VCD 파일로 저장한다 |
| `$value$plusargs`, `$test$plusargs` | 실행할 때의 옵션을 읽는다. `+vec=` 등 |
| `$finish` | 시뮬레이션을 끝낸다 |

## 흔한 실수

| 실수 | 결과 | 관련 장 |
|---|---|---|
| 부호 있는 수에 `signed` 선언을 잊는다 | 음수가 아주 큰 양수로 읽힌다 | 3, 6 |
| 부호 있는 수와 부호 없는 수를 한 식에 섞는다 | 식 전체가 부호 없는 연산이 된다 | 6 |
| 조합 논리의 `if`나 `case`를 다 쓰지 않는다 | 래치가 생긴다 | 4 |
| 플립플롭에 `=`를, 조합 논리에 `<=`를 쓴다 | 시뮬레이션과 논리 합성의 결과가 어긋난다 | 4 |
| 결과의 비트 폭이 모자란다 | 위쪽 비트가 잘려 나가거나, 오버플로해서 랩어라운드한다 | 3, 15 |
| 클록 도메인을 건너는 신호를 그대로 쓴다 | 준안정 상태 때문에 가끔 오류가 난다 | 5 |
| 일반 나눗셈에 `/`나 `%`를 쓴다 | 크고 느린 나눗셈기가 합성된다 | 7 |

---

[← 부록 C 참고 자료](further-reading.md) ｜ [목차](../README.md) ｜ [처음으로: 제0장 IC 설계의 전체 그림 →](../0-before-you-start/00-overview/README.md)
