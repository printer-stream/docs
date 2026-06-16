## C O N F I D E N T I A L

## GS ( M pL pH fn m &lt;Function 3&gt;

[Name] Select the setting values loaded to the work area after the initialization process [Format] ASCII GS ( M pL pH  fn  m Hex 1D 28 4D 02 00 fn m Decimal 29 40 77 2 0 fn m [Range] ( pL + pH × 256 ) = 2 , ( pL = 2 , pH = 0 ), fn = 3, 51 TM-J2000/J2100 , TM-T90 , TM-L90 , TM-P60 : m = 0,1, 48, 49

[Default] [Description]

[Notes]

m

```
= 0
```

Selects the command setting values loaded to the work area after the printer performs the initialization process.

- When m = 0, 48, the default values described in this guide are applied.
- When m ≠ 0, 48, the setting values are stored in the storage area specified by m .
- ■ This function does not change the values in the work area and storage area.
- ■ The setting of this function affects the following initializations.
- Turning on the power.
- Resetting the hardware by using a reset terminal.
- Executing ESC @ .
- Executing a software reset.
- ■ The specification of this function is maintained after turning off the power.
- ■ In autoload processing, the values of the commands that are in the work area and are not affected by this function and the values in the storage area are not changed.
- ■ The values affected by autoload processing of this function are different, depending on the printer models. See model-dependent variations for details.
