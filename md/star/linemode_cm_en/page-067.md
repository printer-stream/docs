**ESC GS EM DC1 m n1 n2** 

|[Name]|External buzzer drive pulse condition settings|External buzzer drive pulse condition settings|External buzzer drive pulse condition settings|External buzzer drive pulse condition settings||
|---|---|---|---|---|---|
|[Code]|ASCII|ESC GS EM DC1|m|n1|n2|
||Hex.|1B<br>1D<br>19<br>11|m|n1|n2|
||Decimal|Decimal<br>27<br>29<br>25<br>17|m|n1|n2|
|[Defined Area]||1≤<br> m≤<br> 2<br>49≤<br>|m≤<br>|50||
|||0≤<br> n1≤<br> 255||||
|||0≤<br> n2≤<br> 255||||
|[Initial Value]||n1=0<br>n2=0||||
|[Function]||Sets external buzzer derive pulse condition.||||
|||m specifies the buzzer drive terminal toperform the condition settings.||||
||m|Buzzer DriveTerminal||||
||1, 49|Buzzer Drive Terminal 1||||
||2, 50|Buzzer DriveTerminal 2||||



n1 specifies the energizing time; n2 specifies the delay time. 

- Energizing time: =20msec x n1 

- Delay time: =20msec x n2 

Drives for external buzzers set using this command is performed by <ESC> <GS> <EM> <DC2> m n1 n2. The setting value is not initialized by <ESC> “@” and <CAN>. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-49 
