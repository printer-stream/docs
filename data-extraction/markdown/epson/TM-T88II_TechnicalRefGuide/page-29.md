## Stand alone

Both the TM printer and DM-D are connected to the host computer directly via the serial port.

| Application control TM side control setting   |   Application control TM side control setting | XON/XOFF (except OPOS)                 | DTR/DSR (DOS, OPOS, Visual C)   | RTS/CTS (DOS, Windows driver, Visual C, Visual Basic MSComm)   |
|-----------------------------------------------|-----------------------------------------------|----------------------------------------|---------------------------------|----------------------------------------------------------------|
| XON/XOFF                                      |                                             1 | Type A or B                            | -                               | -                                                              |
|                                               |                                             2 | DM-D500: A, B Other DM-D: not possible | -                               | -                                                              |
| DTR/DSR                                       |                                             1 | -                                      | Type A or B                     | Type B                                                         |
|                                               |                                             2 | -                                      | Type A or B                     | Type B                                                         |

Figure 2-5  Configuration of stand-alone connection

<!-- image -->

## Pass-through connection

The host computer is connected to the TM printer over the serial interface via DM-D.

| Application control TM side control setting   | Application control TM side control setting   | XON/XOFF (except OPOS)   | DTR/DSR (DOS, OPOS, Visual C)   | RTS/CTS (DOS, Windows driver, Visual C, Visual Basic MSComm)   |
|-----------------------------------------------|-----------------------------------------------|--------------------------|---------------------------------|----------------------------------------------------------------|
| XON/XOFF                                      | XON/XOFF                                      | Not possible             | -                               | -                                                              |
| DTR/DSR                                       | 1                                             | -                        | Type A or B                     | Type B                                                         |
|                                               | 2                                             | -                        | Type A or B                     | Type A or B                                                    |

Figure 2-6  Configuration of pass-though connection

<!-- image -->
