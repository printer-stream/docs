Rev.2.52 

<When using GS1 Databar Expanded (m = 78)> 

To print GS1 Databar Expanded on this printer, be careful of the following points to send the bar code data. 

The following special characters operate as shown below. 

|Special<br>Characters||||
|---|---|---|---|
||Hex.|Decimal||
|(|28|40|““(“ is refected by the HRI. This is<br>useful when using “(“,”)” to highlight<br>the AI.<br>It is not included in encodingdata.<br>|
|)|29|41|The frst “)“ after d1 is the data<br>division identifer for identifying (AI).<br>The “)“ is refected by the HRI but is<br>not included in the encodingdata.|



## Also the following characters are expressed as 2 bytes. 

|Special<br>Characters|Transmission Data|Transmission Data|Transmission Data|
|---|---|---|---|
||ASCII|Hex.|Decimal|
|FNC1|{1|7B,31|123,49|
|’(‘|{(|7B,28|123,40|
|’)‘|{}|7B,29|123,41|



- ・ If the double-digit lead for the bar code data line is not a number, or is not “(“ and a number, command 

- processing is stopped at this point and the next data is processed as standard data. 

- ・ If the combination of ‘{‘ and the character directly behind does not correspond to, command processing is 

- stopped at this point and the next data is processed as standard data. 

- ・ Although “*” can be used, it is not reflected in the HRI or the encoding data. 

## STAR 

Reference 

• If printing bar codes that require check digits on STAR printers, even if the check digit is sent as a bar code, the check digit that was calculated on the printer is printed. 

GS H, GS f, GS h, GS w, Appendix-6 

ESC/POS Command Specifications 

156 
