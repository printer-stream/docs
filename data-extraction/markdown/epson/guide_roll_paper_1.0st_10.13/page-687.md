## C O N F I D E N T I A L

## GS ( C pL pH m fn b c1 c2 d1...dk &lt;Function 1&gt;

```
[Name] Store the data in the specified record [Format] ASCII GS ( C pL pH m fn b c1 c2 d1...dk Hex 1D 28 43 pL pH 00 fn 00 c1 c2 d1...dk Decimal 29 40 67 pL pH 0 fn 0 c1 c2 d1...dk [Range] 6 ≤ ( pL + pH × 256) ≤ 65535 (0 ≤ pL ≤ 255, 0 ≤ pH ≤ 255) m = 0 fn = 1, 49 b = 0 32 ≤ c1 ≤ 126 32 ≤ c2 ≤ 126 32 ≤ d ≤ 254 k = ( pL + pH × 256) -5
```

[Description]

[Notes]

Stores the data ( d1... dk ) as the record specified by the key codes ( c1 , c2 ) in the NV user memory.

- When the specified record already exists, the data is overwritten.
- A terminator is automatically assigned.
- ■ In standard mode, this command is valid only at the beginning of the line.
- ■ You cannot include macros with this command, so do not use this command while defining macros.
- ■ You cannot use this command when the NV user memory does not have enough capacity to store the specified records. The available capacity is confirmed by Function 4.

[Model-dependent variations]

TM-J2000/J2100 , TM-T90 , TM-T70 , TM-L90 , TM-P60 , TM-U220

## TM-J2000/J2100 , TM-T90 , TM-T70 , TM-L90 , TM-U220

This function uses the 'data quantity ( k ) + number of control information data (3 byte)' area for execution.
