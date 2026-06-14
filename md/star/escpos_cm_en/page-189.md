Rev.2.52 

## **ESC GS ETX s n1 n2** 

Name Send print-end counter, initialize 

Code 

Code ASCII ESC GS ETX s n1 n2 Hex. 1B 1D 03 s n1 n2 Decimal 27 29 3 s n1 n2 Defined Region Spec. A: 0 ≤ s ≤ 2 Spec. B: 0 ≤ s ≤ 4 Spec. C: 0 ≤ s ≤ 5 0 ≤ n1 ≤ 255, 0 ≤ n2 ≤ 255 

Function This command is run when reading from the reception buffer. Processes the print end counter according to the s parameter. 

|s|Name|Function|
|---|---|---|
|0|Print end counter reference|Sends the current print end counter to the host.<br>(Does not wait forprint end. Does not count up.)|
|1|Print end counter update|Runs the next operation.<br>(1) Prints data in line bufer, if data exists.<br>(2) Waits until printing ends (motor stops).<br>(3) Updates print end counter (+1)<br>(4)Sendsprint end counter to host.|
|2|Print end counter clear|Returns the print end counter to its default value (zero clear).<br>(Does not wait for print end. Does not send the print end counter<br>to the host.|
|3|Start document<br>n1, n2 = 0|(1) Sets data intake mode<br>(2) Initialize|
|4|End document<br>n1, n2 = 0|(1) Prints data in line bufer, if data exists.<br>(2) Waits until printing ends (motor stops).<br>(3)Cancels data intake mode|
|5|Data timeout setting|n1=0 : Initializes to the content of MSW. (n2=0)<br>n1=1 : Data timeout setting<br>n2=0: Timeout disabled<br>Others: n2 = Data timeout time (units: seconds 1 to 255 seconds)<br>n1=2 : Sends the current timeout settingto the host.(n2=0)|



When s = 0, or s = 1 is specified, the data format returned to the host is as shown below. 

<Returned Data Formats> 

|Code|ASCII|ESC|GS|ETX|s|n1|n2|[Print end counter]|NUL|
|---|---|---|---|---|---|---|---|---|---|
||Hex.|1B|1D|03|s|n1|n2|[Print end counter]|00|
||Decimal|27|29|3|s|n1|n2|[Print end counter]|0|



* Echoes back the specified contents from the host as is until ESC GS ETX s n1 n2, and then sends the print end counter value and NUL. 

When [Print end counter] is 1 byte in length, the initial value is 0x00. 

When s = 1, increments by 1 each time the command is processed. After 0xFF, returns to 0x00. 

There is one [Print end counter] in the printer that is unrelated to the n1, n2 values. 

(There is no counter for the n1, n2 values.) 

ESC/POS Command Specifications 

189 
