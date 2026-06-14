## **5.1.4. Co de 128** 

These are bar code symbols that can print ASCII 128 characters.  For that reason, use thereof is increasing. 

1.  Each module and module width 

|Items|Mode1|Mode2|Mode 3|
|---|---|---|---|
|ModuleWidth|2dots|3 dots|4dots|
|Length of 1<br>Character(*)|2.75 mm|4.125 mm|5.5 mm|



(*) Start and stop bars not included. 

## 2.  Regulations 

When using <LF> with the command, control codes are not sent by the host PC, so the control codes are sent as data, as shown below. 

- When sending the following data, it represents a 2 character set. 

- % (25H) represents %0 (25H 30H). 

Control codes (00H to 1FH) represent 40H to 5FH applied behind %. Control code (7FH) represents %5 (25H 35H). 

Function codes represent 1 to 4 (31H to 34H) applied behind %. Start codes represent 6 to 8 (36H to 38H) applied behind %. 

- Stop code (SC)/Check character (CK) are automatically applied. 

- When start code is omitted: 

Uses START C when more than 4 digits continue after header. 

Uses START A when initial data other than numbers are the control code. 

Uses START B for other cases. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-3 
