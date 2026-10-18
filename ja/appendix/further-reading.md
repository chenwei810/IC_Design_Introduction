<!-- source: zh-TW/appendix/further-reading.md | sha: f011f3142716 -->

# 付録 C　参考文献

この付録では、各章で挙げた参考資料と、さらに深く知りたいときに役立つ書籍、規格、オープンソースのツールをまとめます。資料の多くは英語なので、読むときは[付録 A　用語集](glossary.md)と合わせて使ってください。

---

## 入門と総合

| 資料 | 説明 | 関連する章 |
|---|---|---|
| Neil H. E. Weste、David Money Harris『CMOS VLSI Design: A Circuits and Systems Perspective』第 4 版 | トランジスタからシステムまでを扱う定番の教科書。本書の主題のほとんどを含む | 0、2、7、8 |
| Jan M. Rabaey、Anantha Chandrakasan、Borivoje Nikolić『Digital Integrated Circuits: A Design Perspective』第 2 版 | 回路のレベルに重点を置き、遅延と電力を深く扱う | 2 |

## デジタル論理と Verilog

| 資料 | 説明 | 関連する章 |
|---|---|---|
| David Money Harris、Sarah L. Harris『Digital Design and Computer Architecture』第 2 版 | 2 進数と論理ゲートからプロセッサまで。Verilog の例がある | 3、4 |
| M. Morris Mano、Michael D. Ciletti『Digital Design』第 6 版 | デジタル論理の定番の入門書 | 3 |
| Samir Palnitkar『Verilog HDL: A Guide to Digital Design and Synthesis』第 2 版 | Verilog の入門書であり参考書 | 4 |
| Clifford E. Cummings「Nonblocking Assignments in Verilog Synthesis, Coding Styles That Kill!」2000 年 | ブロッキング代入とノンブロッキング代入についての定番の論文 | 4 |
| Clifford E. Cummings「Clock Domain Crossing (CDC) Design & Verification Techniques Using SystemVerilog」2008 年 | シンクロナイザ、ハンドシェイク、非同期 FIFO | 5 |
| Clifford E. Cummings、Don Mills、Steve Golson「Asynchronous & Synchronous Reset Design Techniques - Part Deux」2003 年 | リセットの設計方法とリセットシンクロナイザ | 5 |

## 検証

| 資料 | 説明 | 関連する章 |
|---|---|---|
| Janick Bergeron『Writing Testbenches: Functional Verification of HDL Models』第 2 版 | 検証手法の定番の本。テストベンチからカバレッジまで | 6 |
| Chris Spear、Greg Tumbush『SystemVerilog for Verification』第 3 版 | SystemVerilog による制約付きランダムテストとカバレッジ | 6 |
| Accellera『Universal Verification Methodology (UVM) User's Guide』 | 業界標準の検証方法論の公式の手引き | 6 |

## 論理合成、タイミング、テスト、物理設計

| 資料 | 説明 | 関連する章 |
|---|---|---|
| Giovanni De Micheli『Synthesis and Optimization of Digital Circuits』 | 論理合成の背後にあるアルゴリズム | 7 |
| J. Bhasker、Rakesh Chadha『Static Timing Analysis for Nanometer Designs: A Practical Approach』 | STA の実務書。ライブラリ、寄生成分、クロストーク、SDC を扱う | 8、13 |
| Michael L. Bushnell、Vishwani D. Agrawal『Essentials of Electronic Testing for Digital, Memory and Mixed-Signal VLSI Circuits』 | 故障モデル、ATPG、スキャン、メモリのテスト | 9 |
| Andrew B. Kahng、Jens Lienig、Igor L. Markov、Jin Hu『VLSI Physical Design: From Graph Partitioning to Timing Closure』 | フロアプラン、配置、配線、クロックツリー、タイミングクロージャのアルゴリズム | 10～12 |
| Alfred Kwok-Kit Wong『Resolution Enhancement Techniques in Optical Lithography』 | OPC などの解像度向上技術 | 14 |
| Prabhat Mishra、Farimah Farahmandi 編『Post-Silicon Validation and Debug』 | ポストシリコン検証とデバッグの方法 | 15 |

## AI チップとアーキテクチャ

| 資料 | 説明 | 関連する章 |
|---|---|---|
| John L. Hennessy、David A. Patterson『Computer Architecture: A Quantitative Approach』第 6 版、第 7 章 | ドメイン固有アーキテクチャ。ニューラルネットワークのアクセラレータを含む | 1 |
| Vivienne Sze、Yu-Hsin Chen、Tien-Ju Yang、Joel S. Emer『Efficient Processing of Deep Neural Networks』 | ニューラルネットワークのアクセラレータのデータフロー、量子化、エネルギー | 1 |

## 規格

| 資料 | 説明 | 関連する章 |
|---|---|---|
| IEEE 1364 | ハードウェア記述言語 Verilog | 4 |
| IEEE 1800 | SystemVerilog。Verilog の完全な文法も含む | 4、6 |
| IEEE 1800.2 | 検証方法論 UVM | 6 |
| IEEE 1801 | 低消費電力の設計意図を記述する UPF | 10 |
| IEEE 1149.1 | JTAG のテストインターフェースとバウンダリスキャン | 9、15 |

## やってみようで使うオープンソースのツール

| 資料 | 説明 | 関連する章 |
|---|---|---|
| [Icarus Verilog](https://steveicarus.github.io/iverilog/) | Verilog のシミュレータ。本書では 12.0 を使う | 4、6、8、15 |
| [Yosys](https://yosyshq.readthedocs.io/projects/yosys/) | オープンソースの論理合成ツール。本書では 0.33 を使う | 7、8 |
| [GTKWave](https://github.com/gtkwave/gtkwave) | 波形ビューア | 6 |

## シリーズのほかの本

| 資料 | 説明 | 関連する章 |
|---|---|---|
| 『[半導体製造入門](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/ja/README.md)』 | 本書の続編。1 枚のウェーハを追いかけて、マスクのあとの製造の旅をたどる | 0～2、9～15 |
| 『[Git 入門](https://github.com/chenwei810/Git_Introduction/blob/main/ja/README.md)』 | RTL や練習ファイルの管理に欠かせないバージョン管理 | 4 |

---

[← 付録 B　設計現場の言い回し](jargon.md) ｜ [目次](../README.md) ｜ [付録 D　Verilog クイックリファレンス →](verilog-quick-reference.md)
