<!-- source: zh-TW/2-front-end/07-logic-synthesis/README.md | sha: 0a2e24cac2d1 -->

# Chapter 7: Logic Synthesis — From RTL to Netlist

> 📍 **Where the design is**
>
> - Previous stop: verification, where `mac` passed every test after being declared `signed`
> - **This chapter: synthesizing the RTL of `mac` into logic gates and seeing how big it becomes**
> - Next stop: static timing analysis, checking whether these gates can keep up with 500 MHz

🪜 Abstraction level: Spec ▸ **RTL ▸ Netlist** ▸ Layout ▸ GDS ▸ Chip

---

## What synthesis does

RTL describes what the circuit should do, but a fab needs to know which cells to use and how to connect them. Turning the first into the second is called **logic synthesis**.

It is like shopping from a recipe. The recipe says "make one plate of fried rice," and the synthesis tool turns it into a shopping list that may use only what the store sells, which is the standard cell library from Chapter 2.

**Translate → Optimize → Map to cells**

1. **Translate**: read the RTL and turn it into generic circuit blocks, such as adders, multipliers, multiplexers and flip-flops.
2. **Optimize**: simplify the logic, share repeated parts, and remove circuits whose outputs nobody uses.
3. **Map to cells**: replace the generic circuits with real cells from the library, choosing the drive strength of each cell to meet the timing requirements.

The result of synthesis is a **netlist**.

> [!NOTE]
> **📖 Term | Netlist (網表)**
>
> - **Definition**: A file that lists every cell in a circuit and how the cells are connected.
> - **On the job**: "The netlist has gone to the back-end team," "This is the gate-level netlist after synthesis."
> - **Related terms**: standard cell, synthesis, equivalence checking, ECO
> - **Common confusion**: A netlist is usually written in Verilog format too, but it contains only cells and connections, with no `if` and no `+`. It describes structure, not behavior.

---

## The three inputs to synthesis

- **RTL**: the design written and verified in Chapters 4–6.
- **Standard cell library**: the function and area of each cell, and its delay and power at different voltages and temperatures, usually described in the Liberty format.
- **Timing constraints**: how fast the clocks are, when input signals arrive and when outputs must be ready, usually described in the SDC format.

The first few lines of the timing constraints for `tiny_npu` look roughly like this:

```tcl
create_clock -name core_clk -period 2.0  [get_pins u_pll/clk_out]
create_clock -name bus_clk  -period 10.0 [get_ports bus_clk]
set_clock_groups -asynchronous -group {core_clk} -group {bus_clk}
```

The first line defines the 500 MHz (2 ns period) compute clock on the output pin of the PLL inside the chip; the second defines the 100 MHz (10 ns period) bus clock that comes in through a pin. The third line tells the tool that the two clocks are asynchronous: the paths between them are handled by the synchronizers from Chapter 5, so their timing is not checked.

> [!NOTE]
> **📖 Term | Timing constraints (時序限制)**
>
> - **Definition**: Settings that tell the tools how fast the clocks are, when inputs and outputs arrive, and which paths do not need to be checked.
> - **On the job**: Usually called constraints or the SDC, as in "No wonder the timing looks so good; the constraints are wrong."
> - **Related terms**: SDC, clock, static timing analysis
> - **Common confusion**: Looser constraints make the reports look better, but they do not make the chip any faster. Wrong constraints hide real problems until the chips come back.

---

## What mac becomes

Synthesizing `mac` with an open-source synthesis tool gives 865 cells, 24 of which are flip-flops: exactly the 24-bit accumulator. 20 lines of RTL become a 5,168-line netlist.

The 64 MACs add up to about 55,000 cells, which makes the MAC array the largest block of logic in `tiny_npu`.

This synthesis uses the tool's built-in generic gates, not a foundry's real cell library. With a real library, there would be fewer cells and more kinds of them; a single cell might be a whole full adder, for example. But the conclusion stays the same: the multiplier takes up most of it.

> [!IMPORTANT]
> **💻 Software analogy | Synthesis is a lot like compiling, but every cell in the output costs money**
>
> - **Like**: A compiler turns source code into machine code, and it optimizes too.
> - **Unlike**: Hardly anyone reads compiled machine code, but the netlist is the input to every back-end stage, and every extra cell means more area and power. Also, the same RTL with different timing constraints gives a different circuit.
> - **Watch out**: The way you write RTL turns straight into hardware. Write a `/`, for example, and the tool faithfully builds a large, slow divider. If a division can be done with a shift, do not write it as a division.

<details>
<summary>🔍 Going deeper: Why there are so many XORs</summary>

The "sum" of a full adder is the XOR of three bits, and the carry is made of ANDs and ORs. The partial products of a multiplier are added up by a large array of full adders, so XOR and XNOR together make up nearly a third of the cells.

