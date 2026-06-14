Rev.2.52 

## **ESC GS * 1 h v** 

|**ESC GS* 1 h v**||||
|---|---|---|---|
|Name|Specify mark height and line feed|||
|Code|ASCII<br>ESC<br>GS<br>*<br>1|h|v|
||Hex<br>1B<br>1D<br>2A<br>31|h|v|
||Decimal<br>27<br>29<br>42<br>49|h|v|
|Defned Region|“001”≤h≤”255”|||
||“001”≤v≤”255”|||
||h≤v|||
|Initial Value|Non-volatile memory|||
|Function|Specifes mark height and line feed amount|||
||h is the mark height (number of dots); v is the line feed amount for the mark (number of dots)|||
||h and v are ASCII character strings that are||represented by decimals; They are composed of|
||character codes “0” to “9.”|||
||If a small line feed amount is specifed, missing print can occur, so more than v = 16 dots is|||
||recommended.|||
|Reference|ESC GS * 0, ESC GS * 2, ESC GS * W, ESC GS * C|||



ESC/POS Command Specifications 

202 
