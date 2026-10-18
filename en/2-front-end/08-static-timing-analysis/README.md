<!-- source: zh-TW/2-front-end/08-static-timing-analysis/README.md | sha: c46d880dc210 -->

# Chapter 8: Static Timing Analysis — Every Path Must Make It in Time

> 📍 **Where the design is**
>
> - Previous stop: logic synthesis, where `mac` became 865 cells
> - **This chapter: checking whether `mac` keeps up at 500 MHz, and adding a pipeline stage**
> - Next stop: design for test, letting the factory find bad chips

🪜 Abstraction level: Spec ▸ RTL ▸ **Netlist** ▸ Layout ▸ GDS ▸ Chip

---

## A relay race: the data must arrive before the next whistle

At every clock edge, flip-flops send out data. The data passes through a chain of combinational logic and must reach the next flip-flop before the next clock edge. It is like a relay race: each runner must hand the baton to the next before the whistle blows.

There are two more rules for the hand-off:

- **Setup**: before the clock edge, the data must be stable for a short time, so that the flip-flop can take a clear picture.
- **Hold**: after the clock edge, the data must stay unchanged for a short time, so that it is not overwritten too soon by the next data.

So the setup requirement can be written as: **clock period ≥ the flip-flop's output delay + the delay of the combinational logic + the setup time**.

