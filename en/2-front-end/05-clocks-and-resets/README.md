<!-- source: zh-TW/2-front-end/05-clocks-and-resets/README.md | sha: 9038c71fcf5d -->

# Chapter 5: Clocks and Resets — Keeping Every Flip-Flop in Step

> 📍 **Where the design is**
>
> - Previous stop: RTL and Verilog, where `mac` got its first answer right in a simulator
> - **This chapter: following the two clock domains in the spec, adding synchronizers, reset synchronization and clock gating to `tiny_npu`**
> - Next stop: verification, testing `mac` with two hundred random inputs

🪜 Abstraction level: Spec ▸ **RTL** ▸ Netlist ▸ Layout ▸ GDS ▸ Chip

---

## Where the clock comes from

A crystal oscillator on the circuit board provides a very stable reference clock, but not a fast one. A **PLL** on the chip multiplies it up to 500 MHz and sends it to the MAC array, the SRAMs and the control logic.

On the other side, the CPU reaches the registers of `tiny_npu` over a bus, and the bus runs on the system's 100 MHz clock. So `tiny_npu` has two clocks at the same time.

> [!NOTE]
> **📖 Term | Phase-locked loop (PLL) (鎖相迴路)**
>
> - **Definition**: An analog circuit that multiplies an external reference clock up to the frequency the chip needs inside.
> - **On the job**: A PLL has to "lock" before its output clock is stable enough to use. "Is the PLL locked?" is one of the first things checked when a chip is brought up.
> - **Related terms**: reference clock, clock jitter, clock tree
> - **Common confusion**: A PLL is not written in RTL; it is analog IP that you buy. In simulation, a simplified behavioral model usually stands in for it.

---

## Two clock domains

All the flip-flops driven by the same clock form one **clock domain**. `tiny_npu` has two:

- **Bus side** (100 MHz): the register interface. Firmware writes `CTRL` and `LEN` and reads `STATUS`.
- **Compute side** (500 MHz): the control logic, the MAC array and the SRAMs.

The two clocks have different frequencies, and their phases have no fixed relationship, so they are **asynchronous**. The `START` that firmware writes must travel from the bus side to the compute side, and the `DONE` from the compute side must travel back. Both are clock domain crossing signals.

> [!NOTE]
> **📖 Term | Clock domain and clock domain crossing (CDC) (時脈域與跨時脈域)**
>
> - **Definition**: A group of flip-flops driven by the same clock is a clock domain; a signal that passes from one clock domain to another is a clock domain crossing.
> - **On the job**: "That's a CDC path; it has to go through a synchronizer," "The CDC report has to be clean before tape-out."
> - **Related terms**: synchronizer, asynchronous FIFO, metastability
> - **Common confusion**: Two clocks with the same frequency are still different clock domains if they come from different sources.

---

## Metastability: a photo taken mid-motion

Chapter 3 compared a flip-flop to pressing a camera shutter at the clock edge. If the data changes right as the shutter is pressed, the photo comes out blurred. The flip-flop's output may hang between 0 and 1 for a while before it falls randomly to one side. This is called **metastability**.

Within one clock domain, the timing analysis in Chapter 8 makes sure the data never changes around the shutter. But when two clocks are asynchronous, nothing can guarantee that, and sooner or later metastability will happen.

The solution is a **synchronizer**: two flip-flops in a row on the receiving side. Even if the first flip-flop takes a blurred photo, it has nearly a whole clock period to settle, so the second flip-flop almost always reads a clean 0 or 1.

```verilog
module sync_2ff (
    input  wire clk,      // clock of the receiving domain
    input  wire rst_n,
    input  wire d,        // comes from another clock domain
    output reg  q
);
    reg meta;             // may go metastable; never use it directly
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) {q, meta} <= 2'b00;
        else        {q, meta} <= {meta, d};
    end
endmodule
```

> [!NOTE]
> **📖 Term | Metastability (亞穩態)**
>
> - **Definition**: The state in which a flip-flop that has read changing data leaves its output hanging between 0 and 1 for a while before it settles.
> - **On the job**: Often shortened to "meta," as in "The first-stage flop can go meta, so never use it directly."
> - **Related terms**: synchronizer, setup, hold, mean time between failures (MTBF)
> - **Common confusion**: Metastability is not caused by a design mistake; any flip-flop can go metastable. The design's job is to make sure it settles before anything uses it.

> [!IMPORTANT]
> **💻 Software analogy | A clock domain crossing is like two threads sharing a variable**
>
> - **Like**: Two threads reading and writing the same variable without a lock, which causes a race condition.
> - **Unlike**: In a software race, you read either the old value or the new one. With metastability, the output can be neither 0 nor 1 for a while, and two circuits downstream may even read different answers.
> - **Watch out**: Simulators have no metastability, so clock domain crossing bugs are almost impossible to catch in simulation. Every crossing signal must go through a synchronizer and be checked one by one with a CDC checking tool.

