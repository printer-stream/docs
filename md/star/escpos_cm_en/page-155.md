Rev.2.52 

<When using GS1-128 (m = 74)> 

• Be sure to note the following points when sending bar code data for GS1-128 bar code printing. 

The following four special characters operate as shown below. 

|Special<br>Characters||||
|---|---|---|---|
||Hex.|Decimal||
|SP|20|32|The frst SP after d1 is the data<br>division identifer for identifying (AI).<br>The SP is refected by the HRI but is<br>not included in the encodingdata.<br>|
|(|28|40|““(“ is refected by the HRI. This is<br>useful when using “(“,”)” to highlight<br>the AI.<br>It is not included in encodingdata.<br>|
|)|29|41|The frst “)“ after d1 is the data<br>division identifer for identifying (AI).<br>The “)“ is refected by the HRI but is<br>not included in the encodingdata.|
|*|2A|42|The check digit calculated by<br>modulus 10 is inserted automatically<br>at the<br>position specifed in “*”.<br>The check digit is refected in the HRI<br>instead of the “*”.|



## Also the following characters are expressed as 2 bytes. 

|Special<br>Characters|Transmission Data|Transmission Data|Transmission Data|
|---|---|---|---|
||ASCII|Hex.|Decimal|
|FNC1|{1|7B,31|123,49|
|FNC3|{3|7B,33|123,51|
|’(‘|{(|7B,28|123,40|
|’)‘|{}|7B,29|123,41|
|’*‘|{*|7B,2A|123,42|
|’{‘|{{|7B,7B|123,123|
|FNC3|{3|7B,33|123,51|
|FNC4|{4|7B,34|123,52|
|’{‘|{{|7B,7B|123,123|



- ・ A space character is used as the HRI character for FNC1 and FNC3 function characters. ・ A space character is used as the HRI control characters (00H to 1FH and 7FH). 

ESC/POS Command Specifications 

155 
