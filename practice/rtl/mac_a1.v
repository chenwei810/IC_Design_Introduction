// mac_a1.v - Chapter 15: the A1 fix. Same pipeline as mac_ch08.v, plus the
// saturation that the spec asked for from the start.
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

    // Stage 2: accumulate with saturation.
    wire signed [24:0] sum = acc + prod;     // one extra bit
    wire               ovf = sum[24] ^ sum[23]; // top two bits differ
    wire signed [23:0] sat = sum[24] ? 24'sh800000   // most negative
                                     : 24'sh7FFFFF;  // most positive
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            acc <= 24'sd0;
        else if (clr_d)
            acc <= 24'sd0;
        else if (en_d)
            acc <= ovf ? sat : sum[23:0];
    end
endmodule
