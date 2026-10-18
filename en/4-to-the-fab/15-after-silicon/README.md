<!-- source: zh-TW/4-to-the-fab/15-after-silicon/README.md | sha: 179ef6b36cf3 -->

# Chapter 15: After Silicon Returns — Bring-up, Debug and a New Stepping

> 📍 **Where the design is**
>
> - Previous stop: tape-out; the masks, wafer fabrication, test and packaging are all done (*Introduction to Semiconductor Manufacturing*, Chapters 4–22)
> - **This chapter: powering up `tiny_npu` for the first time, finding the problem that `mac` hid the longest, and fixing it in the A1 version**
> - Next stop: the journey ends; the appendices have the glossary, designer jargon and a Verilog quick reference

🪜 Abstraction level: Spec ▸ RTL ▸ Netlist ▸ Layout ▸ GDS ▸ **Chip**

---

## Bring-up: waking the chip one step at a time

A few months later, the packaged A0 samples arrive back at the lab. Powering a chip for the first time is called **bring-up**. It must be done very carefully, and in order:

**Power on with a current limit → Check the clock → Connect over JTAG → Access the registers → Run memory self-test → Run computations with known answers**

1. **Power on with a current limit**: Set a current limit on the power supply first. An unusually large current may mean a short circuit, and the power must be cut at once.
2. **Check the clock**: Confirm that the PLL has locked and that the measured clock frequency is right.
3. **Connect over JTAG**: Read out the chip's ID code and check that the scan chains are intact (Chapter 9).
4. **Access the registers**: Firmware writes and reads back the registers of `tiny_npu` over the bus.
5. **Run memory self-test**: Start MBIST and confirm that both SRAMs pass.
6. **Run computations with known answers**: Start with a small example such as 3 × 4 + 5 × 6, then run real neural networks and compare with the reference model.

> [!NOTE]
> **📖 Term | Bring-up (點亮)**
>
> - **Definition**: The process of powering a newly returned chip for the first time and confirming its basic functions in order.
> - **On the job**: "We saw PLL lock on day one of bring-up, and everyone breathed a sigh of relief."
> - **Related terms**: post-silicon validation, JTAG, test board, firmware
> - **Common confusion**: Bring-up only confirms that the chip is "alive." It is not full validation. Weeks to months of post-silicon validation follow.

---

## Post-silicon validation and characterization

After bring-up comes a much longer phase, **post-silicon validation**: running real firmware and real workloads on the real chip to find problems that simulation missed. Occasional boot failures (the resets of Chapter 5), rare errors in clock domain crossings (Chapter 5) and voltage drops under the heaviest load (Chapter 13) are all almost invisible in simulation.

At the same time, the team does **characterization**: varying the voltage, frequency and temperature to measure the range in which the chip works correctly. Once the chip has masks of its own, the fab also deliberately makes some wafers on the fast side and some on the slow side, so the design team can confirm that the process corners in Chapter 8 were right. In volume production, the tester uses the test patterns from Chapter 9 to test every single chip (*Introduction to Semiconductor Manufacturing*, Chapters 19 and 22).

> [!NOTE]
> **📖 Term | Shmoo plot (Shmoo 圖)**
>
> - **Definition**: A chart with voltage and frequency on its two axes that marks whether the chip works correctly under each combination.
> - **On the job**: "The shmoo boundary looks really clean," "It starts failing in the low-voltage corner."
> - **Related terms**: characterization, process corner, binning
> - **Common confusion**: One shmoo plot represents only the chips that were measured. To represent the whole process, you need enough chips, including fast and slow ones.

---

## A problem that hid for a long time

Most neural networks compute correctly. Only one image model often gets very bright photos wrong. The engineers compare the results layer by layer and narrow the problem down to one convolution layer: a dot product of 3 × 3 × 128 = 1,152 terms, where the activations and weights both happen to be large, around 100.

1,152 × 100 × 100 = 11,520,000, which is more than the 8,388,607 that 24 bits can hold. The spec says the result should saturate here and stop at 8,388,607 (Chapter 1). But at the 839th term, the accumulator of `mac` jumps from 8,380,000 straight to -8,387,216, and the final result is -5,257,216. A number that should be large and positive has become large and negative. The next stage turns every negative number into 0, so the bright areas vanish entirely.

This is the second problem hidden in Chapter 4: **the saturation the spec requires was never written in the RTL**. Why did no one find it along the way?

