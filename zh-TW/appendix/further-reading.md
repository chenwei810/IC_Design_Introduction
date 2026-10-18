# 附錄 C　延伸閱讀

本附錄整理書中各章引用的參考資料，以及想深入了解時可以參考的書籍、標準與開源工具。這些資料大多是英文，閱讀時可以搭配[附錄 A 術語總表](glossary.md)。

---

## 入門與總論

| 資料 | 說明 | 相關章節 |
|---|---|---|
| Neil H. E. Weste、David Money Harris，《CMOS VLSI Design: A Circuits and Systems Perspective》第四版 | 從電晶體到系統的經典教科書，涵蓋本書大部分的主題 | 0、2、7、8 |
| Jan M. Rabaey、Anantha Chandrakasan、Borivoje Nikolić，《Digital Integrated Circuits: A Design Perspective》第二版 | 偏重電路層級，延遲與功耗講得很深入 | 2 |

## 數位邏輯與 Verilog

| 資料 | 說明 | 相關章節 |
|---|---|---|
| David Money Harris、Sarah L. Harris，《Digital Design and Computer Architecture》第二版 | 從二進位、邏輯閘到處理器，附有 Verilog 範例 | 3、4 |
| M. Morris Mano、Michael D. Ciletti，《Digital Design》第六版 | 數位邏輯的經典入門書 | 3 |
| Samir Palnitkar，《Verilog HDL: A Guide to Digital Design and Synthesis》第二版 | Verilog 的入門與參考書 | 4 |
| Clifford E. Cummings，〈Nonblocking Assignments in Verilog Synthesis, Coding Styles That Kill!〉，2000 年 | 阻隔式與非阻隔式指定的經典論文 | 4 |
| Clifford E. Cummings，〈Clock Domain Crossing (CDC) Design & Verification Techniques Using SystemVerilog〉，2008 年 | 同步器、交握與非同步 FIFO | 5 |
| Clifford E. Cummings、Don Mills、Steve Golson，〈Asynchronous & Synchronous Reset Design Techniques - Part Deux〉，2003 年 | 重置的設計方式與重置同步器 | 5 |

## 驗證

| 資料 | 說明 | 相關章節 |
|---|---|---|
| Janick Bergeron，《Writing Testbenches: Functional Verification of HDL Models》第二版 | 驗證方法的經典書，從 Testbench 到覆蓋率 | 6 |
| Chris Spear、Greg Tumbush，《SystemVerilog for Verification》第三版 | 用 SystemVerilog 做受約束的亂數測試與覆蓋率 | 6 |
| Accellera，《Universal Verification Methodology (UVM) User's Guide》 | 業界標準驗證方法學的官方說明 | 6 |

## 合成、時序、測試與實體設計

| 資料 | 說明 | 相關章節 |
|---|---|---|
| Giovanni De Micheli，《Synthesis and Optimization of Digital Circuits》 | 邏輯合成背後的演算法 | 7 |
| J. Bhasker、Rakesh Chadha，《Static Timing Analysis for Nanometer Designs: A Practical Approach》 | STA 的實務書，涵蓋元件庫、寄生、串音與 SDC | 8、13 |
| Michael L. Bushnell、Vishwani D. Agrawal，《Essentials of Electronic Testing for Digital, Memory and Mixed-Signal VLSI Circuits》 | 故障模型、ATPG、掃描與記憶體測試 | 9 |
| Andrew B. Kahng、Jens Lienig、Igor L. Markov、Jin Hu，《VLSI Physical Design: From Graph Partitioning to Timing Closure》 | 平面規劃、擺置、繞線、時脈樹與時序收斂的演算法 | 10～12 |
| Alfred Kwok-Kit Wong，《Resolution Enhancement Techniques in Optical Lithography》 | OPC 等解析度增強技術 | 14 |
| Prabhat Mishra、Farimah Farahmandi 編，《Post-Silicon Validation and Debug》 | 矽後驗證與除錯的方法 | 15 |

## AI 晶片與架構

| 資料 | 說明 | 相關章節 |
|---|---|---|
| John L. Hennessy、David A. Patterson，《Computer Architecture: A Quantitative Approach》第六版，第 7 章 | 領域專用架構，包括神經網路加速器 | 1 |
| Vivienne Sze、Yu-Hsin Chen、Tien-Ju Yang、Joel S. Emer，《Efficient Processing of Deep Neural Networks》 | 神經網路加速器的資料流、量化與能耗 | 1 |

## 標準

| 資料 | 說明 | 相關章節 |
|---|---|---|
| IEEE 1364 | Verilog 硬體描述語言 | 4 |
| IEEE 1800 | SystemVerilog，也包含 Verilog 的完整語法 | 4、6 |
| IEEE 1800.2 | UVM 驗證方法學 | 6 |
| IEEE 1801 | UPF 低功耗設計意圖 | 10 |
| IEEE 1149.1 | JTAG 測試介面與邊界掃描 | 9、15 |

## 跟著做使用的開源工具

| 資料 | 說明 | 相關章節 |
|---|---|---|
| [Icarus Verilog](https://steveicarus.github.io/iverilog/) | Verilog 模擬器，書中用 12.0 版 | 4、6、8、15 |
| [Yosys](https://yosyshq.readthedocs.io/projects/yosys/) | 開源的邏輯合成工具，書中用 0.33 版 | 7、8 |
| [GTKWave](https://github.com/gtkwave/gtkwave) | 波形檢視工具 | 6 |

## 系列的其他書

| 資料 | 說明 | 相關章節 |
|---|---|---|
| 《[半導體製造概論](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/zh-TW/README.md)》 | 這本書的續集：跟著一片晶圓，走完光罩之後的製造旅程 | 0～2、9～15 |
| 《[Git 概論](https://github.com/chenwei810/Git_Introduction/blob/main/zh-TW/README.md)》 | 管理 RTL 與練習檔都用得到的版本控制 | 4 |

---

[← 附錄 B 設計現場行話](jargon.md) ｜ [目錄](../README.md) ｜ [附錄 D Verilog 速查 →](verilog-quick-reference.md)
