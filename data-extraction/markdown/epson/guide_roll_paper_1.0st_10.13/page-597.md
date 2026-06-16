## C O N F I D E N T I A L

## GS ( k &lt;Function 066&gt;

```
[Name] PDF417: Set the number of rows [Format] ASCII GS ( k pL pH cn fn n Hex 1D 28 6B 03 00 30 42 n Decimal 29 40 107 3 0 48 66 n [Range] ( pL + pH × 256) = 3 ( pL =3, pH =0) cn = 48 fn = 66 n = 0, 3 ≤ n ≤ 90 [Default] n = 0 [Description] Sets the number of rows  for PDF417.
```

- When n = 0 specifies automatic processing.
- When n is not 0, sets the number of rows to n rows.
- ■ Settings of this function affect the processing of Functions 081 and 082.
- ■ When automatic processing ( n = 0) is specified, the maximum number of rows is 90.
- ■ When automatic processing ( n = 0) is specified, the number of rows is calculated by the print area when processing Functions 081, 082, and module height (Function 068).
- ■ Settings of this function are effective until ESC @ is executed, the printer is reset, or the power is turned off.

[Model-dependent variations]

## TM-T88IV , TM-T70

This function is not supported in the Japanese specification.

## TM-T20 , TM-T88V

This printer supports this function.

TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-P60

[Notes]
