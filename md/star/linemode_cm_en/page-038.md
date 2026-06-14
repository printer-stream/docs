## **3.3.4. L ine Spacing** 

**LF** [Name] Line feed [Code] ASCII LF Hex. 0A Decimal 10 [Defined Area] - - - [Initial Value] - - - [Function] Feeds the currently specified amount of paper. If print data exists in the line buffer, it prints that data. The initial value for the amount of paper is set according to the memory switch settings. 

|**CR**|||
|---|---|---|
|[Name]|Carriage return (line feed)|Carriage return (line feed)|
|[Code]|ASCII|CR|
||Hex.|0D|
||Decimal|13|
|[Defined Area]||- - -|
|[Initial Value]||- - -|
|[Function]|[Function]|When the CR code is enabled, the CR code functions in the same way as the LF code.|
|||If the CR code is disabled, it ignores 1 byte.|
|||Enabling and disabling the CR code is done using the memory switch settings.|



**ESC a n** [Name] Feed paper n lines [Code] ASCII ESC a n Hex. 1B 61 n Decimal 27 97 n [Defined Area] 1≤n≤127 [Initial Value] - - - [Function] Executes a paper feed for (the currently specified line feed amount x n). If print data exists in the line buffer, it prints that data. The initial value for the amount of paper is set according to the memory switch settings. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-20 
