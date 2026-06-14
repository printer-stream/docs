**ESC RS r n** [Name] Set printing speed [Code] ASCII ESC RS r n Hex. 1B 1E 72 n Decimal 27 30 114 n 

[Defined Area] 0≤n≤3 48≤n≤51 (”0”≤n≤”3”) [Initial Value] Memory switch setting [Function] Sets print speed. 

This command stops printing to be executed. 

Because two-color print mode prints in one speed, the speed settings with this command are invalid.  This command setting becomes valid when returned from the two-color print mode to the single color print mode. 

|N|Print Speed<br>Single Color PrintingMode<br>Two Color PrintingMode|
|---|---|
|0,48|Highspeed<br>Two Color PrintingMode Speed|
|1,49<br>~~a~~|Mid-speed<br>Two Color PrintingMode Speed|
|2, 50<br>~~a~~|Slow speed<br>Two Color Printing Mode Speed|
|3, 51<br>~~a~~|Optionspeed (differs accordingtothemodel)<br>Two Color PrintingMode Speed|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-97 
