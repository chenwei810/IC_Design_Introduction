<!-- source: zh-TW/3-physical-design/10-floorplan-and-power/README.md | sha: 52480cf240ea -->

# Chapter 10: Floorplanning and the Power Network — Drawing the Map First

> 📍 **Where the design is**
>
> - Previous stop: design for test, where scan chains and MBIST were added to the netlist
> - **This chapter: deciding the size of the chip, putting the SRAMs, the MAC array and the I/O in the right places, and laying out the power**
> - Next stop: placement and the clock tree, putting every standard cell down and sending the clock to every flip-flop

🪜 Abstraction level: Spec ▸ RTL ▸ Netlist ▸ **Layout** ▸ GDS ▸ Chip

---

## From netlist to layout

A netlist says only "what connects to what," not "what goes where." **Physical design**, which starts in this chapter, gives every cell a position and then connects them with real metal wires.

**Floorplan → Placement → Clock tree → Routing → Signoff**

1. **Floorplan**: Decide the chip size, where the big blocks go and the power network (this chapter).
2. **Placement**: Find a position for every standard cell (Chapter 11).
3. **Clock tree**: Deliver the clock to every flip-flop (Chapter 11).
4. **Routing**: Connect every net with metal wires (Chapter 12).
5. **Signoff**: Finish the last checks before tape-out, item by item (Chapter 13).

It is like planning a new city: first set the city limits, place the big buildings such as the stadium and the hospital, and lay the main water pipes and power lines; only then build the houses one by one.

Besides the netlist and the timing constraints, physical design needs the physical information of every cell: how big its outline is, where its pins are and which metal layers it blocks, usually described in the LEF format. The process rules come from the foundry's **process design kit** (PDK).

> [!NOTE]
> **📖 Term | Floorplan (平面規劃)**
>
> - **Definition**: The step that decides the die size, the positions of large blocks, the arrangement of the I/O and the structure of the power network.
> - **On the job**: "The floorplan isn't settled yet; don't rush into placement."
> - **Related terms**: macro, I/O cell, power grid, utilization
> - **Common confusion**: Floorplanning does not place individual standard cells; that is the job of placement in the next chapter.

---

## How big the chip is

The size of a die is set by whichever of two things is bigger:

- **The core**: the total area of all standard cells and SRAMs, plus some room for routing.
- **The pads around the edge**: the metal contacts that connect the chip to its package, which must be lined up in a ring along the edge of the die.

`tiny_npu` has about a hundred thousand standard cells and two SRAMs, so its core is actually small. But it needs about a hundred pads: for the bus, the clocks, the reset and JTAG, plus many power and ground pads. A hundred pads in a ring need a die nearly 2 mm on a side. So the size of `tiny_npu` is set by its pads, and its core has room to spare.

> [!NOTE]
> **📖 Term | Pad-limited and core-limited**
>
> - **Definition**: A die whose size is set by the number of pads is pad-limited; one whose size is set by the area of the core circuits is core-limited.
> - **On the job**: "This one is pad-limited, so we can afford a few more decaps inside."
> - **Related terms**: bond pad, I/O cell, die area, utilization
> - **Common confusion**: Shrinking the logic of a pad-limited chip does not make the die any smaller. To save area, first cut down the pads.

---

## Placing the big blocks

A **macro** is a large block with a fixed shape, such as an SRAM or a PLL. Macros are placed first, and the remaining space is left for standard cells.

The floorplan of `tiny_npu` looks like this: I/O cells and pads all around the edge; the data SRAM on the left and the weight SRAM on the right; the MAC array in the middle, with both SRAMs right next to it; and the PLL in a corner, close to its clock pin and away from the busily switching MAC array.

![Floorplan of tiny_npu: pads around the edge, a power ring around the core, an SRAM on each side, the MAC array in the middle and the PLL in a corner](../../../images/10-floorplan.svg)

*Figure: ① I/O cells and pads around the edge ② Data SRAM ③ Weight SRAM ④ The 8 × 8 MAC array ⑤ PLL ⑥ The power ring around the core.*

> [!TIP]
> **🔧 Know-how | Point the SRAM pins toward the circuit that uses them**
>
> - **Situation**: An SRAM's data and address pins are grouped on one side, and the macro can be rotated or flipped when it is placed.
> - **Practice**: Turn the pin side toward the MAC array and line up the data wires on both sides; leave enough routing channels between macros.
> - **Why**: Each SRAM sends out 64 bits of data every cycle. With the pins on the wrong side, all those wires have to go around the whole SRAM.
> - **If you skip it**: The path from the SRAM to the MACs gets longer and misses timing, and the wires crowd together until they may not route at all.
> - **Related chapters**: [Chapter 12: Routing and Parasitics](../12-routing-and-parasitics/README.md)

---

## The power network: every cell needs water

