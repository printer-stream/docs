## Notes

- The data within brackets in the Format section above is repeated for each character you define.
- The format of the attribute byte 'a' is different for draft and NLQ characters.

## Draft

You can define characters 11-dots wide by 8-dots high. You must specify whether to define the upper or lower 8 dots of the 9 dots available. You can also specify the columns not printed on the left and right of the characters during proportional spacing. Set both these parameters with the a parameter, as described below:

## Attribute byte table

| Beginning Column   | Beginning Column   | Ending Column   | Ending Column   | Upper/Lower 8 pins   | Upper/Lower 8 pins   |
|--------------------|--------------------|-----------------|-----------------|----------------------|----------------------|
| Column number      | Value              | Column number   | Value           | Pin group            | Value                |
| 0                  | 0                  | 1               | 1               | Upper 8 pins         | 128                  |
| 1                  | 16                 | 2               | 2               | Lower 8 pins         | 0                    |
| 2                  | 32                 | 3               | 3               |                      |                      |
| 3                  | 48                 | 4               | 4               |                      |                      |
| 4                  | 64                 | 5               | 5               |                      |                      |
| 5                  | 80                 | 6               | 6               |                      |                      |
| 6                  | 96                 | 7               | 7               |                      |                      |
| 7                  | 112                | 8               | 8               |                      |                      |
|                    |                    | 9               | 9               |                      |                      |
|                    |                    | 10              | 10              |                      |                      |
|                    |                    | 11              | 11              |                      |                      |

Add up the values for all three settings; the value for a is this total.

## NLQ

The attribute byte a equals the width of the character, between 1 and 12 dot columns.

- Only NLQ characters can be defined on LX printers, ActionPrinter Apex 80, ActionPrinter 2000, ActionPrinter 2250, and ActionPrinter T-1000.
- When you switch to NLQ printing on FX printers, the printer enhances user-defined characters to appear as NLQ-mode characters.
- Defining characters during draft or NLQ mode results in the user-defined characters having the draft or NLQ attribute. You cannot define characters of different attributes at the same time; previously defined characters will be deleted.
- Always cancel italic characters with the ESC 5 command before defining characters. After defining user-defined characters, you can italicize them by sending the ESC 4 command.
- Do not define continuous dots on the same row during draft mode; the printer ignores the second of two continuous dots.
- Send the ESC % 1 command to switch to user-defined characters.
- Send the ESC I 1 command to allow you to print the characters between 128 and 159 and the non-control code characters between 0 and 31.
