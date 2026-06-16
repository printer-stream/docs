## C O N F I D E N T I A L

## · When a = 8, memory switch 8 is set as follows:

| Msw        |   Setting value ( b ) | Function                                                                                         |
|------------|-----------------------|--------------------------------------------------------------------------------------------------|
| 8-1 to 8-4 |                    50 | Reserved                                                                                         |
| 8-5        |                    48 | The printer status is sent back as 'the paper empty' when the roll paper cover is opened.        |
| 8-5        |                    49 | The printer status is sent back 'the roll paper cover open' when the roll paper cover is opened. |
| 8-6        |                    48 | Reserved: Fixed to OFF (Don't change the setting)                                                |
| 8-7        |                    48 | Printer BUSY is released when the remaining capacity of the receive buffer goes to 256 bytes.    |
| 8-7        |                    49 | Printer BUSY is released when the remaining capacity of the receive buffer goes to 138 bytes.    |
| 8-8        |                    48 | Printer cover open during operation: Error that automatically recovers.                          |
| 8-8        |                    49 | Printer cover open during operation: Error that can possibly recover.                            |

- Setting of [Msw 8-5] affects the statuses as follows:
- ■ Basic ASB status (See 'GS a ' command)
- ■ Real-time status (See 'DLE EOT ' command)

Setting the memory switch ([Msw 8-5], [Msw 8-7]) can be changed by 'Memory switch setting mode' by the panel switch operation when the power supply is turned on.
