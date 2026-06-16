Before you can define and save your user-defined characters, you must change the printer settings to match your planned characters. The following combinations of character traits are possible.

## 24 /48-pin printers

| Print quality                  |   Proportional |   Fixed pitch |
|--------------------------------|----------------|---------------|
| Draft                          |                |             3 |
| LQ Normal size Super/Subscript |              3 |             3 |
| LQ Normal size Super/Subscript |              3 |             3 |

## 9-Pin printers

| Print quality Draft   |   3 |
|-----------------------|-----|
| NLQ                   |     |
|                       |   3 |

## Note:

You should not store characters in RAM memory when the printer is set to italic printing (with the ESC 4 command). Always send the ESC 5 command to cancel italic printing before you define user-defined characters or copy characters to RAM memory.

Follow the steps below when setting the traits of your planned user-defined and other RAM characters. (Only steps 1 and 2 are necessary for 9-pin printers.)

1. Select the print quality: LQ, NLQ, or draft.
2. Cancel italic printing.
3. Select or cancel proportional spacing.
4. Select or cancel super/subscript characters.
