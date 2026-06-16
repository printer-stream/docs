## C O N F I D E N T I A L

## GS ( M pL pH fn m &lt;Function 2&gt;

```
[Name] Load the setting values stored in the storage area to the work area [Format] ASCII GS ( M pL pH  fn  m Hex 1D 28 4D 02 00 fn m Decimal 29 40 77 2 0 fn m [Range] ( pL + pH × 256 ) = 2 , ( pL = 2 , pH = 0 ), fn = 2 , 50
```

TM-J2000/J2100 , TM-T90 , TM-L90 , TM-P60 : m = 0,1, 48, 49

Loads the command setting values stored in the storage area specified by m to the work area.

- When m = 0, 48, the default values described in this guide are applied.
- When m ≠ 0, 48, the setting values are stored in the storage area specified by m .
- ■ This function is effective at the beginning of a line in standard mode.
- ■ This function cannot be included in a macro. Do not use this function when executing a macro.
- ■ The value in the work area is set to the default value by the following:
- Executing this function by specifying m = 0, 48.
- Executing Function 2 with the condition that the storage area that has not executed Function 1 is specified.
- Initializing when an autoload process has been canceled by Function 3.
- ■ The values in the work area that are not affected by this command are not changed.
- ■ The values in the storage area are not changed.
- ■ The values affected by this command are different, depending on the printer models. See modeldependent variations for details.

[Description]

[Notes]
