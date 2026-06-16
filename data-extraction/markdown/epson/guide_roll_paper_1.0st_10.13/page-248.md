## C O N F I D E N T I A L

## GS ( L pL pH m fn a kc1 kc2 b xL xH yL yH [c d1...dk]1...[c d1...dk]b &lt;Function 67 &gt;

## GS 8 L p1 p2 p3 p4 m fn a kc1 kc2 b xL xH yL yH [c d1...dk]1...[c d1...dk]b

```
[Name] Define the NV graphics data (raster format). [Format] ASCII GS ( L pL pH m fn a kc1 kc2 b xL xH yL yH [c d1...dk]1...[c d1...dk]b Hex 1D 28 4C pL pH 30 43 30 kc1 kc2 b xL xH yL yH [c d1...dk]1...[c d1...dk]b Decimal 29 40 76 pL pH 48 67 48 kc1 kc2 b xL xH yL yH [c d1...dk]1...[c d1...dk]b ASCII GS 8 L p1 p2 p3 p4 m fn a kc1 kc2 b xL xH yL yH [c d1...dk]1...[cd1...dk]b Hex 1D 38 4C p1 p2 p3 p4 30 43 30 kc1 kc2 b xL xH yL yH [c d1...dk]1...[cd1...dk]b Decimal 29 56 76 p1 p2 p3 p4 48 67 48 kc1 kc2 b xL xH yL yH [c d1...dk]1...[cd1...dk]b [Range] 12 ≤ ( pL + pH × 256) ≤ 65535 (0 ≤ pL ≤ 255, 0 ≤ pH ≤ 255) [When using GS 8 L : 12 ≤ ( p1 + p2 × 256 + p3 × 65536 + p4 × 16777216) ≤ 4294967295] m = 48, fn = 67, a = 48, a = 52 (TM-T88V only) 32 ≤ kc1 ≤ 126 32 ≤ kc2 ≤ 126 0 ≤ d ≤ 255 k = (int(( xL + xH × 256) + 7)/8) × ( yL + yH × 256) TM-J2000 [single-color printing model] : b = 1 1 ≤ ( xL + xH × 256) ≤ 8192 (0 ≤ xL ≤ 255, 0 ≤ xH ≤ 32) 1 ≤ ( yL + yH × 256) ≤ 2304 (0 ≤ yL ≤ 255, 0 ≤ yH ≤ 9) c = 49 TM-J2100 [two-color printing model]: b = 1, 2 (when c = 49, 50) b = 1 (when c = 51) 1 ≤ ( xL + xH × 256) ≤ 8192 (0 ≤ xL ≤ 255, 0 ≤ xH ≤ 32) 1 ≤ ( yL + yH × 256) ≤ 2304 (0 ≤ yL ≤ 255, 0 ≤ yH ≤ 9) 49 ≤ c ≤ 51 TM-T90 , TM-L90 : b = 1 (when the recommended monochrome paper is used) b = 1, 2 (when the recommended two-color paper is used)
```
