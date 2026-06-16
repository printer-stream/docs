<!-- image -->

## ESC GS ETX s n1 n2

[Name] [Code]

Send print-end counter, initialize

ASCII

ESC

GS  ETX

s

n1

n2

Hexadecimal 1B 1D 03 s n1 n2

Decimal

27 30 3 s n1 n2

[Defined Area]

0 ≤ s ≤ 4

0 ≤ n1 ≤ 255, 0 ≤ n2 ≤ 255

[Function]

This command is run when reading from the reception buffer. Processes the print end counter according to the s parameter.

|   s | Name                        | Function                                                                                                                                                                                                              |
|-----|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   0 | Print end counter reference | Sends the current print end counter to the host. (Does not wait for print end. Does not count up.)                                                                                                                    |
|   1 | Print end counter update    | Runs the following operations. (1) Prints data in line buffer, if data exists. (2) Waits until printing ends (motor stops). (3) Updates the print end counter (increments by 1). (4) Sends print end counter to host. |
|   2 | Print end counter clear     | Returns the print end counter to its default value (zero clear). (Does not wait for print end. Does not send the print end counter to the host.                                                                       |
|   3 | Start document n1, n2 = 0   | (1) Sets data intake mode (2) Initialize                                                                                                                                                                              |
|   4 | End document n1, n2 = 0     | (1) Prints data in line buffer, if data exists. (2) Waits until printing ends (motor stops). (3) Cancels data intake mode                                                                                             |

The data formats sent to the host when s = 0 or s =1 are shown below.

```
<Returned Data Formats> [Code] ASCII ESC GS ETX s n1 n2 [Print end counter]  NUL Hexadecima l 1B 1D 03 s n1 n2 00 [Print end counter] Decimal 27 30 3 s n1 n2 [Print end counter] 0
```

* Echoes back the specified contents from the host as is until ESC GS ETX s n1 n2, and then sends the print end counter value and NUL.

When [Print end counter] is 1 byte in length, the initial value is 0x00.

When s = 1, increments by 1 each time the command is processed. After 0xFF, returns to 0x00.

There is one [Print end counter] in the printer that is unrelated to the n1, n2 values.

(There is no counter for the n1, n2 values.)

-----------------------------------------------------------------------------
