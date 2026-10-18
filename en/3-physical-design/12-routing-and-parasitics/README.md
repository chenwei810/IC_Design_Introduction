<!-- source: zh-TW/3-physical-design/12-routing-and-parasitics/README.md | sha: 7bfb7864e066 -->

# Chapter 12: Routing and Parasitics — After the Wires Go In

> 📍 **Where the design is**
>
> - Previous stop: placement and the clock tree, every cell has a position and the clock has been delivered
> - **This chapter: connecting every cell with about ten layers of metal, then working out the resistance and capacitance of every wire**
> - Next stop: signoff, the last checks before tape-out

🪜 Abstraction level: Spec ▸ RTL ▸ Netlist ▸ **Layout** ▸ GDS ▸ Chip

---

## A road network ten layers high

The wires of a chip are metal layers that the fab builds, one by one, above the transistors (*Introduction to Semiconductor Manufacturing*, Chapter 10). A 28 nm-class process usually has about ten of them:

- **Lower metal layers**: thin and dense, used for short connections near the cells, like side streets.
- **Upper metal layers**: thick and wide, used for long-distance signals, clocks and power, like highways.
- **Vias**: connect one metal layer to the next, like highway interchanges.

Each metal layer usually has a fixed main direction; the layers alternate between horizontal and vertical as they stack up.

> [!NOTE]
> **📖 Term | Via (導通孔)**
>
> - **Definition**: A metal-filled hole that connects two neighboring metal layers.
> - **On the job**: "Put a few more vias on this power line," "Use double vias on signal wires where you can."
> - **Related terms**: metal layer, routing, electromigration, contact
> - **Common confusion**: The hole that connects a transistor to the first metal layer is a contact; only a hole that connects metal to metal is a via.

---

## Routing: plan the route, then draw every wire

**Routing** turns every connection in the netlist into a real metal wire. A hundred thousand cells means more than a hundred thousand connections.

**Global routing → Detailed routing → Fixing**

1. **Global routing**: divide the chip into a grid and decide which grid cells each connection passes through, like choosing which highways to take before you leave home.
2. **Detailed routing**: inside each grid cell, put each connection on exact tracks and vias, following the foundry's design rules, such as the minimum width and the minimum spacing.
3. **Fixing**: fix places that break the design rules, and make the last adjustments for timing.

The clock and the critical signals are routed first, and they can be given wider wires or more spacing. The hardest place to route in `tiny_npu` is where the two SRAMs meet the MAC array: every cycle, 64 bits of data from each one have to squeeze into the array.

> [!IMPORTANT]
> **💻 Software analogy | Routing is like network routing, but every wire has a physical cost**
>
> - **Like**: Packets finding a path between network nodes and avoiding congested links.
> - **Unlike**: Every wire on a chip occupies its own stretch of physical track and cannot share bandwidth with anyone. The longer a wire, the slower it is and the more power it uses, and it disturbs the wires next to it too.
> - **Watch out**: Placement and routing go together. If the cells are placed badly, no routing tool can save the design.

---

## Parasitics: wires are not ideal

In a schematic, a wire is just a line. A real metal wire has **resistance**, and it forms **capacitance** with ground and with the wires beside it. This resistance and capacitance, which the schematic does not show, are called **parasitics**.

The longer a wire, the larger both its resistance and its capacitance, so its delay grows faster than its length. In advanced processes, wire delay is often as important as gate delay, or even more so. That is why very long wires get buffers inserted along the way to drive them in segments.

After routing, the tool uses process data from the foundry to compute the resistance and capacitance of every wire from the geometry of the layout. This step is called **parasitic extraction**, and the results are usually saved in the SPEF format and handed to the signoff STA in Chapter 13.

> [!NOTE]
> **📖 Term | Parasitic extraction (寄生萃取)**
>
> - **Definition**: Computing the resistance and capacitance of every wire from the geometry of the layout.
> - **On the job**: Often called "extracting RC," as in "Rerun STA after RC extraction."
> - **Related terms**: SPEF, parasitic capacitance, crosstalk, static timing analysis
> - **Common confusion**: STA after synthesis can only estimate wire delay. The numbers after extraction are close to reality, and the two can differ a lot.

<details>
<summary>🔍 Going deeper: Why wire delay grows faster than length</summary>

