# 附錄 A　術語總表

本表收錄書中出現的主要術語，依英文字母排序。「章節」欄是該術語主要出現或說明的章節編號。

「繁體中文」欄寫的是書中實際使用的說法。現場習慣直接講英文的術語，例如 RTL、setup、slack，正文就直接用英文，這一欄會同時列出中文譯名，方便查詢。和《半導體製造概論》重疊的術語，例如光罩、晶粒、電遷移，用詞和那本書一致。

這份術語表也是全書用詞的**單一來源**：撰寫或翻譯時，請以本表的用詞為準。新增語言時，在表格中加上該語言的欄位即可，詳見 [TRANSLATIONS.md](../../TRANSLATIONS.md)。

想知道現場怎麼講這些詞，可以參考[附錄 B 設計現場行話](jargon.md)。

| 英文 | 縮寫 | 繁體中文 | 說明 | 章節 |
|---|---|---|---|---|
| Accumulator | — | 累加器 | 不斷把新的乘積加進總和、並記住總和的暫存器 | 1、3 |
| Activation | — | 活化值 | 神經網路每一層的輸入資料 | 1 |
| Adder | — | 加法器 | 把兩個二進位數相加的組合邏輯 | 3 |
| Antenna Effect | — | 天線效應 | 製造時長金屬線收集電荷，損傷所連接的閘極 | 12 |
| Application-Specific Integrated Circuit | ASIC | 特定應用積體電路 | 為特定用途設計與製造的晶片 | 0 |
| Architecture Model | — | 架構模型 | 寫 RTL 之前，用軟體模擬資料流與效能的模型 | 1 |
| Assertion | — | 斷言 | 寫在設計或 Testbench 裡、永遠必須成立的規則 | 6 |
| Asynchronous FIFO | — | 非同步 FIFO | 在兩個時脈域之間安全傳遞大量資料的佇列 | 5 |
| Asynchronous Reset | — | 非同步重置 | 不必等時脈就立刻生效的重置 | 5 |
| At-speed Test | — | 全速測試 | 用正常工作頻率擷取結果，找出延遲類缺陷的測試 | 9 |
| Automatic Test Pattern Generation | ATPG | 自動測試圖樣產生 | 用工具算出能找出製造缺陷的測試資料 | 9 |
| Blocking Assignment | — | 阻隔式指定 | Verilog 的 `=`，同一個區塊的下一行馬上看到新值 | 4 |
| Bond Pad | Pad | 焊墊 | 晶片上與封裝連接的金屬接點 | 10 |
| Bring-up | — | 點亮 | 晶片第一次回來時，依序通電並確認基本功能 | 15 |
| Buffer | — | 緩衝器 | 增強訊號驅動能力或增加延遲的元件 | 8、11 |
| Carry | — | 進位 | 加法中傳給下一個位元的值 | 3 |
| Characterization | — | 特性分析 | 改變電壓、頻率與溫度，量出晶片能正常工作的範圍 | 15 |
| Clock | — | 時脈 | 讓正反器一起更新的週期性訊號 | 3、5 |
| Clock Domain | — | 時脈域 | 由同一個時脈驅動的一群正反器 | 5 |
| Clock Domain Crossing | CDC | 跨時脈域 | 訊號從一個時脈域傳到另一個時脈域 | 5 |
| Clock Gating | — | 時脈閘控 | 關掉閒置區塊的時脈以節省動態功耗 | 5 |
| Clock Skew | — | 時脈偏移 | 同一個時脈抵達不同正反器的時間差 | 11 |
| Clock Tree Synthesis | CTS | 時脈樹合成 | 用多層緩衝器把時脈送到每一個正反器 | 11 |
| Code Coverage | — | 程式碼覆蓋率 | RTL 的每一行與每個分支是否被執行過 | 6 |
| Combinational Logic | — | 組合邏輯 | 輸出只由當下輸入決定的電路 | 3 |
| Complementary Metal-Oxide-Semiconductor | CMOS | 互補式金屬氧化物半導體 | NMOS 與 PMOS 成對使用的電路技術 | 2 |
| Congestion | — | 擁塞 | 要通過的導線比可用軌道還多的區域 | 11 |
| Constrained Random Test | — | 受約束的亂數測試 | 限制在合法範圍、並偏向邊界值的亂數測試 | 6 |
| Contact | — | 接觸窗 | 連接電晶體與第一層金屬的金屬孔 | 12 |
| Convolution | — | 卷積 | 在影像上逐一取一小塊範圍、和權重做點積的神經網路運算 | 1、15 |
| Core-limited | — | core-limited（受限於核心面積） | 晶粒大小由核心電路的面積決定 | 10 |
| Critical Path | — | 關鍵路徑 | 延遲最長、決定最高頻率的路徑 | 8 |
| Crosstalk | — | 串音 | 相鄰導線透過電容互相干擾 | 12 |
| Decoupling Capacitor | — | 去耦合電容 | 放在元件附近、就近提供瞬間電流的電容 | 10、13 |
| Design for Test | DFT | 可測試性設計 | 在設計階段加入讓晶片容易被測試的電路 | 9 |
| Design Rule | — | 設計規則 | 晶圓廠規定的幾何限制，例如最小線寬與最小間距 | 12、13 |
| Design Rule Check | DRC | 設計規則檢查 | 確認佈局符合設計規則 | 13 |
| Design Under Test | DUT | 待測設計 | 被 Testbench 測試的設計 | 6 |
| Die | — | 晶粒 | 晶圓上一個個相同的電路單元 | 10 |
| Directed Test | — | 定向測試 | 由工程師挑選特定輸入的測試 | 4、6 |
| Dot Product | — | 點積 | 兩串數字逐項相乘再加總，神經網路的主要運算 | 1 |
| Dummy Fill | — | 假圖形 | 為了讓 CMP 磨得均勻而補上的不通電金屬圖形 | 13、14 |
| Dynamic IR Drop | — | 動態 IR 壓降 | 大量元件同時切換時，電源電壓瞬間下降 | 13 |
| Dynamic Power | — | 動態功耗 | 訊號切換時對電容充放電所消耗的功率 | 2 |
| ECO Cell | — | ECO 元件 | 平常是填充元件，只改金屬層就能變成邏輯閘的元件 | 11、15 |
| Electromigration | EM | 電遷移 | 電流長期推動金屬原子，造成導線斷裂 | 10、13 |
| Electronic Design Automation | EDA | 電子設計自動化 | 設計晶片用的軟體工具 | 0 |
| Engineering Change Order | ECO | 工程變更命令 | 直接在網表或佈局上做的小幅修改 | 15 |
| Equivalence Checking | — | 等價性檢查 | 用形式方法證明兩個版本的電路功能相同 | 7 |
| Errata | — | 勘誤表 | 晶片已知問題與避開方法的清單 | 15 |
| Fabless | — | IC 設計公司 | 設計晶片、但沒有自己工廠的公司 | 0 |
| Fault Coverage | — | 故障涵蓋率 | 假設的故障中，能被測試圖樣偵測到的比例 | 9 |
| Fault Model | — | 故障模型 | 把製造缺陷簡化成可以分析的假設 | 9 |
| Field-Programmable Gate Array | FPGA | 現場可程式化邏輯閘陣列 | 內部邏輯可以重新設定的晶片 | 0、6 |
| Filler Cell | — | 填充元件 | 補在元件排的空隙、讓結構保持連續的元件 | 12 |
| Finite State Machine | FSM | 有限狀態機 | 依目前狀態與輸入決定下一個狀態的電路 | 3 |
| Flip-Flop | — | 正反器 | 在時脈邊緣讀進輸入並保持住的 1 位元記憶元件 | 3 |
| Floorplan | — | 平面規劃 | 決定晶粒大小、大區塊位置與電源結構的步驟 | 10 |
| Formal Verification | — | 形式驗證 | 用數學方法證明某個性質對所有輸入都成立 | 6 |
| Foundry | — | 晶圓代工 | 替客戶製造晶片的商業模式 | 0 |
| Front End / Back End | — | 前段／後段 | IC 設計裡指邏輯設計與驗證／實體設計 | 0 |
| Full Adder | — | 全加器 | 把兩個位元和一個進位相加的電路 | 3 |
| Functional Coverage | — | 功能覆蓋率 | 規格裡的功能與邊界情況是否被測到 | 6 |
| Gate Count | — | 邏輯閘數 | 以 NAND2 等效數量表示的電路大小 | 2、7 |
| GDSII | — | GDSII | 記錄積體電路佈局的標準檔案格式 | 14 |
| Half Adder | — | 半加器 | 把兩個位元相加、輸出和與進位的電路 | 3 |
| Handshake | — | 交握 | 先固定資料，再用一個同步過的控制訊號通知對方讀取的跨時脈域做法 | 5 |
| Hardware Description Language | HDL | 硬體描述語言 | 用來描述電路的語言，例如 Verilog | 4 |
| Hierarchy | — | 階層 | 模組一層包一層的結構 | 4 |
| Hold Time | — | hold 時間（保持時間） | 時脈邊緣之後，資料必須保持不變的時間 | 8 |
| I/O Cell | — | I/O 元件 | 負責晶片內外訊號傳遞與靜電保護的元件 | 10 |
| Inrush Current | — | 湧入電流 | 電源開關打開的瞬間，對放光電的電容充電所產生的大電流 | 10 |
| Insertion Delay | — | 插入延遲 | 時脈從源頭走到正反器的時間 | 11 |
| Instance | — | 實例 | 依照模組放進電路裡的一份實體 | 4 |
| INT8 | — | INT8 | 8 位元有號整數，能表示 -128 到 127 | 1 |
| Integrated Circuit | IC | 積體電路 | 在一片半導體上做出的大量電晶體與導線 | 0 |
| Integrated Clock Gating Cell | ICG | 整合式時脈閘控元件 | 元件庫裡不會產生短脈衝的時脈閘控元件 | 5 |
| Inverter | — | 反相器 | 把 0 變成 1、1 變成 0 的最簡單邏輯閘 | 2 |
| IR Drop | — | IR 壓降 | 電流流過電源導線的電阻造成的電壓下降 | 10、13 |
| Isolation Cell | — | 隔離元件 | 把斷電區塊的輸出固定成已知值的元件 | 10 |
| Jitter | — | 時脈抖動 | 同一個地點時脈每一拍之間的時間變化 | 11 |
| Joint Test Action Group | JTAG | JTAG | 測試與除錯用的標準介面（IEEE 1149.1） | 9、15 |
| Latch | — | 閂鎖器 | 時脈在某個準位的期間讓資料通過的記憶元件 | 3、4 |
| Latency | — | 延遲（拍數） | 從資料進入到結果出來所需的時脈數 | 8 |
| Layout | — | 佈局 | 晶片每一層實際的幾何圖形 | 10、14 |
| Layout Versus Schematic | LVS | 佈局與電路圖比對 | 確認佈局裡的電路和網表一致 | 13 |
| Leakage Power | — | 漏電功耗 | 電晶體關不緊所消耗的功率 | 2 |
| LEF / DEF | — | LEF／DEF | 描述元件外框與接腳位置／擺置與繞線結果的檔案格式 | 10 |
| Level Shifter | — | 準位轉換器 | 在不同電壓的電源域之間轉換訊號準位的元件 | 10 |
| Liberty | — | Liberty | 描述標準元件時序、功耗與面積的檔案格式 | 7 |
| Lint | — | Lint | 不用模擬就能檢查 RTL 寫法問題的靜態工具 | 6 |
| Logic Depth | — | 邏輯深度 | 路徑上經過的邏輯閘級數 | 8 |
| Logic Gate | — | 邏輯閘 | 依固定規則輸出 0 或 1 的基本電路 | 2 |
| Logic Synthesis | — | 邏輯合成 | 把 RTL 轉成由標準元件組成的網表 | 7 |
| Macro | — | 巨集 | 形狀固定的大區塊，例如 SRAM 與 PLL | 10 |
| March Test | — | March 演算法 | 依序走過每個位址讀寫的記憶體測試方法 | 9 |
| Mask / Reticle | — | 光罩 | 帶有一層電路圖形的石英板 | 14 |
| Mask Data Preparation | — | 光罩資料準備 | 下線後把 GDS 轉成光罩用的資料，包括 OPC | 14 |
| Mature Node | — | 成熟製程 | 已量產多年、成本較低的製程世代 | 1 |
| Mean Time Between Failures | MTBF | 平均故障間隔 | 平均多久失敗一次，用來評估同步器 | 5 |
| Memory Built-In Self-Test | MBIST | 記憶體內建自我測試 | 在晶片內測試 SRAM 的控制電路 | 9 |
| Memory Compiler | — | 記憶體編譯器 | 依需求產生 SRAM 區塊的工具 | 1 |
| Metastability | — | 亞穩態 | 正反器的輸出暫時停在 0 與 1 之間的狀態 | 5 |
| Mode | — | 模式 | 晶片的運作狀態，例如正常運算或掃描移位 | 13 |
| Module | — | 模組 | Verilog 描述電路的基本單位 | 4 |
| Multi-Corner Multi-Mode | MCMM | 多模式多角落分析 | 在所有模式與角落的組合下分析時序 | 13 |
| Multi-Project Wafer | MPW | 多專案晶圓 | 多個設計共用光罩與晶圓下線，分攤費用 | 14 |
| Multiplexer | MUX | 多工器 | 依選擇訊號讓其中一個輸入通過的電路 | 4、9 |
| Multiplier | — | 乘法器 | 計算兩數乘積的組合邏輯 | 3 |
| Multiply-Accumulate Unit | MAC | 乘加單元 | 兩數相乘後加進累加器的單元，本書的主角 | 0 |
| NAND2 Equivalent | — | NAND2 等效閘數 | 以兩輸入 NAND 的面積為單位表示的電路大小 | 2 |
| Netlist | — | 網表 | 元件與元件之間連線的清單 | 7 |
| Neural Processing Unit | NPU | 神經網路處理器 | 專門執行神經網路運算的晶片或區塊 | 0 |
| NMOS / PMOS | — | NMOS／PMOS | 閘極為 1 時導通／閘極為 0 時導通的電晶體 | 2 |
| Non-blocking Assignment | — | 非阻隔式指定 | Verilog 的 `<=`，所有更新在同一個時間點一起生效 | 4 |
| OASIS | — | OASIS | 比 GDSII 更精簡的佈局檔案格式 | 14 |
| On-Chip Variation | OCV | 晶片上變異 | 同一顆晶片上不同位置的元件特性差異 | 8 |
| Optical Proximity Correction | OPC | 光學鄰近效應修正 | 修改光罩圖形，補償曝光時的變形 | 14 |
| Outsourced Semiconductor Assembly and Test | OSAT | 封裝測試廠 | 提供封裝與測試服務的公司 | 0 |
| Overflow | — | 溢位 | 運算結果超出位元寬度能表示的範圍 | 1、15 |
| Pad-limited | — | pad-limited（受限於焊墊） | 晶粒大小由焊墊的數量決定 | 10 |
| Parasitic Extraction | — | 寄生萃取 | 從佈局算出每條導線的電阻與電容 | 12 |
| Partial Product | — | 部分積 | 乘法中，乘數的一個位元乘上被乘數的結果 | 3 |
| Peak Performance | — | 峰值運算量 | 所有運算單元都在工作時的理論最高效能 | 1 |
| Performance, Power, Area | PPA | 效能、功耗、面積 | 評估設計的三個基本指標 | 1 |
| Phase-Locked Loop | PLL | 鎖相迴路 | 把參考時脈倍頻成晶片內部時脈的類比電路 | 5 |
| Pipeline | — | 管線 | 用正反器把一段長運算切成好幾段 | 8 |
| Placement | — | 擺置 | 決定每一個標準元件位置的步驟 | 11 |
| Post-Silicon Validation | — | 矽後驗證 | 晶片回來後，在真正的晶片上做的驗證 | 15 |
| Power Domain | — | 電源域 | 可以獨立開關電源的區塊 | 10 |
| Power Gating | — | 電源閘控 | 切斷閒置區塊的電源以節省漏電 | 10 |
| Power Grid | — | 電源網路 | 把電源送到每一個元件的導線網路 | 10 |
| Power Ring / Power Stripe | — | 電源環／電源條 | 環繞核心的粗電源線／上層金屬平行的電源線 | 10 |
| Process Corner | — | 製程角落 | 製程、電壓、溫度極端值組合出的分析條件 | 8 |
| Process Design Kit | PDK | 製程設計套件 | 晶圓廠提供給設計者的設計規則與電性模型 | 10、13 |
| Quantization | — | 量化 | 把浮點數換成位元數較少的整數來計算 | 1 |
| Random Seed | — | 亂數種子 | 決定亂數測試輸入的初始值，用來重現測試 | 6 |
| Redundancy Repair | — | 修補 | 用備用的記憶單元取代壞掉的記憶單元 | 9 |
| Reference Model | — | 參考模型 | 依照規格算出正確答案的軟體模型，也叫 golden model | 6 |
| Register | — | 暫存器 | 由多個正反器組成、存放多位元資料的元件 | 3 |
| Register Map | — | 暫存器對照表 | 列出每個暫存器的位址、名稱與用途，韌體依它撰寫驅動程式 | 1 |
| Register Transfer Level | RTL | 暫存器傳輸層級 | 以暫存器之間的資料搬移來描述電路的抽象層級 | 4 |
| Regression Test | — | 回歸測試 | 定期重跑所有測試，確認修改沒有弄壞原有功能 | 6 |
| Reset | — | 重置 | 讓電路回到已知初始狀態的訊號 | 5 |
| Reset Synchronizer | — | 重置同步器 | 讓重置的解除對齊時脈邊緣的電路 | 5 |
| Ripple Carry Adder | — | 漣波進位加法器 | 進位一位一位往上傳的加法器 | 3 |
| Routing | — | 繞線 | 用金屬導線連接元件的步驟 | 12 |
| Saturation | — | 飽和 | 溢位時停在最大值或最小值 | 1、15 |
| Scan Chain | — | 掃描鏈 | 測試模式下串接成移位暫存器的正反器 | 9 |
| Scan Compression | — | 掃描壓縮 | 用少數接腳驅動大量掃描鏈的電路 | 9 |
| Scan Flip-Flop | — | 掃描正反器 | 前面多了一個多工器、可以串進掃描鏈的正反器 | 9 |
| Scribe Line | — | 切割道 | 晶粒之間留給切割與測試結構的區域 | 14 |
| SDC | — | SDC | 常用的時序限制檔案格式 | 7 |
| Seal Ring | — | 密封環 | 沿著晶粒邊緣、防止裂痕與濕氣進入電路的金屬牆 | 14 |
| Sequential Logic | — | 循序邏輯 | 含有記憶元件、輸出也和過去狀態有關的電路 | 3 |
| Setup Time | — | setup 時間（建立時間） | 時脈邊緣之前，資料必須穩定的時間 | 8 |
| Shielding | — | 屏蔽 | 在敏感導線旁放接地線以減少串音 | 12 |
| Shmoo Plot | — | Shmoo 圖 | 以電壓和頻率為兩軸，標出晶片能否正常工作的圖 | 15 |
| Sign Extension | — | 符號延伸 | 有號數加寬時，把最高位元複製到新的位元 | 3 |
| Signal Integrity | SI | 訊號完整性 | 訊號在串音與雜訊下仍保持正確的程度 | 12 |
| Signed / Unsigned | — | 有號數／無號數 | 能不能表示負數的兩種位元解讀方式 | 3、6 |
| Signoff | — | 簽核 | 下線前逐項確認並由負責人正式核可 | 13 |
| Silicon Intellectual Property | IP | 矽智財 | 可以授權放進晶片裡的電路區塊 | 0 |
| Slack | — | slack（時序餘裕） | 最晚必須抵達的時間減去實際抵達的時間 | 8 |
| Spare Cell | — | 備用元件 | 預先撒在佈局裡、供之後修改使用的元件 | 11、15 |
| Specification | — | 規格書 | 描述晶片功能、效能、介面與限制的文件 | 1 |
| SPEF | — | SPEF | 記錄寄生電阻與電容的檔案格式 | 12 |
| Standard Cell Library | — | 標準元件庫 | 高度一致、特性已量好的邏輯閘與正反器集合 | 2、7 |
| Static Random-Access Memory | SRAM | 靜態隨機存取記憶體 | 晶片上常用的記憶體，每個位元通常用 6 個電晶體 | 1、9 |
| Static Timing Analysis | STA | 靜態時序分析 | 不需要輸入，檢查每一條路徑時序的方法 | 8 |
| Stepping | — | 晶片版本 | 修正設計後的晶片版本代號，例如 A0、A1 | 15 |
| Stuck-at Fault | — | 固定型故障 | 假設某個訊號固定在 0 或 1 的故障模型 | 9 |
| Synchronizer | — | 同步器 | 讓跨時脈域的訊號安全進入新時脈域的電路 | 5 |
| Tape-out | — | 下線 | 把簽核完成的設計正式交給晶圓廠 | 14 |
| Temperature Inversion | — | 溫度反轉 | 低溫時電路反而變慢的現象 | 8 |
| Test Key | — | 測試鍵 | 晶圓廠放在切割道上、用來確認製程結果的測試結構 | 14 |
| Testbench | TB | Testbench（測試平台） | 送入輸入並檢查輸出的驗證程式 | 6 |
| Threshold Voltage | Vt | 臨界電壓 | 讓電晶體導通所需的最低閘極電壓 | 2 |
| Throughput | — | 吞吐量 | 每個時脈週期能完成的工作量 | 8 |
| Timing Closure | — | 時序收斂 | 反覆修正，直到沒有時序違規 | 8 |
| Timing Constraints | — | 時序限制 | 描述時脈與輸入輸出時序要求的設定 | 7 |
| Toggle Rate | — | 切換率 | 訊號切換的頻繁程度，用來估算功耗 | 2、13 |
| Total Negative Slack | TNS | 總負 slack | 所有違規路徑的負 slack 總和 | 8 |
| Transition Fault | — | 轉態故障 | 訊號在一個時脈週期內來不及改變的故障模型 | 9 |
| Truth Table | — | 真值表 | 列出所有輸入組合與輸出的表 | 2 |
| Two's Complement | — | 二補數 | 數位電路最常用的負數表示法 | 3 |
| Unified Power Format | UPF | UPF | 描述電源域與低功耗設計意圖的標準格式（IEEE 1801） | 10 |
| Universal Verification Methodology | UVM | UVM | 業界標準的驗證方法學（IEEE 1800.2） | 6 |
| Useful Skew | — | 有用偏移 | 刻意安排、讓慢路徑借時間的時脈偏移 | 11 |
| Utilization | — | 使用率 | 標準元件佔核心可擺放面積的比例 | 11 |
| Verification | — | 驗證 | 證明設計照規格工作的工作 | 6 |
| Verification Plan | — | 驗證計畫 | 從規格逐條寫出的驗證項目清單 | 6、15 |
| Verilog / SystemVerilog | — | Verilog／SystemVerilog | 最常用的硬體描述語言（IEEE 1364／IEEE 1800） | 4 |
| Via | — | 導通孔 | 連接上下兩層金屬的金屬孔 | 12 |
| Waiver | — | 豁免 | 經過分析與核准、刻意不修正的違規 | 13 |
| Waveform | — | 波形 | 模擬時訊號隨時間變化的紀錄，常存成 VCD 檔 | 6 |
| Weight | — | 權重 | 神經網路訓練出來、和活化值相乘的參數 | 1 |
| Worst Negative Slack | WNS | 最差負 slack | 所有路徑中最差的 slack | 8 |
| Wrap-around | — | 繞回 | 溢位時從最大值直接跳到最小值 | 1、15 |

---

[← 第 15 章 晶片回來之後](../4-to-the-fab/15-after-silicon/README.md) ｜ [目錄](../README.md) ｜ [附錄 B 設計現場行話 →](jargon.md)
