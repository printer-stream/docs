## Format

| ASCII   | ESC   |   & |   NUL | n   | m   | [a 0   | a 1   | a 2   | d 1   | d 2   | . . .   | d k ]   |
|---------|-------|-----|-------|-----|-----|--------|-------|-------|-------|-------|---------|---------|
| Hex     | 1B    |  26 |    00 | n   | m   | [a 0   | a 1   | a 2   | d 1   | d 2   | . . .   | d k ]   |
| Decimal | 27    |  38 |     0 | n   | m   | [a 0   | a 1   | a 2   | d 1   | d 2   | . . .   | d k ]   |

## Parameter range

0 ≤ n ≤ 127 0 ≤ m ≤ 127 n ≤ m

## LQ mode

Draft mode

0 ≤ a1 ≤ 37 0 ≤ a1 ≤ 15 0 ≤ a0 + a1 + a2 ≤ 42 0 ≤ a0 +a1 + a2 ≤ 18

## Super/subscript characters

Normal characters k = 3 × a1 k = 2 × a1

## Function

Sets the parameters for user-defined characters and then sends the data for those characters, as described below:

| n         | Character code of the first character to be user-defined       |
|-----------|----------------------------------------------------------------|
| m         | Character code of the last character to be user-defined        |
| a 0       | Space to the left of each proportional user-defined character  |
| a 1       | Actual width of user-defined characters                        |
| a 2       | Space to the right of each proportional user-defined character |
| d 1 . . . | Character data                                                 |

## Notes

- The data within brackets in the Format section above is repeated for each character you define.
- Defining characters when the following attributes are set results in the user-defined characters having those attributes: superscript, subscript, proportional spacing, draft mode, and LQ mode.
- Always cancel italic characters with the ESC 5 command before defining characters. After defining user-defined characters, you can italicize them by sending the ESC 4 command.
- User-defined characters with differing attributes cannot exist at the same time. For example, if normal-size user-defined characters have already been defined, and you use this command to define subscript characters, the previous normal-size characters are lost.
- Do not define continuous horizontal dots on the same row; the printer ignores the second of two continuous dots.
