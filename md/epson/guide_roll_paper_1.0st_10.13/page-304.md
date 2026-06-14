## **C O N F I D E N T I A L** 

- After processing this command, the printer executes a software reset. Therefore, processing this command enables the printer to be in the correct status when the power is turned on. 

## ■ The limitations during processing of this command are as follows: 

   - Even if the PAPER FEED button is pressed, the printer does not feed paper. 

   - The real-time commands are not processed. 

   - Even if the ASB function is effective, the ASB status cannot be transmitted. 

- The NV bit image is printed by FS p. 

## ■ Bit image data and print result are as follows: 

|d1|dY+1|...|.<br>.|MSB<br>LSB<br>MSB<br>LSB<br>MSB<br>LSB<br>MSB<br>LSBY=yL+yH ×256|
|---|---|---|---|---|
|d2|dY+2|...|dk-2||
|.<br>.|.<br>.|...|dk-1||
|dY|dY×2|...|dk||



- Data is written to the non-volatile memory by this command. Note the following when using this command. 

   - Do not turn off the power or reset the printer from the interface when this command is being executed. 

   - The printer is BUSY when writing the data to the non-volatile memory. In this case, be sure not to transmit data from the host because the printer does not receive data. 

   - Excessive use of this function may destroy the non-volatile memory. As a guideline, do not use any combination of the following commands more than 10 times per day for writing data to the nonvolatile memory: GS ( A (part of functions), GS ( C (part of functions), GS ( E (part of functions), GS ( L / GS 8 L (part of functions), GS ( M (part of functions), GS g 0, FS g 1 ,FS q. 
