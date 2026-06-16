## C O N F I D E N T I A L

## GS ( L pL pH m fn a kc1 kc2 b xL xH yL yH [c d1... dk ]1...[c d1... dk ]b &lt;Function 84&gt;

## GS 8 L p1 p2 p3 p4 m fn a kc1 kc2 b xL xH yL yH [c d1... dk ]1...[c d1... dk ]b

```
[Name] Define the downloaded graphics data (column format). [Format] ASCII GS ( L pL pH m fn a kc1 kc2 b xL xH yL yH [c d1...dk]1...[c d1...dk]b Hex 1D 28 4C pL pH 30 54 30 kc1 kc2 b xL xH yL yH [c d1...dk]1...[c d1...dk]b Decimal 29 40 76 pL pH 48 84 48 kc1 kc2 b xL xH yL yH [c d1...dk]1...[c d1...dk]b ASCII GS 8 L p1 p2 p3 p4 m fn a kc1 kc2 b xL xH yL yH [c d1...dk]1...[cd1...dk]b Hex 1D 38 4C p1 p2 p3 p4 30 54 30 kc1 kc2 b xL xH yL yH [c d1...dk]1...[cd1...dk]b Decimal 29 56 76 p1 p2 p3 p4 48 84 48 kc1 kc2 b xL xH yL yH [c d1...dk]1...[cd1...dk]b [Range] 12 ≤ ( pL + pH × 256) ≤ 65535 (0 ≤ pL ≤ 255, 0 ≤ pH ≤ 255) [When using GS 8 L :12 ≤ ( p1 + p2 × 256 + p3 × 65536 + p4 × 16777216) ≤ 4294967295] m = 48, fn = 84, a = 48 32 ≤ kc1 ≤ 126 32 ≤ kc2 ≤ 126 0 ≤ d ≤ 255 k = ( xL + xH × 256) × (int(( yL + yH × 256) + 7)/8) TM-J2000 [single-color printing model] : b = 1 1 ≤ ( xL + xH × 256) ≤ 8192 (0 ≤ xL ≤ 255, 0 ≤ xH ≤ 32) 1 ≤ ( yL + yH × 256) ≤ 2304 (0 ≤ yL ≤ 255, 0 ≤ yH ≤ 9) c = 49 TM-J2100 [two-color printing model]: b = 1, 2 (when c = 49, 50) b = 1 (when c = 51) 1 ≤ ( xL + xH × 256) ≤ 8192 (0 ≤ xL ≤ 255, 0 ≤ xH ≤ 32) 1 ≤ ( yL + yH × 256) ≤ 2304 (0 ≤ yL ≤ 255, 0 ≤ yH ≤ 9) 49 ≤ c ≤ 51
```

[Description]

Defines the downloaded graphics data (column format) as a record specified by the key codes ( kc1 and kc2 ) in the downloaded graphics area.
