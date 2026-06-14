Rev.2.52 

## **GS ^ r t m** 

|**GS^ r t m**||
|---|---|
|Name|Execute macro|
|Code|ASCII<br>GS<br>^<br>r<br>t<br>m|
||Hex.<br>1D<br>5E<br>r<br>t<br>m|
||Decimal<br>29<br>94<br>r<br>t<br>m|
|Defned Region|0≤r≤255|
||0≤t≤255|
||0≤m≤1|
|Function|• Executes a defned macro.|
||r specifes the number of times to execute the macro.|
||t specifes the time to wait when executing the macro.|
||m specifes the macro execution mode.|
||m = 0: Executes the macro continuously the r number of times while interposing time gaps<br>specifed by t.|
||m = 1: After an amount of time specifed by t, the POWER LED fashes and waits for the|
||paper feed switch to be pressed.|
||The macro is executed once when the paper feed switch is pressed.|
||This operation is repeated the number of times specifed by r.|
|Details|• After executing a macro once, the printer waits approximately (t x 100 m) sec according to<br>that specifed by t.|
||• When processing this command while defning a macro, the macro defnition is terminated<br>and the contents of the defnition are cleared.|
||• When a macro is undefned, and r = 0, this command is ignored.|
||• When m = 1, paper is not fed using the paper feed switch while the macro is being executed.|
|STAR|• If a raster graphic command (GS v) is received while executing a macro on a printer|
||equipped with a parallel interface, the user should be aware that the printer will enter aBUSY|
||state.|
|Reference|GS :|



ESC/POS Command Specifications 

145 
