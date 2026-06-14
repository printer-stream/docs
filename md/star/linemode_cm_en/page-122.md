**ESC GS SUB DC1 m t1 t2** 

|**ESC GS SUB DC1 m t1 t2**|**ESC GS SUB DC1 m t1 t2**|**ESC GS SUB DC1 m t1 t2**|**ESC GS SUB DC1 m t1 t2**|**ESC GS SUB DC1 m t1 t2**|||
|---|---|---|---|---|---|---|
|[Name]|Specify snout operation mode||||||
|[Code]|ESC GS SUB DC1<br>m<br>ASCII||||t1|t2|
||1B<br>Hexadecimal|||1D<br>1A<br>11<br>m|t1|t2|
||Decimal<br>27|||29<br>26<br>17<br>m|t1|t2|
|[Defined Area]|||0≤<br> m≤<br>3, 48≤|≤<br> m≤<br> 51 (“0”≤<br> m≤<br> “3”)|||
||||t1 = 0, t2 =0||||
|[Initial Value]|||MSW Setting|MSW Setting|||
|[Function]|[Function]||Specifythe snout operation mode usingthe mparameter.||||
||||m<br>Snout Operating Mode|Snout Operating Mode|||
||||0, 48<br>Snout LED output OFF|Snout LED output OFF|||
||||1, 49<br>Snout LED output ON (while printing, or during presenter operation)|Snout LED output ON (while printing, or during presenter operation)|Snout LED output ON (while printing, or during presenter operation)||
||||2, 50<br>SnoutLED|LEDoutput ON(during an||nerror)|
||||3, 51<br>Snout LED output ON (while printing, or during presenter operation or an error)|Snout LED output ON (while printing, or during presenter operation or an error)|Snout LED output ON (while printing, or during presenter operation or an error)||
||||This command is valid when a presenter is connected.|||This command is valid when a presenter is connected.|
||||When the snout is not connected, this command is prohibited from use.||||



|**ESC GS SUB DC2 m t1 t2**|**ESC GS SUB DC2 m t1 t2**|**ESC GS SUB DC2 m t1 t2**|**ESC GS SUB DC2 m t1 t2**|
|---|---|---|---|
|[Name]|Specify Snout LED ON/OFF|||
|[Code]|ESC GS SUB<br>DC2<br>m<br>t1<br>t2<br>ASCII|||
||1B 1D<br>1A<br>12<br>m<br>t1<br>t2<br>Hexadecimal|||
||Decimal<br>27<br>29<br>26<br>18<br>m<br>t1<br>t2|||
|[Defined Area]|||1≤<br> m≤<br>2, 49≤<br> m≤<br> 50, (“1”≤<br> m≤<br> “2”)|
||||0≤<br> t1≤<br>255, 0≤<br> t2≤<br> 255|
|[Initial Value]|||t1 = 2, t2 = 2|
|[Function]|[Function]||Specify Snout LED ON/OFF times.|
||||m specifies the snout operation mode.|
||||m<br>Snout OperatingMode|
||||1, 49<br>This command specifies the LED ON/OFF times while the presenter is operating.|
||||(LED lights in orange while the printer is printing.)|
||||2, 50<br>This command specifies the LED ON/OFF times for recoverable and non-recoverable|
||||errors.|
||||t1 specifies the snout LED ON time.|
||||When 1≤<br> t1≤<br>255:  ON time = t1 x 50 msec|
||||When t1 = 0:   When ON time is default value (t1=2)|
||||T2 specifies the snout LED OFF time.|
||||When 1≤<br> t2≤<br>255:  OFF time = t2 x 50 msec|
||||When t2 = 0:   When OFF time is default value (t2=2)|
||||This command is valid when a presenter is connected.|
||||When the snout is not connected, this command is prohibited from use.|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-104 
