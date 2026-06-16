## C O N F I D E N T I A L

## GS ( k &lt;Function 080&gt;

[Name] PDF417: Store the data in the symbol storage area [Format] ASCII GS ( k pL pH cn fn m d1...dk Hex 1D 28 6B pL pH 30 50 30 d1...dk Decimal 29 40 107 pL pH 48 80 48 d1...dk [Range] 4 ≤ ( pL + pH × 256) ≤ 65535 (0 ≤ pL ≤ 255, 0 ≤ pH ≤ 255) cn = 48 fn = 80 m = 48 0 ≤ d ≤ 255 k = ( pL + pH × 256) - 3

[Description] [Notes]

Stores the PDF417 symbol data ( d1...dk ) in the symbol storage area.

- ■ The symbol data saved in the symbol storage area by this function is encoded by &lt;Function 081&gt; and &lt;Function 082&gt; of this command. After &lt;Function 081&gt; and &lt;Function 082&gt; are executed, the symbol data in the symbol storage area is kept.
- ■ k bytes of d1...dk are processed as symbol data.
- ■ Specify only the data codeword of the symbol with this function. Be sure not to include the following data in the data d1...dk because they are added automatically by the printer.
- Start pattern and stop pattern
- Indicator codeword of left and right
- The descriptor of symbol length (the first codeword in the data area)
- The error correction codeword calculated by modulus 929
- ■ Settings of this function are effective until the following processing is performed:
- Function 080 or 180 or 280 or 380 or 480 is executed
- ESC @ is executed
- The printer is reset or the power is turned off

[Model-dependent variations]

TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-P60
