<!-- source: zh-TW/2-front-end/README.md | sha: 1418aa7c1e9e -->

# 제2부 프런트엔드 설계

사양을 RTL로 쓰고, 그것이 맞다는 것을 보이고, 네트리스트로 합성한 뒤 타이밍을 확인하고 테스트 회로를 넣습니다. 이 부에서 `mac`이 작성되고, 첫 번째 문제가 발견되고, 파이프라인 한 단이 들어갑니다.

| 장 | 읽을 내용 |
|---|---|
| [제4장 RTL과 Verilog](04-rtl-and-verilog/README.md) | Verilog로 `mac` 작성하기, 그리고 하드웨어와 프로그램의 차이 |
| [제5장 클록과 리셋](05-clocks-and-resets/README.md) | PLL, 클록 도메인 크로싱, 준안정 상태, 리셋 동기화, 클록 게이팅 |
| [제6장 검증](06-verification/README.md) | 테스트벤치, 참조 모델, 랜덤 테스트, 커버리지, 검증 계획 |
| [제7장 논리 합성](07-logic-synthesis/README.md) | 표준 셀 라이브러리, 타이밍 제약, 네트리스트, 등가성 검사 |
| [제8장 정적 타이밍 분석](08-static-timing-analysis/README.md) | 셋업, 홀드, 슬랙, 공정 코너, 파이프라인 |
| [제9장 테스트 용이성 설계](09-design-for-test/README.md) | 스캔 체인, ATPG, MBIST, JTAG |

---

[← 제1부 디지털 논리 기초](../1-digital-logic/README.md) ｜ [목차](../README.md) ｜ [제3부 물리 설계 →](../3-physical-design/README.md)
