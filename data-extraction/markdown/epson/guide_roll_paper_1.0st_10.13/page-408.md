## C O N F I D E N T I A L

## ESC &lt;

[Name]

Return home

[Format]

ASCII

ESC &lt;

Hex

1B 3C

Decimal

27 60

[Range]

None

[Default]

None

[Printers not featuring this command] TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60

[Description]

[Notes]

Moves the print head to the standby position.

- ■ The standby position is different, depending on the printer model.
- ■ The command rechecks the standby position; therefore, the print position might be shifted before and after checking the standby position.

[Model-dependent variations]

TM-J2000/J2100 , TM-U230 , TM-U220

## Program Example for all printers

PRINT #1, CHR$(&amp;H1B);"&lt;";

## TM-J2000/J2100

The standby position is on the right.

## TM-U230

The standby position is on the left.

## TM-U220

The standby position is on the left.

EXECUTING COMMAND
