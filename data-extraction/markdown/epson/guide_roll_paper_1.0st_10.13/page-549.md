## C O N F I D E N T I A L

- In the online recovery wait status, the printer recovers by any of the following and the paper is fed to the print starting position:
- The FEED button is pressed.
- The recovery confirmation time ( t2 × 500 msec) has elapsed.
- DLE ENQ ( n = 0) is executed
- ■ During the online recovery time, the paper cannot be fed by pressing the paper feed button.
- ■ When the online recovery time is canceled ( t2 = 0), the printer recovers online by executing DLE ENQ ( n = 0) or pressing the paper feed button.
- ■ When the panel buttons are disabled by ESC c 5 , the paper feed button can be used temporarily during the online recovery wait time.
- ■ The PAPER OUT LED is off when the printer recovers online.
- ■ Online recovery wait time status is checked by the ASB status or DLE EOT ( n =1: Printer status).
- ■ The procedures for online recovery from when the roll paper cover is closed to when the PAPER FEED button is pressed is as follows:

## Print Status:

- ➀ The printer feeds paper to the peeling position. The PAPER OUT LED flashes.
- ➁ The printer recovers online. The PAPER OUT LED is off.

## User Operation:

- ➀ Insert roll paper and close the cover.
- ➁ Insert paper through the peeler. Close the peeler cover. Press the FEED button.
- ■ Supplement print status
- ■ Status ➀ : The printer feeds paper in paper feed direction.
- ■ Printer status ➁ : The printer feeds the paper in either paper feed direction or in the reverse direction.
