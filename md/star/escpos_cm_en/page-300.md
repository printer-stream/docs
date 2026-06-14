Rev.2.52 

## **6-6-2 General Description of GS-1 Bar Codes** 

## Basic structure of data 

|Basic structure of data|||||||
|---|---|---|---|---|---|---|
|Start character|FNC1|AI|Data|check<br>digit A|check<br>digit B|Stop<br>character|
|Added automatically||(d1...dn)|||Added automatically||



## Connection structure of data 

|Start character|FNC1|AI|Data|check<br>digit A|FNC1|AI|Data|check<br>digit A|check<br>digit B|Stop<br>character|
|---|---|---|---|---|---|---|---|---|---|---|
|Added automatically||(d1...dn)|||||||Added automatically||



The following four special characters (SP, “(“, “)”, “*”) operate as shown below. 

|The following four special characters(SP, “(“, “)”, “*”)operate as shown below.|The following four special characters(SP, “(“, “)”, “*”)operate as shown below.|The following four special characters(SP, “(“, “)”, “*”)operate as shown below.|The following four special characters(SP, “(“, “)”, “*”)operate as shown below.|
|---|---|---|---|
|Special Characters||||
|Characters|Hex.|Decimal||
|SP|20|32|The frst SP after d1 is the data division identifer for identifying (AI).<br>The SP is refected bythe HRI but is not included in the encodingdata.<br>|
|(|28|40|<br>“(“ is refected by the HRI. This is useful when using “(“,”)” to highlight the AI.<br>It is not included in encodingdata.|
|)|29|41|The frst “)“ after d1 is the data division identifer for identifying (AI).<br>The “)“ is refected bythe HRI but is not included in the encodingdata.|
|*|2A|42|<br>The check digit calculated by modulus 10 is inserted automatically at the<br>position specifed in “*”.<br>The check digit is refected in the HRI instead of the “*”.|



Data added automatically is not entered in the HRI characters. 

Special HRI characters are processed as shown below. 

- Start characters (CODE A, CODE B, CODE C) are not printed in HRI characters. 

- SP is used for HRI characters for function characters (FNC1 and FNC3) and control characters (00H to 1FH and 7FH). 

- HRI characters for SP and “(“,”)” are printed as they are. 

- The check digit is printed in the “*” position. 

The available data ranges for each code set (CODE A, CODE B, CODE C) are shown in the following table. Bar code data for special characters (FNC1, FNC3) or “(“,”)”, “*”, “{“ sends double-byte characters as shown in the following table. 

ESC/POS Command Specifications 

296 
