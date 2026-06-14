**ESC GS EM DC2 m n1 n2** 

|[Name]|External buzzer drive execution|External buzzer drive execution|||||
|---|---|---|---|---|---|---|
|[Code]|ASCII|ESC GS EM DC2|m|n1|n2||
||Hex.|1B<br>1D<br>19<br>12|m|n1|n2||
||Decimal|Decimal<br>27<br>29<br>25<br>18|m|n1|n2||
|[Defined Area]||1≤<br> m≤<br> 2<br>49≤<br>|m≤<br>|50|||
|||1≤<br> n1≤<br> 20|||||
|||n2=0|||||
|[Initial Value]||---|||||
|[Function]||Repeatedly drives the buzzer according to the ON/OFF conditions set by the external buzzer drive|||||
|||pulse conditions command <ESC> <GS> <EM> <DC1> m t1 t2.|||pulse conditions command <ESC> <GS> <EM> <DC1> m t1 t2.||
|||m specifies the buzzer drive terminal to drive.|||||
||m|Buzzer DriveTerminal|||||
||1,49|Buzzer DriveTerminal 1|||||
||2, 50|Buzzer DriveTerminal 2|||||



Specifies the number of repetitions of the buzzer drive with (n2 x 256 + n1). The buzzer will not ring while printing. 

This command is prohibited for uses other than to ring the buzzer. 

(If this command is used to drive the cash drawer on models that have an external device terminal, the system will be damaged. Absolutely never use it for other purposes.) 

The buzzer can be stopped by pressing the paper feed switch or opening the cover when it is ringing. 

Example: 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-50 
