## C O N F I D E N T I A L

## GS ( K &lt;Function 49&gt;

[Name] Select the print density [Format] ASCII GS ( K pL pH fn m Hex 1D 28 4B 02 00 31 m Decimal 29 49 75 2 0 48 m [Range] ( pL + pH × 256) = 2     ( pL = 2, pH = 0) fn = 49 TM-T90 : 250 ≤ m ≤ 255, 0 ≤ m ≤ 6 TM-L90 : 250 ≤ m ≤ 255, 0 ≤ m ≤ 8 [Default] m = 0 [Description] Selects the print density by m .

| m         | Function                                                                        |
|-----------|---------------------------------------------------------------------------------|
| 128 - 255 | Pale density                                                                    |
| 0         | Standard density [setting value of GS ( E Function 5 customize value ( a = 5) ] |
| 1 - 127   | Strong density                                                                  |

- The specification of each print density differs, depending on the printer model. See model-dependent variations.
- ■ When a standard mode is selected, all the data in a line is printed in the same density.

[Notes]

- ■ When a page mode is selected, all the data printed collectively by FF or ESC FF is printed in the same density.

[Model-dependent variations]

TM-J2000/J2100 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-T90 , TM-L90 , TM-P60

TM-J2000/J2100 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-P60

This printer does not support this function.
