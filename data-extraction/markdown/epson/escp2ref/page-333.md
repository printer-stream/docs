The following binary commands are applicable to the TIFF compressed mode. All other commands are ignored after entering extended raster graphics.

&lt;XFER&gt; Transfer raster graphics data &lt;MOVX&gt; Set relative horizontal position &lt;MOVY&gt; Set relative vertical position &lt;COLR&gt; Select printing color &lt;CR&gt; Carriage return to left-most print position &lt;EXIT&gt; Exit TIFF compressed mode &lt;MOVXBYTE&gt; Set &lt;MOVX&gt; unit to 8 dots &lt;MOVXDOT&gt; Set &lt;MOVX&gt; unit to 1 dot

The binary mode commands are divided into three classes:

Class Description 1 command without parameter 2 command with parameter 3 command with parameter and data

## Bit assignments

Bit assignments for the binary mode commands are as follows:

## Class 1 commands (without parameter)

Command ID

Bits 0-3 Bit 4 Flag bit Bits 5-7 Opcode

Class 2 commands (with parameter) Bits 0-3 Parameter or counter Bit 4 Flag bit Bits 5-7 Opcode

## Class 3 commands (with parameter and data)

Bits 0-3 Definition changes based on bit 4 Bit 4 = 0 Bits 0-3 are twos complement parameter Bit 4 = 1 Bits 0-3 are parameter byte count Bits 5-7 Opcode
