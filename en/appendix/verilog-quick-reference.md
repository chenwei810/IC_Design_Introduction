<!-- source: zh-TW/appendix/verilog-quick-reference.md | sha: 2d8e9f0de079 -->

# Appendix D: Verilog Quick Reference

This appendix collects the Verilog syntax used in the book, for quick lookup while reading Chapters 4–8 and the code in `practice/`. For the full syntax, see the IEEE 1800 standard. The comments in the examples are in English, as in the practice files.

---

## Modules and ports

```verilog
module mac (
    input  wire               clk,
    input  wire signed [7:0]  a,      // 8-bit signed input
    output reg  signed [23:0] acc     // assigned inside an always block
);
    // the circuit goes here
endmodule
```

| Syntax | Meaning |
|---|---|
| `input`, `output`, `inout` | The direction of a port |
| `wire` | A connection, driven by `assign` or by the output of another module |
| `reg` | A signal assigned inside an `always` block; it does not necessarily become a flip-flop |
| `[7:0]` | The bit width: here 8 bits, with bit 7 as the most significant |
| `signed` | Read as a signed number (two's complement); see Chapters 3 and 6 |

## Writing numbers

| Syntax | Meaning |
|---|---|
| `8'd42` | 42 in decimal, 8 bits wide |
| `8'hFF` | FF in hexadecimal, 8 bits wide |
| `4'b1010` | 1010 in binary, 4 bits wide |
| `24'sd0` | 0 in decimal, signed, 24 bits wide |
| `1'bx` | An unknown value; appears only in simulation |
| `$signed(x)` | Treat `x` as a signed number; synthesizable |

## Operators

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

If even one operand in an expression is unsigned, the whole expression is evaluated as unsigned (Chapter 6).

## Three ways to describe a circuit

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

## Conditions and selection

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

## Parameters and repeated circuits

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

A `for` inside `generate` does not "run many times." It makes many copies of the circuit (Chapter 4).

## Testbench-only syntax

The following only have meaning in simulation. They cannot be synthesized into an ASIC circuit.

| Syntax | Purpose |
|---|---|
| `` `timescale 1ns / 1ps `` | The unit and precision of time |
| `#1` | Wait for a period of time |
| `initial begin ... end` | Run once when simulation starts |
| `@(negedge clk)` | Wait for the falling edge of the clock |
| `$display("acc = %0d", acc)` | Print a message |
| `$fopen`, `$fscanf`, `$fclose` | Read and write files, such as a vector file |
| `$dumpfile`, `$dumpvars` | Record waveforms into a VCD file |
| `$value$plusargs`, `$test$plusargs` | Read run-time options, such as `+vec=` |
| `$finish` | End the simulation |

## Common mistakes

| Mistake | Result | Chapters |
|---|---|---|
| Forgetting to declare a signed number `signed` | Negative numbers are read as very large positive numbers | 3, 6 |
| Mixing signed and unsigned values in one expression | The whole expression becomes unsigned | 6 |
| An incomplete `if` or `case` in combinational logic | A latch is inferred | 4 |
| Using `=` for flip-flops, or `<=` for combinational logic | Simulation and synthesis disagree | 4 |
| A result that is not wide enough | The top bits are cut off, or the value overflows and wraps around | 3, 15 |
| Using a signal from another clock domain directly | Metastability causes occasional errors | 5 |
| Using `/` or `%` for general division | Synthesizes a large, slow divider | 7 |

---

[← Appendix C: Further Reading](further-reading.md) | [Contents](../README.md) | [Back to the start: Chapter 0: The Big Picture →](../0-before-you-start/00-overview/README.md)
