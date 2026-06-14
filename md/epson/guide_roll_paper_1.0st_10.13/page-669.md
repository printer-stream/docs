## **C O N F I D E N T I A L** 

## (b) Concatenated code structure 

|Start<br>character|FNC<br>1|AI|Data<br>part|Check digit<br>A|FNC<br>1|AI|Data<br>part|Check digit<br>A|Check digit<br>B|Stop<br>character|
|---|---|---|---|---|---|---|---|---|---|---|
|Automatically<br>added||<Function 480 (d1...dn)>|||||||Automatically added||



## ■ The data shown below is added automatically in encoding. 

   - Start character (CODE A, CODE B, CODE C) and FNC1 

   - Check digit B (1 character) 

   - Stop character 

- The 4 special characters (SP, "(," ")," "*") are processed as shown in the table below. 

|■The 4 special characters (SP, "(," ")," "*") are processed as shown in the table below.|■The 4 special characters (SP, "(," ")," "*") are processed as shown in the table below.|■The 4 special characters (SP, "(," ")," "*") are processed as shown in the table below.|■The 4 special characters (SP, "(," ")," "*") are processed as shown in the table below.|
|---|---|---|---|
|||||
|**Special characters**||||
|**Character**|**Hex**|**Decimal**|**Processing**|
|SP|20|32|Afterd1, the first SP is processed as AI and the data part delimiter, and<br>a space is inserted for the HRI characters. Spaces are inserted for the<br>HRI characters for subsequent SP. These spaces do not constitute<br>encoded data.|
|(|28|40|"(" is inserted for the HRI character. "(" does not constitute encoded<br>data.|
|)|29|41|Afterd1, the first ")" is processed as AI and the data part delimiter,<br>and ")" is inserted for the HRI characters. ")" are inserted for the HRI<br>characters for subsequent ")". In case of any, "(" does not constitute<br>encoded data.|
|*|2A|42|Check digit A (1 character), calculated with modulus 10 is added as the<br>data part at the position of *. "*" is not an HRI character, but check<br>digits are inserted for HRI characters.|



■ The HRI characters of special characters are processed as follows. (“SP” indicates a space) 
