## C O N F I D E N T I A L

[Model-dependent variations] TM-L90 , TM-P60

## TM-L90

This printer does not support this function.

## TM-P60

Since combinations with the parameters in the table below result in invalid values, this function will not work.

| sm   | Combinations resulting in invalid values                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| '1'  | If ( sa ≤ sb + sc + &#124; se &#124;) when ( sa ≠ '0')                                                                                                                                                                                                                                                                                                                                                                                                                          |
| '2'  | If ( sa ≤ &#124; sb &#124; + sc + &#124; se &#124;) when ( sa ≠ '0') and ( se < '0') If ( sa ≤ &#124; sb &#124; + sc ) when ( sa ≠ '0') and ('0' ≤ se ) If ( sc < sd ) If ( sd < se ) when ('0' ≤ se )                                                                                                                                                                                                                                                                          |
| '3'  | If ( sa ≤ &#124; sc &#124;) when ( sa ≠ '0') and ( sb < '0') and ( sc < '0') If ( sa ≤ sb + &#124; sc &#124;) when ( sa ≠ '0') and ('0' ≤ sb ) and ( sc < '0') If ( sa ≤ sb ) when ( sa ≠ '0') and ('0' ≤ sb ) and ('0' ≤ sc ) If ( sb < '0') and ('0' ≤ sc ) If (&#124; sc &#124; ≤ &#124; sb &#124; + 20) when ( sb < '0') and ( sc < '0') If (&#124; sb &#124; + &#124; sc &#124; ≤ 20) when ('0' ≤ sb ) and ( sc < '0') If ( sb < sc + 20) when ('0' ≤ sb ) and ('0' ≤ sc ) |

When using die cut labels (when layout reference ( sm = "1," "2") is specified), note the caution below when setting the paper layout.

- Set the cutting position ( sc ) between labels and as far from the top and bottom edges of the labels as possible.
- Sets a value in excess of 2.0 mm for the distance from the cutting position to the next print starting position. If it is set to less than 2.0 mm, the paper feed operation may not be executed normally.
