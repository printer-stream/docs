## **ESC GS BEL m t1 t2** 

|[Name]|Ring buzzer|Ring buzzer||||||
|---|---|---|---|---|---|---|---|
|[Code]|ASCII|ESC|GS BEL||m|t1|t2|
||Hex.|1B|1D|07|m|t1|t2|
||Decimal|27|29|7|m|t1|t2|
|[Defined Area]||1≤<br>m≤<br>2, 49≤<br>m≤<br>50 (”1”≤<br>m≤<br>“2”)||||||
|||1≤<br>t1≤<br>255|255|||||
|||1≤<br>t2≤<br>255|255|||||
|[Initial Value]||- - -||||||
|[Function]|[Function]|Rings the buzzer.|Rings the buzzer.|||||
|||m specifies the drive terminal of the buzzer.|||m specifies the drive terminal of the buzzer.|||



|m|Buzzer DriveTerminal|
|---|---|
|1, 49|Buzzer Drive Terminal 1|
|2, 50|Buzzer DriveTerminal 2|



t1 specifies energizing time; t2 specifies the delay time. 

• Energizing time = 20 msec x t1 

• Delay time = 20 msec x t2 The buzzer will not ring while printing. Use of this command other than for ringing the buzzer is prohibited. (There is the possibility of damage if using this command for driving the drawer on models that support external device terminals.) 

ON Drive Pulse OFF 20 × t1 (msec) 20 × t2 (msec) (Energizing Time) (Delay Time) Print Operation Lo Printing and Paper Feed Prohibited 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-48 
