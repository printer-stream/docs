A computer must issue special commands to initiate and terminate a serial poll. During a serial poll, a device must be instructed to talk and the computer to listen. Therefore, a serial poll cannot be executed when a plotter is in listen-only mode. 

## The Parallel Poll 

**==> picture [343 x 263] intentionally omitted <==**

**----- Start of picture text -----**<br>
Parallel polling can only be done to plotters with an address 0 through<br>7. Plotters with address settings from 8 through 30 cannot respond to a<br>parallel poll. The plotter will respond positively to a parallel poll only if<br>the conditions specified in the P-mask are satisfied and parallel poll<br>response is enabled. The P-mask parameter of the input mask instruc-<br>tion, IM, is used to specify which status byte conditions will result in a<br>logical 1 response to a parallel poll. The response to a parallel poll is<br>limited to setting the appropriate data line to a logical 1. The line used<br>is determined by the plotter’s address value as shown in the table below: —<br>Plotter ;{ Parallel Poll | HP-IB Data<br>Address | Bit Position | Line Number<br>078<br>16 7<br>256<br>34 5<br>po 64|BB3J 42 | Plotter Preset Address<br>7 0 1<br>**----- End of picture text -----**<br>


To execute a parallel poll, the controller sets the ATN and EOI lines to 1. The controller reads the eight data lines, and determines from these lines which instrument on the bus is requesting service. The computer then sends the parallel poll disable command. Not all computers have parallel poll capability. 

It is important to remember that the 7470 will not send a logical 1 unless the P-mask bit value has been changed from the default value of 0 and some condition included in the new P-mask value is true. The plotter does not respond to a parallel poll in listen-only mode. 

Positive responses to parallel polls will continue to occur until all bits of the status byte included in the P-mask value have been reset to 0. (See The Output Status Instruction, OS, Chapter 7.) 

HP-IBINTERFACING 9-5 
