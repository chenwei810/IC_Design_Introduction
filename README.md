<div align="center">

<img src="images/cover.svg" width="200" alt="A chip floorplan: an 8 by 8 array of multiply-accumulate units between two memory blocks, with one unit highlighted">

# IC 設計概論<br>Introduction to IC Design

## [繁體中文](zh-TW/README.md) ｜ [English](en/README.md) ｜ [日本語](ja/README.md) ｜ [한국어](ko/README.md)

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE)
![Chapters](https://img.shields.io/badge/chapters-16-blue.svg)
![Languages](https://img.shields.io/badge/languages-zh--TW%20%7C%20en%20%7C%20ja%20%7C%20ko-red.svg)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>

An open book on IC design for readers with a science or engineering background who have never designed a chip, and for newcomers getting ready to join the industry. It follows a small AI inference chip and one multiply-accumulate unit inside it, from a line in the specification, through Verilog, verification, synthesis, timing and physical design, to tape-out and the first chips on the lab bench. It is the prequel to [Introduction to Semiconductor Manufacturing](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction): the masks handed off at the end of this book are the masks used in that book's lithography chapter. Each chapter has term and know-how boxes, a software analogy for programmers, and optional deep dives. Five chapters have hands-on sections that use open-source tools and the practice files in this repository.

---

## 目錄 · Contents · 目次 · 목차

### 第 0 部　開始之前 · Part 0: Before You Start · 第 0 部　はじめる前に · 제0부 시작하기 전에

| 章 | 繁體中文 | English | 日本語 | 한국어 |
|:---:|---|---|---|---|
| 0 | [IC 設計全景](zh-TW/0-before-you-start/00-overview/README.md) | [The Big Picture](en/0-before-you-start/00-overview/README.md) | [IC 設計の全体像](ja/0-before-you-start/00-overview/README.md) | [IC 설계의 전체 그림](ko/0-before-you-start/00-overview/README.md) |
| 1 | [規格與架構](zh-TW/0-before-you-start/01-spec-and-architecture/README.md) | [Specification and Architecture](en/0-before-you-start/01-spec-and-architecture/README.md) | [仕様とアーキテクチャ](ja/0-before-you-start/01-spec-and-architecture/README.md) | [사양과 아키텍처](ko/0-before-you-start/01-spec-and-architecture/README.md) |

### 第 1 部　數位邏輯基礎 · Part 1: Digital Logic Basics · 第 1 部　デジタル論理の基礎 · 제1부 디지털 논리 기초

| 章 | 繁體中文 | English | 日本語 | 한국어 |
|:---:|---|---|---|---|
| 2 | [從電晶體到邏輯閘](zh-TW/1-digital-logic/02-transistors-to-gates/README.md) | [From Transistors to Logic Gates](en/1-digital-logic/02-transistors-to-gates/README.md) | [トランジスタから論理ゲートへ](ja/1-digital-logic/02-transistors-to-gates/README.md) | [트랜지스터에서 논리 게이트로](ko/1-digital-logic/02-transistors-to-gates/README.md) |
| 3 | [組合邏輯與循序邏輯](zh-TW/1-digital-logic/03-combinational-and-sequential/README.md) | [Combinational and Sequential Logic](en/1-digital-logic/03-combinational-and-sequential/README.md) | [組み合わせ回路と順序回路](ja/1-digital-logic/03-combinational-and-sequential/README.md) | [조합 논리와 순차 논리](ko/1-digital-logic/03-combinational-and-sequential/README.md) |

### 第 2 部　前段設計 · Part 2: Front-End Design · 第 2 部　フロントエンド設計 · 제2부 프런트엔드 설계

| 章 | 繁體中文 | English | 日本語 | 한국어 |
|:---:|---|---|---|---|
| 4 | [RTL 與 Verilog](zh-TW/2-front-end/04-rtl-and-verilog/README.md) | [RTL and Verilog](en/2-front-end/04-rtl-and-verilog/README.md) | [RTL と Verilog](ja/2-front-end/04-rtl-and-verilog/README.md) | [RTL과 Verilog](ko/2-front-end/04-rtl-and-verilog/README.md) |
| 5 | [時脈與重置](zh-TW/2-front-end/05-clocks-and-resets/README.md) | [Clocks and Resets](en/2-front-end/05-clocks-and-resets/README.md) | [クロックとリセット](ja/2-front-end/05-clocks-and-resets/README.md) | [클록과 리셋](ko/2-front-end/05-clocks-and-resets/README.md) |
| 6 | [驗證](zh-TW/2-front-end/06-verification/README.md) | [Verification](en/2-front-end/06-verification/README.md) | [検証](ja/2-front-end/06-verification/README.md) | [검증](ko/2-front-end/06-verification/README.md) |
| 7 | [邏輯合成](zh-TW/2-front-end/07-logic-synthesis/README.md) | [Logic Synthesis](en/2-front-end/07-logic-synthesis/README.md) | [論理合成](ja/2-front-end/07-logic-synthesis/README.md) | [논리 합성](ko/2-front-end/07-logic-synthesis/README.md) |
| 8 | [靜態時序分析](zh-TW/2-front-end/08-static-timing-analysis/README.md) | [Static Timing Analysis](en/2-front-end/08-static-timing-analysis/README.md) | [静的タイミング解析](ja/2-front-end/08-static-timing-analysis/README.md) | [정적 타이밍 분석](ko/2-front-end/08-static-timing-analysis/README.md) |
| 9 | [可測試性設計](zh-TW/2-front-end/09-design-for-test/README.md) | [Design for Test](en/2-front-end/09-design-for-test/README.md) | [テスト容易化設計](ja/2-front-end/09-design-for-test/README.md) | [테스트 용이성 설계](ko/2-front-end/09-design-for-test/README.md) |

### 第 3 部　實體設計 · Part 3: Physical Design · 第 3 部　物理設計 · 제3부 물리 설계

| 章 | 繁體中文 | English | 日本語 | 한국어 |
|:---:|---|---|---|---|
| 10 | [平面規劃與電源網路](zh-TW/3-physical-design/10-floorplan-and-power/README.md) | [Floorplanning and the Power Network](en/3-physical-design/10-floorplan-and-power/README.md) | [フロアプランと電源網](ja/3-physical-design/10-floorplan-and-power/README.md) | [플로어플랜과 전원망](ko/3-physical-design/10-floorplan-and-power/README.md) |
| 11 | [擺置與時脈樹](zh-TW/3-physical-design/11-placement-and-cts/README.md) | [Placement and the Clock Tree](en/3-physical-design/11-placement-and-cts/README.md) | [配置とクロックツリー](ja/3-physical-design/11-placement-and-cts/README.md) | [배치와 클록 트리](ko/3-physical-design/11-placement-and-cts/README.md) |
| 12 | [繞線與寄生效應](zh-TW/3-physical-design/12-routing-and-parasitics/README.md) | [Routing and Parasitics](en/3-physical-design/12-routing-and-parasitics/README.md) | [配線と寄生成分](ja/3-physical-design/12-routing-and-parasitics/README.md) | [배선과 기생 성분](ko/3-physical-design/12-routing-and-parasitics/README.md) |
| 13 | [簽核](zh-TW/3-physical-design/13-signoff/README.md) | [Signoff](en/3-physical-design/13-signoff/README.md) | [サインオフ](ja/3-physical-design/13-signoff/README.md) | [사인오프](ko/3-physical-design/13-signoff/README.md) |

### 第 4 部　交給晶圓廠 · Part 4: Handing Off to the Fab · 第 4 部　ファブへ渡す · 제4부 팹에 넘기기

| 章 | 繁體中文 | English | 日本語 | 한국어 |
|:---:|---|---|---|---|
| 14 | [下線](zh-TW/4-to-the-fab/14-tape-out/README.md) | [Tape-out](en/4-to-the-fab/14-tape-out/README.md) | [テープアウト](ja/4-to-the-fab/14-tape-out/README.md) | [테이프아웃](ko/4-to-the-fab/14-tape-out/README.md) |
| 15 | [晶片回來之後](zh-TW/4-to-the-fab/15-after-silicon/README.md) | [After Silicon Returns](en/4-to-the-fab/15-after-silicon/README.md) | [チップが戻ってきたら](ja/4-to-the-fab/15-after-silicon/README.md) | [칩이 돌아온 뒤](ko/4-to-the-fab/15-after-silicon/README.md) |

### 附錄 · Appendices · 付録 · 부록

| | 繁體中文 | English | 日本語 | 한국어 |
|:---:|---|---|---|---|
| A | [術語總表](zh-TW/appendix/glossary.md) | [Glossary](en/appendix/glossary.md) | [用語集](ja/appendix/glossary.md) | [용어집](ko/appendix/glossary.md) |
| B | [設計現場行話](zh-TW/appendix/jargon.md) | [Designer Jargon](en/appendix/jargon.md) | [設計現場の言い回し](ja/appendix/jargon.md) | [설계 현장 용어](ko/appendix/jargon.md) |
| C | [延伸閱讀](zh-TW/appendix/further-reading.md) | [Further Reading](en/appendix/further-reading.md) | [参考文献](ja/appendix/further-reading.md) | [참고 자료](ko/appendix/further-reading.md) |
| D | [Verilog 速查](zh-TW/appendix/verilog-quick-reference.md) | [Verilog Quick Reference](en/appendix/verilog-quick-reference.md) | [Verilog クイックリファレンス](ja/appendix/verilog-quick-reference.md) | [Verilog 빠른 참조](ko/appendix/verilog-quick-reference.md) |

---

## Reading paths

| Path | Suggested chapters |
|---|---|
| 🚀 Quick overview | Chapters 0, 1, 7, 10 and 14 |
| 💻 Software and firmware engineers | Chapters 0, 1, 3, 4, 6, 8 and 15, and the software analogy in every chapter |
| 🏭 Joining the IC design industry | The whole book in order, with extra attention to Chapters 6, 8 and 13 and Appendix B |
| 🔬 Read *Introduction to Semiconductor Manufacturing* first | Chapters 0, 2, 10, 12, 13 and 14, to see how design connects to the process |
| 🧪 Just want to try it | The Try-it sections of Chapters 4, 6, 7, 8 and 15 |

To follow along, install Icarus Verilog and Yosys as described in [practice/README.md](practice/README.md), then run the commands in each Try-it section from the `practice/` folder. `bash practice/run_all.sh` re-runs every Try-it section and checks the output against the book.

---

## Contributing

- **Found a mistake?** Open an [issue](../../issues) with the "Erratum" template.
- **Want to add content or figures?** Read the [contributing guide](CONTRIBUTING.md) and the [style guide](STYLE_GUIDE.md).
- **Want to translate the book into another language?** Read the [translation guide](TRANSLATIONS.md).

The original text is written in Traditional Chinese, and the other languages are translations of it. If this book helps you, please give it a ⭐ star so that more people can find it.

---

## Disclaimer

This book is based on public information and common industry practice. It contains no confidential information, internal flows or design data of any company, and no real values from any foundry's process design kit. It is not affiliated with any semiconductor company or EDA vendor; the only tools named are the open-source tools used in the Try-it sections. `tiny_npu` is a made-up chip for teaching, and most numbers are orders of magnitude or rough values.

## License

The text, images and practice files are licensed under [CC BY-NC-SA 4.0](LICENSE). You may share, adapt and translate them for non-commercial purposes, as long as you give credit and share your work under the same license.
