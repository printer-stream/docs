2. Unscrew the screw to remove the DIP switch cover from the base of the printer.
3. Set the DIP switches as desired, using the tip of a tool, such as a small screwdriver.
4. Attach the DIP switch cover, and screw in place.

Figure 2-2  Removing the DIP switch cover

<!-- image -->

<!-- image -->

New DIP switch settings are enabled after the printer is turned on.

## 2.2.2  DIP Switch Functions

The DIP switch functions depend on your printer's interface specifications.

## 2.2.2.1  DIP switch settings for serial interface specifications

Note that the functions of DIP SW1-7, 1-8, and 2-5 differ on the TM-T88II and TM-88III. (The functions of other DIP switch settings are the same.)

<!-- image -->

Table 2-1  Switch bank 1 settings

| SW       | Function                                                                                                                         | ON                                                                                                                               | OFF                                                                                                                              |
|----------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| 1-1      | Data receive error                                                                                                               | Ignore                                                                                                                           | ' ? ' is printed *                                                                                                               |
| 1-2      | Receive buffer size                                                                                                              | 45 bytes                                                                                                                         | 4KB *                                                                                                                            |
| 1-3      | Handshake                                                                                                                        | XON/XOFF                                                                                                                         | DTR/DSR *                                                                                                                        |
| 1-4      | Bit length                                                                                                                       | 7 bits                                                                                                                           | 8 bits *                                                                                                                         |
| 1-5      | Parity check                                                                                                                     | Yes                                                                                                                              | No *                                                                                                                             |
| 1-6      | Parity selection                                                                                                                 | Even                                                                                                                             | Odd *                                                                                                                            |
| 1-7, 1-8 | Baud rate selection (See the 'Baud rate selection' tables below. (Note that the settings differ on the TM-T88II and TM-T88III.)) | Baud rate selection (See the 'Baud rate selection' tables below. (Note that the settings differ on the TM-T88II and TM-T88III.)) | Baud rate selection (See the 'Baud rate selection' tables below. (Note that the settings differ on the TM-T88II and TM-T88III.)) |

For details on DIP SW1-2: Receive buffer size, also refer to DIP SW2-5: Cancellation of receive buffer full BUSY state.
