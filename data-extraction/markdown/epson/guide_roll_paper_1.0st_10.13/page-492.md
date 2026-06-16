## C O N F I D E N T I A L

## TM-L90

The following print control modes are available.

| m     | Print control mode                                            |
|-------|---------------------------------------------------------------|
| 0, 48 | Print control mode when power supply is turned on             |
| 1, 49 | Standard print control mode                                   |
| 2, 50 | Suitable print control mode for printing a fence bar code     |
| 3, 51 | Suitable print control mode for printing a ladder bar code    |
| 4, 52 | Suitable print control mode for printing a two dimension code |

This printer selects 'Standard print control mode' at setting of ( m = 0,48).

In printing when m = 3, 4, 51, or 52, the printer starts actual printing after it reaches control speed. The paper must be fed 10 dots or less in this operation. Therefore, when the printer starts printing, paper feeding for 10 dots or less without printing might occur.

## TM-P60

The following printing control modes are selectable:

|   m | Print control mode   |
|-----|----------------------|
|  49 | High speed           |
|  50 | Fine                 |

When printing ladder bar code (bar code rotated by 90 degrees in page mode) or two dimension code, it is printed with the 'printing control mode = fine' regardless of the setting of this command.
