Rev.2.52 

## **4-3-6 STAR Original Mark Commands** 

This command is specialized for printing mark sheets for lotteries.  This command can print lines. 

**==> picture [333 x 208] intentionally omitted <==**

**----- Start of picture text -----**<br>
<Print Sample><br>L O T T E R Y  1 0<br>01 05 32 85 86 50 70 77 08<br>50 21 42 46 40 12 02 06 78<br>Mark Printing<br>;<br>2003/04/08  STAR Micronics co., ltd.<br>No. 0304081254896<br>**----- End of picture text -----**<br>


## **<Example of Command Transmission>** 

## • Mark Format 

Mark Height h = 10 dots, Mark line feed amount v = 20 dots Mark number 0: Mark Color c = White, Mark horizontal width w = 16 dots Mark number 1: Mark Color c = Black, Mark horizontal width w = 40 dots Mark number 2: Mark Color c = White, Mark horizontal width w = 40 dots 

||Mark 1|||Mark 0|||Mark 2|||
|---|---|---|---|---|---|---|---|---|---|
||Hor. W|||Hor. W|||Hor. W|||
||Mark 1|Mark 0|Mark 1|Mark 0|Mark 1|Mark 0|Mark 2||Mark height h Mark LF amount v|
|||||||||||
|Mark 1<br>Mark 0<br>Mark 2<br>Mark 0<br>Mark 1<br>Mark 0<br>Mark 1<br>Mark 0<br>Mark 1<br>Mark 0<br>Mark 2<br>Mark 0<br>~~Ss~~|||||||Mark 1<br>Mark 2||Mark height h Mark LF amount v<br> Mark height h Mark LF amount v<br>||
|**• Example Transmission**||||||||||



1. Mark height, Line feed amount setting 

<ESC> <GS> *1 h v (h = “010”, v = “020”) 

2. Color of each mark number, Horizontal width setting 

   - <ESC> <GS> *2 m c w  (Mark number 0 setting: m = “0”, c = “0”, w = “016”) <ESC> <GS> *2 m c w  (Mark number 0 setting: m = “1”, c = “1”, w = “040”) <ESC> <GS> *2 m c w  (Mark number 0 setting: m = “2”, c = “0”, w = “040”) 

3. Register the mark format specified by 1 and 2 in advance in the non-volatile memory (it is possible to print marks that are not registered in the non-volatile memory.) 

   - <ESC> <GS> *W 

4. Printing Marks 

   - <ESC><GS>*0nm1m2m3m4m5m6m7 (n = “007”, m1 = “1”, m2 = “0”, m3 = “1”, m4 = “0”, m5 = “1”, m6 = “0”, m7 = “2”) 

   - <ESC><GS>*0nm1m2m3m4m5m6m7 

   - (n = “007”,m1 = “1”, m2 = “0”, m3 = “2”, m4 = “0”, m5 = “1”, m6 = “0”, m7 = “1”) 

   - <ESC><GS>*0nm1m2m3m4m5m6m7 (n = “007”, m1 = “1”, m2 = “0”, m3 = “1”, m4 = “0”, m5 = “2”, m6 = “0”, m7 = “2”) 

ESC/POS Command Specifications 

200 
