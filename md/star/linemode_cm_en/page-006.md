## **1.1.3. Communic ation Protocol** 

## 1)  General description of operations in the DTR mode 

This mode abides by the DIP switch settings.  (Ex-factory settings) 

This mode performs communication while handshaking with the DTR signals.  In the operations to receive printer data, this mode controls the DTR signals by confirming the BUSY signal.  A SPACE indicates that the printer is ready to receive data; conversely, a “mark” indicates that the printer cannot receive data. 

**==> picture [383 x 239] intentionally omitted <==**

**----- Start of picture text -----**<br>
<When ON-LINE><br>    RXD     DATA                             DATA                          DATA<br>    DTR<br>Printing<br>Power ON     Buffer full               Buffer empty<br><When out of paper><br>    RXD                                  OFF-LINE                                                          ON-LINE<br>    DTR                                                                                                             ON-LINE Recovery<br>Printing                  Out of paper<br>No paper signal<br>                      Power ON<br>**----- End of picture text -----**<br>


If there is no printer error after turning ON the power, the DTR signal line is set to a SPACE.  When the host computer confirms that the DTR signal line is a SPACE, it sends the data text to the RXD signal line.  The printer sets the DTR signal line to a “Mark” after the empty area of the data buffer reaches a maximum of 256 bytes.  When the host computer confirms that the DTR signal line is a Mark, it stops the transmission of data text to the printer buffer, but at this point as well, the printer is still capable of receiving data, up to the amount of empty space in the data buffer.  If the host computer ignores the DTR signal and transmits data, all data exceeding the amount of space in the data buffer is simply discarded.  The printer sets the DTR signal line to SPACE again when the amount of empty space in the data buffer increased because of the printing and the data in the buffer is a maximum of 256 bytes.  As the empty area in the data buffer increases because of printing, the printer sets the DTR signal line to “SPACE.” 

## 2)  Buffer full/Buffer full cancel in the DTR mode 

|Empty area: 256 bytes|Empty area: 512 bytes||
|---|---|---|
|DTR "Mark"                                                                           DTR "SPACE"|DTR "Mark"                                                                           DTR "SPACE"|DTR "Mark"                                                                           DTR "SPACE"|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 1-2 
