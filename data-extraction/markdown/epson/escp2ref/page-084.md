## Format

```
ASCII ESC t n Hex 1B 74 n Decimal 27 116 n
```

## Parameter range

```
0 ≤ n ≤ 3, 48 ≤ n ≤ 51
```

## Function

Selects the character table to be used for printing from among the four character tables described below:

```
n = 0 or 48 Character table 0 1 or 49 Character table 1 2 or 50 Character table 2 3 or 51 Character table 3
```

## Default

```
table 0 Italic table 1 PC437 table 2 User-defined characters table 3 PC437
```

## Notes

- Use the ESC ( t command to assign any registered character table to any character table.
- To copy user-defined characters (that have been created with the ESC &amp; or ESC : commands) to the upper half of the character table, send the ESC % 0 command, followed by the ESC t 2 command. However, you cannot copy user-defined characters using ESC t 2 if you have previously assigned another character table to table 2 using the ESC ( t command.

## Printers not featuring this command

None
