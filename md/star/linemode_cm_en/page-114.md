## **ESC RS d n** 

[Name] Set print density [Code] ASCII ESC RS d n Hex. 1B 1E 64 n Decimal 27 30 100 n [Defined Area] 0≤n≤15 48≤n≤57 (”0”≤n≤”9”) 65≤n≤70 (”0”≤n≤”F”) [Initial Value] Memory switch setting [Function] Sets print density. This command stops printing to be executed. When in two-color print mode, this can set the print density of red print. 

|n|Print Density<br>Single Color PrintingMode<br>Two Color PrintingModeRedPrintDensity|
|---|---|
|0,48|Print density1.3<br>Print density1.2|
|1, 49<br>~~es~~|Print density 1.2<br>Print density 1.2<br>|
|2, 50<br>~~es~~|Print density1.1<br>Print density1.0<br>|
|3, 51<br>~~esa~~|Print density1.0<br>Print density1.0<br>~~a~~|
|4, 52<br>~~a~~|Print density 0.9<br>Print density1.0<br>~~a~~|
|5, 53|Print density 0.8<br>Print density 0.8|
|6, 54<br>~~a~~|Print density 0.7<br>Print density 0.8<br>~~a~~|
|7, 55<br>~~a~~|(Reserved)<br>(Reserved)<br>~~a~~|
|8, 56<br>~~a~~|(Reserved)<br>(Reserved)<br>~~a~~|
|9, 57|(Reserved)<br>(Reserved)|
|10, 65|(Reserved)<br>(Reserved)|
|11, 66|(Reserved)<br>(Reserved)|
|12, 67<br>~~a~~|(Reserved)<br>(Reserved)<br>~~a~~|
|13, 68<br>~~a~~|(Reserved)<br>(Reserved)<br>~~a~~|
|14, 69|(Reserved)<br>(Reserved)|
|15,70|(Reserved)<br>(Reserved)|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-96 
