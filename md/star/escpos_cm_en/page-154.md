Rev.2.52 

<When using CODE 128 bar code (m = 73)> 

- See Appendix-6 for details on CODE 128 bar codes and code tables. 

- To print CODE 128 bar codes on this printer, be careful of the following points to send the bar code data. 

- a. At the top of the bar code string, always set the code set selection characters (either of the CODE A, CODE B, or CODE C) to select the initial code set. 

- b. Specify special characters using the two characters of ‘{‘ and one subsequent character. Also, the ‘{‘ of the ASCII characters are specified by sending ‘{‘ for two characters consecutively. 

|Special<br>Characters|Transmission Data|Transmission Data|Transmission Data|
|---|---|---|---|
||ASCII|Hex.|Decimal|
|SHIFT|{S|7B,53|123,83|
|CODE A|{A|7B,41|123,65|
|CODE B|{B|7B,42|123,66|
|CODE C|{C|7B,43|123,67|
|FNC1|{1|7B,31|123,49|
|FNC2|{2|7B,32|123,50|
|FNC3|{3|7B,33|123,51|
|FNC4|{4|7B,34|123,52|
|’{‘|{{|7B,7B|123,123|



- If the top of the bar code data string is not a code set selection character, the command is stopped and processing is handled normally from subsequent data. 

- If the combination of ‘{‘ and 1 character immediately after does not conform to either of the special characters, the command is stopped and processing is handled normally from subsequent data. 

- If a character that cannot be used with the selected code set is received, the command is 

stopped and processing is handled normally from subsequent data. 

- HRI characters that correspond to shift characters and code set selection characters are not printed. 

- HRI characters of function characters are printed with a space. 

- HRI characters of the control characters (00H to 1FH and 7FH) are printed with a space. 

ESC/POS Command Specifications 

154 
