Rev.2.52 

## **ESC& yc1c2 [x1d1...d (y x x1) ] ... [axd1...d (yxax)]** 

|Name|Defne download characters||
|---|---|---|
|Code|ASCII<br>ESC<br>&<br>y|c1 c2 [x1 d1 ... d (yX x1)] ... [a xd1 ... d (y× ax)]|
||Hex.<br>1B<br>26<br>y|c1 c2 [x1 d1 ... d (yX x1)] ... [a xd 1 ... d (y×ax)]|
||Decimal<br>27<br>38<br>y|c1 c2 [x1 d1 ... d (yX x1)] ... [a xd 1 ... d (y×ax)]|
|Defned Region|y = 3||
||32≤c1≤c2≤126||
||0≤x≤12 (Font A), 0≤x≤9|(Font B)|
||0≤d1....d (y×ax)≤255||
|Initial Value|Same pattern as internal character set||
|Function|Defnes the download characters to the specifed character code.||
||• y specifes the number of bytes in the vertical direction.||



   - c1 specifies the starting character code for the definition; c2 specifies the final character 

   - code. 

   - x specifies the number of dots in the horizontal direction for the definition. 

- Details • The definable character code range is from ASCII code <20>H to <7E>H. 

   - It is possible to define multiple characters for consecutive character codes with one definition. If only one character is desired, use c1 = c2. 

   - If x=0, a space is registered. 

   - d is the dot data for the characters. It indicates the horizontal direction x dot pattern from the left side.  If x does not meet the number of dots configuring the character, any remaining dots on the right side are blank. 

   - The data to define download characters is (y x x) bytes. 

   - Bits that correspond to the dots to print are 1, and the bits that correspond to the dots that are not printed are 0 in the definition data. 

   - This command can define different download characters for each font. To select a font, use ESC M or ESC !. 

   - ESC & (define download characters) and GS * (define download bit images) cannot both be defined simultaneously. 

   - a. When download characters are defined, previously defined download bit images are cleared. 

   - b. Conversely, when download bit images are defined, previously defined download characters are cleared and the definition returns to same the internal character set. 

   - Defined download characters are cleared under the following executions. 

   - a. When the printer is initialized (ESC@) 

   - b. When download bit images are defined (GS*) 

   - c. When download characters are deleted (ESC?) 

   - d. When NV bit images are defined (FSq) 

   - e. When the printer power is turned off 

STAR Font configurations and regions for effective parameters on STAR printers 

|Character Fonts|Horizontal Dots x Vertical Dots|y|x|Data Count|
|---|---|---|---|---|
|Font A|12 x 24 Dots|3|12|36 bytes|
|Font B|9 x 24 Dots|3|9|27 bytes|
|For the STAR printer, the font select commands, <ESC> <RS> F, can also be used.<br>Reference<br>ESC %, ESC ?|||||



ESC/POS Command Specifications 

46 
