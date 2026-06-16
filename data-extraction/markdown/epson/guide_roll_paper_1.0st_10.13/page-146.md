## C O N F I D E N T I A L

## GS ( N

[Name]

Select character effects

[Printers not featuring this command] TM-T70 , TM-T20 , TM-P60 , TM-U230 , TM-U220 , TM-T88V

[Description] Selects the character style(s)

- Function code fn specifies the function.
- pL , pH specifies ( pL + pH × 256) as the number of bytes after pH ( fn and [parameters] ). Description of the [parameters] is described in each function.
- ■ The function is defined by function code ( fn ). Details of performance differ, depending on the function.
- ■ Settings of this command affect printing of alphanumeric, Katakana, multilingual, user-defined, and userdefined Kanji characters.
- ■ Settings of this command are effective until ESC @ is executed, the printer is reset, or the power is turned off.
- ■ Settings of this command do not affect printing of graphics, bit image, bar code (including HRI characters), and two dimension code.
- ■ The color of the graphics can be specified by GS ( L .

|   fn | Function No.   | Function name            |
|------|----------------|--------------------------|
|   48 | Function 48    | Select character color   |
|   49 | Function 49    | Select background color  |
|   50 | Function 50    | Turn shading mode on/off |

[Model-dependent variations]

TM-J2000/J2100 , TM-T90 , TM-T88IV , TM-L90

## [Notes]

SETTING COMMAND
