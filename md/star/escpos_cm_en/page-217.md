Rev.2.52 

## **ESC GS EM DC1 m n1 n2** 

Name External buzzer drive pulse condition settings Code ASCII ESC GS EM DC1 m n1 n2 Hex. 1B 1D 19 11 m n1 n2 Decimal 27 29 25 17 m n1 n2 1 ≤ m ≤ 2 49 ≤ m ≤ 50 Defined Area 0 ≤ n1 ≤ 255 

1 ≤ n2 ≤ 255 Initial Value n1=0,n2=0 Function Sets external buzzer derive pulse condition. 

m specifies the buzzer drive terminal to perform the condition settings. 

|Function|Sets external buzzer derive pulse condition.<br>m specifes the buzzer drive terminal to perform the condition settings.|
|---|---|
|m|Buzzer Drive Terminal|
|1,49|Buzzer Drive Terminal 1|
|2,50|Buzzer Drive Terminal 2|



n1 specifies the energizing time; n2 specifies the delay time. 

- Energizing time: =20msec x n1 

- Delay time: =20msec x n2 

**==> picture [334 x 110] intentionally omitted <==**

**----- Start of picture text -----**<br>
ON<br>Drive Pulse<br>OFF<br>20 × n1 (msec)  20 × n2 (msec)<br>(Energizing Time) (Delay Time)<br>Print Operation   Printing and Paper Feed Prohibited<br>**----- End of picture text -----**<br>


Drives for external buzzers set using this command is performed by <ESC> <GS> <EM> <DC2> m n1 n2. 

The setting value is not initialized by <ESC> “@” and <CAN>. 

ESC/POS Command Specifications 

217 
