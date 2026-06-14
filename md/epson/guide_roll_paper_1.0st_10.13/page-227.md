## **C O N F I D E N T I A L** 

   - Do not turn off the power or reset the printer from the interface when the relevant functions are being executed. 

   - The printer may be BUSY when storing data and will not receive any data. In this case, be sure not to transmit data from the host. 

   - Excessive use of this function may destroy the non-volatile memory. As a guideline, do not use any combination of the following commands more than 10 times per day for writing data to the nonvolatile memory: GS ( A (part of functions), GS ( C (part of functions), GS ( E (part of functions), GS ( L / GS 8 L (part of functions), GS ( M (part of functions), GS g 0, FS q 1, FS q. 

- The following restrictions apply when performing non-volatile memory operations (including data store and delete). 

   - The paper cannot be fed by paper feed switch. 

   - The real time command is not processed. 

   - The ASB status will not be sent, even when the ASB function is set to enable. 

[Notes for transmission process] 

- Data send operations are performed using Functions 48, 51, 52, 64, and 80. When you use these functions, obey the following rules. 

   - When the host PC transmits the function data, transmit the next data after receiving the corresponding data (Header ~ NULL) from the printer. 

   - When operating with a serial interface, be sure to configure operation so that the host computer uses the printer only when it is READY. 

   - When operating with a parallel interface, the data sent by this function (starting with Header and ending with NUL), as with other data, is first stored in the send buffer, then output in sequential order when the host computer changes to the reverse mode. Note that the send buffer capacity is 99 bytes, and any data exceeding this volume limit will be lost; therefore, when using this command, it is important to configure the operation so that the host computer’s change to the reverse mode and the subsequent status send/receive process is performed quickly. 

- During the interval between the sending of the data header and NUL, ASB status and the real time commands are rendered invalid. 
