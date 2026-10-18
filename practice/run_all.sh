#!/usr/bin/env bash
# Re-run every Try-it section of the book and compare the output with the
# copies in expected/. Run from anywhere:
#
#   bash practice/run_all.sh            # check
#   bash practice/run_all.sh --update   # after changing the book's outputs
#
# The outputs in the book come from Icarus Verilog 12.0 and Yosys 0.33.
# Other versions may give slightly different cell counts in Chapter 7.
set -u
cd "$(dirname "$0")"
work=$(mktemp -d)
trap 'rm -rf "$work"; rm -f sim netlist.v mac.vcd' EXIT
fail=0

yosys_ltp()  { yosys -q -p "read_verilog $1; synth -top mac; tee -o /dev/stdout ltp -noff" | grep Longest; }

{   # Chapter 4: the first RTL passes the directed test.
    iverilog -o sim rtl/mac_ch04.v tb/tb_mac.v
    vvp sim +vec=vectors/directed.txt +verbose
} > "$work/ch04.txt" 2>&1

{   # Chapter 6: random test against the reference model, then the fix.
    python3 ref_model.py random --seed 1 > "$work/random.txt"
    cmp -s "$work/random.txt" vectors/random.txt || echo "vectors/random.txt differs"
    head -n 3 vectors/random.txt
    vvp sim +vec=vectors/random.txt
    iverilog -o sim rtl/mac_ch06.v tb/tb_mac.v
    vvp sim +vec=vectors/random.txt
    vvp sim +vec=vectors/directed.txt
} > "$work/ch06.txt" 2>&1

{   # Chapter 7: synthesis.
    yosys -q -p "read_verilog rtl/mac_ch06.v; synth -top mac; write_verilog -noattr -noexpr netlist.v; tee -o /dev/stdout stat" | sed -n '/Number of cells/,$p'
    wc -l rtl/mac_ch06.v netlist.v
    grep -m 1 -A 4 '_XOR_' netlist.v
    grep -A 6 'acc_reg\[6\]' netlist.v
} > "$work/ch07.txt" 2>&1

{   # Chapter 8: logic depth before and after the pipeline; latency changes.
    yosys_ltp rtl/mac_ch06.v
    yosys_ltp rtl/mac_ch08.v
    iverilog -o sim rtl/mac_ch08.v tb/tb_mac.v
    vvp sim +vec=vectors/random.txt
    iverilog -P tb.LAT=2 -o sim rtl/mac_ch08.v tb/tb_mac.v
    vvp sim +vec=vectors/random.txt
} > "$work/ch08.txt" 2>&1

{   # Chapter 15: overflow on A0, the firmware workaround, and the A1 fix.
    python3 ref_model.py overflow > "$work/overflow.txt"
    cmp -s "$work/overflow.txt" vectors/overflow.txt || echo "vectors/overflow.txt differs"
    python3 ref_model.py overflow --chunk 511 > "$work/chunk.txt"
    cmp -s "$work/chunk.txt" vectors/overflow_chunk511.txt || echo "vectors/overflow_chunk511.txt differs"
    iverilog -P tb.LAT=2 -o sim rtl/mac_ch08.v tb/tb_mac.v
    vvp sim +vec=vectors/overflow.txt +show_sums
    vvp sim +vec=vectors/overflow_chunk511.txt +show_sums
    iverilog -P tb.LAT=2 -o sim rtl/mac_a1.v tb/tb_mac.v
    vvp sim +vec=vectors/overflow.txt +show_sums
    vvp sim +vec=vectors/random.txt
} > "$work/ch15.txt" 2>&1

for ch in ch04 ch06 ch07 ch08 ch15; do
    if [ "${1:-}" = "--update" ]; then
        mkdir -p expected
        cp "$work/$ch.txt" "expected/$ch.txt"
        echo "SAVED $ch"
    elif diff -u "expected/$ch.txt" "$work/$ch.txt" > "$work/$ch.diff"; then
        echo "OK    $ch"
    else
        echo "DIFF  $ch"
        cat "$work/$ch.diff"
        fail=1
    fi
done
exit $fail
