<!-- image -->

Rev. 2.31

- --- Specification (3) tone print mode compatible models compatible ---

## ESC RS C n

[Name]

Select print mode

[Code]

ASCII

ESC RS C n

Hex

1B 1E 43 n

Decimal

[Defined Area]  0

27 30 67 n

≦ n ≦ 1, 48 ≦ n ≦ 49 ('0' ≦ n ≦ '1'), 8 ≦ n ≦ 8

[Initial Value]

n = 0, 48

[Function]

Selects the print mode.

| n     | Select print mode                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0, 48 | Selection of monochromatic print mode When in two-color printing mode/gradation printing mode, select monochromatic printing mode with this command If the monochromatic printing mode is already selected, the command is ignored When the monochromatic printing mode is selected with this command, the following process is executed ・ If there is non-printed data, print the non-printed data with the current print mode (two-color printing mode/gradation print mode) ・ Initialize the print color (two-color printing mode is set to black) ・ Set the print density setting in the monochromatic print mode ・ Set the print speed setting in the monochromatic print mode |
| 1, 49 | Selection of two-color printing mode When in monochromatic printing mode/monochromatic print mode, select two-color printing mode with this command If the two-color printing mode is already selected, this command is ignored When the two-color printing mode is selected by this command, the following process is executed ・ If there is non-printed data, print the non-printed data with the current print mode (monochromatic print mode/gradation print mode) ・ Initialize the print color (two-color printing mode is set to black) ・ And set the print density setting in the two-color printing mode (Printing speed fixed in the two-color printing mode)              |
| 8, 56 | Selection of tone print mode When in monochromatic printing mode/two-color print mode, select gradation printing mode with this command If the gradation printing mode is already selected, this command is ignored When the gradation printing mode is selected with this command, the following process is executed ・ If there is non-printed data, print the non-printed data with the current print mode (monochromatic print mode/two-color print mode) ・ Initialize the printing gradation (set to the tone mode gradation 1) ・ Set the print density setting in the monochromatic print mode (Printing speed fixed in the gradation printing mode)                           |

--------------------------------------------------------------------------------------
