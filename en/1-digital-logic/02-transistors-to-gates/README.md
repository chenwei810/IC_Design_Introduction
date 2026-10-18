<!-- source: zh-TW/1-digital-logic/02-transistors-to-gates/README.md | sha: 5f1ee105ed9e -->

# Chapter 2: From Transistors to Logic Gates — Making 0 and 1 with Switches

> 📍 **Where the design is**
>
> - Previous stop: specification and architecture, deciding what `tiny_npu` computes
> - **This chapter: looking down to the very bottom, at the switches and logic gates that every `mac` is made of**
> - Next stop: combinational and sequential logic, combining logic gates into circuits that compute and remember

🪜 Abstraction level: Spec ▸ RTL ▸ **Netlist** ▸ Layout ▸ GDS ▸ Chip

---

## A transistor is a switch

In a digital circuit, the transistors on a chip are used only as switches. A transistor is like a valve on a water pipe: the gate is the handle. Turn the handle one way and water flows; turn it the other way and the flow stops.

Digital circuits use two kinds of transistors:

- **NMOS**: conducts when its gate is 1 (a high voltage) and is off when its gate is 0.
- **PMOS**: the opposite; it conducts when its gate is 0 and is off when its gate is 1.

Chapter 2 of *Introduction to Semiconductor Manufacturing* explains in detail why a transistor can switch like this. For this book, you only need to remember that it is a switch controlled by a voltage.

> [!NOTE]
> **📖 Term | Complementary metal-oxide-semiconductor (CMOS) (互補式金屬氧化物半導體)**
>
> - **Definition**: The circuit technology that uses NMOS and PMOS in pairs; almost every digital chip uses it.
> - **On the job**: It names the process as well as the circuits, as in "This chip is in a 28 nm CMOS process."
> - **Related terms**: NMOS, PMOS, inverter, threshold voltage
> - **Common confusion**: The "CMOS sensor" in a camera is an image sensor made with this technology, not a different circuit technology.

---

## The inverter: the simplest logic gate

Put a PMOS between the supply and the output, an NMOS between the output and ground, and tie the two gates together as the input. That is an **inverter**:

- Input 1: the NMOS conducts and pulls the output down to ground, so the output is 0.
- Input 0: the PMOS conducts and pulls the output up to the supply, so the output is 1.

![A CMOS inverter: a PMOS between the supply and the output, an NMOS between the output and ground, with both gates tied together as the input](../../../images/02-cmos-inverter.svg)

*Figure: ① Supply ② PMOS; the small circle in front of its gate means "conducts when the gate is 0" ③ Input ④ Output ⑤ NMOS ⑥ Ground.*

Whatever the input, one of the two switches is always off, so current never flows straight from the supply to ground. This is why CMOS saves power: the circuit uses noticeable power only at the moment it switches.

---

## NAND, NOR and the truth table

With a few more transistors you can build other **logic gates**. For example, two PMOS in parallel and two NMOS in series make a two-input NAND: only when both inputs are 1 is the path at the bottom fully connected, so only then is the output 0.

The clearest way to describe a logic gate is a **truth table** that lists every combination of inputs:

| A | B | AND | OR | NAND | NOR | XOR |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

The gates that CMOS builds naturally are "inverting" gates; NAND and NOR are the simplest and the fastest. An AND is really a NAND followed by an inverter.

Any logic at all can be built from NANDs alone. That is why the industry likes to describe the size of a circuit as "how many two-input NANDs it is equal to."

> [!NOTE]
> **📖 Term | Gate count (邏輯閘數)**
>
> - **Definition**: The area of a circuit expressed as the number of two-input NANDs (NAND2) it is equal to; used to compare circuit sizes.
> - **On the job**: Usually given in K or M, as in "This block is about 50K gates."
> - **Related terms**: NAND2 equivalent, standard cell, area report
> - **Common confusion**: One gate is not one transistor; a single NAND2 has 4 transistors. And the gate count is not the real number of logic gates; it is converted from area.

---

## Delay: switching takes time

When the output of a logic gate goes from 0 to 1, it has to charge the inputs of the next stage and the wire; going from 1 to 0, it has to discharge them. It is like filling a bucket with a hose: the bigger the bucket (more loads, longer wire) or the thinner the hose (a smaller transistor), the longer it takes.

In a 28 nm-class process, the delay of one logic gate is a few tens of picoseconds (ps). When a signal leaves a flip-flop and passes through a chain of logic gates to the next flip-flop, the delays add up all the way. The delay of that chain decides how fast the chip's clock can run, which Chapter 8 works out in detail.

---

## Power: every switch costs energy

A chip's power comes mainly in two kinds:

- **Dynamic power**: every time a signal switches, a capacitance has to be charged and then discharged. The more often it switches and the higher the voltage, the more power it uses.
- **Leakage power**: even when a transistor is off, it does not shut completely, and a little current always leaks. The hotter the chip, the more it leaks.

