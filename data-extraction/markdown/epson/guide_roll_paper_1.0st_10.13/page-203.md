## C O N F I D E N T I A L

## ESC ✻

```
[Name] Select bit-image mode [Format] ASCII ESC ✻ m nL nH d1 ... dk Hex 1B 2A m nL nH d1 ... dk Decimal 27 42 m    nL    nH    d1 ... dk [Range] TM-J2000/J2100 , TM-T90 , TM-L90 : m = 0, 1, 32, 33 1 ≤ ( nL + nH × 256) ≤ 1023 (0 ≤ nL ≤ 255) 0 ≤ d ≤ 255 k = nL + nH × 256 [in case of m = 0, 1] k = ( nL + nH × 256) × 3 [in case of m = 32, 33] TM-T20 , TM-T88IV , TM-T88V , TM-T70 : m = 0, 1, 32, 33 1 ≤ ( nL + nH × 256) ≤ 2047 (0 ≤ nL ≤ 255, 0 ≤ nH ≤ 7) 0 ≤ d ≤ 255 k = nL + nH × 256 [in case of m = 0, 1] k = ( nL + nH × 256) × 3 [in case of m = 32, 33] TM-U230 , TM-U220 : m = 0, 1 1 ≤ ( nL + nH × 256) ≤ 2047 (0 ≤ nL ≤ 255, 0 ≤ nH ≤ 3) 0 ≤ d ≤ 255 k = nL + nH × 256 [Default] None [Printers not featuring this command] TM-P60
```

EXECUTING COMMAND
