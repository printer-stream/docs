**ESC * r e s NUL** [Name] Set/cancel data intake mode [Code] ASCII ESC * r e s NUL Hexadecimal 1B 2A 72 65 s 00 Decimal 27 42 114 101 s 0 

[Defined Area] s = 33H, 34H [Function] This command is run when reading from the reception buffer. Processes for document start and end according to the s parameter. 

n is a decimal (max. 255 digits) using ASCII characters. 

|s|Name|Function|
|---|---|---|
|33H|Start document|(1) Sets data intake mode<br>(2) Initialize|
|34H|End document|(1) Prints data in line buffer, if data exists.<br>(2) Waits until printing ends (motor stops).<br>(3) Cancels data intake mode|



(1)  Receive and discard all data being received. 

(Document start command) 

(2) Receive and discard only the current page. (Document start command + document end command) 

If there is an error after receiving the document start command, reception data is received and discarded until the document end command is received when the printer is recovered from the error. If the document end command cannot be recognized, all reception data is destroyed. Timeouts are two seconds. Automatically cancels the data intake mode. 

Restrictions 

1) Sleep mode decrease 

2) Invalid when in Page mode 

When s = 33H, initialize the following settings using the initializing process. 

• Left/right margins 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-83 
