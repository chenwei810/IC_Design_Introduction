<!-- source: zh-TW/appendix/further-reading.md | sha: f011f3142716 -->

# 부록 C 참고 자료

이 부록에서는 각 장에서 인용한 참고 자료와, 더 깊이 알고 싶을 때 참고할 만한 책, 표준, 오픈 소스 도구를 정리합니다. 자료는 대부분 영어이므로, 읽을 때 [부록 A 용어집](glossary.md)을 함께 쓰면 좋습니다.

---

## 입문과 총론

| 자료 | 설명 | 관련 장 |
|---|---|---|
| Neil H. E. Weste, David Money Harris, 『CMOS VLSI Design: A Circuits and Systems Perspective』 제4판 | 트랜지스터부터 시스템까지 다루는 고전 교과서. 이 책의 주제 대부분을 담고 있다 | 0, 2, 7, 8 |
| Jan M. Rabaey, Anantha Chandrakasan, Borivoje Nikolić, 『Digital Integrated Circuits: A Design Perspective』 제2판 | 회로 수준에 무게를 두고, 지연과 전력을 깊이 다룬다 | 2 |

## 디지털 논리와 Verilog

| 자료 | 설명 | 관련 장 |
|---|---|---|
| David Money Harris, Sarah L. Harris, 『Digital Design and Computer Architecture』 제2판 | 2진수와 논리 게이트부터 프로세서까지. Verilog 예제가 있다 | 3, 4 |
| M. Morris Mano, Michael D. Ciletti, 『Digital Design』 제6판 | 디지털 논리의 고전 입문서 | 3 |
| Samir Palnitkar, 『Verilog HDL: A Guide to Digital Design and Synthesis』 제2판 | Verilog 입문서이자 참고서 | 4 |
| Clifford E. Cummings, 「Nonblocking Assignments in Verilog Synthesis, Coding Styles That Kill!」, 2000 | 블로킹 대입과 논블로킹 대입에 관한 고전 논문 | 4 |
| Clifford E. Cummings, 「Clock Domain Crossing (CDC) Design & Verification Techniques Using SystemVerilog」, 2008 | 동기화기, 핸드셰이크, 비동기 FIFO | 5 |
| Clifford E. Cummings, Don Mills, Steve Golson, 「Asynchronous & Synchronous Reset Design Techniques - Part Deux」, 2003 | 리셋 설계 방법과 리셋 동기화기 | 5 |

## 검증

| 자료 | 설명 | 관련 장 |
|---|---|---|
| Janick Bergeron, 『Writing Testbenches: Functional Verification of HDL Models』 제2판 | 검증 방법의 고전. 테스트벤치부터 커버리지까지 | 6 |
| Chris Spear, Greg Tumbush, 『SystemVerilog for Verification』 제3판 | SystemVerilog로 하는 제약 랜덤 테스트와 커버리지 | 6 |
| Accellera, 『Universal Verification Methodology (UVM) User's Guide』 | 업계 표준 검증 방법론의 공식 안내서 | 6 |

## 논리 합성, 타이밍, 테스트, 물리 설계

| 자료 | 설명 | 관련 장 |
|---|---|---|
| Giovanni De Micheli, 『Synthesis and Optimization of Digital Circuits』 | 논리 합성 뒤에 있는 알고리즘 | 7 |
| J. Bhasker, Rakesh Chadha, 『Static Timing Analysis for Nanometer Designs: A Practical Approach』 | STA 실무서. 라이브러리, 기생 성분, 크로스토크, SDC를 다룬다 | 8, 13 |
| Michael L. Bushnell, Vishwani D. Agrawal, 『Essentials of Electronic Testing for Digital, Memory and Mixed-Signal VLSI Circuits』 | 고장 모델, ATPG, 스캔, 메모리 테스트 | 9 |
| Andrew B. Kahng, Jens Lienig, Igor L. Markov, Jin Hu, 『VLSI Physical Design: From Graph Partitioning to Timing Closure』 | 플로어플랜, 배치, 배선, 클록 트리, 타이밍 클로저의 알고리즘 | 10～12 |
| Alfred Kwok-Kit Wong, 『Resolution Enhancement Techniques in Optical Lithography』 | OPC 등 해상도 향상 기술 | 14 |
| Prabhat Mishra, Farimah Farahmandi 엮음, 『Post-Silicon Validation and Debug』 | 포스트 실리콘 검증과 디버깅 방법 | 15 |

## AI 칩과 아키텍처

| 자료 | 설명 | 관련 장 |
|---|---|---|
| John L. Hennessy, David A. Patterson, 『Computer Architecture: A Quantitative Approach』 제6판, 제7장 | 도메인 특화 아키텍처. 신경망 가속기를 포함한다 | 1 |
| Vivienne Sze, Yu-Hsin Chen, Tien-Ju Yang, Joel S. Emer, 『Efficient Processing of Deep Neural Networks』 | 신경망 가속기의 데이터 흐름, 양자화, 에너지 | 1 |

## 표준

| 자료 | 설명 | 관련 장 |
|---|---|---|
| IEEE 1364 | 하드웨어 기술 언어 Verilog | 4 |
| IEEE 1800 | SystemVerilog. Verilog의 전체 문법도 포함한다 | 4, 6 |
| IEEE 1800.2 | 검증 방법론 UVM | 6 |
| IEEE 1801 | 저전력 설계 의도를 기술하는 UPF | 10 |
| IEEE 1149.1 | JTAG 테스트 인터페이스와 바운더리 스캔 | 9, 15 |

## 따라 해 보기에서 쓰는 오픈 소스 도구

| 자료 | 설명 | 관련 장 |
|---|---|---|
| [Icarus Verilog](https://steveicarus.github.io/iverilog/) | Verilog 시뮬레이터. 이 책에서는 12.0을 쓴다 | 4, 6, 8, 15 |
| [Yosys](https://yosyshq.readthedocs.io/projects/yosys/) | 오픈 소스 논리 합성 도구. 이 책에서는 0.33을 쓴다 | 7, 8 |
| [GTKWave](https://github.com/gtkwave/gtkwave) | 파형 뷰어 | 6 |

## 시리즈의 다른 책

| 자료 | 설명 | 관련 장 |
|---|---|---|
| 『[반도체 제조 입문](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/ko/README.md)』 | 이 책의 속편. 웨이퍼 한 장을 따라 마스크 이후의 제조 여정을 걷는다 | 0～2, 9～15 |
| 『[Git 입문](https://github.com/chenwei810/Git_Introduction/blob/main/ko/README.md)』 | RTL과 실습 파일을 관리하는 데 꼭 필요한 버전 관리 | 4 |

---

[← 부록 B 설계 현장 용어](jargon.md) ｜ [목차](../README.md) ｜ [부록 D Verilog 빠른 참조 →](verilog-quick-reference.md)
