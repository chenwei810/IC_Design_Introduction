<!-- source: zh-TW/3-physical-design/13-signoff/README.md | sha: 1208f09b3a30 -->

# Chapter 13: Signoff — The Last Checks Before Tape-out

> 📍 **Where the design is**
>
> - Previous stop: routing and parasitics, every wire is connected and its resistance and capacitance have been extracted
> - **This chapter: confirming item by item that timing, physical rules, power and power consumption are all fine, with formal approval from the people responsible**
> - Next stop: tape-out, handing the layout to the fab

🪜 Abstraction level: Spec ▸ RTL ▸ Netlist ▸ **Layout ▸ GDS** ▸ Chip

---

## Signoff: someone answers for every item

The layout is finished, but it cannot go out yet. After tape-out there is no easy way back, so every check is done once more, using the strictest methods. Each item is confirmed and approved by the person responsible for it. This process is called **signoff**.

| Item | What is checked | If it fails |
|---|---|---|
| Timing | Setup and hold in every mode and at every corner | The chip misses its target frequency, or does not work at all |
| DRC | Whether the layout follows the foundry's design rules | The foundry rejects it, or the yield is very poor |
| LVS | Whether the circuit in the layout matches the netlist | The chip that gets built is not the circuit that was designed |
| Power integrity | IR drop and electromigration | The chip runs slower, or its wires break after years of use |
| Power consumption | Whether the total power meets the spec | Overheating, short battery life |
| Function and test | The final netlist is equivalent to the RTL, and the test patterns pass | Functional errors, or chips that cannot be tested |

> [!NOTE]
> **📖 Term | Signoff (簽核)**
>
> - **Definition**: The process before tape-out of confirming that every check has passed, with formal approval from the person responsible.
> - **On the job**: "Timing isn't signed off yet," "The signoff meeting is tomorrow."
> - **Related terms**: DRC, LVS, multi-corner multi-mode analysis, waiver
> - **Common confusion**: Signoff is not just running the tools once. It is a recorded decision with a named owner, including which violations were analyzed and allowed to remain.

---

## Timing signoff: every mode, every corner

At signoff, the STA from Chapter 8 uses the real extracted resistance and capacitance, includes the effects of crosstalk, and runs once for every combination of:

- **Modes**: normal operation, scan shift, scan capture and MBIST, each with its own clocks and paths.
- **Corners**: fast and slow process, high and low voltage, high and low temperature, plus wire resistance and capacitance on the high side and the low side.

Modes and corners together can make dozens of cases. This is called **multi-corner multi-mode analysis** (MCMM). In every case, setup and hold must have no violations.

---

## Physical verification: DRC and LVS

A foundry's PDK includes a set of design rules, often thousands of them for an advanced process: the minimum width, the minimum spacing, how far metal must extend around a via, the range the metal density of each layer must stay within, and so on.

> [!NOTE]
> **📖 Term | DRC and LVS**
>
> - **Definition**: A **design rule check** (DRC) confirms that the shapes in the layout follow the design rules; **layout versus schematic** (LVS) extracts the circuit from the layout and compares it with the netlist, element by element.
> - **On the job**: "Three DRC violations left," "LVS is finally clean."
> - **Related terms**: design rule, PDK, dummy fill, signoff
> - **Common confusion**: A clean DRC means only that the chip can be built, not that the circuit is right; a clean LVS means only that the circuit matches the netlist, not that it can be built. Both must pass.

<details>
<summary>🔍 Going deeper: Why metal density is checked</summary>

After building each metal layer, the fab polishes the surface flat with chemical mechanical planarization (CMP). Areas with dense patterns and areas with sparse ones are polished away at different rates, so the surface becomes uneven, which affects every layer built on top of it (*Introduction to Semiconductor Manufacturing*, Chapter 8).

So the design rules require the metal density of every small region of the chip to stay within a certain range. Empty areas are automatically filled with non-functional **dummy fill**.

Dummy fill is metal too, and it adds capacitance to the wires next to it. So after dummy fill is added, the resistance and capacitance have to be extracted again and timing signoff rerun.

</details>

---

## Power signoff: the moment the MAC array starts

At signoff, the IR drop from Chapter 10 is computed again with the real layout and currents, in two forms:

