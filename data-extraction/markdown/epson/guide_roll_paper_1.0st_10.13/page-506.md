## C O N F I D E N T I A L

## &lt;Function 48&gt; GS ( Q pL pH fn x1L x1H y1L y1H x2L x2H y2L y2H c m1 m2

```
[Name] Draw line [Format] ASCII GS ( Q pL pH fn x1L x1H y1L y1H x2L x2H y2L y2H c m1 m2 Hex 1D 28 51 0C 00 30 x1L x1H y1L y1H x2L x2H y2L y2H c m1 m2 Decimal 29 40 81 12 0 48 x1L x1H y1L y1H x2L x2H y2L y2H c m1 m2 [Range] ( pL + pH × 256) = 12 ( pL = 12, pH = 0) fn = 48 TM-P60 : When the start position specified with ESC T is 'top left or bottom right': 0 ≤ ( x1L + x1H × 256) ≤ 431 (0 ≤ x1L ≤ 255, x1H = 0,1) 0 ≤ ( y1L + y1H × 256) ≤ 1199 (0 ≤ y1L ≤ 255, 0 ≤ y1H ≤ 4) 0 ≤ ( x2L + x2H × 256) ≤ 431 (0 ≤ x2L ≤ 255, x2H = 0, 1) 0 ≤ ( y2L + y2H × 256) ≤ 1199 (0 ≤ y2L ≤ 255, 0 ≤ y2H ≤ 4) When the start position specified with ESC T is 'bottom left or top right': 0 ≤ ( x1L + x1H × 256) ≤ 1199 (0 ≤ x1L ≤ 255, 0 ≤ x1H ≤ 4) 0 ≤ ( y1L + y1H × 256) ≤ 431 (0 ≤ y1L ≤ 255, y1H = 0,1) 0 ≤ ( x2L + x2H × 256) ≤ 1199 (0 ≤ x2L ≤ 255, 0 ≤ x2H ≤ 4) 0 ≤ ( y2L + y2H × 256) ≤ 431 (0 ≤ y2L ≤ 255, y2H = 0, 1) c = 1 1 ≤ m1 ≤ 3 m2 = 48
```

[Description]

Saves line data in the print buffer when page mode is selected.

- ■ x1L , x1H , y1L , y1H set the line drawing start coordinate [X start position, Y start position] as the start position reference.
- X start position:  [( x1L + x1H × 256) × horizontal and vertical motion units]
- Y start position:  [( y1L + y1H × 256) × horizontal and vertical motion units]