- The verification plan in Chapter 6 was not written item by item from the spec, so no test checked overflow.
- The dot products in the random test have only 25 terms. The accumulator never goes above about fifty thousand, so it never comes close to the limit.
- Code coverage is 100%, because a feature that was never written has no code to measure.

> [!TIP]
> **🔧 Know-how | Reproduce a silicon problem in simulation first**
>
> - **Situation**: In the lab, the chip computes the wrong answer in some situation.
> - **Practice**: Record the register settings and input data from the test board, and feed them unchanged into an RTL simulation. If simulation is wrong too, it is a design bug; if simulation is right, look at timing, power or manufacturing defects instead.
> - **Why**: You can hardly see any signal inside the chip, but simulation shows every wire on every clock cycle.
> - **If you skip it**: You can only guess from experience. A design bug may be taken for a process problem, and the fab spends weeks investigating for nothing.
> - **Related chapters**: [Chapter 6: Verification](../../2-front-end/06-verification/README.md), *Introduction to Semiconductor Manufacturing*, [Chapter 16: Yield and Failure Analysis](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/en/4-yield-and-quality/16-yield-analysis/README.md)

---

## Working around it in firmware first

The A0 chips have already been made and cannot be changed. The team first adds the problem to the **errata**, then asks the firmware to work around it:

Chapter 1 showed that a dot product of 511 terms or fewer can never overflow. So the firmware splits the 1,152-term dot product into three pieces of 511, 511 and 130 terms. It writes each length to `LEN` and lets `tiny_npu` compute it, and the CPU adds the three results together in 32 bits. The answer is exactly right. The cost is that large convolution layers need extra passes, so they run slower.

> [!IMPORTANT]
> **💻 Software analogy | Errata are like writing a wrapper for a library you cannot change**
>
> - **Like**: A third-party library has a bug you cannot fix, so you wrap it in your own code that avoids the inputs that trigger it.
> - **Unlike**: This "library" is silicon that has already been made. Every A0 chip carries the same bug, and every version of the firmware and everyone who uses the chip must work around it.
> - **Watch out**: A workaround always has a cost. The errata must state clearly which steppings are affected, how to work around the problem, and how much performance is lost.

---

## A new stepping: A1 changes only the metal layers

The RTL fix is simple: compute one extra bit and check whether the top two bits differ. If they do, the result has overflowed, so output the largest or smallest value instead. This is the second part of `rtl/mac_a1.v`:

```verilog
    wire signed [24:0] sum = acc + prod;     // one extra bit
    wire               ovf = sum[24] ^ sum[23]; // top two bits differ
    wire signed [23:0] sat = sum[24] ? 24'sh800000   // most negative
                                     : 24'sh7FFFFF;  // most positive
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            acc <= 24'sd0;
        else if (clr_d)
            acc <= 24'sd0;
        else if (en_d)
            acc <= ovf ? sat : sum[23:0];
    end
```

After synthesis, each MAC gains about 40 logic gates. The logic depth does not increase, so timing is not affected.

The real problem is how to put this into a layout that is already finished and signed off. Running the full flow again would mean redoing synthesis, placement, the clock tree and signoff from the start, with a lot of time and risk. So the team does a **metal ECO** instead: the ECO cells scattered near every MAC in Chapter 11 come into use now. The base layout is left untouched; changing only the connections on the top few metal layers is enough to wire them into the saturation circuit, and timing and physical verification only need to recheck what changed.

A0 was built on an MPW whose masks were shared with other designs; A1 is the first mask set of `tiny_npu`'s own, for volume production. If another fix is needed later, it can reuse the base layers of this mask set and replace only the metal masks. The fab can even hold a batch of wafers just before the metal layers and continue as soon as the new masks arrive.

The modified netlist is checked for equivalence against the A1 RTL once more (Chapter 7), then goes through signoff and tape-out again. This version is called **A1**.

> [!NOTE]
> **📖 Term | Engineering change order (工程變更，ECO)**
>
> - **Definition**: A small change made directly to the netlist or layout, without rerunning the full design flow.
> - **On the job**: "This fix goes in as a metal ECO," "We only swap three metal masks."
> - **Related terms**: spare cell, ECO cell, equivalence checking, stepping
> - **Common confusion**: An ECO does not always touch only the metal layers. Before tape-out, an ECO can change anything; after tape-out, teams try to change only the metal layers so that fewer masks have to be replaced. An ECO is also not the fab's ECN, which is the review process for changing a manufacturing process (*Introduction to Semiconductor Manufacturing*, Chapter 18).

