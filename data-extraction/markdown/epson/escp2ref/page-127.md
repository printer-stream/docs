## Format

```
ASCII ESC ! n Hex 1B 21 n Decimal 27 33 n
```

## Parameter range

0 ≤ n ≤ 255

## Function

Selects any combination of several font attributes and enhancements by setting or clearing the appropriate bit in the n parameter, as shown below:

|   Bit | On/Off   |   Hex |   Dec | Function              | Equivalent   |
|-------|----------|-------|-------|-----------------------|--------------|
|     0 | Off      |    00 |     0 | Selects 10 cpi        | ESC P        |
|     0 | On       |    01 |     1 | Selects 12 cpi        | ESC M        |
|     1 | Off      |    00 |     0 | Cancels proportional  | ESC p 0      |
|     1 | On       |    02 |     2 | Selects proportional  | ESC p 1      |
|     2 | Off      |    00 |     0 | Cancels condensed     | DC2          |
|     2 | On       |    04 |     4 | Selects condensed     | ESC SI, SI   |
|     3 | Off      |    00 |     0 | Cancels bold          | ESC F        |
|     3 | On       |    08 |     8 | Selects bold          | ESC E        |
|     4 | Off      |    00 |     0 | Cancels double-strike | ESC H        |
|     4 | On       |    10 |    16 | Selects double-strike | ESC G        |
|     5 | Off      |    00 |     0 | Cancels double-width  | ESC W 0      |
|     5 | On       |    20 |    32 | Selects double-width  | ESC W 1      |
|     6 | Off      |    00 |     0 | Cancels italics       | ESC 5        |
|     6 | On       |    40 |    64 | Selects italics       | ESC 4        |
|     7 | Off      |    00 |     0 | Cancels underline     | ESC - 0      |
|     7 | On       |    80 |   128 | Selects underline     | ESC - 1      |

Add the numbers of the features to be selected and send the total as the parameter n.

## Notes

- This command cancels any attributes or enhancements that are not selected.
- All attributes or enhancements may not be available on some models. For details, see the command explanation for the equivalent command listed in the above table.

## Printers not featuring this command

None

## Model-dependent variations

None

## Related topics

Select a font
