<!-- image -->

Rev. 2.31

## 3-1-2) Print Settings

## ESC RS A n

[Name]

Set print area

[Code]

ASCII

ESC RS A n

Hex

1B 1E 41 n

Decimal 27 30 65

n

## [Defined Area]  0 ≦ n ≦ 1

[Initial Value]

Memory SW setting

[Function]

Sets the print area according to n.

Set n to be the same as the print area setting of MSW. (See MSW setting of each model for details) If unprinted data exists when processing this command, the data is printed out and then the command is executed.

(Cutting and feeding operations are not performed.)

This command is executed after the print operation is stopped.

The raster left and right margin settings are initialized.

This setting value is initialized with a soft reset.

--------------------------------------------------------------------------------------
