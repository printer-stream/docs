## Format

```
ASCII ESC EM n Hex 1B 19 n Decimal 27 25 n
```

## Parameter range

```
n = 49, 50, 66, 70, 82
```

## Function

Controls feeding of continuous and single-sheet paper, according to the parameters below:

```
n = 49 '1' Selects loading from bin 1 of the cut-sheet feeder 50 '2' Selects loading from bin 2 of the cut-sheet feeder 66 'B' Loads paper from the rear tractor 70 'F' Loads paper from the front tractor 82 'R' Ejects one sheet of single-sheet paper
```

## Notes

- This command was formerly known as 'Control cut-sheet feeder.'
- The former parameters '0' and '4' that control cut-sheet feeder mode are nonrecommended, and have been discontinued in ESC/P 2. ESC/P 2 printers do not have a separate cut-sheet feeder mode; the former cut-sheet feeder mode is now integrated into normal printer operation.
- The parameter 'R' ejects the currently loaded single-sheet paper without printing data from the line buffer; this is not the equivalent of the FF command (which does print line-buffer data).

## Printers not featuring this command

None

## Model-dependent variations

On non-ESC/P 2 printers:

- Only use this command when a cut-sheet feeder is installed.
- The following additional parameters are available:
- However, these parameters are nonrecommended; cut-sheet feeder mode should be selected by DIP switch instead.

```
n = 48 '0' Exits cut-sheet feeder mode 52 '4' Enters cut-sheet feeder mode
```

## Related topics

Set the Printing Area
