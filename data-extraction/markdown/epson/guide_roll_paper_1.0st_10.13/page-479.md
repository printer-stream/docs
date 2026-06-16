## C O N F I D E N T I A L

## GS ( H p L p H fn m d &lt;Function 49&gt;

```
[Format] ASCII GS ( H pL pH  fn  m d Hex 1D 28 48 03 00 31 30 d Decimal 29 40 72 3 0 49 48 d [Range] ( pL + pH × 256) = 3( pL = 3, pH = 0) fn = 49 m = 48 0 ≤ d ≤ 2 , 48 ≤ d ≤ 50 [Default] d = 0 [Description] Specifies or turns off the offline response transmission.
```

| d     | Function                                                                       |
|-------|--------------------------------------------------------------------------------|
| 0, 48 | Turns off the offline response transmission.                                   |
| 1, 49 | Specifies the offline response transmission (not including the offline cause). |
| 2, 50 | Specifies the offline response transmission (including the offline cause).     |

When specifying offline response transmitting ( d = 1, 2, 49, 50), offline response is transmitted when the printer goes offline for any of the following causes.

- Any paper cover open
- Printing stop because of paper out
- Automatically recoverable error
- Recoverable error
- Unrecoverable error
- ■ Confirm that untransmitted offline responses aren't stored in the printer when specifying or turning off offline response transmitting by this function.

[Notes]
