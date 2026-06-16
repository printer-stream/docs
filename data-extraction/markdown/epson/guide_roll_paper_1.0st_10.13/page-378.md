## C O N F I D E N T I A L

## GS h

SETTING COMMAND

[Name]

Set bar code height

[Format]

ASCII

GS h n

Hex

1D 68 n

Decimal

29 104 n

[Range]

1 ≤ n ≤ 255

[Default]

TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60 : n = 162

[Printers not featuring this command] TM-U230 , TM-U220

[Description]

Sets the height of a bar code to n dots.

[Notes]

- ■ The units for n depend on the printer model.

- ■ This command setting is effective until performing of ESC @ , reset or power-off.

[Model-dependent variations]

TM-J2000/J2100 , TM-T20 , TM-T88IV , TM-T88V , TM-T90 , TM-T70 , TM-L90 , TM-P60

## Program Example for all printers

```
PRINT #1, CHR$(&H1D);"h";CHR$(50); ← Set height to 50 PRINT #1, CHR$(&H1D);"k";CHR$(2); ← Print bar code PRINT #1, "496595707379";CHR$(0); PRINT #1, CHR$(&HA); PRINT #1, CHR$(&H1D);"h";CHR$(100); ← Set height to 100 PRINT #1, CHR$(&H1D);"k";CHR$(2); ← Print bar code PRINT #1, "496595707379";CHR$(0);
```

## TM-J2000/J2100 , TM-T88IV , TM-T88V

A set unit is one dot. One dot corresponds to 0.141 mm {1/180 inch}.

<!-- image -->
