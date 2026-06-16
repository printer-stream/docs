## C O N F I D E N T I A L

## &lt;The second byte: information for unrecoverable errors&gt;

| Bit   | Off/On   | Hex   | Decimal   | Information   |
|-------|----------|-------|-----------|---------------|
| 3 ~ 5 | -        | -     | -         | Reserved.     |
| 6     | On       | 40    | 64        | Fixed.        |
| 7     | 0        | 00    | 0         | Fixed.        |

When one of above errors occurs, turn off the printer immediately.

## &lt;The third byte: information for unrecoverable errors&gt;

| Bit   | Off/On   | Hex   | Decimal   | Information                       |
|-------|----------|-------|-----------|-----------------------------------|
| 0     | Off      | 00    | 0         | Thermostat error hasn't occurred. |
|       | On       | 01    | 1         | Thermostat error has occurred.    |
| 1 ~ 5 | -        | -     | -         | Reserved.                         |
| 6     | On       | 40    | 64        | Fixed.                            |
| 7     | Off      | 00    | 0         | Fixed.                            |

When one of above errors occurs, turn off the printer immediately.

## &lt;The fourth byte: information for recoverable error&gt;

| Bit   | Off/On   | Hex   | Decimal   | Information                                                        |
|-------|----------|-------|-----------|--------------------------------------------------------------------|
| 0     | Off      | 00    | 0         | Autocutter error hasn't occurred.                                  |
|       | On       | 01    | 1         | Autocutter error has occurred.                                     |
| 1     | Off      | 00    | 0         | Roll paper cover open error hasn't occurred.(When Msw [8-8] is ON) |
|       | On       | 02    | 2         | Roll paper cover open error hasn't occurred.(When Msw [8-8] is ON) |
| 2 ~ 5 | -        | -     | -         | Reserved.                                                          |
