Rev.2.52 

## **4-3-8 STAR Original Buzzer Commands** 

## **ESC GS BEL m t1 t2** 

Name Ring buzzer Code ASCII ESC GS BEL m t1 t2 Hex. 1B 1D 07 m t1 t2 Decimal 27 29 7 m t1 t2 1 ≤ m ≤ 2 Defined Area 1 ≤ t1 ≤ 255 1 ≤ t2 ≤ 255 Initial Value - - - Function Rings the buzzer. 

m specifies the drive terminal of the buzzer. 

|Function|Rings the buzzer.<br>m specifes the drive terminal of the buzzer.|
|---|---|
|m|Buzzer Drive Terminal|
|1,49|Buzzer Drive Terminal 1|
|2,50|Buzzer Drive Terminal 2|



t1 specifies energizing time; t2 specifies the delay time. 

- Energizing time = 20 msec x t1 

- Delay time = 20 msec x t2 

The buzzer will not ring while printing. 

Use of this command other than for ringing the buzzer is prohibited. 

(There is the possibility of damage if using this command for driving the drawer on models that support external device terminals.) 

**==> picture [334 x 110] intentionally omitted <==**

**----- Start of picture text -----**<br>
ON<br>Drive Pulse<br>OFF<br>20 × t1 (msec)  20 × t2 (msec)<br>(Energizing Time) (Delay Time)<br>Print Operation   Printing and Paper Feed Prohibited<br>**----- End of picture text -----**<br>


ESC/POS Command Specifications 

216 
