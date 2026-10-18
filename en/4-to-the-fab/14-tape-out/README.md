<!-- source: zh-TW/4-to-the-fab/14-tape-out/README.md | sha: f3b09d69d037 -->

# Chapter 14: Tape-out — Handing the Design to the Fab

> 📍 **Where the design is**
>
> - Previous stop: signoff, every check has passed and has been approved by the people responsible
> - **This chapter: exporting the layout as GDS, handing it to the fab, and catching a multi-project wafer (MPW) run**
> - Next stop: after silicon returns, powering up the real `tiny_npu` for the first time

🪜 Abstraction level: Spec ▸ RTL ▸ Netlist ▸ Layout ▸ **GDS** ▸ Chip

---

## Why it is called tape-out

In the early days, design data was written to magnetic tape and handed to the fab, so in English the step is called **tape-out** (in Taiwan, 下線). Tape-out is the last step of the design flow: from this moment, this version of the `tiny_npu` design is frozen.

> [!NOTE]
> **📖 Term | Tape-out (下線)**
>
> - **Definition**: Formally handing the signed-off design data to the fab for manufacturing.
> - **On the job**: "We tape out next month," "A0 has taped out." A0 is a common name for the first version of a chip.
> - **Related terms**: GDS, multi-project wafer, mask, stepping
> - **Common confusion**: Tape-out does not mean the chip is finished. Only after tape-out are the masks made and the wafers started, and the chips take several more months to come back.

---

## GDS: the final form of the chip

What goes to the fab is a layout file. The most common format is **GDSII**, along with **OASIS**, which makes smaller files. The file holds nothing about what the circuit "does." It holds only polygons, layer by layer: which layer, at which coordinates, with what shape.

Each layer corresponds roughly to one of the fab's masks. `tiny_npu` uses dozens of layers, from the shapes of the transistors all the way up to the top metal and the pads.

> [!NOTE]
> **📖 Term | GDSII and OASIS**
>
> - **Definition**: Standard file formats that record the layout of an integrated circuit; OASIS is the newer format and makes smaller files.
> - **On the job**: Whatever the format, people usually just say GDS, as in "Has the GDS gone out yet?"
> - **Related terms**: layout, layer, mask, tape-out
> - **Common confusion**: GDS is not a picture. It is the coordinates of the polygons on every layer. The fab cannot tell what the circuit is supposed to do. It only builds the shapes.

> [!IMPORTANT]
> **💻 Software analogy | GDS is like a shipped binary, and the fab just builds it**
>
> - **Like**: What you give the customer is a compiled binary, not the source code.
> - **Unlike**: The fab does not know what your circuit is for. It faithfully builds the shapes on every layer. A wrong shape in the GDS gets built exactly as drawn.
> - **Watch out**: The GDS you hand over must be the exact one that was signed off. Check the file version, the layer map and the file hash one more time.

> [!TIP]
> **🔧 Know-how | Check the version one last time before tape-out**
>
> - **Situation**: In the last few days before tape-out, the GDS is updated every day, and the folder holds several versions.
> - **Practice**: Record the RTL commit, netlist version and tool versions that this GDS comes from, and compute the file hash. When the fab receives it, both sides check the same hash.
> - **Why**: In the chaos of the last moment, sending the wrong file is easier than you think.
> - **If you skip it**: The fab makes masks from a layout that was never signed off, and months of time and a large sum of money are wasted.
> - **Related chapters**: [Chapter 4: RTL and Verilog](../../2-front-end/04-rtl-and-verilog/README.md)

<details>
<summary>🔍 Going deeper: There is more on the die than your circuit</summary>

Besides the `tiny_npu` circuit, the GDS contains a few other things:

- **Seal ring**: a wall of metal around the edge of the die that keeps cracks from wafer dicing, and moisture, out of the circuit.
- **Chip markings**: the product code, the version number, and sometimes a small drawing by the design team, visible only under a microscope.

In the scribe lines between dies, the fab also places its own alignment marks and **test keys**, used to align each layer and check the results of its process (*Introduction to Semiconductor Manufacturing*, Chapters 4 and 19).

</details>

---

## After the fab receives the GDS

**Check → Add dummy fill → Mask data preparation → Make the masks → Start the wafers**

1. **Check**: The fab checks the GDS again with its own rules to confirm that it can be manufactured.
2. **Add dummy fill**: The dummy fill from Chapter 13 is added. Sometimes the design team adds it first, and sometimes the fab does; when the fab adds it, the design team estimates it with the same rules during signoff to confirm that timing is not affected.
3. **Mask data preparation**: The layers are converted into the data that mask making needs. The most important part is **optical proximity correction** (OPC): the shapes are deliberately distorted so that they print correctly on the wafer.
4. **Make the masks**: An electron beam writes the shapes of each layer onto a quartz plate, producing dozens of masks.
5. **Start the wafers**: Blank wafers enter the fab, and the chip is built up layer by layer.

From here on, the journey belongs to *Introduction to Semiconductor Manufacturing*. The masks of `tiny_npu` are the masks used in the lithography area in Chapter 4 of that book.

---

## MPW: sharing a wafer with others

A full set of masks is very expensive. The first version of a chip only needs to prove that the design works, and only a few dozen chips are needed. Paying for a whole set of masks alone is not worth it.

A **multi-project wafer** (MPW) lets many companies and many designs share one set of masks and one batch of wafers, splitting the cost by area. The fab runs these on a regular schedule. Like a shuttle bus, it leaves when the time comes. The A0 of `tiny_npu` tapes out on an MPW.

> [!NOTE]
> **📖 Term | Multi-project wafer (多專案晶圓，MPW)**
>
> - **Definition**: A way for several designs to share one set of masks and wafers at tape-out, splitting the cost.
> - **On the job**: Usually called a shuttle, as in "If we miss this shuttle, we wait for the next one."
> - **Related terms**: mask, die, tape-out, stepping
> - **Common confusion**: An MPW is for samples, not for volume production. The number of chips you get is limited, and the die size is limited by the area you are given on the mask.

> [!TIP]
> **🔧 Know-how | Use the months of waiting to prepare for bring-up**
>
> - **Situation**: After tape-out, the chips take several months to come back, and the team suddenly seems to have nothing to do.
> - **Practice**: Use this time to prepare the test board, the firmware, the test programs for the tester and the lab equipment, and list the items to check, in order, when the chips arrive.
> - **Why**: The moment the chips arrive, the countdown to product launch starts. Every day of preparation pays off then.
> - **If you skip it**: The chips arrive and the test board is not ready; or a problem appears and there is no tool to look inside the chip, so everyone just waits.
> - **Related chapters**: [Chapter 15: After Silicon Returns](../15-after-silicon/README.md)

---

## Key takeaways

1. Tape-out formally hands the signed-off design to the fab, and the design is frozen from then on.
2. GDS and OASIS record the polygons on every layer; the fab builds only the shapes.
3. Before handing it over, check the version: the GDS must be the exact one that was signed off.
4. After the fab receives the GDS, it checks it, adds dummy fill, runs OPC and makes the masks before the wafers start.
5. The first version of a chip often tapes out on an MPW, sharing the mask cost with other designs.

---

## Further reading

- *Introduction to Semiconductor Manufacturing*, [Chapter 4: Lithography](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/en/2-process-modules/04-lithography/README.md)
- Alfred Kwok-Kit Wong, *Resolution Enhancement Techniques in Optical Lithography*, chapters on OPC

---

[← Chapter 13: Signoff](../../3-physical-design/13-signoff/README.md) | [Contents](../../README.md) | [Chapter 15: After Silicon Returns →](../15-after-silicon/README.md)
