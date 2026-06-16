## C O N F I D E N T I A L

- ■ Second byte (printer information)
- Bits 0, 1, and 2 of the second byte are undefined.
- ■ Third byte (paper sensor information)
- When the cover is open, the states of the roll paper near end sensor (bit 0, 1) and the roll paper end sensor (bit 2, 3) retain the values when the cover was closed immediately before.

## TM-P60

## TM-P60 with Peeler

The function of Bit 0 of parameter ( n ) is not supported. Specify 1 to bit 0 of n or bits of 'Reserved.'

- ■ First byte (printer information)
- Bit 2 status is as follows:
- Bit 5 indicates the open/closed status of the peeler cover.
- ■ Basic second byte (printer information)
- Bits 0 and 3 of the second byte are not supported.
- If the cause of an automatically recoverable error (bit 6) is a "paper error," recovery from the error is possible by opening and closing the peeler cover.
- ■ Basic third byte (paper sensor information)
- Bits 0 and 1 of the third byte are not supported.
- When the cover is open, the status of the roll paper end sensor (bit 2, 3) retains the value when the cover was closed immediately before.
- ■ Basic fourth byte (paper sensor information)

|   n: Bit |   Binary |   Hex |   Decimal | Function                               |
|----------|----------|-------|-----------|----------------------------------------|
|        2 |        0 |    00 |         0 | Does not go to offline by low battery. |
|          |        1 |    04 |         4 | Offline by low battery.                |
