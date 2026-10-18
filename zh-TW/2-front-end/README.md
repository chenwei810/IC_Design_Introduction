# 第 2 部　前段設計

把規格寫成 RTL、證明它是對的，再合成成網表，確認時序並加入測試電路。`mac` 在這一部被寫出來、測出第一個問題，也插入了一級管線。

| 章節 | 你會讀到 |
|---|---|
| [第 4 章　RTL 與 Verilog](04-rtl-and-verilog/README.md) | 用 Verilog 寫出 `mac`，以及硬體和程式的不同 |
| [第 5 章　時脈與重置](05-clocks-and-resets/README.md) | PLL、跨時脈域、亞穩態、重置同步與時脈閘控 |
| [第 6 章　驗證](06-verification/README.md) | Testbench、參考模型、亂數測試、覆蓋率與驗證計畫 |
| [第 7 章　邏輯合成](07-logic-synthesis/README.md) | 標準元件庫、時序限制、網表與等價性檢查 |
| [第 8 章　靜態時序分析](08-static-timing-analysis/README.md) | setup、hold、slack、製程角落與管線 |
| [第 9 章　可測試性設計](09-design-for-test/README.md) | 掃描鏈、ATPG、MBIST 與 JTAG |

---

[← 第 1 部　數位邏輯基礎](../1-digital-logic/README.md) ｜ [目錄](../README.md) ｜ [第 3 部　實體設計 →](../3-physical-design/README.md)
