## **ESC * r V m n NUL** 

[Name] Execute external buzzer drive [Code] ASCII ESC * r V m n NUL Hex. 1B 2A 72 56 m n 0 Decimal 27 42 114 86 4m n 0 [Defined Area] m=49,50 1≤n≤20 [Initial Value] - - - [Function] Repeatedly drives the buzzer according to the ON/OFF conditions set by the external buzzer drive pulse conditions command <ESC> <GS> <EM> <DC1> m n1 n2. 

||m specifies the buzzer drive terminal to drive.|m specifies the buzzer drive terminal to drive.|
|---|---|---|
|m|m|Buzzer DriveTerminal|
|49||Buzzer DriveTerminal 1|
|50||Buzzer DriveTerminal 2|



Specifies the number of repetitions of the buzzer drive with n. The buzzer will not ring while printing. 

This command is prohibited for uses other than to ring the buzzer. 

(If this command is used to drive the cash drawer on models that have an external device terminal, the system will be damaged. Absolutely never use it for other purposes.) 

The buzzer can be stopped by pressing the paper feed switch or opening the cover when it is ringing. 

Conditions must not be set in advance with the external buzzer drive pulse condition command <ESC> <GS> <EM> <DC1> m n1 n2 prior to entering the raster mode. 

n is expressed in decimal (maximum 255 digits) using ASCII characters. Invalid in page mode. 

Example: 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-82 
