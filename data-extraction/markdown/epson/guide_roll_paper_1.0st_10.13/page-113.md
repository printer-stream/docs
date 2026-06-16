## C O N F I D E N T I A L

## ESC %

```
[Name] Select/cancel user-defined character set [Format] ASCII ESC % n Hex 1B 25 n Decimal 27 37 n [Range] 0 ≤ n ≤ 255 [Default] n = 0
```

[Printers not featuring this command] TM-P60

[Description]

[Notes]

Selects or cancels the user-defined character set.

- When the LSB of n is 0, the user-defined character set is canceled.
- When the LSB of n is 1, the user-defined character set is selected.
- ■ When the user-defined character set is canceled, the resident character set is automatically selected.
- ■ Settings of this command are effective until ESC @ is executed, the printer is reset, or the power is turned off.

[Model-dependent variations]

None

See program example and print sample for ESC %, ESC &amp;, and ESC ? .

SETTING COMMAND
