## C O N F I D E N T I A L

- ■ A set value of ESC = after this command is executed is shown in the following table.
- When the setting of ESC = is ( n = 2), n is not changed because ESC @ is not executed.
- For the model not equipped with the switch of the parallel interface specification and the DM-D (customer display) connection, the settings are the same as when the switch is OFF in the above table.

| Setting of ESC = immediately before execution of ESC @   | Setting of ESC = immediately before execution of ESC @            |   1 | 2   |   3 |
|----------------------------------------------------------|-------------------------------------------------------------------|-----|-----|-----|
| Setting after                                            | When the switch of the DM-D (customer display) connection is OFF. |   1 | -   |   1 |
| ESC @ is executed                                        | When the switch of the DM-D (customer display) connection is ON.  |   1 | -   |   2 |

[Model-dependent variations]

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60 , TM-U230 , TM-U220

```
Program Example for all printers Initialize printer
```

```
PRINT #1, CHR$(&H1D);"P";CHR$(180);CHR$(180); PRINT #1, CHR$(&H1B);"3";CHR$(60); PRINT #1, CHR$(&H1B);"U";CHR$(1); PRINT #1, CHR$(&H1B);"E";CHR$(1); PRINT #1, CHR$(&H1B);"-";CHR$(1); PRINT #1, CHR$(&H1D);"!";CHR$(17); PRINT #1, "AAAAA"; CHR$(&HA); PRINT #1, CHR$(&H1B);"@"; ← PRINT #1, "BBBBB"; CHR$(&HA);
```

## TM-J2000/J2100

The memory switch which selects the connection of DM-D (customer display) is Msw 1-6.

TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60 , TM-U230 , TM-U220

These printers do not have the switch that selects 'the connection of DM-D (customer display).'

<!-- image -->
