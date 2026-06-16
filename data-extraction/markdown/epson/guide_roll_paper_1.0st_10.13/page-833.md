## C O N F I D E N T I A L

## FS ( L pL pH fn sn &lt;Function 80&gt;

```
[Name] Paper layout error special margin setting [Format] ASCII FS ( L pL pH fn sn Hex 1C 28 4C pL pH 50 sn Decimal 28 40 76 pL pH 80 sn [Range] ( pL + pH × 256) = 2,3 ( pL = 2, 3, pH = 0) fn = 80 TM-P60 : '0' ≤ sn ≤ '50' [Default] sn = '0' [Description] Sets the paper layout error special margin.
```

- Sets the special margin for the vertical layout ( sa ) of &lt;Function 33&gt; of this command to [± ( sn × 0.1 mm)]. The setting unit is 0.1 mm.
- ■ The setting values of ( sn ) expressed as decimals are converted to text data and the high-order values are specified first. Example: When specifying 10, the data is the 2 bytes '10' [Hexadecimal = 31H, 30H / Decimal = 49, 48].
- ■ A paper layout error may occur with ( sn ) of this function and with the paper layout (vertical layout (sa)) with the print reference detection when the first page is printed when the paper is replaced or after turning on the power, when a setting other than "No reference" (sm ≠ "0") is specified for paper layout (layout reference) for &lt;Function 33&gt; of this command. For details of the paper layout error, refer to the model information.
- ■ The setting value of this function is enabled until the following operations are executed. It is not initialized by ESC @ . The setting value for this function is the saved data of GS ( M &lt;Function 1&gt;.
- Executing this function
- Turning off the power or resetting
- ■ The setting value of this function is affected by detection of the print reference when the first sheet is printed at the time of the operations below.
- When closing the cover
- When turning off the power or resetting

[Notes]
