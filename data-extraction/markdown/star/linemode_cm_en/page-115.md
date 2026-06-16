<!-- image -->

## ESC RS r n

[Name] [Code]

Set printing speed

ASCII

ESC RS r n

Hex.

1B 1E 72 n

Decimal

27 30 114 n

[Defined Area]

[Initial Value] [Function]

0 ≤ n ≤ 3

48 ≤ n ≤ 51 ('0' ≤ n ≤ '3')

Memory switch setting

Sets print speed.

This command stops printing to be executed.

Because two-color print mode prints in one speed, the speed settings  with this command are invalid.  This command setting becomes valid when returned from the two-color print mode to the single color print mode.

| N     | Print Speed                                   | Print Speed                   |
|-------|-----------------------------------------------|-------------------------------|
|       | Single Color Printing Mode                    | Two Color Printing Mode       |
| 0, 48 | High speed                                    | Two Color Printing Mode Speed |
| 1, 49 | Mid-speed                                     | Two Color Printing Mode Speed |
| 2, 50 | Slow speed                                    | Two Color Printing Mode Speed |
| 3, 51 | Option speed (differs according to the model) | Two Color Printing Mode Speed |

-----------------------------------------------------------------------------
