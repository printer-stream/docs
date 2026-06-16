## C O N F I D E N T I A L

## TM-L90

For the TM-L90 with Peeler, this function applies to the roll paper cover. The offline cause of this printer is constructed of 5 bytes as shown in the following tables.

## &lt;The first byte: information for unrecoverable error&gt;

| Bit   | Off/On   | Hex   | Decimal   | Information                                  |
|-------|----------|-------|-----------|----------------------------------------------|
| 0     | Off      | 00    | 0         | CPU execution error hasn't occurred.         |
| 0     | On       | 01    | 1         | CPU execution error has occurred.            |
| 1     | Off      | 00    | 0         | ROM error hasn't occurred in the memory.     |
| 1     | On       | 02    | 2         | ROM error has occurred in the memory.        |
| 2     | Off      | 00    | 0         | G/A error hasn't occurred in the gate array. |
| 2     | On       | 04    | 4         | G/A error has occurred in the gate array.    |
| 3 ~ 5 | -        | -     | -         | Reserved.                                    |
| 6     | On       | 40    | 64        | Fixed.                                       |
| 7     | 0        | 00    | 0         | Fixed.                                       |

When one of above errors occurs, turn off the printer immediately.

## &lt;The second byte: information for unrecoverable errors&gt;

|   Bit | Off/On   |   Hex |   Decimal | Information                         |
|-------|----------|-------|-----------|-------------------------------------|
|     0 | Off      |    00 |         0 | High voltage error hasn't occurred. |
|       | On       |    01 |         1 | High voltage error has occurred.    |
|     1 | Off      |    00 |         0 | Low voltage error hasn't occurred.  |
|       | On       |    02 |         2 | High voltage error has occurred.    |
|     2 | Off      |    00 |         0 | Over current error hasn't occurred. |
|       | On       |    02 |         2 | Over current error has occurred.    |
