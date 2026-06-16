## Dot density

| Parameter m in ESC * command   | Horizontal density (dpi)   | Vertical density (dpi)   | Vertical density (dpi)   | Adjacent dot printing   | Dots per column   | Bytes per column   |
|--------------------------------|----------------------------|--------------------------|--------------------------|-------------------------|-------------------|--------------------|
| Parameter m in ESC * command   | Horizontal density (dpi)   | 24 pin                   | 48 pin                   | Adjacent dot printing   | Dots per column   | Bytes per column   |
| 0                              | 60                         | 60                       | 60                       | Yes                     | 8                 | 1                  |
| 1                              | 120                        | 60                       | 60                       | Yes                     | 8                 | 1                  |
| 2                              | 120                        | 60                       | 60                       | No                      | 8                 | 1                  |
| 3                              | 240                        | 60                       | 60                       | No                      | 8                 | 1                  |
| 4                              | 80                         | 60                       | 60                       | Yes                     | 8                 | 1                  |
| 6                              | 90                         | 60                       | 60                       | Yes                     | 8                 | 1                  |
| 32                             | 60                         | 180                      | 180                      | Yes                     | 24                | 3                  |
| 33                             | 120                        | 180                      | 180                      | Yes                     | 24                | 3                  |
| 38                             | 90                         | 180                      | 180                      | Yes                     | 24                | 3                  |
| 39                             | 180                        | 180                      | 180                      | Yes                     | 24                | 3                  |
| 40                             | 360                        | 180                      | 180                      | No                      | 24                | 3                  |
| 71                             | 180                        | N/A                      | 360                      | Yes                     | 48                | 6                  |
| 72                             | 360                        | N/A                      | 360                      | No                      | 48                | 6                  |
| 73                             | 360                        | N/A                      | 360                      | Yes                     | 48                | 6                  |

## Notes

- Not all values for m are available on all printers; see the Command Table for a list of which values are available on your printer.
- Printing 48-dot columns is available only on 48-dot printers.

## Printers not featuring this command

None

## Model-dependent variations

ActionPrinter 3000, ActionPrinter 4000, ActionPrinter 4500, LQ-510, LQ-550, LQ-850, LQ850+, LQ-860, LQ-860+, LQ-950, LQ-1010, LQ-1050, LQ-1050+, LQ-1060, LQ-1060+, LQ2550, and all ESC/P 2 printers

A vertical print density of 360 dpi can be achieved on 24-pin printers that feature the ESC + command. Advance the paper 1/360 inch (using the ESC + command) and then overprint the previous graphics line.

## Related topics

Sending graphics data, Bit-image graphics
