## C O N F I D E N T I A L

## GS D

[Name]

Specify Windows BMP graphics data

[Printers not featuring this command] TM-U230 , TM-U220 , TM-J2000/J2100 , TM-T90 , TM-T88IV , TM-T70 , TM-L90 , TM-P60

[Description]

Processes Windows BMP data.

- Function code ( fn ) specifies the function.
- ■ Frequent write command executions by an NV memory write command may damage the NV memory. Therefore, it is recommended to limit using the commands to no more than 10 times a day.
- ■ If the power is turned off or the printer is reset via an interface while this command is being executed, the printer may go into an abnormal condition. Be careful not to turn the power off or let the printer be reset via an interface while this command is being executed.
- ■ The printer may be BUSY when processing this command and will not receive any data. Therefore, be sure not to transmit data.

|   fn | Function No.   | Function name                              |
|------|----------------|--------------------------------------------|
|   67 | Function 67    | Define Windows BMP NV graphics data.       |
|   83 | Function 83    | Define Windows BMP download graphics data. |

## [Notes]

EXECUTING + SETTING
