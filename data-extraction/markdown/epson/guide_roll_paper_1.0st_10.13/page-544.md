## C O N F I D E N T I A L

- The printer recovers online after the recovery confirmation time ( t2 × 500 msec) has elapsed.
- The printer can be set online by DLE ENQ ( n = 0).
- ■ During recovery confirmation time, the paper cannot be fed by pressing the paper feed button.
- ■ When the recovery confirmation time is canceled ( t2 = 0), the printer recovers online by executing DLE ENQ ( n = 0) or pressing the paper feed button.
- ■ During the paper wait time and recovery confirmation time, if a paper-end is detected, the printer restarts processing from loading a roll paper.
- ■ When the panel buttons are disabled by ESC c 5 , the paper feed button can be used temporarily during the paper wait time and recovery confirmation time.
- ■ The paper out LED is off when the printer recovers online.
- ■ Online recovery wait time status is checked by DLE EOT ( n =1: Printer status).
- ■ The paper out LED and paper feed button are different, depending on the printer model.
