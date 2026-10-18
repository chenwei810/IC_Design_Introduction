// tb_mac.v - testbench for the MAC unit.
// Reads one operation per line from a vector file ("clr en a b expected"),
// drives the MAC, and compares acc with the expected value LAT cycles later.
//
//   vvp sim +vec=vectors/directed.txt +verbose
//   vvp sim +vec=vectors/random.txt
//   iverilog -P tb.LAT=2 ...   (the pipelined MAC of Chapter 8)
`timescale 1ns / 1ps
module tb;
    parameter LAT = 1;              // clock cycles from input to acc
    localparam MAXV = 4096;

    reg clk = 0, rst_n = 0, clr = 0, en = 0;
    reg signed [7:0] a = 0, b = 0;
    wire [23:0] acc_bits;
    wire signed [23:0] acc = acc_bits;

    mac dut (.clk(clk), .rst_n(rst_n), .clr(clr), .en(en),
             .a(a), .b(b), .acc(acc_bits));

    always #1 clk = ~clk;           // 2 ns period: 500 MHz

    integer v_clr [0:MAXV-1], v_en [0:MAXV-1];
    integer v_a   [0:MAXV-1], v_b  [0:MAXV-1], v_exp [0:MAXV-1];
    integer n, i, k, fd, r, errors, verbose, show_sums;
    reg [1023:0] vec_file;

    task check(input integer j);
        begin
            if (show_sums && (j == n - 1 || (j + 1 < n && v_clr[j + 1] == 1)) && v_clr[j] == 0)
                $display("dot product done: acc = %0d", acc);
            if (acc !== v_exp[j]) begin
                errors = errors + 1;
                if (errors <= 3)
                    $display("MISMATCH at line %0d: a = %0d, b = %0d, expected %0d, got %0d",
                             j + 1, v_a[j], v_b[j], v_exp[j], acc);
            end else if (verbose) begin
                if (v_clr[j])
                    $display("clr                ->  acc = %0d   (expected %0d)", acc, v_exp[j]);
                else
                    $display("a = %4d, b = %4d  ->  acc = %0d   (expected %0d)",
                             v_a[j], v_b[j], acc, v_exp[j]);
            end
        end
    endtask

    initial begin
        if (!$value$plusargs("vec=%s", vec_file)) vec_file = "vectors/directed.txt";
        verbose   = $test$plusargs("verbose");
        show_sums = $test$plusargs("show_sums");
        if ($test$plusargs("vcd")) begin
            $dumpfile("mac.vcd");
            $dumpvars(0, tb);
        end
        fd = $fopen(vec_file, "r");
        if (fd == 0) begin
            $display("cannot open %0s", vec_file);
            $finish(0);
        end
        n = 0;
        while (!$feof(fd) && n < MAXV) begin
            r = $fscanf(fd, "%d %d %d %d %d\n", v_clr[n], v_en[n], v_a[n], v_b[n], v_exp[n]);
            if (r == 5) n = n + 1;
        end
        $fclose(fd);

        errors = 0;
        repeat (2) @(negedge clk);
        rst_n = 1;
        // Apply line k at a falling edge; its result appears LAT rising edges later.
        for (k = 0; k < n + LAT; k = k + 1) begin
            @(negedge clk);
            if (k - LAT >= 0) check(k - LAT);
            if (k < n) begin
                clr = v_clr[k]; en = v_en[k]; a = v_a[k]; b = v_b[k];
            end else begin
                clr = 0; en = 0; a = 0; b = 0;
            end
        end
        if (errors == 0)
            $display("PASS: %0d of %0d checks passed", n, n);
        else
            $display("FAIL: %0d of %0d checks failed", errors, n);
        $finish(0);
    end
endmodule
