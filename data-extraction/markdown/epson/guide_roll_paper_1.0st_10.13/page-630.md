## C O N F I D E N T I A L

## GS ( k &lt;Function 280&gt;

```
[Name] [Format] [Range]
```

```
MaxiCode: Store the data in the symbol storage area ASCII GS ( k pL pH cn fn m d1...dk Hex 1D 28 6B pL pH 32 50 30 d1...dk Decimal 29 40 107 pL pH 50 80 48 d1...dk 4 ≤ ( pL + pH × 256) ≤ 141 (4 ≤ pL ≤ 141, 0 ≤ pH ≤ 0) cn = 50 fn = 80 m = 48 0 ≤ d ≤ 255 k = ( pL + pH × 256) - 3
```

[Description] [Notes]

Stores the MaxiCode symbol data ( d1...dk ) in the symbol storage area.

- ■ The symbol data saved in the symbol storage area by this function is encoded by &lt;Function 081&gt; and &lt;Function 082&gt; of this command. After &lt;Function 081&gt; and &lt;Function 082&gt; are executed, the symbol data in the symbol storage area is kept.
- ■ k bytes of d1...dk are processed as the symbol data.
- ■ Settings of this function are effective until the following processing is performed:
- Function 080 or 180 or 280 or 380 or 480 is executed
- ESC @ is executed
- The printer is reset or the power is turned off

[Model-dependent variations]

TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-P60

## TM-T90 , TM-T88IV , TM-T70

This model does not support this function.

## TM-T20 , TM-T88V

This printer supports this function.
