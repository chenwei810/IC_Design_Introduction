<!-- source: zh-TW/appendix/glossary.md | sha: 7ee343cad621 -->

# Appendix A: Glossary

This glossary lists the main terms in the book in alphabetical order. The "Chapter" column gives the chapters where each term mainly appears or is explained.

The "繁體中文" column shows the wording used in the Traditional Chinese original, which is useful when you work with Chinese-speaking colleagues. For terms that designers usually say in English, such as RTL, setup and slack, the Chinese original uses the English word too, and this column also gives the Chinese translation for reference. Terms shared with *Introduction to Semiconductor Manufacturing*, such as mask, die and electromigration, use the same wording as that book.

This glossary is also the **single source** for the book's wording: when writing or translating, follow the terms in this table. To add a language, add a column for it. See [TRANSLATIONS.md](../../TRANSLATIONS.md) for details.

To see how design teams actually use these words, see [Appendix B: Designer Jargon](jargon.md).

| English | Abbr. | 繁體中文 | Description | Chapter |
|---|---|---|---|---|
| Accumulator | — | 累加器 | A register that keeps adding new products into a running total | 1, 3 |
| Activation | — | 活化值 | The input data of each layer of a neural network | 1 |
| Adder | — | 加法器 | Combinational logic that adds two binary numbers | 3 |
| Antenna Effect | — | 天線效應 | Charge built up on long metal wires during manufacturing damages the connected gates | 12 |
| Application-Specific Integrated Circuit | ASIC | 特定應用積體電路 | A chip designed and built for a specific purpose | 0 |
| Architecture Model | — | 架構模型 | A software model of data flow and performance written before the RTL | 1 |
| Assertion | — | 斷言 | A rule written in the design or testbench that must always hold | 6 |
| Asynchronous FIFO | — | 非同步 FIFO | A queue that safely passes large amounts of data between two clock domains | 5 |
| Asynchronous Reset | — | 非同步重置 | A reset that takes effect immediately, without waiting for the clock | 5 |
| At-speed Test | — | 全速測試 | A test that captures results at the real operating frequency to find delay defects | 9 |
| Automatic Test Pattern Generation | ATPG | 自動測試圖樣產生 | Tools that compute test data able to find manufacturing defects | 9 |
| Blocking Assignment | — | 阻隔式指定 | Verilog `=`; the next line in the same block sees the new value immediately | 4 |
| Bond Pad | Pad | 焊墊 | A metal contact on the chip used to connect it to the package | 10 |
| Bring-up | — | 點亮 | Powering a chip for the first time and confirming its basic functions step by step | 15 |
| Buffer | — | 緩衝器 | A cell that strengthens a signal or adds delay | 8, 11 |
| Carry | — | 進位 | The value passed to the next bit in addition | 3 |
| Characterization | — | 特性分析 | Varying voltage, frequency and temperature to measure where the chip works correctly | 15 |
| Clock | — | 時脈 | A periodic signal that makes flip-flops update in step | 3, 5 |
| Clock Domain | — | 時脈域 | A group of flip-flops driven by the same clock | 5 |
| Clock Domain Crossing | CDC | 跨時脈域 | A signal passing from one clock domain to another | 5 |
| Clock Gating | — | 時脈閘控 | Turning off the clock to idle blocks to save dynamic power | 5 |
| Clock Skew | — | 時脈偏移 | The difference in arrival time of the same clock at different flip-flops | 11 |
| Clock Tree Synthesis | CTS | 時脈樹合成 | Delivering the clock to every flip-flop through layers of buffers | 11 |
| Code Coverage | — | 程式碼覆蓋率 | Whether every line and branch of the RTL was executed | 6 |
| Combinational Logic | — | 組合邏輯 | A circuit whose output depends only on its current inputs | 3 |
| Complementary Metal-Oxide-Semiconductor | CMOS | 互補式金屬氧化物半導體 | Circuit technology that uses NMOS and PMOS in pairs | 2 |
| Congestion | — | 擁塞 | An area where more wires must pass than there are tracks | 11 |
| Constrained Random Test | — | 受約束的亂數測試 | A random test kept within legal ranges and deliberately biased toward edge values | 6 |
| Contact | — | 接觸窗 | A metal-filled hole connecting a transistor to the first metal layer | 12 |
| Convolution | — | 卷積 | A neural network operation that takes one small patch of an image at a time and computes a dot product with the weights | 1, 15 |
| Core-limited | — | core-limited（受限於核心面積） | The die size is set by the area of the core circuitry | 10 |
| Critical Path | — | 關鍵路徑 | The path with the longest delay, which sets the maximum frequency | 8 |
| Crosstalk | — | 串音 | Neighboring wires interfering with each other through capacitance | 12 |
| Decoupling Capacitor | — | 去耦合電容 | A capacitor placed near cells to supply sudden current | 10, 13 |
| Design for Test | DFT | 可測試性設計 | Adding circuits during design that make the chip easy to test | 9 |
| Design Rule | — | 設計規則 | Geometric limits set by the foundry, such as minimum width and spacing | 12, 13 |
| Design Rule Check | DRC | 設計規則檢查 | Confirming that the layout follows the design rules | 13 |
| Design Under Test | DUT | 待測設計 | The design being tested by the testbench | 6 |
| Die | — | 晶粒 | One of the identical circuit units on a wafer | 10 |
| Directed Test | — | 定向測試 | A test with specific inputs chosen by an engineer | 4, 6 |
| Dot Product | — | 點積 | Multiplying two lists item by item and adding up the results; the main operation in neural networks | 1 |
| Dummy Fill | — | 假圖形 | Non-functional metal shapes added to even out density for CMP; also called metal fill | 13, 14 |
| Dynamic IR Drop | — | 動態 IR 壓降 | A sudden dip in supply voltage when many cells switch at once | 13 |
| Dynamic Power | — | 動態功耗 | Power used to charge and discharge capacitance when signals switch | 2 |
| ECO Cell | — | ECO 元件 | A filler cell that can become a logic gate by changing only the metal layers | 11, 15 |
| Electromigration | EM | 電遷移 | Long-term current pushing metal atoms along until a wire breaks | 10, 13 |
| Electronic Design Automation | EDA | 電子設計自動化 | Software tools for chip design | 0 |
| Engineering Change Order | ECO | 工程變更命令 | A small change made directly on the netlist or layout | 15 |
| Equivalence Checking | — | 等價性檢查 | Using formal methods to prove that two versions of a circuit behave the same | 7 |
| Errata | — | 勘誤表 | A list of a chip's known problems and their workarounds | 15 |
| Fabless | — | IC 設計公司 | A company that designs chips but has no fab of its own | 0 |
| Fault Coverage | — | 故障涵蓋率 | The share of assumed faults that can be detected | 9 |
| Fault Model | — | 故障模型 | A simplification of manufacturing defects into assumptions that can be analyzed | 9 |
| Field-Programmable Gate Array | FPGA | 現場可程式化邏輯閘陣列 | A chip whose internal logic can be reconfigured | 0, 6 |
| Filler Cell | — | 填充元件 | A cell placed in empty spots of a cell row to keep the structure continuous | 12 |
| Finite State Machine | FSM | 有限狀態機 | A circuit that decides the next state from the current state and inputs | 3 |
| Flip-Flop | — | 正反器 | A 1-bit memory element that samples at a clock edge and holds the value | 3 |
| Floorplan | — | 平面規劃 | Deciding the die size, where large blocks go and the power structure | 10 |
| Formal Verification | — | 形式驗證 | Using mathematics to prove that a property holds for every input | 6 |
| Foundry | — | 晶圓代工 | A business model of manufacturing chips for customers | 0 |
| Front End / Back End | — | 前段／後段 | Logic design and verification / physical design | 0 |
| Full Adder | — | 全加器 | A circuit that adds two bits and a carry | 3 |
| Functional Coverage | — | 功能覆蓋率 | Whether the features and edge cases in the specification were tested | 6 |
| Gate Count | — | 邏輯閘數 | Circuit size expressed in NAND2 equivalents | 2, 7 |
| GDSII | — | GDSII | The standard file format for recording integrated circuit layouts | 14 |
| Half Adder | — | 半加器 | A circuit that adds two bits and outputs a sum and a carry | 3 |
| Handshake | — | 交握 | A way to cross clock domains: hold the data steady, then tell the other side to read it with one synchronized control signal | 5 |
| Hardware Description Language | HDL | 硬體描述語言 | A programming language for describing circuits, such as Verilog | 4 |
| Hierarchy | — | 階層 | The structure of modules containing other modules, layer by layer | 4 |
| Hold Time | — | hold 時間（保持時間） | How long data must stay unchanged after the clock edge | 8 |
| I/O Cell | — | I/O 元件 | A cell that handles communication with the outside and protects against electrostatic discharge | 10 |
| Inrush Current | — | 湧入電流 | The large current that flows when a power switch turns on and recharges the empty capacitors | 10 |
| Insertion Delay | — | 插入延遲 | The time for the clock to travel from its source to a flip-flop | 11 |
| Instance | — | 實例 | One actual copy of a circuit created from a module | 4 |
| INT8 | — | INT8 | An 8-bit signed integer, from -128 to 127 | 1 |
| Integrated Circuit | IC | 積體電路 | Many transistors and wires built on one piece of semiconductor | 0 |
| Integrated Clock Gating Cell | ICG | 整合式時脈閘控元件 | A library clock gating cell that produces no short pulses | 5 |
| Inverter | — | 反相器 | The simplest logic gate, which turns 0 into 1 and 1 into 0 | 2 |
| IR Drop | — | IR 壓降 | The voltage drop caused by current flowing through power wires | 10, 13 |
| Isolation Cell | — | 隔離元件 | A cell that holds the outputs of a powered-off domain at known values | 10 |
| Jitter | — | 時脈抖動 | The cycle-to-cycle variation of clock timing at the same place | 11 |
| Joint Test Action Group | JTAG | JTAG | A standard interface for test and debug (IEEE 1149.1) | 9, 15 |
| Latch | — | 閂鎖器 | A memory element that lets data through while the clock is at one level | 3, 4 |
| Latency | — | 延遲（拍數） | The number of clock cycles from a piece of data entering to its result | 8 |
| Layout | — | 佈局 | The actual geometric shapes of every layer of the chip | 10, 14 |
| Layout Versus Schematic | LVS | 佈局與電路圖比對 | Confirming that the circuit in the layout matches the netlist | 13 |
| Leakage Power | — | 漏電功耗 | Power lost because transistors never shut off completely | 2 |
| LEF / DEF | — | LEF／DEF | File formats for the outline and pins of cells / the result of placement and routing | 10 |
| Level Shifter | — | 準位轉換器 | A cell that converts signal levels between power domains at different voltages | 10 |
| Liberty | — | Liberty | A file format describing the timing, power and area of standard cells | 7 |
| Lint | — | Lint | A static tool that checks RTL for coding problems | 6 |
| Logic Depth | — | 邏輯深度 | The number of levels of logic gates along a path | 8 |
| Logic Gate | — | 邏輯閘 | A basic circuit that outputs 0 or 1 according to a fixed rule | 2 |
| Logic Synthesis | — | 邏輯合成 | Turning RTL into a netlist made of standard cells | 7 |
| Macro | — | 巨集 | A large block with a fixed shape, such as an SRAM or a PLL | 10 |
| March Test | — | March 演算法 | A memory test that walks through every address in order, reading and writing | 9 |
| Mask / Reticle | — | 光罩 | A quartz plate carrying the pattern of one circuit layer | 14 |
| Mask Data Preparation | — | 光罩資料準備 | Turning the GDS into mask data after tape-out, including OPC | 14 |
| Mature Node | — | 成熟製程 | A process generation that has been in production for years and costs less | 1 |
| Mean Time Between Failures | MTBF | 平均故障間隔 | The average time between failures, used to rate synchronizers | 5 |
| Memory Built-In Self-Test | MBIST | 記憶體內建自我測試 | An on-chip controller that tests the SRAM | 9 |
| Memory Compiler | — | 記憶體編譯器 | A tool that generates SRAM blocks to order | 1 |
| Metastability | — | 亞穩態 | A flip-flop output hanging between 0 and 1 for a while | 5 |
| Mode | — | 模式 | An operating state of the chip, such as normal computation or scan shift | 13 |
| Module | — | 模組 | The basic unit of Verilog for describing a circuit | 4 |
| Multi-Corner Multi-Mode | MCMM | 多模式多角落分析 | Analyzing timing for every combination of modes and process corners | 13 |
| Multi-Project Wafer | MPW | 多專案晶圓 | A way of taping out in which many designs share masks and wafers | 14 |
| Multiplexer | MUX | 多工器 | A circuit that lets one of its inputs through according to a select signal | 4, 9 |
| Multiplier | — | 乘法器 | Combinational logic that computes the product of two numbers | 3 |
| Multiply-Accumulate Unit | MAC | 乘加單元 | A unit that multiplies two numbers and adds the product into an accumulator; the main character of this book | 0 |
| NAND2 Equivalent | — | NAND2 等效閘數 | Circuit size expressed in units of the area of a two-input NAND | 2 |
| Netlist | — | 網表 | A list of cells and their connections | 7 |
| Neural Processing Unit | NPU | 神經網路處理器 | A chip or block dedicated to running neural networks | 0 |
| NMOS / PMOS | — | NMOS／PMOS | Transistors that turn on when the gate is 1 / when the gate is 0 | 2 |
| Non-blocking Assignment | — | 非阻隔式指定 | Verilog `<=`; all updates happen together at the end of the time step | 4 |
| OASIS | — | OASIS | A more compact layout file format than GDSII | 14 |
| On-Chip Variation | OCV | 晶片上變異 | Differences in device characteristics at different places on the same chip | 8 |
| Optical Proximity Correction | OPC | 光學鄰近效應修正 | Modifying mask shapes to compensate for distortion during exposure | 14 |
| Outsourced Semiconductor Assembly and Test | OSAT | 封裝測試廠 | A company that provides packaging and test services | 0 |
| Overflow | — | 溢位 | A result that goes beyond what the bit width can represent | 1, 15 |
| Pad-limited | — | pad-limited（受限於焊墊） | The die size is set by the number of pads | 10 |
| Parasitic Extraction | — | 寄生萃取 | Calculating wire resistance and capacitance from the layout | 12 |
| Partial Product | — | 部分積 | In multiplication, the multiplicand times one digit of the multiplier | 3 |
| Peak Performance | — | 峰值運算量 | The theoretical maximum performance with every compute unit busy | 1 |
| Performance, Power, Area | PPA | 效能、功耗、面積 | The three basic measures for judging a design | 1 |
| Phase-Locked Loop | PLL | 鎖相迴路 | An analog circuit that generates the chip's internal clock | 5 |
| Pipeline | — | 管線 | Splitting a long computation into stages with flip-flops | 8 |
| Placement | — | 擺置 | The step that decides where every standard cell goes | 11 |
| Post-Silicon Validation | — | 矽後驗證 | Validation done on real chips after they come back | 15 |
| Power Domain | — | 電源域 | A block whose power can be switched on and off independently | 10 |
| Power Gating | — | 電源閘控 | Cutting power to idle blocks to save leakage | 10 |
| Power Grid | — | 電源網路 | The network of wires that delivers power to every cell | 10 |
| Power Ring / Power Stripe | — | 電源環／電源條 | A thick power wire around the core / a power mesh on the upper metal layers | 10 |
| Process Corner | — | 製程角落 | Analysis conditions representing extreme combinations of process, voltage and temperature | 8 |
| Process Design Kit | PDK | 製程設計套件 | The design rules and electrical models a foundry provides to designers | 10, 13 |
| Quantization | — | 量化 | Converting the weights and data of a neural network from floating point to integers with fewer bits | 1 |
| Random Seed | — | 亂數種子 | The starting value that determines random test inputs, used to reproduce tests | 6 |
| Redundancy Repair | — | 修補 | Replacing bad memory cells with spare ones | 9 |
| Reference Model | — | 參考模型 | A software model that computes the correct answers from the specification; also called a golden model | 6 |
| Register | — | 暫存器 | A group of flip-flops that stores multi-bit data | 3 |
| Register Map | — | 暫存器對照表 | A table of each register's address, name and purpose, used to write the driver | 1 |
| Register Transfer Level | RTL | 暫存器傳輸層級 | Describing circuits in terms of data moving between registers | 4 |
| Regression Test | — | 回歸測試 | Rerunning all tests regularly to make sure changes have not broken anything | 6 |
| Reset | — | 重置 | A signal that returns the circuit to a known starting state | 5 |
| Reset Synchronizer | — | 重置同步器 | A circuit that releases reset in step with the clock | 5 |
| Ripple Carry Adder | — | 漣波進位加法器 | An adder in which the carry passes from bit to bit | 3 |
| Routing | — | 繞線 | The step that connects cells with metal wires | 12 |
| Saturation | — | 飽和 | Stopping at the maximum or minimum value on overflow | 1, 15 |
| Scan Chain | — | 掃描鏈 | Flip-flops connected into a shift register in test mode | 9 |
| Scan Compression | — | 掃描壓縮 | Circuits that let a few pins drive many scan chains | 9 |
| Scan Flip-Flop | — | 掃描正反器 | A flip-flop with a multiplexer in front, so it can be joined into a scan chain | 9 |
| Scribe Line | — | 切割道 | The space between dies reserved for dicing and test structures | 14 |
| SDC | — | SDC | A common file format for timing constraints | 7 |
| Seal Ring | — | 密封環 | A metal wall along the edge of the die that keeps cracks and moisture out of the circuit | 14 |
| Sequential Logic | — | 循序邏輯 | A circuit whose output also depends on past states | 3 |
| Setup Time | — | setup 時間（建立時間） | How long data must be stable before the clock edge | 8 |
| Shielding | — | 屏蔽 | Placing grounded wires next to sensitive wires to reduce crosstalk | 12 |
| Shmoo Plot | — | Shmoo 圖 | A chart with voltage and frequency on its two axes, showing where the chip works correctly | 15 |
| Sign Extension | — | 符號延伸 | Copying the top bit when widening a signed number | 3 |
| Signal Integrity | SI | 訊號完整性 | How well a signal stays correct despite crosstalk and noise | 12 |
| Signed / Unsigned | — | 有號數／無號數 | Two ways of interpreting bits: able or unable to represent negative numbers | 3, 6 |
| Signoff | — | 簽核 | Confirming every item before tape-out, with formal approval by the person responsible | 13 |
| Silicon Intellectual Property | IP | 矽智財 | A circuit block that can be licensed for use in a chip | 0 |
| Slack | — | slack（時序餘裕） | The latest required arrival time minus the actual arrival time | 8 |
| Spare Cell | — | 備用元件 | Cells scattered in the layout in advance for later fixes | 11, 15 |
| Specification | — | 規格書 | A document describing a chip's functions, performance, interfaces and limits | 1 |
| SPEF | — | SPEF | A file format recording parasitic resistance and capacitance | 12 |
| Standard Cell Library | — | 標準元件庫 | A set of logic gates and flip-flops with a uniform height, already characterized | 2, 7 |
| Static Random-Access Memory | SRAM | 靜態隨機存取記憶體 | Common on-chip memory, usually 6 transistors per bit | 1, 9 |
| Static Timing Analysis | STA | 靜態時序分析 | A method that checks the timing of every path without needing inputs | 8 |
| Stepping | — | 晶片版本 | The version label of a chip after a design fix, such as A0 or A1; naming rules vary by company | 15 |
| Stuck-at Fault | — | 固定型故障 | A fault model in which a signal is fixed at 0 or 1 | 9 |
| Synchronizer | — | 同步器 | A circuit that safely brings a signal into a new clock domain | 5 |
| Tape-out | — | 下線 | Formally handing the signed-off design to the foundry | 14 |
| Temperature Inversion | — | 溫度反轉 | Circuits becoming slower at low temperature | 8 |
| Test Key | — | 測試鍵 | A test structure that the fab places in the scribe lines to check the results of its process | 14 |
| Testbench | TB | Testbench（測試平台） | Verification code that sends inputs and checks outputs | 6 |
| Threshold Voltage | Vt | 臨界電壓 | The minimum gate voltage needed to turn a transistor on | 2 |
| Throughput | — | 吞吐量 | The amount of work completed per clock cycle | 8 |
| Timing Closure | — | 時序收斂 | Fixing repeatedly until there are no timing violations | 8 |
| Timing Constraints | — | 時序限制 | Settings that describe clock and input/output timing requirements | 7 |
| Toggle Rate | — | 切換率 | How often a signal switches, used to estimate power | 2, 13 |
| Total Negative Slack | TNS | 總負 slack | The sum of the negative slack of all violating paths | 8 |
| Transition Fault | — | 轉態故障 | A fault in which a signal cannot finish changing within one clock cycle | 9 |
| Truth Table | — | 真值表 | A table listing every input combination and its output | 2 |
| Two's Complement | — | 二補數 | The most common way to represent negative numbers in digital circuits | 3 |
| Unified Power Format | UPF | UPF | A standard format describing power domains and low-power intent (IEEE 1801) | 10 |
| Universal Verification Methodology | UVM | UVM | The industry-standard verification methodology (IEEE 1800.2) | 6 |
| Useful Skew | — | 有用偏移 | Skew arranged on purpose to lend time to a slower path | 11 |
| Utilization | — | 使用率 | The share of the core area occupied by cells | 11 |
| Verification | — | 驗證 | The work of proving that a design is correct | 6 |
| Verification Plan | — | 驗證計畫 | A list of items to verify, written line by line from the specification | 6, 15 |
| Verilog / SystemVerilog | — | Verilog／SystemVerilog | The most widely used hardware description languages (IEEE 1364 / IEEE 1800) | 4 |
| Via | — | 導通孔 | A metal hole connecting two neighboring metal layers | 12 |
| Waiver | — | 豁免 | A violation that, after analysis and sign-off, is deliberately not fixed | 13 |
| Waveform | — | 波形 | A record of how signals change over time in simulation, often saved as a VCD file | 6 |
| Weight | — | 權重 | A trained parameter of a neural network that is multiplied by an activation | 1 |
| Worst Negative Slack | WNS | 最差負 slack | The worst slack of all paths | 8 |
| Wrap-around | — | 繞回 | Jumping straight from the maximum value to the minimum on overflow | 1, 15 |

---

[← Chapter 15: After Silicon Returns](../4-to-the-fab/15-after-silicon/README.md) | [Contents](../README.md) | [Appendix B: Designer Jargon →](jargon.md)
