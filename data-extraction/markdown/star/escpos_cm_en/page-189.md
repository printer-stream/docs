<!-- image -->

## ESC	GS	ETX	s	n1	n2

| Name           | Send print-end counter, initialize   | Send print-end counter, initialize   | Send print-end counter, initialize   | Send print-end counter, initialize   | Send print-end counter, initialize   | Send print-end counter, initialize   |
|----------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|
| Code           | ASCII                                | ESC                                  | GS                                   | ETX                                  | s n1                                 | n2                                   |
| Code           | Hex.                                 | 1B                                   | 1D                                   | 03                                   | s n1                                 | n2                                   |
| Code           | Decimal                              | 27                                   | 29                                   | 3                                    | s n1                                 | n2                                   |
| Defined Region | Spec. A:                             | 0 ≤ s ≤ 2                            | 0 ≤ s ≤ 2                            | 0 ≤ s ≤ 2                            |                                      |                                      |
| Defined Region | Spec. B:                             | 0 ≤ s ≤ 4                            | 0 ≤ s ≤ 4                            | 0 ≤ s ≤ 4                            |                                      |                                      |
| Defined Region | Spec. C:                             | 0 ≤ s ≤ 5                            | 0 ≤ s ≤ 5                            | 0 ≤ s ≤ 5                            |                                      |                                      |
| Defined Region | 0 ≤ n1 ≤ 255, 0 ≤ n2 ≤ 255           | 0 ≤ n1 ≤ 255, 0 ≤ n2 ≤ 255           | 0 ≤ n1 ≤ 255, 0 ≤ n2 ≤ 255           | 0 ≤ n1 ≤ 255, 0 ≤ n2 ≤ 255           |                                      |                                      |

## Function

This command is run when reading from the reception buffer. Processes the print end counter according to the s parameter.

|   s | Name                        | Function                                                                                                                                                                                                                          |
|-----|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   0 | Print end counter reference | Sends the current print end counter to the host. (Does not wait for print end. Does not count up.)                                                                                                                                |
|   1 | Print end counter update    | Runs the next operation. (1) Prints data in line buffer, if data exists. (2) Waits until printing ends (motor stops). (3) Updates print end counter (+1) (4) Sends print end counter to host.                                     |
|   2 | Print end counter clear     | Returns the print end counter to its default value (zero clear). (Does not wait for print end. Does not send the print end counter to the host.                                                                                   |
|   3 | Start document n1, n2 = 0   | (1) Sets data intake mode (2) Initialize                                                                                                                                                                                          |
|   4 | End document n1, n2 = 0     | (1) Prints data in line buffer, if data exists. (2) Waits until printing ends (motor stops). (3) Cancels data intake mode                                                                                                         |
|   5 | Data timeout setting        | n1=0 : Initializes to the content of MSW. (n2=0) n1=1 : Data timeout setting n2=0: Timeout disabled Others: n2 = Data timeout time (units: seconds 1 to 255 seconds) n1=2 : Sends the current timeout setting to the host. (n2=0) |

When s = 0, or s = 1 is specified, the data format returned to the host is as shown below.

## &lt;Returned Data Formats&gt;

| Code   | ASCII   | ESC   | GS   |   ETX | s n1   | n2   | [Print end counter]   |   NUL |
|--------|---------|-------|------|-------|--------|------|-----------------------|-------|
|        | Hex.    | 1B    | 1D   |    03 | s n1   | n2   | [Print end counter]   |    00 |
|        | Decimal | 27    | 29   |     3 | s n1   | n2   | [Print end counter]   |     0 |

When [Print end counter] is 1 byte in length, the initial value is 0x00.

When s = 1, increments by 1 each time the command is processed. After 0xFF, returns to 0x00.

There is one [Print end counter] in the printer that is unrelated to the n1, n2 values.

(There is no counter for the n1, n2 values.)
