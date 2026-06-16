## C O N F I D E N T I A L

## GS ( M

[Name]

Customize printer control value(s)

[Printers not featuring this command] TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-U230 , TM-U220

[Description] Customizes the printer control value(s).

- Function code ( fn ) specifies the function.
- pL , pH specifies ( pL + pH × 256) as the number of bytes after pH ( fn and m ). In each function m is described.
- ■ The function of this command is determined by the function code ( fn ). Operation differs, depending on the functions.
- ■ Setting value means the values stored in the work area. They are set by commands such as line spacing, print area, or ASB function specification commands; are defined data such as user-defined data or 2-byte characters; and are the setting status such as Kanji mode. The values are different, depending on the printer models. See the model-dependent information.
- ■ Work area means the area that stores the values and is cleared when the power is turned off. The printer's actions are based on the values in the work area.
- ■ Storage area means non-volatile memory area that is used to accomplish the functions of this command. The values stored in the storage area are not cleared when power is turned off. The values in the storage area do not affect the printer operation.
- ■ A default value for each command is stored in the storage area when the printer is shipped.
- ■ The values stored in the storage area are loaded to the work area when Function 1 is executed or when an autoload specified by Function 3 is initialized. These values affect the printer's operation afterward.

| fn    | Function No.   | Function name                                                                       |
|-------|----------------|-------------------------------------------------------------------------------------|
| 1, 49 | Function 1     | Save the setting values from the work area into the storage area.                   |
| 2, 50 | Function 2     | Load the setting values stored in the storage area to the work area.                |
| 3, 51 | Function 3     | Select the setting values loaded to the work area after the initialization process. |

## [Notes]

SETTING COMMAND