<details>
<summary>🔍 Going deeper: Why a synchronizer has two stages</summary>

Metastability dies out quickly: each extra bit of settling time makes the chance that the flip-flop has still not settled drop exponentially. Designers rate a synchronizer by its **mean time between failures** (MTBF), the average time between one failure and the next.

With a single flip-flop, it gets almost no time to settle, and the MTBF may be only seconds. A second stage adds nearly a whole clock period, which can stretch the MTBF far beyond the lifetime of the chip. Chips with very fast clocks or very strict reliability requirements use three stages.

Cell libraries usually include dedicated synchronizer cells, with the two flip-flops placed close together and optimized for metastability.

</details>

A one-bit control signal can be handled with a synchronizer. Data with several bits is harder:

> [!TIP]
> **🔧 Know-how | Never synchronize the bits of a multi-bit value one by one**
>
> - **Situation**: Firmware writes `LEN` on the bus side, and the compute side has to read that number.
> - **Practice**: First hold `LEN` steady, then send only the one-bit `START` through a synchronizer; the compute side reads `LEN` only after `START` arrives. This is called a **handshake**. For a continuous stream of data, use an **asynchronous FIFO**.
> - **Why**: The synchronizer of each bit may settle in a different clock cycle.
> - **If you skip it**: In the cycle when `LEN` happens to change, the compute side may read some old bits and some new bits, and get a number that is neither the old value nor the new one. This kind of bug is rare, and when it happens, it is very hard to reproduce.
> - **Related chapters**: [Chapter 15: After Silicon Returns](../../4-to-the-fab/15-after-silicon/README.md)

---

## Reset: starting the chip from a known state

Right after power-up, every flip-flop holds a random value. A **reset** sets them to known starting values, such as returning the state machine to `IDLE` and clearing the accumulator.

`mac` uses an **asynchronous reset**: as soon as `rst_n` goes low, the flip-flops clear at once, without waiting for the clock. Entering reset is not a problem; the trouble is the moment reset is released. If it is released close to a clock edge, some flip-flops leave reset in this cycle and others in the next, and the state machine may go wrong from the very start.

> [!TIP]
> **🔧 Know-how | Enter reset asynchronously, leave it synchronously**
>
> - **Situation**: The external reset comes from a button or a power management circuit and has nothing to do with the clocks inside the chip.
> - **Practice**: Give each clock domain its own **reset synchronizer**. When reset arrives, the whole domain enters reset immediately; when it is released, the release is lined up with that domain's clock edge.
> - **Why**: This way, every flip-flop in a clock domain leaves reset at the same clock edge.
> - **If you skip it**: The chip occasionally fails to boot, depending on temperature, voltage and even which chip it is. Problems like this are very hard to reproduce in the lab.
> - **Related chapters**: [Chapter 15: After Silicon Returns](../../4-to-the-fab/15-after-silicon/README.md)

---

## Clock gating: no work, no clock

The clock switches every cycle; it is the busiest signal on the chip. As Chapter 2 explained, switching uses power. So the clock and the flip-flops often account for a large share of a chip's dynamic power.

Before firmware gives a command, the MAC array has nothing to do, yet its clock keeps ticking. **Clock gating** turns off the clock to the whole MAC array at such times, and turns it back on when `START` arrives.

Clock gating must use the library's dedicated **integrated clock gating cell** (ICG), not just any AND gate (Chapter 3). Synthesis tools can also insert clock gating automatically from the enable conditions in the RTL. This is the book's first low-power technique applied at the RTL level; Chapters 10 and 13 come back to the subject.

---

## Key takeaways

1. A chip's clock is made by a PLL that multiplies an external reference clock; `tiny_npu` has two clock domains, the bus side and the compute side.
2. A signal that crosses clock domains can drive a flip-flop into metastability. Use a two-stage synchronizer for a single bit, and a handshake or an asynchronous FIFO for several bits.
3. Simulators cannot show metastability, so clock domain crossings must be checked one by one with a CDC checking tool.
4. Enter reset asynchronously and leave it synchronously, with a reset synchronizer in each clock domain.
5. Clock gating turns off the clock when a block is idle, and it is one of the most common ways to save power.

---

## Further reading

- Clifford E. Cummings, "Clock Domain Crossing (CDC) Design & Verification Techniques Using SystemVerilog," 2008
- Clifford E. Cummings, Don Mills and Steve Golson, "Asynchronous & Synchronous Reset Design Techniques - Part Deux," 2003

---

[← Chapter 4: RTL and Verilog](../04-rtl-and-verilog/README.md) | [Contents](../../README.md) | [Chapter 6: Verification →](../06-verification/README.md)
