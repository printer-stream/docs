## **ESC ? LF NUL** 

[Name] Reset printer (execute self print) [Code] ASCII ESC ? LF NUL Hex. 1B 3F 0A 00 Decimal 27 63 10 0 [Defined Area] - - - [Initial Value] - - - [Function] Hardware resets the printer and executes on self print. 

After sending this command, the next data is not sent until the printer is online (in a state wherein it can receive data). 

When resetting the printer, the following processes are performed. 

|I/F<br>~~a ~~|Mode<br> ~~SC~~|Process<br>~~SC~~|
|---|---|---|
|Parallel<br>~~sss~~<br>~~ee~~|- - -<br>~~sss~~<br>~~a~~<br>|BUSY output<br>~~sss~~<br>|
|RS-232C<br>~~ee~~|DTR mode<br>~~a~~<br>~~T,__H~~|DTR mark output<br>~~T,__H~~|
||Xon/Xoff mode<br>~~a~~<br>~~T,__H~~|Xoffoutput<br>~~T,__H~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-66 
