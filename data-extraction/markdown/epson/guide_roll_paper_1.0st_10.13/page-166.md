## C O N F I D E N T I A L

| n: Bit   | Off/On   | Hex   | Decimal   | Function                        |
|----------|----------|-------|-----------|---------------------------------|
| 3        | Off      | 00    | 0         | Roll paper end sensor disabled. |
|          | On       | 08    | 8         | Roll paper end sensor enabled.  |
| 4-7      | -        | -     | -         | Undefined.                      |

## [Notes]

- ■ This command is enabled only with a parallel interface and is ignored with a serial interface.
- ■ The roll paper near-end sensor is enabled when either bit 0 or bit 1 is on or both are on.
- ■ The roll paper end sensor is enabled when either bit 2 or bit 3 is on or both are on.
- ■ It is possible to select multiple sensors to output signals. When any of the sensors detects a paper-end, the paper-end signal is output.
- ■ When all sensors are disabled, the paper-end signal is always paper present.
- ■ Some sensors are not present, depending on the printer model.
- ■ The names of some sensors differ, depending on the printer model.
- ■ The settings of this command are effective until ESC @ is executed, the printer is reset, or the power is turned off.

[Model-dependent variations]

## TM-T90 , TM-U220

## Program Example for all printers

PRINT #1, CHR$(&amp;H1B);"c3";CHR$(4); ← Roll paper end sensor enabled

## TM-T90

The memory switch can be set by Function 3 of GS ( E .

## TM-U220

The roll paper near-end sensor is an option. If the roll paper near-end sensor is not included, this printer does not detect a roll paper near-end.
