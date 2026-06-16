<!-- image -->

Rev. 2.31

## ESC RS d n

[Name]

Set print density

[Code]

ASCII

ESC RS d n

Hex

1B 1E 64 n

Decimal

27 30  100 n

[Defined Area]  0 ≦ n ≦ 6

48 ≦ n ≦ 57 ('0' ≦ n ≦ '6')

## [Initial Value] [Function]

Memory SW setting

Sets print density.

If unprinted data exists when processing this command, the data is printed out and then the command is executed.

This command is executed after the print operation is stopped.

When in two-color printing mode, only print density for red printing can be set by this command.

| n     | Print Density              | Print Density                                                    | Print Density            | Print Density            |
|-------|----------------------------|------------------------------------------------------------------|--------------------------|--------------------------|
| n     | Single Color Printing Mode | Two-Color Printing Mode Red Print Density Double Resolution Mode | Energy saving mode 1     | Energy saving mode 2     |
| 0, 48 | Print density +3           | Red print density +                                              | Print density +3         | Print density +3         |
| 1, 49 | Print density +2           | Red print density +                                              | Print density +2         | Print density +2         |
| 2, 50 | Print density +1           | Red print density (Standard)                                     | Print density +1         | Print density +1         |
| 3, 51 | Print density (Standard)   | Red print density (Standard)                                     | Print density (Standard) | Print density (Standard) |
| 4, 52 | Print density -1           | Red print density (Standard)                                     | Print density -1         | Print density -1         |
| 5, 53 | Print density -2           | Red print density -                                              | Print density -2         | Print density -2         |
| 6, 54 | Print density -3           | Red print density -                                              | Print density -3         | Print density -3         |

## ESC RS r n

[Name]

Set print speed

[Code]

ASCII

ESC RS r n

Hex

1B 1E 72 n

Decimal

27 30 114 n

[Defined Area]  0 ≦ n ≦ 2

48 ≦ n ≦ 50 ('0' ≦ n ≦ '2')

## [Initial Value] [Function]

Memory SW setting

Sets print speed.

If unprinted data exists when processing this command, the data is printed out and then the command is executed.

This command is executed after the print operation is stopped.

Since the printing  speed  in two-color  printing mode  and  energy  saving mode  1  are  fixed,  the  speed settings  with  this  command  are  invalid.  However,  the  settings  of  this  command  become  valid  when returning from two-color printing mode or energy saving mode 1 to single color printing mode.

| n     | Print Speed                | Print Speed             | Print Speed          | Print Speed          |
|-------|----------------------------|-------------------------|----------------------|----------------------|
|       | Single Color Printing Mode | Two-color Printing Mode | Energy saving mode 1 | Energy saving mode 2 |
| 0, 48 | High speed                 | Invalid                 | Invalid              | Invalid              |
| 1, 49 | Mid-speed                  | Invalid                 | Invalid              | Invalid              |
| 2, 50 | Slow speed                 | Invalid                 | Invalid              | Invalid              |

--------------------------------------------------------------------------------------
