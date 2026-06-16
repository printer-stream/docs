## Format

| ASCII   | DEL   |
|---------|-------|
| Hex     | 7F    |
| Decimal | 127   |

## Function

Deletes the last printable character in the print buffer's current line

## Notes

- This is a nonrecommended command.
- This command only deletes printable characters; printer control codes are not affected.
- The printer ignores this command if it follows a command that moves the horizontal print position (ESC $, ESC \, or HT)

## Printers not featuring this command

None

## Model-dependent variations

None
