## C O N F I D E N T I A L

## ESC p

```
[Name] Generate pulse [Format] ASCII ESC p m t1 t2 Hex 1B 70 m t1 t2 Decimal 27 112 m t1 t2 [Range] m = 0, 1, 48, 49 0 ≤ t1 ≤ 255 0 ≤ t2 ≤ 255 [Default] None
```

[Printers not featuring this command] TM-P60

[Description]

Outputs the pulse specified by t1 and t2 to the specified connector pin m as follows:

| m     | Connector pin                   |
|-------|---------------------------------|
| 0, 48 | Drawer kick-out connector pin 2 |
| 1, 49 | Drawer kick-out connector pin 5 |

- The pulse for ON time is ( t1 × 2 msec) and for OFF time is ( t2 × 2 msec).

[Notes]

- ■ If t2 &lt; t1 , the OFF time is equal to the ON time.

[Model-dependent variations]

TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-U230 , TM-U220

```
Program Example for all printers PRINT #1, CHR$(&H1B);"p";CHR$(0);CHR$(25);CHR$(250);
```

## TM-T20

The BUSY condition is selected by memory switch 1-3.

When the optional external buzzer is enabled with GS ( E &lt;Function 5&gt;, the optional external buzzer sounds (a pulse signal is not output).

EXECUTING COMMAND
