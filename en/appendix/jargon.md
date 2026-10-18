<!-- source: zh-TW/appendix/jargon.md | sha: 8d4dd4cca1e9 -->

# Appendix B: Designer Jargon

IC design teams have their own everyday vocabulary, such as "The slack on this path blew up. Cut it in the middle." Newcomers hearing it for the first time are often lost.

This appendix lists expressions commonly heard on IC design teams, with example sentences. The second column shows how each one is usually said on Taiwanese teams, where people mix Chinese with English terms; this is useful if you work with Taiwanese colleagues. Habits differ between companies and teams, so these are the most widely used forms. For formal definitions, see [Appendix A: Glossary](glossary.md).

---

## Flow and schedule

| Expression | On Taiwanese teams | Meaning | Example |
|---|---|---|---|
| Spec | spec | The specification | "The spec says saturate. Why does the RTL wrap around?" |
| Freeze | freeze | Frozen; no casual changes after this point | "After RTL freeze, every change has to go through an ECO." |
| Tape out | 下線、tape-out | Hand the design to the fab | "We tape out next month, so let's wrap up signoff this week." |
| Shuttle | shuttle | One scheduled MPW run | "If we miss this shuttle, we wait another two months." |
| Sign off | signoff | Formally pass one of the checks | "DRC is signed off. IR is what's left." |
| Back to the front end | 打回前段 | A problem so big that the RTL has to change | "We're this far off? Then it goes back to the front end for an architecture change." |

## Front-end design

| Expression | On Taiwanese teams | Meaning | Example |
|---|---|---|---|
| Instantiate, instance | instantiate、instance | Place a copy of a module; the copy itself | "The top level instantiates 64 `mac`s." |
| Lint it | lint 一下 | Run lint to check the coding style | "Lint it before you send it to synthesis." |
| Infer a latch | 長出 latch | Synthesis creates a latch by accident | "The `case` has no `default`, so it inferred a latch." |
| Optimized away | 被 optimize 掉 | Removed by the synthesis tool | "This register got optimized away. Your output isn't connected." |
| Go through CDC | 過 CDC | A signal crossing clock domains goes through a synchronizer | "`START` comes from the bus side, so it has to go through CDC." |
| Meta | meta | Metastability | "The first flop can go meta. Don't use it directly." |

## Verification

| Expression | On Taiwanese teams | Meaning | Example |
|---|---|---|---|
| TB | TB | Testbench | "Hook up the TB first and run a smoke test." |
| Smoke test | smoke test | The most basic, fastest test, to confirm nothing is badly broken | "If the smoke test doesn't pass, don't bother with regression." |
| Golden, golden model | golden、golden model | The reference model | "The RTL doesn't match golden." |
| Run regression | 跑 regression | Run the regression tests | "Three tests failed in tonight's regression." |
| Fail | 掛了 | A test failed | "Seed 7 failed. I'll take a look." |
| Seed | seed | The random seed | "Give me the seed and I'll rerun it." |
| Covered | cover 到 | Measured by coverage | "The overflow case isn't covered." |
| Dump waves | dump 波形 | Save the simulation waveform for debugging | "Dump the waves and you'll see it." |
| Corner case | corner case | A rare edge condition | "Did we test the corner case where `LEN` is 0?" |

## Timing and the back end

| Expression | On Taiwanese teams | Meaning | Example |
|---|---|---|---|
| Close timing | 收 timing | Fix timing violations until there are none | "The back end is still closing timing. Don't touch the netlist." |
| Violation | violation | A violation | "There are still two hundred setup violations." |
| Slack blew up | slack 爆了 | The slack is negative, by a lot | "This path is 0.3 ns negative." |
| Cut it | 切一刀 | Insert a pipeline stage | "The multiply plus add is too long. Cut it in the middle." |
| Add hold buffers | 補 hold buffer | Insert delay buffers to fix hold | "Add the hold buffers after CTS." |
| P&R, APR | P&R、APR | Placement and routing | "This P&R run took all night." |
| Congested | 塞爆 | So crowded that wires cannot get through | "It's totally congested next to the MAC array." |
| Extract RC | 抽 RC | Parasitic extraction | "Timing dropped again after RC extraction." |
| Clean | clean | A check with no violations at all | "LVS is finally clean." |
| Waive it | waive 掉 | Put it on the waiver list | "`LEN` is fixed before `START`, so we can waive this CDC violation." |

## After silicon returns

| Expression | On Taiwanese teams | Meaning | Example |
|---|---|---|---|
| Samples are back | 樣品回來了 | The first chips have arrived at the lab | "Samples come back next week. The boards need to be ready first." |
| Bring up | 點亮 | Power up for the first time and confirm the basics | "We brought it up on day one. The PLL locked." |
| Run a shmoo | 跑 shmoo | Measure the working range of voltage and frequency | "Run a shmoo first and see where the low-voltage edge is." |
| Workaround | 繞過、workaround | Avoid a hardware bug in firmware or software | "Work around it in firmware for this stepping. A1 will fix it." |
| Metal fix | metal fix | A fix that changes only the metal layers | "A metal fix is enough for this bug. No need to redo everything." |
| Full respin | full respin | Remake every mask from the bottom layer up | "If the transistor layers have to change, it's a full respin." |
| A0, A1, B0 | A0、A1、B0 | Steppings | "If A2 needs another fix, we only swap three metal masks." |

---

[← Appendix A: Glossary](glossary.md) | [Contents](../README.md) | [Appendix C: Further Reading →](further-reading.md)
