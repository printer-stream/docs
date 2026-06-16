## C O N F I D E N T I A L

## GS z 0 (TM-L90 w/ Peeler)

[Name]

Set online recovery wait time

[Format]

ASCII GS z 0 t1 t2 Hex 1D 7A 30 t1 t2 Decimal 29 122 48 t1 t2

t1 = 0, 0 ≤ t2 ≤ 255

t1 = 0, t2 = 0

When the peeling issuing mode is selected, sets the online recovery wait time, the wait time for the FEED button to be pressed when the printer goes online (recovery confirmation time), to ( t2 × 500 msec). When t2 = 0, the recovery confirmation time is canceled.

[Range] [Default] [Description]

[Notes]

- ■ when the peeling issuing mode is selected, the settings of this command affect the online recovery wait status described below. The peeling issuing mode and the continuous issuing mode can be selected by a switch. This is a slide switch that can be used when the roll paper cover is open:
- Waiting for the FEED button to be pressed after closing the roll paper cover.
- Waiting for the FEED button to be pressed after removing a label (when the peeling detector cannot detect a label due to sunlight.)
- ■ After the paper roll cover is closed, in the online recovery wait status, the printer executes the following:
- Flashes the PAPER OUT LED and feeds the paper to the peeling position.
- In the online recovery wait status, the printer recovers by any of the following and the paper is fed to the print starting position:
- The FEED button is pressed.

The recovery confirmation time ( t2 × 500 msec) has elapsed.

DLE ENQ ( n = 0) is executed

- ■ In the online recovery wait time when a label is removed, the printer executes the following:
- Flashes the PAPER OUT LED for removing the label (Example: Execution of Function 65 of FS ( L )
- Operators need to remove the label. If the PAPER OUT LED still flashes after the label is removed, the printer is in the wait status for the FEED button to be pressed.

SETTING COMMAND
