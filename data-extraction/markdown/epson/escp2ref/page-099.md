## Format

```
ASCII ESC % n Hex 1B 25 n Decimal 27 37 n
```

## Parameter range

```
n = 0, 1, 48, 49
```

## Function

Switches between normal and user-defined characters, as follows:

```
n = 0 or 48 Normal (ROM) characters 1 or 49 User-defined (RAM) characters
```

## Default

Normal (ROM) characters

## Printers not featuring this command

None

## Model-dependent variations

FX-850 and FX-1050

Draft user-defined characters are converted to LQ characters during LQ mode.

## Related topics

ESC :, ESC &amp;, ESC 6, ESC 7, Switching to RAM character printing