Dynamic power follows a simple relationship: it is proportional to "capacitance × voltage squared × switching frequency." Because the voltage is squared, lowering the voltage is the most effective way to save power.

> [!IMPORTANT]
> **💻 Software analogy | Putting the CPU to sleep versus keeping circuits from switching**
>
> - **Like**: To save power in software, you put an idle CPU to sleep.
> - **Unlike**: Every signal wire in a circuit uses power each time it switches between 0 and 1, even if nobody uses the result. A MAC that has no work to do keeps using power as long as its clock is ticking and its inputs are changing.
> - **Watch out**: Saving power in hardware starts with stopping unnecessary switching: turn off the clock of idle blocks (Chapter 5), or even their power (Chapter 10).

<details>
<summary>🔍 Going deeper: Why the voltage is squared</summary>

Charging a capacitor to a voltage V draws an energy of C × V² from the supply. Half of it is stored in the capacitor; the other half turns into heat along the way. When the capacitor discharges, the stored half turns into heat too. So each charge-and-discharge cycle uses C × V² of energy.

When the voltage goes up, the same capacitor holds more charge, and each bit of charge also "falls" through a larger voltage. The two effects multiply, and that gives the square.

The number of times a node actually switches per second is the clock frequency f times the **toggle rate** (α, the average fraction of nodes that charge from 0 to 1 each cycle). So the dynamic power is about α × C × V² × f. Lowering the voltage by 10% cuts the dynamic power by about 19%.

</details>

---

## Standard cells: the designer's building blocks

Designers do not draw transistors one by one. The foundry or an IP vendor provides a **standard cell library**: inverters, NANDs, NORs, XORs, multiplexers, adders, flip-flops and more, each with its layout already drawn and its speed and power already measured.

All standard cells have the same height, so they can be lined up row by row like building blocks (Chapter 11). Synthesis in Chapter 7 picks suitable cells from this library to build the circuit that the RTL describes.

> [!TIP]
> **🔧 Know-how | The same logic gate comes in several drive strengths**
>
> - **Situation**: The library has a NAND2 in several sizes, usually labeled X1, X2, X4 and so on by drive strength.
> - **Practice**: Use a strong cell to drive a long wire or many inputs, and a small one when it drives only one or two nearby cells. Synthesis and physical design tools pick and adjust them automatically.
> - **Why**: A big cell drives faster, but it takes more area, and its own input capacitance is bigger too, so the stage before it has to work harder and uses more power.
> - **If you skip it**: Use only big cells and you waste area and power; use only small ones and the long paths cannot keep up with the clock.
> - **Related chapters**: [Chapter 7: Logic Synthesis](../../2-front-end/07-logic-synthesis/README.md), [Chapter 8: Static Timing Analysis](../../2-front-end/08-static-timing-analysis/README.md)

> [!TIP]
> **🔧 Know-how | Use fast cells on the critical paths and low-power cells everywhere else**
>
> - **Situation**: A process offers cells with several threshold voltages (Vt). Low-Vt cells switch fast but leak more; high-Vt cells are slower but save a lot of power.
> - **Practice**: Use low-Vt cells only on the paths with the least time to spare, and high-Vt cells for most of the circuit.
> - **Why**: When the chip is idle, leakage is the main source of power use, and most paths do not need to be that fast anyway.
> - **If you skip it**: With only low-Vt cells, the chip keeps leaking even in standby and drains the battery quickly; with only high-Vt cells, it cannot reach the target clock.
> - **Related chapters**: *Introduction to Semiconductor Manufacturing*, [Chapter 2: From Physics to Transistors](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/en/1-fundamentals/02-transistor-basics/README.md)

---

## Key takeaways

1. In a digital circuit, a transistor is a switch: an NMOS conducts when its gate is 1, and a PMOS conducts when its gate is 0.
2. Using NMOS and PMOS in pairs is CMOS. When nothing is switching, no current flows straight to ground, which saves power.
3. A truth table lists every input combination of a logic gate; circuit size is often given as the number of equivalent NAND2 gates.
4. Gate delays add up along a path and limit the clock; dynamic power is proportional to the square of the voltage.
5. Designers use the foundry's standard cell library, where the same logic gate comes in different drive strengths and threshold voltages.

---

## Further reading

- Neil H. E. Weste and David Money Harris, *CMOS VLSI Design: A Circuits and Systems Perspective*, 4th edition, Chapters 1 and 2
- Jan M. Rabaey, Anantha Chandrakasan and Borivoje Nikolić, *Digital Integrated Circuits: A Design Perspective*, 2nd edition
- *Introduction to Semiconductor Manufacturing*, [Chapter 2: From Physics to Transistors](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/en/1-fundamentals/02-transistor-basics/README.md)

---

[← Chapter 1: Specification and Architecture](../../0-before-you-start/01-spec-and-architecture/README.md) | [Contents](../../README.md) | [Chapter 3: Combinational and Sequential Logic →](../03-combinational-and-sequential/README.md)
