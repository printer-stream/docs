## **3.9. Mark Command Details** 

This command is specialized for printing mark sheets for lotteries. This command can print lines. 

<Print Sample> 

**LOTTERY 10 01 05 32 85 86 50 70 77 08 50 21 42 46 40 12 02 06 78** Printed Marks 2003/04/08  STAR micronics.co,ltd No. 0304081254896 ~~srcas~~ 7 

<Example of Command Transmission> 

- Mark Format 

Mark Height h = 10 dots, mark line feed amount v = 20 dots 

Mark number 0: Mark Color c = White, Mark horizontal width w = 16 dots 

Mark number 1: Mark Color c = Black, Mark horizontal width w = 40 dots Mark number 2: Mark Color c = White, Mark horizontal width w = 40 dots 

|Mark||||Mark|||Mark||
|---|---|---|---|---|---|---|---|---|
|number 1||||number 0|||number 2||
|Horizontal||||Horizontal|||Horizontal||
|width w||||width w|||width w||
|Mark|Mark|Mark||Mark|Mark|Mark|Mark|Mark height h<br>Mark line feed|
|number 1|number 0|number 1||number 0|number 1|number 0|number 2|amount v|
||||||||||
|Mark|Mark|Mark||Mark|Mark|Mark|Mark|Mark height h<br>Mark line feed|
|number 1|number 0|number 2||number 0|number 1|number 0|number 1|amount v|
||||||||||
|Mark|Mark|Mark||Mark|Mark|Mark|Mark|Mark height h<br>Mark line feed|
|number 1|number 0|number 1||number 0|number 2|number 0|number 2|amount v|



- Example Transmission 

1. Mark height, Line feed amount setting 

<ESC> <GS> *1 h v (h = “010”, v = “020”) 

2. Color of each mark number, Horizontal width setting 

   - <ESC> <GS> *2 m c w  (Mark number 0 setting: m = “0”, c = “0”, w = “016”) <ESC> <GS> *2 m c w  (Mark number 0 setting: m = “1”, c = “1”, w = “040”) <ESC> <GS> *2 m c w  (Mark number 0 setting: m = “2”, c = “0”, w = “040”) 

3. Register the mark format specified by 1 and 2 in advance in the non-volatile memory (it is possible to print marks that are not registered in the non-volatile memory.) 

<ESC> <GS> * W 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-106 
