## Format

```
ASCII ESC C NUL n Hex 1B 43 00 n Decimal 27 67 0 n
```

## Parameter range

1 ≤ n ≤ 22

## Function

Sets the page length to n inches

## Default

Depends on default-setting mode or DIP-switch setting

## Notes

- This command sets the page length in 1-inch increments only.
- Set the page length before paper is loaded or when the print position is at the top-ofform position. Otherwise, the current print position becomes the top-of-form position.
- Setting the page length cancels the bottom-margin setting.

Printers not featuring this command

None

Model-dependent variations

None

## Related topics

ESC N, FF, LF, Set the Printing Area, Setting page length
