<!--
Chapter template (English): copy this file into a chapter folder under en/ and rename it README.md.
Read section 9 of STYLE_GUIDE.md first, and delete this comment when you are done.
Keep the "🧪 Try it" section only in Chapters 4, 6, 7, 8 and 15.
The first line of a translated file is its source marker. See TRANSLATIONS.md.
-->

# Chapter N: Topic — Subtitle

> 📍 **Where the design is**
>
> - Previous stop: ...
> - **This chapter: ...**
> - Next stop: ...

🪜 Abstraction level: Spec ▸ **RTL** ▸ Netlist ▸ Layout ▸ GDS ▸ Chip

---

## Why this step is needed

Use an everyday comparison to explain the problem this chapter solves.

> [!NOTE]
> **📖 Term | English term (中文術語)**
>
> - **Definition**:
> - **On the job**:
> - **Related terms**:
> - **Common confusion**:

---

## How it works

Comparison first, then the term. Use only the most basic formulas.

```verilog
// Verilog snippets: 15 lines at most, comments in English.
```

> [!IMPORTANT]
> **💻 Software analogy | One sentence that states the comparison**
>
> - **Like**:
> - **Unlike**:
> - **Watch out**:

<details>
<summary>🔍 Going deeper: A title that tells readers whether to open it</summary>

For electrical engineering and computer science students. Readers who skip it must still be able to follow the rest.

</details>

---

## The flow

**Step one → Step two → Step three**

1. **Step one**:
2. **Step two**:
3. **Step three**:

> [!TIP]
> **🔧 Know-how | One sentence that states the point**
>
> - **Situation**:
> - **Practice**:
> - **Why**:
> - **If you skip it**:
> - **Related chapters**:

---

## Common problems

| Problem | Likely cause | Result |
|---|---|---|
| | | |

---

## 🧪 Try it: Title

Run these in the `practice/` folder (see [practice/README.md](../../../practice/README.md) for installation):

```bash
iverilog -o sim rtl/mac_ch04.v tb/tb_mac.v
vvp sim +vec=vectors/directed.txt +verbose
```

```text
(paste the real output)
```

---

## Key takeaways

1. Point one
2. Point two
3. Point three

---

## Further reading

- Author, *Title*, relevant chapters
- *Introduction to Semiconductor Manufacturing*, [Chapter N: Title](https://github.com/chenwei810/Semiconductor_Manufacturing_Introduction/blob/main/en/...)

---

[← Chapter N-1: Title](relative/path) | [Contents](../../README.md) | [Chapter N+1: Title →](relative/path)