The resistance of a wire is proportional to its length, and so is its capacitance. Wire delay is roughly proportional to "resistance × capacitance," so doubling the length roughly quadruples the delay: it grows with the square of the length.

Insert buffers to cut a long wire into several segments, and each segment's delay grows with the square of that segment's length, so the total delay becomes proportional to the length, at the cost of the buffers' own delay and area. Physical design tools decide automatically where to insert them and how many.

</details>

---

## Crosstalk: interference from the neighbors

Two wires side by side have capacitance between them. When one wire switches, it "pushes" the wire next to it through this capacitance; this is called **crosstalk**. If the pushed wire is idle at that moment, a glitch that should not be there may appear; if it is switching too, it may switch faster or slower.

So signoff STA has to include the delay changes caused by crosstalk. Ways to reduce crosstalk include more spacing, shorter parallel runs, a stronger driver on the victim wire, or a grounded wire next to a sensitive wire as a **shield**. Clock wires are protected this way most often.

> [!NOTE]
> **📖 Term | Crosstalk (串音)**
>
> - **Definition**: Neighboring wires interfering with each other through coupling capacitance.
> - **On the job**: "Shield this clock against crosstalk," "SI analysis added a few more violations." SI stands for signal integrity.
> - **Related terms**: coupling capacitance, shielding, signal integrity, parasitic extraction
> - **Common confusion**: Crosstalk does not only cause glitches; it also makes signals faster or slower, so it affects the results of timing analysis.

---

## The antenna effect and redundant vias

Some problems happen not while the chip is working, but while it is being made.

> [!TIP]
> **🔧 Know-how | Make long wires change layers or add a diode to avoid the antenna effect**
>
> - **Situation**: A very long metal wire connects only to the input of one logic gate.
> - **Practice**: Make the wire jump up to a higher metal layer partway, or add a protective diode next to the gate. Design rule checks find places like this.
> - **Why**: Building the metal layers takes several fab steps that use plasma, such as etching. A long wire that is not yet fully connected collects charge like an antenna, and since it is connected only to a very thin gate, the charge has nowhere to go and may damage the gate oxide. This is called the **antenna effect**.
> - **If you skip it**: Transistors on some chips are damaged during manufacturing, so the test yield drops, or the chips fail after some time in use.
> - **Related chapters**: *Introduction to Semiconductor Manufacturing*, [Chapter 6: Etching](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/en/2-process-modules/06-etching/README.md)

> [!TIP]
> **🔧 Know-how | Use two vias where there is room**
>
> - **Situation**: During routing, two metal layers are connected by a single via.
> - **Practice**: Where there is room, use two vias side by side instead, called redundant vias.
> - **Why**: Now and then, a via is not completely filled during manufacturing. With two side by side, if one fails, the other still works; spreading the current also makes electromigration less likely.
> - **If you skip it**: Random open circuits lower the yield, and defects like these show no clear pattern on a wafer map.
> - **Related chapters**: *Introduction to Semiconductor Manufacturing*, [Chapter 16: Yield and Failure Analysis](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/en/4-yield-and-quality/16-yield-analysis/README.md)

After routing, the remaining gaps in the cell rows are filled with **filler cells**, which keep the power rails and wells of every row continuous. The ECO cells mentioned in Chapter 11 normally sit there in the role of filler cells.

---

## Key takeaways

1. A chip's wiring is a stack of about ten metal layers: thin and dense at the bottom, thick and wide at the top, connected by vias.
2. Routing plans globally first, then routes in detail, following the foundry's design rules.
3. Wires have parasitic resistance and capacitance, and their delay grows quickly with length; the extracted values go to signoff STA.
4. Crosstalk causes noise and changes delays; shielding and extra spacing are common remedies.
5. The antenna effect and via defects are manufacturing problems that must be prevented in the design.

---

## Further reading

- Andrew B. Kahng, Jens Lienig, Igor L. Markov and Jin Hu, *VLSI Physical Design: From Graph Partitioning to Timing Closure*, Chapters 5 and 6
- *Introduction to Semiconductor Manufacturing*, [Chapter 10: Metallization](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/en/2-process-modules/10-metallization/README.md)

---

[← Chapter 11: Placement and the Clock Tree](../11-placement-and-cts/README.md) | [Contents](../../README.md) | [Chapter 13: Signoff →](../13-signoff/README.md)
