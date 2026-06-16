## Drawer Circuitry

<!-- image -->

## Setting the Buzzer

Models w it h t he b u zzer f un c ti o n ca n beep t he b u zzer whe n t he drawer i s ope n ed.

The b u zzer se tting i s performed by se tting t he DIP sw it ches for t he b u zzer a n d spec i fy ing co nn ec t or p in nu mbers t o wh i ch a comma n d o ut p ut s a p u lse s ign al.

|   DIP switch | Specified connector pin         | ON            | OFF                   | Initial setting   |
|--------------|---------------------------------|---------------|-----------------------|-------------------|
|            1 | Drawer kick out connector pin 2 | Buzzer beeps. | Buzzer does not beep. | ON                |
|            2 | Drawer kick out connector pin 5 | Buzzer beeps. | Buzzer does not beep. | OFF               |

<!-- image -->

Since the buzzer drive signal and the cash drawer drive signal are common in the printer, do not use the same connector pin numbers to output the signal for the buzzer and the cash drawer.

For detailed information about ESC/POS commands, see the ESC/POS Application Programing Guide.
