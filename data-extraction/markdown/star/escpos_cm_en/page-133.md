<!-- image -->

## GS E n

Name

Set printing speed

Code

ASCII GS E n

Hex.

1D 45 n

Decimal 29 69 n

Defined Region

0 ≤ n ≤ 255

Initial Value

n = 0

Function

Sets print speed.

|   Bit | Function    | '0'               | '1'   |
|-------|-------------|-------------------|-------|
|     7 | Undefined   | --                | --    |
|     6 | Undefined   | --                | --    |
|     5 | Print Speed | (See table below) |       |
|     4 | Print Speed | (See table below) |       |
|     3 | Undefined   | --                | --    |
|     2 | Undefined   | --                | --    |
|     1 | Undefined   | --                | --    |
|     0 | Undefined   | --                | --    |

## Spec. A Print Speed

|   Bit-5 |   Bit-4 | Print Speed   |
|---------|---------|---------------|
|       0 |       0 | High speed    |
|       0 |       1 | Mid-speed     |
|       1 |       0 | Slow speed    |
|       1 |       1 | Undefined     |

## Spec. B

## Print Speed

|   Bit-5 |   Bit-4 | Print Speed   |
|---------|---------|---------------|
|       0 |       0 | High speed    |
|       0 |       1 | Undefined     |
|       1 |       0 | Slow speed    |
|       1 |       1 | Undefined     |

- This command is effective in standard mode.
- This command is enabled only when at the top of the line.
- The speed setting is disabled during reduced printing in the vertical direction. However, this command setting is enabled when reduced printing in the vertical direction is released.
- This command changes the print speed after the test print is stopped.

## Details

## STAR
