## C O N F I D E N T I A L

## ESC ( A

EXECUTING + SETTING

[Name]

Control beeper tones

[Printers not featuring this command] TM-J2000/J2100 , TM-T90 , TM-T88IV , TM-T70 , TM-L90 , TM-U220

[Range]

TM-P60 :

fn = 48

TM-U230 :

fn = 97, 98, 99

TM-T20 , TM-T88V :

fn = 97

[Description]

Performs the various tasks related to the control of the beeper (listed in the table below).

- Function code ( fn ) specifies the function.
- pL , pH specifies ( pL + pH × 256) as the number of bytes after pH ( fn and [parameters] ). Description of the [parameters] is described in each function.
- ■ The functions of this command are determined by the ( fn ) setting. Actual command operation varies according to function.

|   fn | Function No.   | Function name                                                                                                                                    |
|------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
|   48 | Function 48    | Beep integrated beeper                                                                                                                           |
|   97 | Function 97    | Beep integrated beeper in TM-U230 models Sound buzzer in TM-T88V , TM-T20 models (registered sound pattern specified) (optional external buzzer) |
|   98 | Function 98    | Set integrated beeper when offline factors occur in TM-U230 models.                                                                              |
|   99 | Function 99    | Set integrated beeper except when offline factors occur in TM-U230 models.                                                                       |

## Program Example 1

PRINT #1, CHR$(&amp;H1B);"(A";CHR$(4);CHR$(0);CHR$(48);CHR$(49);CHR$(3);CHR$(15); ← &lt;Function 48&gt;

[Notes]
