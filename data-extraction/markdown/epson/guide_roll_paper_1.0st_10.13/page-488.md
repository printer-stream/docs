## C O N F I D E N T I A L

## GS ( K

[Name]

Select print control method(s)

[Printers not featuring this command] TM-U230 , TM-U220

[Description]

Selects the print control methods.

- Function code fn specifies the function.
- pL , pH specifies ( pL + pH × 256) as the number of bytes after pH ( fn and [parameters] ). The [parameters] are described in each function.
- ■ This command decides the function according to the function code ( fn ). Performance of the functions differs, depending on the function.

|   fn | Function No.   | Function name                                              |
|------|----------------|------------------------------------------------------------|
|   48 | Function 48    | Select the print control mode                              |
|   49 | Function 49    | Select the print density                                   |
|   50 | Function 50    | Select the print speed                                     |
|   97 | Function 97    | Select the number of parts for the thermal head energizing |

[Notes]

- ■ The settings of this command are effective until ESC @ is executed, the printer is reset, or the power is turned off.

[Model-dependent variations]

TM-J2000/J2100 , TM-P60 , TM-T90 , TM-L90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70

## Program Example

PRINT #1, CHR$(&amp;H1D); Ó (K Ó ;CHR$(2);CHR$(0);CHR$(048);CHR$(049); ← Function 48

## TM-J2000/J2100 , TM-P60

This printer supports Function 48.

SETTING COMMAND
