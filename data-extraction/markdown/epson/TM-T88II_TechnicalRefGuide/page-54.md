<!-- image -->

For details on NV graphics and NV bit images, see the 'ESC/POS Application Programming Guide.'

## 4.2  Printer Status

There are three ways to get the printer status, and each method has the following features. For details, see the 'ESC/POS Application Programming Guide.'

When a status request is processed as a regular command, the printer automatically returns a status message whenever the status changes. Always monitor the value

- Automatic status back (ASB): returned.
- Real-time status:

When the printer receives a real-time status command, it responds with the specified printer status. Returning the printer status takes priority over any regular print data.

- Status:
- The printer transmits a specified printer status in the same way it processes normal print

data.

## 4.3  Precautions When the Printer Is Offline

When printer handshake is set with DIP SW2-1 ON (BUSY = receive buffer full), use the ASB function to check the printer status. Using the ASB lets the printer send status automatically at the time of switching online/offline. When using a real-time command, make sure the receive buffer is not full.

Example: After using the 4KB receive buffer to send data for each line, check the printer status.

## 4.4  Outputting Hex Dumps

TM printers can print data transmitted from the host computer as hexadecimal numbers and their corresponding characters. Called 'hex dump mode,' this allows you to make sure that data has been sent correctly to the TM printer by comparing the printed result with the program. Follow the steps below to output a hex dump:

1. With the roll paper cover open, turn power on while holding down the paper FEED button.
2. Close the roll paper cover.
3. Data received from then on is printed out from the TM printer in hexadecimal numbers and their corresponding characters.

To quit the hex dump mode, turn the printer off after printing ends.

<!-- image -->

## Note:

Do not use this mode when using OPOS or the APD. Doing so will cause unexpected data to be printed, because the driver uses proprietary control to drive the printer.
