<!-- image -->

Rev. 2.31

## ESC RS S n

[Name]

Select print startup setting

[Code]

ASCII

ESC RS S n

Hex

1B 1E 53 n

Decimal

27 30 83 n

## [Defined Area]  0 ≦ n ≦ 1

48 ≦ n ≦ 49

## [Initial Value] [Function]

Memory Switch Settings

Selects the print startup setting.

If the settings will not change when processing this command, the command is not executed.

If unprinted data exists when processing this command, the data is printed out and then the command is executed.

If printing when processing this command, the command waits for printing to stop and changes the print startup setting.

This command setting is initialized by a printer reset.

## Parameter details

| n     | print startup setting   |
|-------|-------------------------|
| 0, 48 | Page                    |
| 1, 49 | Line                    |

--------------------------------------------------------------------------------------
