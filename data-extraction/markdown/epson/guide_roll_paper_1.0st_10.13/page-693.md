## C O N F I D E N T I A L

## GS ( C pL pH m fn b &lt;Function 5&gt;

[Name] Transmit the key code list [Format] ASCII GS ( C pL pH m fn b Hex 1D 28 43 03 00 00 fn 00 Decimal 29 40 67 3 0 0 fn 0 [Range] ( pL + pH × 256) = 3 ( pL = 3, pH = 0) m = 0 fn = 5, 53 b = 0

[Description]

[Notes]

Transmits the key code list in the NV user memory.

- ESC/POS Handshaking Protocol is required for this function.
- ■ When record exists, the printer sends the 'Header to NUL' data as shown below:
- (*1) When the quantity of stored data exceeds 40 records, the printer performs partial processing:
- If there is unsent data, the identification status of the third byte is 41H or 65 decimal.
- If there is no unsent data, the identification status of the third byte is 40H or 64 decimal.
- (*2) The printer performs batch processing when the data to be stored in the specified record is 40 records or less. At this time, the identification status of the third byte is 40H or 64 decimal.
- (*3) The data is the key code. A terminator is not included in the data.

| Send data                       | Hex        | Decimal   | Data quantity   |
|---------------------------------|------------|-----------|-----------------|
| Header                          | 37H        | 55        | 1 byte          |
| Identifier                      | 71H        | 113       | 1 byte          |
| Identification status (*1) (*2) | 40H or 41H | 64 or 65  | 1 byte          |
| Data (*3)                       | 20H - 7EH  | 32 - 126  | 2 - 80 bytes    |
| NUL                             | 00H        | 0         | 1 byte          |
