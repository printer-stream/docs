The following is an example showing the sending of the commands. 

|(1)|Set bar code type|||
|---|---|---|---|
||<ESC> <GS> “y” “S” “0” 1|Sets to model 1.||
||<ESC> <GS> “y” “S” “1” 0|Sets mistake correction level to L.||
||<ESC> <GS> “y” “S” “2” 3|Sets cell size to 3 dots.||
|(2)|Set bar code data|||
||• <ESC> <GS> “y” “D” “1” 0 20 0  “2005, January, 1 (SAT)” <LF>|• <ESC> <GS> “y” “D” “1” 0 20 0  “2005, January, 1 (SAT)” <LF>||
|||Sets bar code data (Data automatic analysis)|Sets bar code data (Data automatic analysis)|
|||Sets bar code data (Data manual analysis)|Sets bar code data (Data manual analysis)|
||• <ESC> <GS> “y” “D” “2” 10|1 4 0|“2005” “,”|
||4 2 0|“Year” “,”||
||1 1 0|“1” “,”||
||4 2 0|“Month” “,”||
||1 1 0|“1” “,”||
||4 2 0|“Day” “,”|“Day” “,”|
||4 2 0|“(” “,”||
||2 3 0|“SAT” “,”|“SAT” “,”|
||4 2 0|“)” “,”||
||3 1 0|<LF>||



## (3) Print bar code 

To verify whether to print with the current settings, check the bar code expansion information. 

<ESC> <GS> “y” “I” Check bar code expansion information <ESC> <GS> “y” “p” Print 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 3-128 
