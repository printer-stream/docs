## Format

```
ASCII ESC % n Hex 1B 25 n Decimal 27 37 n
```

## Parameter range

<!-- formula-not-decoded -->

## Function

Switches between normal and user-defined characters, as follows:

```
n = 0 or 48 Normal (ROM) characters 1 or 49 User-defined (RAM) characters
```

## Default

Normal (ROM) characters

## Notes

Switch to ROM characters (ESC % 0) before selecting user-defined characters using the ESC t 2 command.

## Printers not featuring this command

None

Model-dependent variations

None

## Related topics

ESC :, ESC &amp;, ESC t, ESC ( t, Switching to RAM character printing