<details>
<summary>🔍 Going deeper: How steppings are named</summary>

Many companies label each **stepping** with a letter and a number. The first version is A0. A fix that changes only the metal layers adds one to the number, giving A1, A2 and so on. A fix that also changes the transistor layers changes the letter, giving B0.

So the stepping name tells you roughly how many mask layers changed. Naming rules differ between companies. Some start at A1, and some use other schemes, so ask first when you see one.

</details>

> [!TIP]
> **🔧 Know-how | After the fix, put the missing test back into the verification plan**
>
> - **Situation**: A bug slipped past verification and was found on silicon.
> - **Practice**: Add "saturate on overflow" to the verification plan, with a directed overflow test and functional coverage. Then read the spec again from the beginning, looking for anything else that was neither implemented nor tested.
> - **Why**: A bug that escaped means there is a hole in the process. Fixing only this one bug leaves the hole open.
> - **If you skip it**: The next chip makes the same kind of mistake in another corner.
> - **Related chapters**: [Chapter 6: Verification](../../2-front-end/06-verification/README.md)

---

## 🧪 Try it: Reproduce the overflow, work around it, then fix it

Run these in the `practice/` folder. First generate a test of 1,152 terms, each 100 × 100, with the expected value saturating as the spec requires, and run it on the A0 version of `mac`:

```bash
python3 ref_model.py overflow > vectors/overflow.txt
iverilog -P tb.LAT=2 -o sim rtl/mac_ch08.v tb/tb_mac.v
vvp sim +vec=vectors/overflow.txt +show_sums
```

```text
MISMATCH at line 840: a = 100, b = 100, expected 8388607, got -8387216
MISMATCH at line 841: a = 100, b = 100, expected 8388607, got -8377216
MISMATCH at line 842: a = 100, b = 100, expected 8388607, got -8367216
dot product done: acc = -5257216
FAIL: 314 of 1153 checks failed
```

Next, follow the errata and split the dot product into pieces of at most 511 terms:

```bash
python3 ref_model.py overflow --chunk 511 > vectors/overflow_chunk511.txt
vvp sim +vec=vectors/overflow_chunk511.txt +show_sums
```

```text
dot product done: acc = 5110000
dot product done: acc = 5110000
dot product done: acc = 1300000
PASS: 1155 of 1155 checks passed
```

None of the three pieces overflows, and the CPU adds them up: 5,110,000 + 5,110,000 + 1,300,000 = 11,520,000, exactly the right answer. Finally, switch to the A1 version and rerun the overflow test and the random test from Chapter 6:

```bash
iverilog -P tb.LAT=2 -o sim rtl/mac_a1.v tb/tb_mac.v
vvp sim +vec=vectors/overflow.txt +show_sums
vvp sim +vec=vectors/random.txt
```

```text
dot product done: acc = 8388607
PASS: 1153 of 1153 checks passed
PASS: 208 of 208 checks passed
```

The accumulator stops at 8,388,607, as the spec says, and the original tests all still pass. From one line in a spec and a dozen or so lines of Verilog, to 64 copies of a circuit and dozens of masks, to a real chip doing real computation, the journey of `mac` ends here.

---

## Key takeaways

1. Bring-up goes in order: power on with a current limit, check the clock, JTAG, registers, self-test, and only then real computation.
2. Post-silicon validation and characterization find the problems simulation missed on the real chip, and measure the range in which it works.
3. The second problem in `mac` is that the saturation required by the spec was never implemented; the verification plan was not written item by item from the spec, so it went unnoticed.
4. Chips already made are handled with errata and a firmware workaround; the next version is fixed with the reserved ECO cells, changing only the metal layers.
5. After fixing a bug, add the missing tests and look for the hole in the process.

---

## Further reading

- Prabhat Mishra and Farimah Farahmandi (eds.), *Post-Silicon Validation and Debug*
- *Introduction to Semiconductor Manufacturing*, [Chapter 22: Final Test and Reliability](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/en/5-backend/22-final-test-and-reliability/README.md)
- *Introduction to Semiconductor Manufacturing*, [Chapter 24: How the Process Shapes Firmware](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/en/6-beyond-the-fab/24-process-and-firmware/README.md)

---

[← Chapter 14: Tape-out](../14-tape-out/README.md) | [Contents](../../README.md) | [Appendices →](../../appendix/README.md)
