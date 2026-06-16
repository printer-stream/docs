## C O N F I D E N T I A L

## GS ( L pL pH m fn a bx by c xL xH yL yH d1... dk &lt;Function 112&gt;

## GS 8 L p1 p2 p3 p4 m fn a bx by c xL xH yL yH d1... dk

```
[Name] Store the graphics data in the print buffer (raster format). [Format] ASCII GS ( L pL pH m fn a bx by c xL xH yL yH d1...dk Hex 1D 28 4C pL pH 30 70 30 bx by c xL xH yL yH d1...dk Decimal 29 40 76 pL pH 48 112 48 bx by c xL xH yL yH d1...dk ASCII GS 8 L p1 p2 p3 p4 m fn a bx by c xL xH yL yH d1...dk Hex 1D 38 4C p1 p2 p3 p4 30 70 30 bx by c xL xH yL yH d1...dk Decimal 29 56 76 p1 p2 p3 p4 48 112 48 bx by c xL xH yL yH d1...dk [Range] 11 ≤ ( pL + pH × 256) ≤ 65535 (0 ≤ pL ≤ 255, 0 ≤ pH ≤ 255) [When using GS 8 L : 11 ≤ ( p1 + p2 × 256 + p3 × 65536 + p4 × 16777216) ≤ 4294967295] m = 48, fn = 112, a = 48, a = 52 (TM-T88V only) 0 ≤ d ≤ 255 k = (int(( xL + xH × 256) + 7)/8) × ( yL + yH × 256) TM-J2000/J2100 : bx = 1, 2 by = 1, 2 49 ≤ c ≤ 51 ( TM-J2100 [two-color printing model] ) c = 49 ( TM-J2000 [single-printing model] ) 1 ≤ ( xL + xH × 256) ≤ 2048 (0 ≤ xL ≤ 255, 0 ≤ xH ≤ 8) 1 ≤ ( yL + yH × 256) ≤ 128 (0 ≤ yL ≤ 128, yH = 0) TM-T90: bx = 1, 2 by = 1, 2 c = 49 (when the recommended monochrome paper is used) c = 49, 50 (when the recommended two-color paper is used) 1 ≤ ( xL + xH × 256) ≤ 1024 (0 ≤ xL ≤ 255, 0 ≤ xH ≤ 4) [Other than Japanese Model] With recommended two-color paper ( by = 1): 1 ≤ ( yL + yH × 256) ≤ 831 (0 ≤ yL ≤ 255, 0 ≤ yH ≤ 3) ( by = 2): 1 ≤ ( yL + yH × 256) ≤ 415 (0 ≤ yL ≤ 255, yH = 0, 1) With recommended monochrome paper
```
