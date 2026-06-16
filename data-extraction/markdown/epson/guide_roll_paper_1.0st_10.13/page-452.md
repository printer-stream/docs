## C O N F I D E N T I A L

## ESC ( A pL pH fn a b n c t1 t2 &lt; Function 98 &gt; (TM-U230)

[Name] Set integrated beeper when offline factors occur in TM-U230 models [Format] ASCII ESC ( A pL pH fn a b n c t1 t2 Hex 1B 28 41 07 00 62 a 01 64 c t1 t2 Decimal 27 40 65 7 0 98 a 1 100 c t1 t2 [Range] ( pL + pH × 256) = 7 ( pL = 7, pH = 0) fn = 98 48 ≤ a ≤ 51 b = 1 n = 100 c = 0, 255 1 ≤ t1 ≤ 50, t1 = 255 1 ≤ t2 ≤ 50

[Default]

No paper printing stops ( a = 49): Beeps the integrated beeper (select sound variation by DIP switch [SW2-5]). Except above ( a = 48, 50, 51): Does not beep the integrated beeper.

[Description]

Set the integrated beeper control when specified offline is occurred.

- a specifies the offline factor.

|   a | Offline factor                        |
|-----|---------------------------------------|
|  48 | Cover open.                           |
|  49 | Printing stop when there is no paper. |
|  50 | Recoverable error occur.              |
|  51 | Unrecoverable error occur.            |
