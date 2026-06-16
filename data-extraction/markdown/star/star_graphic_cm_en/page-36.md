<!-- image -->

Rev. 2.31

## ESC * r e n NUL

[Name]

Set raster EM mode

[Code]

ASCII

ESC * r e n NUL

Hex

1B 2A 72 65 n 00

Decimal

27 42 114 101 n 0

[Defined Area]  n = 0, 1, 2, 3, 8, 9, 12, 13, 32, 33, 36, 37

[Initial Value]

[Function]

Cutter model n = 13

TearBar model n = 3

Sets the raster EM mode.

The EM mode, is an operation to be performed by the raster document end command (ESC FF EM). nI is a decimal notation using ASCII characters (up to 255 digits)

## &lt;EM mode setting format&gt;

|   n | Model   | Model   | Function       | Function       | Function       |
|-----|---------|---------|----------------|----------------|----------------|
|     | Cutter  | TearBar | FormFeed       | Cut Feed       | Cutter         |
|   0 | Valid   | Valid   | Set To Default | Set To Default | Set To Default |
|   1 | Valid   | Valid   | x              | x              | x              |
|   2 | Valid   | Valid   | x              | Cut Feed       | x              |
|   3 | Valid   | Valid   | x              | Tear Bar Feed  | x              |
|   8 | Valid   | Valid   | x              | x              | Full Cut       |
|   9 | Valid   | Valid   | x              | Cut Feed       | Full Cut       |
|  12 | Valid   | Valid   | x              | x              | Partial Cut    |
|  13 | Valid   | Valid   | x              | Cut Feed       | Partial Cut    |
|  32 | Invalid | Invalid |                |                |                |
|  33 | Invalid | Invalid |                |                |                |
|  36 | Invalid | Invalid |                |                |                |
|  37 | Invalid | Invalid |                |                |                |

Cutter only mode: TearBar Feed -&gt; Cut Feed

TearBar only model: Cut Feed -&gt; TearBar Feed

Full cut only model: Partial Cut -&gt; Full Cut

Partial Cut only model: Full Cut -&gt; Partial Cut

--------------------------------------------------------------------------------------
