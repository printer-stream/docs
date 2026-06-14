10 PRINTER IS 705,80 20 OPTION BASE 1 30 INTEGER *(500), (500) ,P(500) 40 FOR C=1 TO 500 50 PRINT "DP;" 60 DISP “ENTER POINT ";C 70 GOSUB 160 B80 PRINT "OOD;" 9O ENTER 705 ; X(C),Y(C),P(C) 100 NEXT C 110 PRINTER IS 2 120 FOR C=1 TQ 500 130 PRINT (CI; ¥CCI;PCC) 140 NEXT C 150 STOP 160 ! Check SUBROUTINE 170 PRINT "OS;" 180 ENTER 705 ; § 190 S*INT(S/4) 200 IF S=INT(S“2)*2 THEN 170 210 RETURN 220 END 

**==> picture [1 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
;<br>**----- End of picture text -----**<br>


## HP-IB Interrupts and Polling 

A third method can be used by advanced programmers thoroughly familiar with the HP-IB interface, polling techniques, and interrupts. It should only be used when the computer can perform useful tasks while waiting for the digitized point to be entered. This method involves setting a value of 4 in the S-mask of the IM command, e.g., IM 223 ,4,0;: to cause the plotter to generate an RQS (service request) when a digitized point is available. With an interrupt routine enabled for service requests, the computer can send a DP command to initiate digitizing, and then proceed with some other task until the digitized point is entered. When the point is available, the computer is interrupted by the RQS, and program execution branches to the routine to process the digitized data. This routine could simply send an OD command and read the digitized point, or it could perform bit checking of the plotter status byte if multiple S-:mask values have been specified to generate the RQS. The status byte can be obtained by serial polling or simply by sending an OS command. Because interrupts and polling are highly machine-dependent and beyond the scope of this manual, no examples are given. 

DIGITIZING 6-7 
