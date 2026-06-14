Rev.2.52 

## **ESC GS SUB DC3 m t1 t2** 

Name Execute snout LED operation Code ASCII ESC GS SUB DC2 m t1 t2 Hex. 1B   1D  1A   13   m  t1  t2 Decimal 27   29  26   19   m  t1  t2 

Defined Region 1 ≤ m ≤ 2, 49 ≤ m ≤ 50 0 ≤ t1 ≤ 255, 0 ≤ t2 ≤ 255 

|Defned Region<br>1 ≤ m ≤ 2, 49 ≤ m ≤ 50<br>0 ≤ t1 ≤ 255, 0 ≤ t2 ≤ 255|Defned Region<br>1 ≤ m ≤ 2, 49 ≤ m ≤ 50<br>0 ≤ t1 ≤ 255, 0 ≤ t2 ≤ 255|
|---|---|
|Initial Value<br>---<br>Function<br>Operate the snout LED.<br>m specifes the snout LED output terminal.||
|m|LED output terminal|
|1,49|Externaloutput terminal 1|
|2, 50|Externaloutput terminal 2|



t1 specifies the ON time for the snout LED operation. When 1 ≤ t1 ≤ 255: ON time = t1 x 50 msec When t1 = 0 When ON time is default value (Default =2 x 50 msec) t2 specifies the OFF time for the snout LED operation. When 1 ≤ t2 ≤ 255: OFF time = t2 x 50 msec When t2 = 0: When OFF time is default value (Default =2 x 50 msec) This command is valid when a presenter is connected. When the snout is not connected, this command is prohibited from use. This command has priority if received while operating the snout LED in the operation mode specified by the 

Reference ESC GS SUB DC2 , ESC GS SUB DC3 

ESC/POS Command Specifications 

199 
