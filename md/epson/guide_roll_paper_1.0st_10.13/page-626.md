## **C O N F I D E N T I A L** 

(*1)”Horizontal size” and “vertical size” indicate the number of dots of the symbol. 

The decimal value of the vertical size and horizontal size is converted to text data and sent starting from the high order end. 

(ex: When horizontal size is 120 dots, horizontal size is “120” (in hexadecimal: 31H, 32H, and 30H / in decimal: 49, 50, and 48 ), which is 3 bytes of data.) 

(*2)”Other information” indicates whether printing of the data in the symbol storage area is possible or impossible. The “Other information“ is the following. 

## **Other information** 

|**Hex**|**Decimal**|**Condition**|
|---|---|---|
|30H|48|Printing is possible|
|31H|49|Printing is impossible|



■ Size information indicates size of symbol that is printed by Function 181. 

■ The quiet zone is not included in the size information. 

- If “other information” is “Printing is impossible“(in decimal: 49), use one of the solutions shown below. 

|**Cause**|**Solution**|
|---|---|
|There are data in the print buffer<br>in the standard mode|Put the printer in the “there is no data in the print<br>buffer” status by executingGS Tor print<br>commands (LF, CR, ESC J).|
|Symbol is bigger than the current<br>print area.|Expand the print area byGS W,ESC W,ESC $.<br>Reduce the module size by Function 167.<br>Lower the error correction level by Function 169.|
|The data in the symbol storage<br>area is too large.|Send correct data by Function 180.<br>Select other model by Function 165<br>Lower the error correction level by Function 169.|
|There is no data in the symbol<br>storage area.|Send data to the symbol storage area by Function<br>180.|
