<!-- source: zh-TW/appendix/further-reading.md | sha: f011f3142716 -->

# Appendix C: Further Reading

This appendix collects the references cited in each chapter, along with books, standards and open-source tools for going deeper. While reading them, you can use [Appendix A: Glossary](glossary.md) to match each term with the wording in this book.

---

## Introductory and general

| Resource | Description | Chapters |
|---|---|---|
| Neil H. E. Weste and David Money Harris, *CMOS VLSI Design: A Circuits and Systems Perspective*, 4th edition | The classic textbook from transistors to systems; covers most of the topics in this book | 0, 2, 7, 8 |
| Jan M. Rabaey, Anantha Chandrakasan and Borivoje Nikolić, *Digital Integrated Circuits: A Design Perspective*, 2nd edition | Focuses on the circuit level, with deep coverage of delay and power | 2 |

## Digital logic and Verilog

| Resource | Description | Chapters |
|---|---|---|
| David Money Harris and Sarah L. Harris, *Digital Design and Computer Architecture*, 2nd edition | From binary and logic gates to a processor, with Verilog examples | 3, 4 |
| M. Morris Mano and Michael D. Ciletti, *Digital Design*, 6th edition | A classic introduction to digital logic | 3 |
| Samir Palnitkar, *Verilog HDL: A Guide to Digital Design and Synthesis*, 2nd edition | An introduction to and reference for Verilog | 4 |
| Clifford E. Cummings, "Nonblocking Assignments in Verilog Synthesis, Coding Styles That Kill!", 2000 | The classic paper on blocking and nonblocking assignments | 4 |
| Clifford E. Cummings, "Clock Domain Crossing (CDC) Design & Verification Techniques Using SystemVerilog", 2008 | Synchronizers, handshakes and asynchronous FIFOs | 5 |
| Clifford E. Cummings, Don Mills and Steve Golson, "Asynchronous & Synchronous Reset Design Techniques - Part Deux", 2003 | How to design resets, and reset synchronizers | 5 |

## Verification

| Resource | Description | Chapters |
|---|---|---|
| Janick Bergeron, *Writing Testbenches: Functional Verification of HDL Models*, 2nd edition | The classic book on verification methods, from testbenches to coverage | 6 |
| Chris Spear and Greg Tumbush, *SystemVerilog for Verification*, 3rd edition | Constrained random testing and coverage in SystemVerilog | 6 |
| Accellera, *Universal Verification Methodology (UVM) User's Guide* | The official guide to the industry-standard verification methodology | 6 |

## Synthesis, timing, test and physical design

| Resource | Description | Chapters |
|---|---|---|
| Giovanni De Micheli, *Synthesis and Optimization of Digital Circuits* | The algorithms behind logic synthesis | 7 |
| J. Bhasker and Rakesh Chadha, *Static Timing Analysis for Nanometer Designs: A Practical Approach* | A practical book on STA, covering libraries, parasitics, crosstalk and SDC | 8, 13 |
| Michael L. Bushnell and Vishwani D. Agrawal, *Essentials of Electronic Testing for Digital, Memory and Mixed-Signal VLSI Circuits* | Fault models, ATPG, scan and memory test | 9 |
| Andrew B. Kahng, Jens Lienig, Igor L. Markov and Jin Hu, *VLSI Physical Design: From Graph Partitioning to Timing Closure* | Algorithms for floorplanning, placement, routing, clock trees and timing closure | 10–12 |
| Alfred Kwok-Kit Wong, *Resolution Enhancement Techniques in Optical Lithography* | OPC and other resolution enhancement techniques | 14 |
| Prabhat Mishra and Farimah Farahmandi (eds.), *Post-Silicon Validation and Debug* | Methods of post-silicon validation and debug | 15 |

## AI chips and architecture

| Resource | Description | Chapters |
|---|---|---|
| John L. Hennessy and David A. Patterson, *Computer Architecture: A Quantitative Approach*, 6th edition, Chapter 7 | Domain-specific architectures, including neural network accelerators | 1 |
| Vivienne Sze, Yu-Hsin Chen, Tien-Ju Yang and Joel S. Emer, *Efficient Processing of Deep Neural Networks* | Dataflow, quantization and energy in neural network accelerators | 1 |

## Standards

| Resource | Description | Chapters |
|---|---|---|
| IEEE 1364 | The Verilog hardware description language | 4 |
| IEEE 1800 | SystemVerilog, which also contains the full Verilog syntax | 4, 6 |
| IEEE 1800.2 | The UVM verification methodology | 6 |
| IEEE 1801 | UPF, for expressing low-power design intent | 10 |
| IEEE 1149.1 | The JTAG test interface and boundary scan | 9, 15 |

## Open-source tools used in Try it

| Resource | Description | Chapters |
|---|---|---|
| [Icarus Verilog](https://steveicarus.github.io/iverilog/) | A Verilog simulator; the book uses version 12.0 | 4, 6, 8, 15 |
| [Yosys](https://yosyshq.readthedocs.io/projects/yosys/) | An open-source logic synthesis tool; the book uses version 0.33 | 7, 8 |
| [GTKWave](https://github.com/gtkwave/gtkwave) | A waveform viewer | 6 |

## Other books in the series

| Resource | Description | Chapters |
|---|---|---|
| *[Introduction to Semiconductor Manufacturing](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/en/README.md)* | The sequel to this book: follows one wafer through the manufacturing journey that begins after the masks | 0–2, 9–15 |
| *[Introduction to Git](https://github.com/chenwei810/Git_Introduction/blob/main/en/README.md)* | The version control you need to manage RTL and the practice files | 4 |

---

[← Appendix B: Designer Jargon](jargon.md) | [Contents](../README.md) | [Appendix D: Verilog Quick Reference →](verilog-quick-reference.md)
