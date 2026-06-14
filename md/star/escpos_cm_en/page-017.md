Rev.2.52 

## **1-2-5  Precautions When Resetting the Printer Using the Interface** 

When applying a printer reset using the interface (#31 pin nInit signal) in the Compatibility Mode, the following characteristics must be met. However, the printer reset is ignored when the signal nSelectln (pin #36, 1284-Active HIGH) is active in reverse mode. 

**==> picture [327 x 165] intentionally omitted <==**

**----- Start of picture text -----**<br>
Reset Minimum Pulse Width   TRS  50μsec (min)<br>Rise Time   tf  500nsec (max)<br>Fall Time  tr  500nsec (max)<br>nSelectIn<br>(1284-Active)<br>min. 0 max. 1<br>nInit<br>tf TRS tf<br>**----- End of picture text -----**<br>


## **1-2-6 Receiving Status from the Printer Using a Bidirectional Parallel Interface** 

It is possible to transmit the status from the printer using bidirectional communications functions according to the Nibble and Byte Mode which conform to IEEE1284 standards, when using a bidirectional parallel interface.  When doing so, compared to RS-232 serial interface specifications, you must pay attention to the following points because the printer cannot insert real-time interrupts to the host. 

• The transmission buffer size in the printer is 128 bytes.  (Excluding ASB status)  Because statuses that exceed this are discarded, create a receive status (Reverse Mode) on the host side so that status are not lost. 

• When using ASB, it is preferred that the host side be in a receive waiting status (a reverse idle status).  If that is not possible, put the host side into a Reverse Mode to constantly monitor the presence of data. 

• When using ASB, ASB status is transmitted with priority over other statuses in the Reverse Mode.  Also, ASB status that are accumulated without being sent from the last sent ASB status to the latest ASB status ate bundled into one ASB status and transmitted, and the latest ASB status is then transmitted after that. 

Example: The following shows an ASB status in a normal (idled) state. 

|FirstStatus<br>Second Status<br>Third Status<br>FourthStatus|FirstStatus<br>Second Status<br>Third Status<br>FourthStatus|FirstStatus<br>Second Status<br>Third Status<br>FourthStatus|FirstStatus<br>Second Status<br>Third Status<br>FourthStatus|
|---|---|---|---|
|0000<br>1000|0000<br>0000|0000<br>0000|0000<br>0000|



The following data is accumulated when a near end detection occurs, the cover is open and cover close is performed. 

|**1**<br>**2**<br>**3**|First Status<br>Second Status<br>Third Status<br>Fourth Status<br>Near End<br>Detection<br>0000<br>1000<br>0000<br>0000<br>0000<br>0011<br>0000<br>0000<br>Cover<br>Open<br>0010<br>1000<br>0000<br>0000<br>0000<br>0011<br>0000<br>0000<br>Cover<br>Closed<br>0000<br>1000<br>0000<br>0000<br>0000<br>0011<br>0000<br>0000|First Status<br>Second Status<br>Third Status<br>Fourth Status<br>Near End<br>Detection<br>0000<br>1000<br>0000<br>0000<br>0000<br>0011<br>0000<br>0000<br>Cover<br>Open<br>0010<br>1000<br>0000<br>0000<br>0000<br>0011<br>0000<br>0000<br>Cover<br>Closed<br>0000<br>1000<br>0000<br>0000<br>0000<br>0011<br>0000<br>0000|First Status<br>Second Status<br>Third Status<br>Fourth Status<br>Near End<br>Detection<br>0000<br>1000<br>0000<br>0000<br>0000<br>0011<br>0000<br>0000<br>Cover<br>Open<br>0010<br>1000<br>0000<br>0000<br>0000<br>0011<br>0000<br>0000<br>Cover<br>Closed<br>0000<br>1000<br>0000<br>0000<br>0000<br>0011<br>0000<br>0000|First Status<br>Second Status<br>Third Status<br>Fourth Status<br>Near End<br>Detection<br>0000<br>1000<br>0000<br>0000<br>0000<br>0011<br>0000<br>0000<br>Cover<br>Open<br>0010<br>1000<br>0000<br>0000<br>0000<br>0011<br>0000<br>0000<br>Cover<br>Closed<br>0000<br>1000<br>0000<br>0000<br>0000<br>0011<br>0000<br>0000|
|---|---|---|---|---|
||0000<br>1000|0000<br>0000|0000<br>0011|0000<br>0000|



Then, when the ASB status is received, the combination of actually transferred ASB is a total of 8 bytes: ASB (1 + 2 + 3) + the latest ASB (3). 

+ 

|ASB (1 + 2 + 3)<br>Latest ASB (3)||First Status<br>Second Status<br>Third Status<br>Fourth Status<br>0010<br>1000<br>0000<br>0000<br>0000<br>0011<br>0000<br>0000<br>First Status<br>Second Status<br>Third Status<br>Fourth Status|First Status<br>Second Status<br>Third Status<br>Fourth Status<br>0010<br>1000<br>0000<br>0000<br>0000<br>0011<br>0000<br>0000<br>First Status<br>Second Status<br>Third Status<br>Fourth Status|First Status<br>Second Status<br>Third Status<br>Fourth Status<br>0010<br>1000<br>0000<br>0000<br>0000<br>0011<br>0000<br>0000<br>First Status<br>Second Status<br>Third Status<br>Fourth Status|First Status<br>Second Status<br>Third Status<br>Fourth Status<br>0010<br>1000<br>0000<br>0000<br>0000<br>0011<br>0000<br>0000<br>First Status<br>Second Status<br>Third Status<br>Fourth Status|
|---|---|---|---|---|---|
|||0001<br>1000|0000<br>0000|0000<br>0011|0000<br>0000|



ESC/POS Command Specifications 

17 
