## C O N F I D E N T I A L

- ■ The default value when the power supply is turned on and when ESC @ is executed might be different.
- The default value when the power supply is turned on becomes the [default value].
- The selection of peripherals after ESC @ is executed is shown in the next table.
- (*1) When the setting of ESC = is ( n = 2), n is not changed because ESC @ is not executed.
- In the model not equipped with the switch of the parallel interface specification and the connection of DM-D (customer display), the settings are the same as when the switch in the above table is off.

|                                                    |                                                                           |   n |   n |   n |
|----------------------------------------------------|---------------------------------------------------------------------------|-----|-----|-----|
| Setting when power supply is                       | When the switch of the [DM-D (customer display) connection] is turned off |   1 |   1 |   1 |
| turned on                                          | When the switch of the [DM-D (customer display) connection] is turned on  |   2 |   2 |   2 |
| Setting immediately before execution of ESC @ (*1) | Setting immediately before execution of ESC @ (*1)                        |   1 |   2 |   3 |
| Setting after ESC @ is executed                    | When the switch of the [DM-D (customer display) connection] is turned off |   1 |   2 |   1 |
| Setting after ESC @ is executed                    | When the switch of the [DM-D (customer display) connection] is turned on  |   1 |   2 |   2 |

[Model-dependent variations]

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60 , TM-U230 , TM-U220

## Program Example for all printers

```
PRINT #1, CHR$(&H1B);"=";CHR$(1); ← Printer enabled PRINT #1, "AAAAA"; PRINT #1, CHR$(&H1B);"=";CHR$(2); ← Printer disabled PRINT #1, "BBBBB"; PRINT #1, CHR$(&H1B);"=";CHR$(3); ← Pinter enabled PRINT #1, " CCCCC"; CHR$(&HA);
```

## TM-J2000/J2100

The memory switch which selects the connection of DM-D (customer display) is Msw 1-6.

## Print Sample

AAAAA CCCCC
