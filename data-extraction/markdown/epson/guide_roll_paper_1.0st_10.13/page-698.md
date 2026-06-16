## C O N F I D E N T I A L

- Excessive use of this function may destroy the non-volatile memory. As a guideline, do not use any combination of the following commands more than 10 times per day for writing data to the nonvolatile memory: GS ( A (part of functions), GS ( C (part of functions), GS ( E (part of functions), GS ( L / GS 8 L (part of functions), GS ( M (part of functions) , GS g 0 , FS g 1 , FS q .

## [Notes for transmission process]

- ■ Data is transmitted by Functions 1, 4, 6, 12, 14 and 50. When you use these functions, obey the following rules.
- When the host PC transmits the function data, transmit the next data after receiving the corresponding data from the printer.
- With a serial interface printer, be sure to use this function when the host can receive data.
- With a parallel interface printer, data transmitted (excluding ASB status) with this command ('Header to NUL') is temporarily stored in the printer transmit buffer, as with other data. When the host goes into reverse mode, the printer then transmits the data sequentially from the beginning of the transmit buffer. Transmit buffer capacity is 99 bytes. Data exceeding this amount is lost. Therefore, when using this command, promptly change into reverse mode to start the data receive process.
- When communication with the printer uses XON/XOFF control with serial interface, the XOFF code may interrupt the 'Header to NUL' data string.
- The transmission information for each function can be identified to other transmission data according to specific data of the transmission data block. When the header transmitted by the printer is [hex = 37H/decimal =55], treat NUL [hex = 00H/decimal =0] as a data group and identify it according to the combination of the header and the identifier.

## [Notes for ESC/POS Handshaking Protocol]

- ■ Use ESC/POS Handshaking Protocol below for Functions 14.

|   Step | Host process                 | Printer process                                                        |
|--------|------------------------------|------------------------------------------------------------------------|
|      1 | Send GS ( C < Function 14 >. | Start processing of Function 14. (Read specified record back to host.) |
|      2 | Receive data from printer.   | Send device data.                                                      |
|      3 | Send response code. (*1)     | Continue processing (*2) (*3) according to response.                   |
