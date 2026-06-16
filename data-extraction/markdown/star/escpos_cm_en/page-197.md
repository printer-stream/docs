<!-- image -->

## ESC	GS	SUB	DC1	m	t1	t2

N ame

Specify snout operation mode

Code

ASCII

ESC GS SUB DC1 m t1 t2

Hex.

1B   1D  1A   11   m  t1  t2

Decimal

27   29  26   17   m  t1  t2

Defined Region

0 ≤ m ≤ 3 (48 ≤ m ≤ 51) t1 = 0, t2 =0 MSW Setting

Initial Value

## Function

Specify the snout operation mode using the m parameter.

| m     | Snout Operating Mode                                                               |
|-------|------------------------------------------------------------------------------------|
| 0, 48 | Snout LED output OFF                                                               |
| 1, 49 | Snout LED output ON (while printing, or during presenter opera - tion)             |
| 2, 50 | Snout LED output ON (during an error)                                              |
| 3, 51 | Snout LED output ON (while printing, or during presenter opera - tion or an error) |

When the snout is not connected, this command is prohibited from use.

Reference

ESC GS SUB DC2, ESC GS SUB DC3
