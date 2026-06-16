## XON/XOFF

Whe n XON/XOFF co nt rol i s selec t ed, t he pr int er t ra n sm it s t he XON or XOFF s ign als as follows. The t ra n sm i ss i o n ti m ing of XON/XOFF d i ffers, depe n d ing o n t he se tting of DIP sw it ch 2-1.

| Signal   | Printer status                                                                            | DIP switch 2-1   | DIP switch 2-1   |
|----------|-------------------------------------------------------------------------------------------|------------------|------------------|
| Signal   | Printer status                                                                            | 1 (ON)           | 0 (OFF)          |
| XON      | 1) When the printer goes online after turning on the power (or reset using the interface) | Transmit         | Transmit         |
| XON      | 2) When the receive buffer is released from the buffer full state                         | Transmit         | Transmit         |
| XON      | 3) When the printer switches from offline to online                                       | -                | Transmit         |
| XON      | 4) When the printer recovers from an error using some ESC/POS commands                    | -                | Transmit         |
| XOFF     | 5) When the receive buffer becomes full                                                   | Transmit         | Transmit         |
| XOFF     | 6) When the printer switches from online to offline                                       | -                | Transmit         |

## Code

The hexadec i mal nu mbers correspo n d ing t o t he XON/XOFF codes are show n below.

- XON code: 11H

- XOFF code: 13H

<!-- image -->

- When the printer goes from offline to online and the receive buffer is full, XON is not transmitted.
- When the printer goes from online to offline and the receive buffer is full, XOFF is not transmitted.
- When DIP switch 1-3 is off, XON is not transmitted as long as the printer is offline, even if a receive buffer full state has been cleared.
