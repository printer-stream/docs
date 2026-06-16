<!-- image -->

Name

Print Mode Selection

Code

ASCII ESC RS C n

Hex. 1B

1E 43 n

Decimal 27 30 67 n

Defined Region

0 ≤ n ≤ 1 48 ≤ n ≤ 49

n=16,n=32

Initial Value

---

Function

Selects print mode

| n    | Print Mode                 |
|------|----------------------------|
| 0,48 | Single color mode          |
| 1,49 | 2-color mode               |
| 16   | Low power consumption mode |
| 32   | Double resolution mode     |

- This command is ignored when low power consumption mode is selected.
- This command is not cleared by ESC @.
- If there is unprinted data in the line buffer, the printing of the line buffer data will be executed.
- This command is processed after the current printing has been completed.
- This command is ignored when reduced printing in the vertical direction is setting.
