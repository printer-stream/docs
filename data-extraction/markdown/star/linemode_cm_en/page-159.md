<!-- image -->

## ESC GS P 6

[Name] Print data in page mode

[Code] ASCII

ESC  GS P 6

Hexadecimal

1B  1D 50 36

Decimal

27 29 80 54

## [Function]

Lump-prints data expanded to the entire print region in page mode.

- Valid only when page mode is selected.
- After printing, the following information is maintained.
- a. Expanded data
- b. Selection of character print direction in page mode (ESC GS P 2)
- c. Setting of print region in page mode (ESC GS P 3)
- d. Character expansion position

## ESC GS P 7

[Name] Print in page mode and recover

[Code]

ASCII

ESC GS P 7

Hexadecima 1B 1D 50 37

l

Decimal

27 29 80 55

## [Function]

Lump-prints data expanded to the entire print region and recovers to standard mode.

- All expanded data is erased after printing.
- Print region set by ESC GS P 3 (Set print region in page mode) is initialized.
- No paper cut is executed.
- After execution, the top of the line is positioned at the next print starting position.
- Valid only when page mode is selected.

## ESC GS P 8

[Name] Cancel print data in page mode

[Code]

ASCII

ESC GS P 8

Hexadecimal

1B 1D 50 38

Decimal

27 29 80 56

## [Function]

Erases all data in presently set print region, in page mode.

- Valid only when page mode is selected.
- Portion included in the currently set print region is deleted even if data of the print region set previously.

-----------------------------------------------------------------------------
