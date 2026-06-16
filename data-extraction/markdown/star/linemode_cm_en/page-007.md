<!-- image -->

## 3)  General description of operations in the XON/XOFF mode

This mode is set when DIPSW #1 to #3 are turned OFF.  This mode notifies the host of the XON (DC1) data when the printer can receive data and the XOFF (DC3) data when the printer cannot receive data, using the TXD signals.

This functions so that XON outputs only 1 byte when the printer shifts from OFFLINE (printer busy) to ONLINE (printer ready) and; XOFF outputs 1 byte when the printer shifts from ONLINE (printer ready) to OFFLINE (printer busy) .

<!-- image -->

If there is no error after turning the power ON, XON (control code name: DC1; Hexadecimal name: 11H) is output by the TXD signal line.  After the host computer receives the XON, it sends the data text to the RXD signal line.  XOFF (DC 3; 13H) is output when the empty space in the data buffer is a maximum of 256 bytes.  The host computer stops sending data text when it receives the XOFF, however, the printer is capable of receiving data at that time for the amount of empty space in the data buffer.  Data exceeding the amount of empty space is discarded.  As the empty space in the data buffer increases through printing, XON is output when the data in the buffer is a maximum of 256 bytes.  When the empty area of the data buffer increases because of printing, the printer outputs XON.

## 4)  Buffer full/Buffer full cancel in the XON/XOFF mode

<!-- image -->

-----------------------------------------------------------------------------