Every standard cell must connect to power and ground. Current comes in through the pads, flows first into a thick **power ring** around the core, then spreads into parallel **power stripes** on the upper metal layers, and finally into the power rail of each row of standard cells. It is like tap water flowing from the main pipe through branch pipes to every house.

Every wire has resistance. When current flows through a resistance, the voltage drops; this is called **IR drop**. The farther a place is from the pads and the more power it uses, the lower the voltage its cells get, and the slower they run. Current that is too concentrated for too long also slowly pushes metal atoms along until the wire breaks, which is called **electromigration**.

So the power network must be dense and thick enough. But the metal it uses cannot carry signal wires, which is another trade-off. Next to the most power-hungry blocks, the design also adds **decoupling capacitors**, which act like small water towers that supply current locally when demand suddenly rises.

> [!NOTE]
> **📖 Term | IR drop (IR 壓降)**
>
> - **Definition**: The current flowing through the resistance of the power wires makes the voltage a cell receives lower than the supply. The name comes from voltage = current × resistance (V = IR).
> - **On the job**: "The IR drop in the middle of the array is too big; we need more timing margin there."
> - **Related terms**: power grid, decoupling capacitor, electromigration
> - **Common confusion**: Static IR drop looks at average current; dynamic IR drop looks at the instant when many cells switch at once, which is often much worse (Chapter 13).

> [!TIP]
> **🔧 Know-how | Settle the power network before placement**
>
> - **Situation**: During floorplanning, you are eager to move on to placement, so you put down a rough power network for now.
> - **Practice**: First estimate the power of each region (the MAC array is the densest and most power-hungry) and size the width and spacing of the power stripes from that.
> - **Why**: Power stripes take up fixed routing tracks. Widen them later, and the placed cells and routed wires all have to be redone.
> - **If you skip it**: Only at signoff in Chapter 13 do you find the IR drop in the MAC array too large, and you have to redo the floorplan and lose weeks.
> - **Related chapters**: [Chapter 13: Signoff](../13-signoff/README.md)

---

## Power domains: turning part of the circuit off completely

The clock gating in Chapter 5 stops idle circuits from switching, but it does nothing about leakage. To save the leakage too, you have to cut the power of that block completely. This is called **power gating**.

`tiny_npu` puts the MAC array in its own **power domain**, controlled by a row of power switches. When firmware has no work for it, the whole array is powered off. This power domain was decided back in the architecture stage of Chapter 1, and synthesis and verification both have to follow it; what the floorplan decides is its area on the chip and where the power switches go. This brings a few new requirements:

- The outputs of a powered-off block float at random values, so every signal that comes out of it must pass through an **isolation cell** that holds it at a known value.
- When two power domains run at different voltages, signals between them must pass through **level shifters**.
- Which blocks can be powered off and how they are isolated is described in a standard format such as UPF (IEEE 1801), so that synthesis, physical design and verification tools all understand it.

> [!IMPORTANT]
> **💻 Software analogy | A power domain is like shutting down an idle server**
>
> - **Like**: Shutting down cloud servers that have no traffic and starting them again when needed.
> - **Unlike**: A powered-off block loses all its state, and powering it up again means waiting for the supply to settle and resetting it. While it is off, its output wires are neither 0 nor 1, so the receiving side must be protected by isolation cells.
> - **Watch out**: The power-up and power-down sequence must be written into the spec, and the firmware must follow it: stop using the block, isolate it, then cut the power; reverse the order when powering up.

<details>
<summary>🔍 Going deeper: Why power switches turn on one at a time</summary>

When the whole MAC array is off, all its capacitances have discharged. If every power switch turned on at once, those capacitances would all charge in an instant, causing a huge inrush current. That inrush current would make the supply voltage of the whole chip dip suddenly, and nearby circuits that are still running could fail.

So power switches are usually connected in a chain: each switch turns on only after the one before it, so the current rises gradually. The cost is that waking up takes longer, and that time must also be written into the spec so that the firmware knows how long to wait.

</details>

---

## Key takeaways

1. Physical design gives every cell in the netlist a position and then connects them with real wires; the first step is floorplanning.
2. The die size is set either by the core area or by the number of pads; `tiny_npu` is pad-limited.
3. Macros such as SRAMs and the PLL are placed first, with their pins facing the circuits that use them.
4. The power network carries current from the pads through the power ring and stripes to every cell, and it must keep IR drop and electromigration under control.
5. Power gating saves leakage too, but it needs isolation cells, level shifters and a clear on/off sequence.

---

## Further reading

- Andrew B. Kahng, Jens Lienig, Igor L. Markov and Jin Hu, *VLSI Physical Design: From Graph Partitioning to Timing Closure*, Chapter 3
- *Introduction to Semiconductor Manufacturing*, [Chapter 10: Metallization](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/en/2-process-modules/10-metallization/README.md)

---

[← Chapter 9: Design for Test](../../2-front-end/09-design-for-test/README.md) | [Contents](../../README.md) | [Chapter 11: Placement and the Clock Tree →](../11-placement-and-cts/README.md)
