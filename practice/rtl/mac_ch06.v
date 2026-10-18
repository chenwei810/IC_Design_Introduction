// mac_ch06.v - Chapter 6: a, b and acc are now declared signed.
// Saturation is still missing (found on real silicon in Chapter 15).
module mac (
    input  wire               clk,
    input  wire               rst_n,
    input  wire               clr,
    input  wire               en,
    input  wire signed [7:0]  a,
    input  wire signed [7:0]  b,
    output reg  signed [23:0] acc
);
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            acc <= 24'sd0;
        else if (clr)
            acc <= 24'sd0;
        else if (en)
            acc <= acc + a * b;
    end
endmodule
