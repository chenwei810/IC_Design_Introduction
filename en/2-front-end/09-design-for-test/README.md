<!-- source: zh-TW/2-front-end/09-design-for-test/README.md | sha: f231aadf5b68 -->

# Chapter 9: Design for Test — Letting the Factory Find Bad Chips

> 📍 **Where the design is**
>
> - Previous stop: static timing analysis, where `mac` got a pipeline stage
> - **This chapter: adding scan chains and SRAM self-test to the netlist, so that every chip can be tested**
> - Next stop: floorplanning and the power network, starting to put the circuit onto the chip

🪜 Abstraction level: Spec ▸ RTL ▸ **Netlist** ▸ Layout ▸ GDS ▸ Chip

---

## A correct design does not mean every chip is made correctly

The verification in Chapter 6 checks the design itself. But during manufacturing, a single particle or a wire that was not etched cleanly can ruin one particular chip, even when the design is perfectly correct.

So every chip is tested before it ships: once on the wafer and once more after packaging (*Introduction to Semiconductor Manufacturing*, Chapters 19 and 22). Tester time is expensive, so the tests must be both fast and thorough.

The difficulty is that the pins show only the outside of the chip. `tiny_npu` has thousands of flip-flops buried deep inside the circuit. To check whether the adder in one MAC is broken, would you really have to run a whole computation from the pins?

> [!NOTE]
> **📖 Term | Design for test (DFT) (可測試性設計)**
>
> - **Definition**: Adding circuits at the design stage that make the chip easy to test.
> - **On the job**: "DFT has inserted the scan," "Ask DFT about that." DFT also often refers to the engineers who do this work.
> - **Related terms**: scan chain, ATPG, MBIST, JTAG
> - **Common confusion**: DFT tests for manufacturing defects, not design errors. If the design is wrong, every chip is wrong in exactly the same way, and that is what verification is for.

---

## Scan chains: lining the flip-flops up in one long queue

The trick is to replace every flip-flop with a **scan flip-flop**, which has a multiplexer in front of it. In test mode, these multiplexers connect all the flip-flops end to end into one long shift register, called a **scan chain**.

**Shift in → Capture → Shift out and compare**

1. **Shift in**: push a test pattern into the chain from one test pin, one cycle at a time, until every flip-flop holds the value you want.
2. **Capture**: switch back to normal mode and pulse the clock once. Each flip-flop reads the result computed by the combinational logic in front of it.
3. **Shift out and compare**: switch back to test mode, push the results out one cycle at a time, and compare them with the expected answers. While shifting out, you can shift in the next pattern at the same time.

It is like a building with no windows: cut a door between every pair of rooms to form a corridor, and you can deliver something to each room in turn and then inspect each room in turn.

> [!NOTE]
> **📖 Term | Scan chain (掃描鏈)**
>
> - **Definition**: A structure that connects the flip-flops of a chip into a shift register in test mode.
> - **On the job**: "The scan chain is too long; test time will blow up," "One of the chains is broken."
> - **Related terms**: scan flip-flop, ATPG, scan compression
> - **Common confusion**: Scan chains are connected only in test mode. In normal operation, every flip-flop works in its original circuit.

---

## ATPG: letting the tools work out the test patterns

Which patterns should be shifted in to find defects? That is computed by **automatic test pattern generation** (ATPG) tools. They first assume all kinds of possible faults, then look for patterns that make those faults show up:

- **Stuck-at fault**: assume that a node is stuck at 0 or stuck at 1 forever.
- **Transition fault**: assume that a node changes too slowly to finish changing within one clock cycle.

A chip has many flip-flops, but a scan chain cannot be endlessly long. So chips add **scan compression** circuits that let a few test pins drive hundreds of short scan chains at once, which shortens the test time.

> [!NOTE]
> **📖 Term | Fault coverage (故障涵蓋率)**
>
> - **Definition**: The share of all assumed faults that the test patterns can detect.
> - **On the job**: "Stuck-at coverage has to be above 99% before we go to production."
> - **Related terms**: fault model, stuck-at fault, transition fault, ATPG
> - **Common confusion**: Fault coverage is the share of *assumed* faults that are detected. It is not the yield, and it does not guarantee that every kind of real defect will be caught.

<details>
<summary>🔍 Going deeper: Why at-speed testing is needed</summary>

While patterns are shifted in and out, the clock is usually slowed down so that thousands of shift cycles are stable and reliable. A slow capture like this can catch stuck-at faults, but not defects such as "a wire is a bit thin and its resistance a bit high, so the signal is a little slow." Defects like that cause errors only at the normal 500 MHz.

