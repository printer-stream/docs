## C O N F I D E N T I A L

- ■ [Position information A] is shown in the following.
- Bit 0 becomes '1' immediately after this command &lt; Function 65&gt; is executed, and becomes '0' by executing mechanical operations with paper feed.
- Bit 1 becomes '1' immediately after this command &lt; Function 66&gt; is executed, and becomes '0' by executing mechanical operations with paper feed.
- Bit 2 becomes '1' when cover closes, manual feeding by pressing the switch is done, the print start according to print instruction, and the power supply is turned on immediately after this command &lt; Function 67&gt; is executed, and becomes '0' by executing mechanical operations with paper feed.
- Bits 0, 1, and 2 always become '0' when the origin of layout is 'paper layout is not used' and when the cover is open.

| Bit    | Function                                                                       | Binary   | Hex   | Decimal   |
|--------|--------------------------------------------------------------------------------|----------|-------|-----------|
| 0      | Relation to the label peeling position; Not at label peeling position.         | 0        | 00    | 0         |
| 0      | Relation to the label peeling position: Standby at the label peeling position. | 1        | 01    | 1         |
| 1      | Relation to the cutting position: Not at cutting position.                     | 0        | 00    | 0         |
| 1      | Relation to the cutting position: Standby at the cutting position.             | 0        | 02    | 2         |
| 2      | Relation to the print start position: Not at print start position.             | 0        | 00    | 0         |
| 2      | Relation to the print start position: Standby at the print start position.     | 1        | 04    | 4         |
| 3 to 5 | Reserved                                                                       | -        | -     | -         |
| 6      | Fixed                                                                          | 1        | 40    | 64        |
| 7      | Fixed                                                                          | 0        | 00    | 0         |
