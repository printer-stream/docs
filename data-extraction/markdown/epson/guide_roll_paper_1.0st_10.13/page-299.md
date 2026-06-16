## C O N F I D E N T I A L

## GS D m fn a kc1 kc2 b c d1...dk &lt;Function 67&gt;

[Name] Define Windows BMP NV graphics data. [Format] ASCII GS D m fn a kc1 kc2 b c d1...dk Hex 1D 44 m fn a kc1 kc2 b c d1...dk Decimal 29 68 m fn a kc1 kc2 b c d1...dk [Range] m = 48, fn = 67, a = 48 32 ≤ kc1 ≤ 126 (20h ≤ kc1 ≤ 7Eh) 32 ≤ kc2 ≤ 126 (20h ≤ kc2 ≤ 7Eh) c = 49 0 ≤ d ≤ 255 TM-T20 : b = 48

## TM-T88V: b = 48, 52

The value of k depends on the BMP file size.

Converts Windows BMP data to the specified tone and defines NV graphics data (raster format) that corresponds to the key codes ( kc1, kc2 ).

- b specifies the tone of data to define.
- c specifies the color of data to define.
- d specifies the defined data (raster format).
- ■ The number of items of NV graphics registered should be within 50 to shorten the execution time of this function. The execution time is 60 seconds or less when the number of items registered is within 50. The execution time for 100 items is 120 seconds or less.

|   b | Tone of data to define   |
|-----|--------------------------|
|  48 | Monochrome (digital)     |
|  52 | Multi-tone               |

|   c | Color of data to define   |
|-----|---------------------------|
|  49 | Color 1                   |

## [Description]

## [Notes]

EXECUTING + SETTING
