<!-- image -->

Rev. 2.31

## ESC GS c h v

[Name]

Set reduced printing

[Code]

ASCII

ESC GS c h v

Hex

1B 1D 63 h v

Decimal

27 29 99 h v

[Defined Area]  0

≦ h ≦ 255

0 ≦ v ≦ 255

[Initial Value]

h = 0 (Always 0)

v = 0 (When not set) or previously set value

[Function]

Sets reduced printing.

If unprinted data exists, the unprinted data is printed out and then the command is executed.

|   h | Set horizontal direction of reduced printing   | Remarks   |
|-----|------------------------------------------------|-----------|
|   0 | Always 0                                       |           |

|   v | Set vertical direction of reduced printing   | Remarks                                  |
|-----|----------------------------------------------|------------------------------------------|
|   0 | Invalid (100%)                               | Setting is stored to non-volatile memory |
|   1 | Valid (50%)                                  | Setting is stored to non-volatile memory |
|   2 | Valid (75%)                                  | Setting is stored to non-volatile memory |

- ・ If the correct setting value is specified, it is stored to non-volatile memory.
- ・ The print quality is not guaranteed for reduced printing (barcodes and 2D barcodes may not be read correctly at times).

--------------------------------------------------------------------------------------