![Timing diagram: before and after the clock's rising edge there is a window in which the data must stay stable](../../../images/08-setup-hold.svg)

*Figure: The clock is at the top and the data at the bottom. ① The rising edge of the clock ② Setup time ③ Hold time ④ The period when the data is stable, which must completely cover ② and ③ ⑤ The moment the data changes, which must fall outside ② and ③.*

> [!NOTE]
> **📖 Term | Setup and hold**
>
> - **Definition**: Setup time is how long the data must be stable before the clock edge; hold time is how long it must stay unchanged after the clock edge.
> - **On the job**: "If setup fails, you can lower the clock. If hold fails, the chip is dead."
> - **Related terms**: slack, critical path, clock skew
> - **Common confusion**: Setup violations depend on the clock frequency, and lowering the frequency fixes them. Hold violations do not depend on the frequency, and lowering it does not help.

---

## Static: timing analysis without inputs

Simulation needs inputs, and it cannot exercise every path. **Static timing analysis** (STA) works differently. It runs no inputs at all. Instead, it looks up the delay of each cell in the library, estimates the delay of each wire, and adds up the delay of every path in the chip, one path at a time.

A chip has millions or even billions of paths, and STA can check them all in a few hours.

> [!NOTE]
> **📖 Term | Static timing analysis (STA) (靜態時序分析)**
>
> - **Definition**: A method that computes the delay of every path, one by one, without test inputs, and checks whether setup and hold are met.
> - **On the job**: "STA is done; WNS is still -0.12 ns," "Set this one as a false path in STA."
> - **Related terms**: slack, WNS, TNS, timing constraints
> - **Common confusion**: STA checks only timing, not function. Wrong logic can still pass STA completely.

---

## Slack: how much time is left

Every path has a "latest time the data must arrive" and an "actual arrival time." The difference between the two is the **slack**:

- Positive slack: the data arrives early, with time to spare.
- Negative slack: the data is late, and the path has a violation.

The path with the worst slack is called the **critical path**, and it sets how fast the chip can run. The two numbers people look at most in the reports are **worst negative slack** (WNS) and **total negative slack** (TNS, the sum of all negative slacks). WNS says how far the worst path misses; TNS says how widespread the problem is.

---

## Process corners: even the slowest chip must keep up

Chips made from the same design do not all run at exactly the same speed. The process varies, the voltage drops and the temperature changes. So STA is not run just once, but once for each of several extreme conditions, called **process corners**:

- **Setup** is usually checked at the slowest corner: slow transistors, low voltage, high temperature.
- **Hold** is usually checked at the fastest corner: fast transistors, high voltage, low temperature.

Newer processes, at low voltage, add a counterintuitive effect: circuits can get slower at low temperature, which is called **temperature inversion**. `tiny_npu`, at the 28 nm class, has to account for it too. So there are more corners to check than intuition suggests. Differences between places on the same chip are covered with an extra margin, called **on-chip variation** (OCV).

> [!NOTE]
> **📖 Term | Process corner (製程角落)**
>
> - **Definition**: An analysis condition that combines extreme values of process, voltage and temperature (PVT).
> - **On the job**: Two letters give the speed of the NMOS and PMOS, as in "Setup fails at the SS corner" or "Check hold at the FF corner."
> - **Related terms**: PVT, OCV, multi-corner multi-mode analysis (MCMM)
> - **Common confusion**: A corner is not a corner of the wafer; it is an extreme combination of process, voltage and temperature.

<details>
<summary>🔍 Going deeper: Why hold does not depend on the clock frequency</summary>

Setup asks whether the data launched in this cycle reaches the next flip-flop before the **next** clock edge. A whole period lies in between, so a longer period makes setup easier to meet.

Hold asks whether the new data launched in this cycle arrives so fast that, at the **same** clock edge, it overwrites the old data the next flip-flop has not finished capturing. Launch and capture happen at the same edge, so the period does not appear in the equation at all.

That is why a hold violation can only be fixed by making the path longer, for example by inserting delay buffers. Once the chip is made, only changing the voltage or the temperature affects it a little; there is almost no way to rescue it.

</details>

---

## mac can't keep up: adding a pipeline stage

The critical path of `mac` starts at the inputs `a` and `b`, goes through the multiplier and the adder, and ends at the accumulator flip-flops. In `tiny_npu`, `a` and `b` are the data the SRAMs send every cycle, so they also come from flip-flops. After synthesis, this path is as long as 32 levels of logic gates. At an average of 70 ps per level, the logic alone takes 2.24 ns, already more than the 2 ns period of 500 MHz.

The fix is to insert a row of flip-flops between the multiplier and the adder, cutting one long path into two. This is called a **pipeline**. Here is the first stage of `rtl/mac_ch08.v`:

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

The second stage then adds `prod` into the accumulator. The longest path drops from 32 levels to 24; the longest part is now the multiplier, and the loop from the adder back to the accumulator is much shorter. The cost is 18 more flip-flops (the 16-bit product plus two control signals delayed by one cycle), and the result comes out one cycle later: the **latency** grows from 1 cycle to 2. Each cycle still completes one multiply-accumulate, so the **throughput** is unchanged.

> [!IMPORTANT]
> **💻 Software analogy | A pipeline is like a CPU's instruction pipeline, but nobody handles the latency for you**
>
> - **Like**: A CPU splits each instruction into several stages and, like an assembly line, works on several instructions at once.
> - **Unlike**: When you add a pipeline stage in RTL, everything that depends on "how many cycles until the result" has to change: the control logic must wait one more cycle, the testbench must compare one cycle later, and the firmware's assumptions may need updating too. Nothing adjusts itself for you.
> - **Watch out**: When you change the pipeline depth, find everything that depends on it and rerun verification. The Try-it section shows what happens if you forget the testbench.

---

## Timing closure

Fixing every violation until no slack is negative is called **timing closure**. Common techniques include changing the RTL architecture or adding pipeline stages, swapping cells for stronger ones, and using low-Vt cells on critical paths; hold violations are fixed by inserting delay buffers.

STA after synthesis can only estimate wire delays. After the real wires are in place in Chapter 12, it has to be done again with the extracted values.

> [!TIP]
> **🔧 Know-how | Fix big timing problems at the RTL stage**
>
> - **Situation**: STA after synthesis shows the critical path missing by several hundred picoseconds.
> - **Practice**: Go back to the RTL and change the architecture or add a pipeline stage. Reserve part of the period at synthesis as margin for the wire delays to come.
> - **Why**: Back-end tools are good at fixing small violations, by resizing and moving cells, for example. A path that misses by a lot can be fixed only by changing the logic structure.
> - **If you skip it**: The back-end team spends weeks trying, still has to go back and change the RTL in the end, and the whole schedule slips.
> - **Related chapters**: [Chapter 12: Routing and Parasitics](../../3-physical-design/12-routing-and-parasitics/README.md)

> [!TIP]
> **🔧 Know-how | Clear every hold violation before tape-out**
>
> - **Situation**: Just before tape-out, a few hold violations miss by only a little, and someone suggests leaving them.
> - **Practice**: Fix hold at every corner until there are no violations. Never count on "lowering the clock when the chips come back."
> - **Why**: Not enough setup margin means you can run the chip slower; hold does not depend on the frequency, so slowing down does not help.
> - **If you skip it**: When the chips come back, they fail no matter how slowly they run, and the only fix is new masks.
> - **Related chapters**: [Chapter 13: Signoff](../../3-physical-design/13-signoff/README.md)

---

## 🧪 Try it: Compare logic depth and verify the pipeline

This exercise is not connected to the delay data of a real cell library, so here **logic depth** (how many levels of logic gates a path passes through) stands in for delay. In the `practice/` folder, compare the longest path before and after the pipeline:

```bash
yosys -q -p "read_verilog rtl/mac_ch06.v; synth -top mac; tee -o /dev/stdout ltp -noff" | grep Longest
yosys -q -p "read_verilog rtl/mac_ch08.v; synth -top mac; tee -o /dev/stdout ltp -noff" | grep Longest
```

```text
Longest topological path in mac (length=32):
Longest topological path in mac (length=24):
```

With other versions of Yosys, the logic depths may differ slightly. Next, test the pipelined `mac` with the testbench from Chapter 6:

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

`mac` did not compute anything wrong: the 6,223 it shows at line 3 is exactly the answer for line 2. The result comes one cycle later, but the testbench still compares at the old time. Tell the testbench that the latency is now 2 cycles and run it again:

```bash
iverilog -P tb.LAT=2 -o sim rtl/mac_ch08.v tb/tb_mac.v
vvp sim +vec=vectors/random.txt
```

```text
PASS: 208 of 208 checks passed
```

This pipelined version is the one that will be taped out.

---

## Key takeaways

1. Data must arrive before the next clock edge and meet setup and hold; the period must be longer than the sum of the delays along the path.
2. STA needs no inputs. It computes the slack of every path, one by one, and checks it at several process corners.
3. Setup violations can be fixed by lowering the frequency; hold violations do not depend on the frequency and must be cleared before tape-out.
4. At 500 MHz, the path in `mac` is too long. After one pipeline stage, the logic depth drops from 32 levels to 24, and the result comes out one cycle later.
5. After the pipeline depth changes, everything that depends on the latency must be updated and verified again.

---

## Further reading

- J. Bhasker and Rakesh Chadha, *Static Timing Analysis for Nanometer Designs: A Practical Approach*
- Neil H. E. Weste and David Money Harris, *CMOS VLSI Design: A Circuits and Systems Perspective*, 4th edition, Chapter 10

---

[← Chapter 7: Logic Synthesis](../07-logic-synthesis/README.md) | [Contents](../../README.md) | [Chapter 9: Design for Test →](../09-design-for-test/README.md)
