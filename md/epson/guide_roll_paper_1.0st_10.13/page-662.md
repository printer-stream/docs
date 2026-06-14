## **C O N F I D E N T I A L** 

■ The 4 special characters (SP, "(," ")," "*") are processed as shown in the table below. 

|■The 4 special characters (SP, "(," ")," "*") are processed as shown in the table below.|■The 4 special characters (SP, "(," ")," "*") are processed as shown in the table below.|■The 4 special characters (SP, "(," ")," "*") are processed as shown in the table below.|■The 4 special characters (SP, "(," ")," "*") are processed as shown in the table below.|
|---|---|---|---|
|||||
|**Special characters**||||
|**Character**|**Hex**|**Decimal**|**Functions**|
|SP|20|32|A space is inserted for the HRI character. It makes the HRI characters<br>look nice when AI and data part are separated with spaces. SP does<br>not constitute encoded data.|
|(|28|40|Each character is inserted to make the HRI characters look nice when<br>used to enclose the AI. The data does not constitute encoded data.|
|)|29|41||
|*|2A|42|Check digit A (1 character), calculated with modulus 10 is added as the<br>data part at the position of *. "*" is not an HRI character, but check<br>digits are inserted for HRI characters.|



■ Examples of symbol data using special characters (SP, "(," ")," "*") are shown below. 

Example:  When [AI = 01/data = 9501234567890/Specify to add check digit A/enclose AI in ()] GS k 23 0 52 80 48 48 77 "(01)9501234567890*" 

When HRI characters are designated to be added, the HRI characters are [(01)95012345678903]. 

Example:  When [AI = 01/data = 9501234567890/Specify to add check digit A/enclose AI in (), and insert a space between the data] 

GS k 23 0 52 80 48 48 77 "(01)9501234567890*" 

When HRI characters are designated to be added, the HRI characters are [(01)95012345678903]. 

- Example:  When linking [AI = 01/data = 9501234567890/Specify to add check digit A/enclose AI in ()] and [AI=3102/data = 000400/enclose AI in ()], and separating the HRI characters between the link with a space 

GS k 38 0  52 80 48 77"(01)9501234567890* {1(3102)000400" 

When HRI characters are designated to be added, the HRI characters are [(01)95012345678903 (3102)000400]. 
