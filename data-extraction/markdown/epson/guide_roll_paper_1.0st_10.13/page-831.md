## C O N F I D E N T I A L

## FS ( L &lt; Function 67 &gt;

[Name] Feed paper to the print starting position [Format] ASCII FS ( L pL pH fn m Hex 1C 28 4C 02 00 43 m Decimal 28 40 76 2 0 67 m [Range] ( pL + pH × 256) = 2 ( pL = 2, pH = 0) m = 48, 49, 50 fn = 67 TM-L90 : [with Peeler] m = 50 [When the peeling issuing mode is selected] 48 ≤ m ≤ 50 [When the continuous issuing mode is selected] [Models other than the above] 48 ≤ m ≤ 50 TM-P60 : 48 ≤ m ≤ 50

[Range]

[Notes]

Executes paper feed until the 'print starting position' specified in the paper layout reaches the print head position.

|   m | Function                                                                                                                                                                                                                                                                                                                                  |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  48 | Feeds paper to the print starting position on the next label. However, if the paper is in standby at the print starting position, the printer does not feed.                                                                                                                                                                              |
|  49 | Feeds paper to the print starting position on the next label. However, if the paper is in standby at the print starting position, the printer feeds paper to the next print starting position.                                                                                                                                            |
|  50 | Feeds paper to the label peeling position. However, if the paper is in standby at the label peeling position, the printer feeds paper to the next label peeling position. Feeds paper to the print starting position on the current label. However, if the paper is in standby at the print starting position, the printer does not feed. |

- ■ Use this function by using 'the first state of the line' in standard mode.
