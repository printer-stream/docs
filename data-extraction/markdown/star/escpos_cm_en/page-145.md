<!-- image -->

Name

Execute macro

Code

ASCII GS ^ r t m

Hex.

1D 5E r t m

Decimal

29 94 r t m

Defined Region

0 ≤ r ≤ 255

0 ≤ t ≤ 255

0 ≤ m ≤ 1

Function

- Executes a defined macro.

r specifies the number of times to execute the macro.

t specifies the time to wait when executing the macro.

m specifies the macro execution mode.

m = 0: Executes the macro continuously the r number of times while interposing time gaps specified by t.

m = 1: After an amount of time specified by t, the POWER LED flashes and waits for the paper feed switch to be pressed.

The macro is executed once when the paper feed switch is pressed.

This operation is repeated the number of times specified by r.

Details

- After executing a macro once, the printer waits approximately (t x 100 m) sec according to that specified by t.

- When processing this command while defining a macro, the macro definition is terminated and the contents of the definition are cleared.

- When a macro is undefined, and r = 0, this command is ignored.

- When m = 1, paper is not fed using the paper feed switch while the macro is being executed.

STAR

- If a raster graphic command (GS v) is received while executing a macro on a printer equipped with a parallel interface, the user should be aware that the printer will enter a BUSY state.

Reference

GS :