In the statistics in the Try-it section, `$_ANDNOT_` and `$_ORNOT_` are the tool's built-in cells for "A AND (NOT B)" and "A OR (NOT B)." `$_DFFE_PN0P_` is a flip-flop with an enable and an asynchronous reset: the enable is `en` or `clr`, so the accumulator updates when either is 1, and the reset is the active-low `rst_n`.

</details>

---

## What to check after synthesis

A finished synthesis does not guarantee a correct netlist. Tool settings, test circuits inserted later (Chapter 9) and manual edits can all make the netlist differ from the RTL.

> [!TIP]
> **🔧 Know-how | Always run equivalence checking after synthesis**
>
> - **Situation**: The netlist comes out of synthesis, and later it gets test circuits inserted, is adjusted by physical design tools, and is edited by hand in engineering change orders (ECOs).
> - **Practice**: After every transformation, use **equivalence checking** to prove that the new netlist does exactly what the RTL does.
> - **Why**: Simulation can test only a limited set of inputs; equivalence checking uses formal methods to prove the results are the same for every input.
> - **If you skip it**: A bug introduced by a tool setting or a manual edit that simulation happens to miss tapes out with the netlist.
> - **Related chapters**: [Chapter 9: Design for Test](../09-design-for-test/README.md), [Chapter 15: After Silicon Returns](../../4-to-the-fab/15-after-silicon/README.md)

> [!TIP]
> **🔧 Know-how | When the area suddenly shrinks, don't celebrate yet**
>
> - **Situation**: You change the RTL, synthesize again, and the area drops by a lot.
> - **Practice**: First read the warnings in the synthesis log: which registers were removed as constants, which outputs are not connected, and whether any latches appeared.
> - **Why**: Synthesis tools remove circuits whose outputs nobody uses. Forget to connect one output, and the whole block in front of it may be removed.
> - **If you skip it**: The area and timing reports look great, and only when the chips come back do you find a feature missing.
> - **Related chapters**: [Chapter 4: RTL and Verilog](../04-rtl-and-verilog/README.md)

---

## 🧪 Try it: Synthesize mac with Yosys

In the `practice/` folder, use the open-source [Yosys](https://yosyshq.readthedocs.io/projects/yosys/) to synthesize the `mac` fixed in Chapter 6, write the netlist to `netlist.v`, and print the cell statistics:

```bash
yosys -q -p "read_verilog rtl/mac_ch06.v; synth -top mac; write_verilog -noattr -noexpr netlist.v; tee -o /dev/stdout stat" | sed -n '/Number of cells/,$p'
```

```text
   Number of cells:                865
     $_ANDNOT_                     297
     $_AND_                         59
     $_DFFE_PN0P_                   24
     $_NAND_                        40
     $_NOR_                         13
     $_NOT_                         41
     $_ORNOT_                       18
     $_OR_                          91
     $_XNOR_                        64
     $_XOR_                        218
```

Compare the length of the RTL and the netlist:

```bash
wc -l rtl/mac_ch06.v netlist.v
```

```text
   20 rtl/mac_ch06.v
 5168 netlist.v
 5188 total
```

Take a look inside the netlist. Find the first XOR, then the flip-flop for bit 6 of the accumulator:

```bash
grep -m 1 -A 4 '_XOR_' netlist.v
grep -A 6 'acc_reg\[6\]' netlist.v
```

```text
  \$_XOR_  _0822_ (
    .A(_0609_),
    .B(_0599_),
    .Y(_0620_)
  );
  \$_DFFE_PN0P_  \acc_reg[6]  /* _1659_ */ (
    .C(clk),
    .D(_0000_[6]),
    .E(_0001_),
    .Q(acc[6]),
    .R(rst_n)
  );
```

Most cells and wires now have automatically generated names such as `_0822_`; only the ports and registers keep their names from the RTL. That is why a netlist is hard to read directly, and why signals in the RTL deserve good names. With other versions of Yosys, the cell counts may differ slightly.

---

## Key takeaways

1. Logic synthesis translates and optimizes the RTL, then maps it to standard cells to produce a netlist.
2. Synthesis needs the RTL, a standard cell library and timing constraints; wrong constraints hide real problems.
3. After synthesis, `mac` has 865 cells, 24 of them flip-flops, and most of them belong to the multiplier.
4. After synthesis, run equivalence checking and read the warnings carefully, especially about removed circuits.

---

## Further reading

- Neil H. E. Weste and David Money Harris, *CMOS VLSI Design: A Circuits and Systems Perspective*, 4th edition, Chapter 14
- Giovanni De Micheli, *Synthesis and Optimization of Digital Circuits*

---

[← Chapter 6: Verification](../06-verification/README.md) | [Contents](../../README.md) | [Chapter 8: Static Timing Analysis →](../08-static-timing-analysis/README.md)
