// mac_ch04.v - the first RTL of the multiply-accumulate unit (Chapter 4).
// It hides two problems that later chapters will find:
//   1. a, b and acc are not declared signed (found in Chapter 6).
//   2. The spec asks for saturation on overflow, but it is not implemented
//      (found on real silicon in Chapter 15).
module mac (
    input  wire        clk,
    input  wire        rst_n,   // active-low reset
    input  wire        clr,     // start a new dot product
    input  wire        en,      // accumulate a * b this cycle
    input  wire [7:0]  a,       // activation, INT8
    input  wire [7:0]  b,       // weight, INT8
    output reg  [23:0] acc      // 24-bit accumulator
);
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            acc <= 24'd0;          // reset: clear the accumulator
        else if (clr)
            acc <= 24'd0;          // a new dot product starts
        else if (en)
            acc <= acc + a * b;    // multiply, then add
    end
endmodule
