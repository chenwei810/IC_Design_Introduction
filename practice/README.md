# 練習檔 / Practice files

這裡是書中主角 `mac`（乘加單元）的練習檔。第 4、6、7、8、15 章的「🧪 跟著做」都用它們。

These are the practice files for `mac`, the multiply-accumulate unit that the book follows. The "🧪 Try it" sections of Chapters 4, 6, 7, 8 and 15 use them.

## 安裝工具 / Install the tools

只需要兩個開源工具：模擬用的 Icarus Verilog，合成用的 Yosys。第 6 章的參考模型另外需要 Python 3。

You need two open-source tools: Icarus Verilog for simulation and Yosys for synthesis. The reference model in Chapter 6 also needs Python 3.

| 系統 System | 指令 Command |
|---|---|
| Ubuntu、Debian | `sudo apt install iverilog yosys` |
| macOS（Homebrew） | `brew install icarus-verilog yosys` |
| Windows | 先安裝 WSL，再在 Ubuntu 裡執行上面那一行 / Install WSL, then run the Ubuntu command inside it |

看波形的 GTKWave 是選用的：`sudo apt install gtkwave`。

GTKWave, for viewing waveforms, is optional: `sudo apt install gtkwave`.

書中的輸出來自 Icarus Verilog 12.0 與 Yosys 0.33（Ubuntu 24.04 的版本）。換了版本，第 7、8 章的元件數量與邏輯深度可能略有不同，模擬結果則應該完全一樣。

The outputs in the book come from Icarus Verilog 12.0 and Yosys 0.33, the versions in Ubuntu 24.04. With other versions, the cell counts and logic depths in Chapters 7 and 8 may differ slightly, but the simulation results should be identical.

## 檔案 / Files

| 檔案 File | 內容 Contents | 章 Chapter |
|---|---|---|
| `rtl/mac_ch04.v` | 第一版 RTL，藏著兩個問題 / First RTL, with two hidden problems | 4 |
| `rtl/mac_ch06.v` | 宣告 `signed` 之後的版本 / After declaring `signed` | 6、7、8 |
| `rtl/mac_ch08.v` | 插入一級管線，A0 下線的版本 / One pipeline stage; the version taped out as A0 | 8、15 |
| `rtl/mac_a1.v` | 加上飽和，A1 修正版 / With saturation; the A1 fix | 15 |
| `tb/tb_mac.v` | Testbench：讀向量檔、驅動 MAC、比對答案 / Reads a vector file, drives the MAC, checks the answers | 4、6、8、15 |
| `ref_model.py` | 參考模型：用軟體算出正確答案 / Reference model: computes the correct answers in software | 6、15 |
| `vectors/` | 測試向量。每行是 `clr en a b expected` / Test vectors, one `clr en a b expected` per line | 4、6、8、15 |
| `expected/` | 書中每一段輸出的存檔 / Saved copies of every output in the book | — |
| `run_all.sh` | 重跑所有跟著做並比對輸出 / Re-runs every Try-it section and compares the output | — |

## 怎麼開始 / Getting started

從這本書的根目錄進入這個資料夾，執行第 4 章的第一個例子：

From the root of this repository, go into this folder and run the first example from Chapter 4:

```bash
cd practice
iverilog -o sim rtl/mac_ch04.v tb/tb_mac.v
vvp sim +vec=vectors/directed.txt +verbose
```

Testbench 的選項 / Testbench options:

| 選項 Option | 用途 Purpose |
|---|---|
| `+vec=<檔案>` | 要跑的向量檔，預設是 `vectors/directed.txt` / Vector file to run |
| `+verbose` | 印出每一筆檢查 / Print every check |
| `+show_sums` | 每做完一次點積，印出累加器的值 / Print the accumulator after each dot product |
| `+vcd` | 產生波形檔 `mac.vcd`，可以用 GTKWave 打開 / Write the waveform `mac.vcd` for GTKWave |
| `-P tb.LAT=2`（編譯時）| 管線版的 MAC 晚一拍出結果 / The pipelined MAC gives its result one cycle later |

## 確認書中的輸出 / Checking the book's outputs

```bash
bash practice/run_all.sh
```

每一章都顯示 `OK` 就表示書中的輸出和實際執行的結果一致。修改了練習檔、確定要改變輸出時，執行 `bash practice/run_all.sh --update`，再把書上的輸出改成一樣。

`OK` for every chapter means the outputs in the book match a real run. After an intended change to the practice files, run `bash practice/run_all.sh --update` and update the book to match.

## 關於程式碼 / About the code

這是教學用的例子：電路刻意寫得很小，`tiny_npu` 的規格也是虛構的。註解使用英文，讓每個語言版本都能共用同一套練習檔。

This is a teaching example: the circuit is kept small on purpose, and the `tiny_npu` specification is made up. Comments are in English so that every language edition shares the same practice files.