- **Static IR drop**: calculated from average currents, to see whether the power network is thick enough.
- **Dynamic IR drop**: how far the voltage falls at the instant many cells switch together.

The most dangerous moment for `tiny_npu` is the cycle in which firmware writes `START`: the clock gating of the MAC array opens, and all 64 MACs start computing on the same clock edge. The analysis shows the voltage in the middle of the array dropping more than expected at that moment, which slows down the cells there. The power stripes were already sized from the power estimate in Chapter 10, so the floorplan does not have to be redone. The team adds more decoupling capacitors in the spare space of the core, and includes this drop in timing signoff to confirm that the paths there still have margin. The chip is pad-limited, so there happens to be room in the core.

> [!TIP]
> **🔧 Know-how | Run power analysis with the worst-case activity**
>
> - **Situation**: Dynamic IR drop and power analysis both need to know how busy the circuit is, that is, its toggle rate.
> - **Practice**: Besides typical workloads, always include the worst case, such as every MAC going from idle to computing at once with constantly changing random data as input.
> - **Why**: Average activity hides the instantaneous peak current.
> - **If you skip it**: The chip works fine most of the time and fails only at the moment of heaviest load. It looks like random crashes and is very hard to track down.
> - **Related chapters**: [Chapter 10: Floorplanning and the Power Network](../10-floorplan-and-power/README.md), [Chapter 15: After Silicon Returns](../../4-to-the-fab/15-after-silicon/README.md)

Power signoff also includes **electromigration** checks: the current density in every segment of power and signal wire must stay below the foundry's limit, so that the chip lasts for years.

---

## Power analysis

The last step is to confirm the power consumption of the whole chip. Dynamic power is estimated from the toggle rates recorded in simulation, and the leakage power at each corner is added on top. The report breaks the power down by block. In `tiny_npu`, the MAC array and the clock tree use the most, which is why the clock gating of Chapter 5 and the power gating of Chapter 10 are applied to them.

> [!IMPORTANT]
> **💻 Software analogy | Signoff is like a release checklist, but no patches after it ships**
>
> - **Like**: The checklist before a software release: every test passes, security scans, code review, and finally approval from the person in charge.
> - **Unlike**: Software can be hotfixed after release. Every violation let through at signoff stays with every chip for its whole life.
> - **Watch out**: For every violation that is allowed to remain, write down why, how far its effects reach, and who approved it.

> [!TIP]
> **🔧 Know-how | Every waiver needs a written reason and a record**
>
> - **Situation**: Analysis shows that some violations cause no problem. Take `LEN` from Chapter 5: it is a multi-bit signal that crosses clock domains, so the CDC check reports it, but firmware guarantees that it stops changing before `START`.
> - **Practice**: Put these violations on a **waiver** list, write down the reason, the analysis and the approver for each one, and confirm them one by one in the signoff meeting.
> - **Why**: A waiver is a conscious decision, not something ignored. With a record, the next revision and other people can see why it was allowed.
> - **If you skip it**: Hidden among a pile of "probably fine" violations, a real problem gets let through with the rest.
> - **Related chapters**: [Chapter 14: Tape-out](../../4-to-the-fab/14-tape-out/README.md)

---

## Key takeaways

1. Signoff confirms every item before tape-out with the strictest methods, and each item is approved and recorded by the person responsible.
2. Timing signoff uses the extracted resistance, capacitance and crosstalk, and checks setup and hold in every mode and at every corner.
3. DRC confirms the chip can be built and LVS confirms the circuit has not changed; both must pass, and timing must be checked again after dummy fill.
4. Dynamic IR drop happens at the instant many cells switch together; for `tiny_npu`, the most dangerous cycle is the one where the MAC array starts computing.
5. Violations that are allowed to remain go on a waiver list, with the reason and the approver written down.

---

## Further reading

- J. Bhasker and Rakesh Chadha, *Static Timing Analysis for Nanometer Designs: A Practical Approach*
- *Introduction to Semiconductor Manufacturing*, [Chapter 8: CMP](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/en/2-process-modules/08-cmp/README.md)

---

[← Chapter 12: Routing and Parasitics](../12-routing-and-parasitics/README.md) | [Contents](../../README.md) | [Chapter 14: Tape-out →](../../4-to-the-fab/14-tape-out/README.md)
