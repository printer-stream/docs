Rev.2.52 

## **ESC c 4 n** 

Select paper out sensor to enable at printing stop 

Name Code ASCII ESC c 4 n Hex. 1B 63 34 n Decimal 27 99 52 n 

0 ≤ n ≤ 255 Defined Region Initial Value n = 0 Function Selects the paper out detector to stop printing when paper has run out. 

|Bit|Function<br>|“0”|“1”|
|---|---|---|---|
|7|Undefned<br>|--|--|
|6|<br>Undefned<br>|--|--|
|5|<br>Undefned<br>|--|--|
|4|<br>Undefned<br>|--|--|
|3|<br>Undefned<br>|--|--|
|2|<br>Undefned|--|--|
|1|<br>Paper roll near end detector|Invalid|Valid|
|0|Paper roll near end detector|Invalid|Valid|



Details 

- To stop printing, the printer stops after printing the current line and feeding paper. 

- The printer goes offline when printing is stopped. 

- If either bit 0 or bit 1 is set to 1, select the paper roll near end detector as the paper out detector effective to stop printing. 

ESC/POS Command Specifications 

72 
