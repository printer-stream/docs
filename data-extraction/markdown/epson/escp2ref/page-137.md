## Format

ASCII ESC S n

```
Hex 1B 53 n Decimal 27 83 n
```

## Parameter range

```
n = 0, 1, 48, 49
```

## Function

Prints characters that follow at about 2/3 their normal height; the printing location depends on the value of n as follows:

n = 1 or 49 Lower part of the character space 0 or 48 Upper part of the character space

## Default

Normal (non-super/subscript) characters

## Notes

- This command does not affect graphics characters.
- The width of super/subscript characters when using proportional spacing is the same as that of normal characters.
- The underline strikes through the descenders on subscript characters during underline mode.
- Use the ESC T command to cancel super/subscript printing.

## Printers not featuring this command

None

Model-dependent variations

FX-850, FX-1050

Selecting double-height printing overrides super/subscript printing; super/subscript printing resumes when double-height printing is canceled.

## Related topics

ESC T, Super/subscript
