<!-- image -->

## ESC RS r n

[Name] [Code]

Set print speed

ASCII

ESC RS r n

Hex.

1B 1E 72 n

Decimal

27 30 114 n

[Defined Area]

[Initial Value] [Function]

## Spec. A

| n     | Print Speed                                        | Print Speed                                                                                                    |
|-------|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
|       | Single Color Printing Mode                         | Two Color Printing Mode Low Peak Current Mode Double Resolution (*) Installed print mode depends on the model. |
| 0, 48 | High speed                                         | Each print mode speed                                                                                          |
| 1, 49 | Mid-speed                                          | Each print mode speed                                                                                          |
| 2, 50 | Slow speed                                         | Each print mode speed                                                                                          |
| 3, 51 | Option-speed (*) Print speed depends on the model. | Each print mode speed                                                                                          |

## Spec. B

| n     | Print Speed                | Print Speed                                                                                                    |
|-------|----------------------------|----------------------------------------------------------------------------------------------------------------|
|       | Single Color Printing Mode | Two Color Printing Mode Low Peak Current Mode Double Resolution (*) Installed print mode depends on the model. |
| 0, 48 | Standard                   | Each print mode speed                                                                                          |
| 1, 49 | Mid-speed                  | Each print mode speed                                                                                          |
| 2, 50 | Slow speed                 | Each print mode speed                                                                                          |
| 3, 51 | High speed                 | Each print mode speed                                                                                          |

-----------------------------------------------------------------------------

0 ≤ n ≤ 3

48 ≤ n ≤ 51 ('0' ≤ n ≤ '3')

Memory switch setting

Sets print speed.

This command stops printing to be executed.

Because two-color print mode, low peak current mode, and double resolution mode print in one speed, the speed settings with this command are invalid.

This  command setting  becomes  valid  when  returned  from  the  two-color  print  mode,  low  peak current mode, and double resolution mode to the single color print mode.

Invalid in page mode.
