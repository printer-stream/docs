## Selecting the BUSY Status

W it h DIP sw it ch 2-1, yo u ca n selec t co n d iti o n s for in vok ing a BUSY s t a t e as e it her of t he follow ing :

- Whe n t he rece i ve b u ffer i s f u ll
- Whe n t he rece i ve b u ffer i s f u ll or t he pr int er i s offl in e

<!-- image -->

In either case above, the printer enters the BUSY state after power is turned on (including resetting with the interface), and when a self-test is being run.

## Printer BUSY condition and status of DIP switch 2-1

| Printer status              | Printer status                                                                                                                    | DIP SW 2-1   | DIP SW 2-1   |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------|--------------|
|                             |                                                                                                                                   | ON           | OFF          |
| Offline                     | During the period after power is turned on (including resetting with the interface) to when the printer is ready to receive data. | BUSY         | BUSY         |
|                             | During the self-test.                                                                                                             | BUSY         | BUSY         |
|                             | When the cover is open.                                                                                                           | -            | BUSY         |
|                             | During paper feed with the FEED button.                                                                                           | -            | BUSY         |
|                             | When the printer stops printing due to a paper- end (when printer has run out of roll paper).                                     | -            | BUSY         |
|                             | When an error has occurred.                                                                                                       | -            | BUSY         |
| When an error has occurred. | When an error has occurred.                                                                                                       | BUSY         | BUSY         |

If DIP switch 2-1 is on, the printer will not become BUSY

- When error has occurred
- When the cover is open
- When printing has stopped for a paper out
- When paper is fed by the FEED button
