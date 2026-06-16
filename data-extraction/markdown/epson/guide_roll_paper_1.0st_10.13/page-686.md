## C O N F I D E N T I A L

## GS ( C pL pH m fn b c1 c2 &lt;Function 0&gt;

[Name]

Delete the specified record

[Format]

ASCII GS ( C pL pH m fn b c1 c2 Hex 1D 28 43 05 00 00 fn 00 c1 c2 Decimal 29 40 67 5 0 0 fn 0 c1 c2

[Range]

( pL + pH × 256) = 5 ( pL = 5, pH = 0)

m = 0

fn = 0, 48

b = 0

32 ≤ c1 ≤ 126

32 ≤ c2 ≤ 126

[Description]

[Notes]

Deletes the record specified by the key codes ( c1 , c2 ) in the NV user memory.

- Deleted areas are designated 'Unused areas.'
- Deleted key codes are designated as undefined.
- ■ In standard mode, this command is valid only at the beginning of the line.
- ■ You cannot include macros with this command, so do not use this command while defining macros.

[Model-dependent variations]

None
