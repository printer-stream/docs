Rev.2.52 

## **<Function 082> GS ( k pL pH cn fn m (cn=48, fn=82)** 

## Name 

Send size information of the symbol data of the PDF417 symbol saving region 

Code ASCII GS ( k pL pH cn fn m Hex. 1D   28  6B  pL  pH cn fn m Decimal   29   40  107  pL  pH cn fn m Defined Region pL = 3, pH = 0 

cn = 48, fn = 82, m = 48 

Function Sends the size information of the symbol data stored in the symbol saving region by GS ( k Function 080. Details 

The size information of the symbol is not printed with the processing of this function. 

Size information indicates the size of the symbol printed by Function 081. 

The quiet zone does not include size information. 

Data of the size information is shown below. 

|Transmission data|Hex|Decimal|Data length|
|---|---|---|---|
|Header<br>|37H|55|1Byte|
|Identifer|2FH|47|1Byte|
|<br>Horizontal Size *1|30H to 39H|48 to 57|1 to 5 Bytes|
|Delimiter|1FH|31|1Byte|
|Vertical Size *1|30H to 39H|48 to 57|1 to 5 Bytes|
|Delimiter|1FH|31|1Byte|
|Fixed Value|31H|49|1Byte|
|Delimiter|1FH|31|1Byte|
|Other Information *2|30H/31H|48/49|1Byte|
|NUL|00H|0|1Byte|



- 1 The horizontal and vertical sizes are shown as the number symbol dots. 

   - The decimal value of the horizontal and vertical sizes are converted to character data and sent in order from the MSB. 

   - Ex.: When the horizontal size is 120 dots, “120” is converted to 3 bytes of data (Hex:31H, 32H, 30H, Decimal:49, 50, 48). 

- 2 “Other information” indicates whether it is possible to print symbol data stored in the saving region. 

|<br>ingregion.|||
|---|---|---|
|Hex|Decimal|Data length|
|30H|48|Printable|
|31H|49|Notprintable|



Reference 

GS ( k Function 080, 082, ESC @ 

ESC/POS Command Specifications 

114 
