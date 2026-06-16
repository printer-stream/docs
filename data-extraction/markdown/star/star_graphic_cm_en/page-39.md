<!-- image -->

Rev. 2.31

## 3-4) Print Mode Command Details

The following command is a command to control the printing mode.

--- Specification (1) power saving mode not compatible models ---

## ESC RS C n

[Name]

Select/Cancel two-color print mode

[Code]

ASCII

ESC RS C n

Hex

1B 1E 43 n

Decimal

27 30 67 n

[Defined Area]  0

≦ n ≦ 1, 48 ≦ n ≦ 49 ('0' ≦ n ≦ '1')

[Initial Value]

n = 0, 48

[Function]

Selects/Cancels two-color print mode

This setting value is initialized with a soft reset.

| n     | Selects/Cancels two-color print mode                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0, 48 | Release two-color printing mode (setting of monochromatic print mode) When in two-color printing mode, delete the two-color mode with this command. If you already have deleted two-color printing mode, this command is ignored. When the two-color printing mode is released with this command, the following process is executed ・ If there is a non-printed data, print the non-printed data in a two-color mode. ・ Initialize the print color (two-color printing mode set to black) ・ Set the print density setting in the monochromatic print mode ・ Set the print speed setting in the monochromatic print mode |
| 1, 49 | Select two-color print mode When in monochromatic printing mode, select two-color printing mode with this command If the two-color printing mode is already selected, the command is ignored When the two-color printing mode is selected by this command, the following process is executed ・ If there is unprinted data, and prints the unprinted data in the monochrome mode ・ Initialize the print color (two-color printing mode is set to black) ・ And set the print density setting in the two-color printing mode                                                                                               |

--------------------------------------------------------------------------------------