So a transition fault test pulses the clock twice in a row at the real operating frequency during capture: the first pulse starts the signal changing, and the second checks whether it finished in time. These two pulses usually come from the PLL on the chip. This is called an **at-speed test**, and its timing must be checked by STA as well.

</details>

---

## SRAM tests itself

The memory cells of an SRAM are packed very densely, their defects differ from those of ordinary logic, and the cells are not flip-flops, so they cannot be joined into a scan chain. So the chip includes a small **memory built-in self-test** (MBIST) circuit.

When it receives a start command, the MBIST follows a fixed algorithm: it walks through every address, writing, reading and comparing, and finally reports pass or fail. The most common algorithms are **March tests**. For example, write 0 to every address, then go through the addresses one by one "reading 0 and writing 1," then go back the other way "reading 1 and writing 0." This catches most memory cell defects.

Large memories also keep spare rows and columns, so a bad memory cell found in test can be replaced with a spare. The SRAMs in `tiny_npu` are only 64 KB each, so they are not repaired.

---

## JTAG: the door to testing

Where do the commands for test mode and MBIST come from? Most chips have a set of **JTAG** (Joint Test Action Group) pins (the IEEE 1149.1 standard). With only four or five pins, it controls the test circuits inside the chip and can also check the connections between chips on a circuit board. When the chip is brought up in Chapter 15, JTAG is also the first channel engineers use to "talk to the chip."

> [!IMPORTANT]
> **💻 Software analogy | DFT is like firmware's power-on self-test, but for every single chip**
>
> - **Like**: The power-on self-test (POST) of an embedded system, or debug interfaces left in a program.
> - **Unlike**: Software testing checks that the code is written correctly. DFT checks whether each physical chip was damaged in manufacturing. One design becomes millions of chips, every one of them is tested on a tester, and every second costs money.
> - **Watch out**: Test time is money. How the scan chains are built, whether to use compression and which memories get self-test must all be decided at the design stage, not after the chips are made.

> [!TIP]
> **🔧 Know-how | Keep the scan chains the same length**
>
> - **Situation**: You need to divide thousands of flip-flops among several scan chains.
> - **Practice**: Make the chains as close to the same length as possible, and keep the flip-flops in each chain in the same clock domain where you can.
> - **Why**: Every pattern has to finish shifting through the longest chain, so the test time is set by the longest chain.
> - **If you skip it**: One unusually long chain stretches the test time of every chip, and the cost of every chip goes up with it.
> - **Related chapters**: [Chapter 11: Placement and the Clock Tree](../../3-physical-design/11-placement-and-cts/README.md)

> [!TIP]
> **🔧 Know-how | The test circuits need verification and timing analysis too**
>
> - **Situation**: Scan chains are usually inserted during or after synthesis, and MBIST is often added at the RTL or netlist stage.
> - **Practice**: After insertion, run equivalence checking again to confirm that normal-mode function has not changed, simulate the test patterns on the netlist, and include test mode in STA.
> - **Why**: The multiplexer in front of each scan flip-flop slows down the original paths, and test mode has clocks and paths of its own.
> - **If you skip it**: The chip works but cannot be tested, so it cannot ship; or good chips are tested as bad and thrown away for nothing.
> - **Related chapters**: [Chapter 7: Logic Synthesis](../07-logic-synthesis/README.md), [Chapter 13: Signoff](../../3-physical-design/13-signoff/README.md)

---

## Key takeaways

1. Verification checks for design errors; DFT checks for manufacturing defects. Every chip is tested before it ships.
2. In test mode, scan chains connect the flip-flops into shift registers, and shift in, capture and shift out check the logic inside.
3. ATPG computes test patterns from fault models, and fault coverage measures whether the testing is enough.
4. SRAMs test themselves with MBIST; JTAG is the standard interface for controlling the test circuits.
5. Test time is cost. Keep scan chains the same length, and verify and time the test circuits as well.

---

## Further reading

- Michael L. Bushnell and Vishwani D. Agrawal, *Essentials of Electronic Testing for Digital, Memory and Mixed-Signal VLSI Circuits*
- *Introduction to Semiconductor Manufacturing*, [Chapter 19: Wafer Test](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/en/5-backend/19-wafer-test/README.md)

---

[← Chapter 8: Static Timing Analysis](../08-static-timing-analysis/README.md) | [Contents](../../README.md) | [Chapter 10: Floorplanning and the Power Network →](../../3-physical-design/10-floorplan-and-power/README.md)
