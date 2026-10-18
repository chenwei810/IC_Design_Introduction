// mac_ch08.v - Chapter 8: one pipeline stage between the multiplier and
// the adder. The result comes out one clock cycle later.
// This is the version taped out as A0. Saturation is still missing.
module mac (
    input  wire               clk,
    input  wire               rst_n,
    input  wire               clr,
    input  wire               en,
    input  wire signed [7:0]  a,
    input  wire signed [7:0]  b,
    output reg  signed [23:0] acc
);
    // Stage 1: multiply, and delay the control signals to match.
    reg signed [15:0] prod;
    reg               clr_d, en_d;
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            prod  <= 16'sd0;
            clr_d <= 1'b0;
            en_d  <= 1'b0;
        end else begin
            prod  <= a * b;
            clr_d <= clr;
            en_d  <= en;
        end
    end

    // Stage 2: accumulate.
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            acc <= 24'sd0;
        else if (clr_d)
            acc <= 24'sd0;
        else if (en_d)
            acc <= acc + prod;
    end
endmodule
