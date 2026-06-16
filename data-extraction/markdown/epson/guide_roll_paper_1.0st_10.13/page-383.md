## C O N F I D E N T I A L

- n specifies the number of bytes of bar code data.
- d specifies the character code data of the bar code data to be printed.

## [Recommended Functions]

Refer to GS ( k for printing the 2-dimensional GS1 DataBar shown below.

GS1 DataBar Stacked, GS1 DataBar Stacked Omnidirectional, GS1 DataBar Expanded Stacked

- ■ When standard mode is selected, this command is enabled only when the print position is at the head of a line or when no data exists in the print buffer.
- ■ When page mode is selected, this command develops the bar code data in the print buffer but the printer does not print the bar code data.
- ■ The bar code width that exceeds the print area cannot be specified.
- ■ This command feeds as much paper as is required to print the bar code, regardless of the line spacing specified by line space setting commands.
- ■ The bar code is not affected by print mode (emphasized, underline, or 90° clockwise-rotated), except for upside-down print mode.
- ■ After bar code printing, the print position moves to the left end of the print area. The printer enters the status of print position at the head of a line or no data exists in the print buffer.
- ■ The values of m from 0 to 6 in (A) and from 65 to 71 in (B) select the same bar code system, respectively. The printing results are the same.
- ■ This command specifies m = 0 to 6 and ends with a NUL code.
- ■ When an odd number of data is processed for ITF bar code system ( m = 5), the printer ignores the last received data.
- ■ The printer processes n bytes from the next data as bar code data by this command specifying m = 65 to 78.
- ■ Print area does not include quiet zone (left/right margin) of bar code. Make sure to secure the quiet zone, using this command.

[Notes for UPC-A ( m = 0, 65) process]

- ■ Modular check character (1 character) is processed as follows:
- Automatically added when processing data is 11 byte.

[Notes]
