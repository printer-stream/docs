## **C O N F I D E N T I A L** 

## (a) Basic structure 

|Start|FNC|AI|Data|Check digit|Check digit|Check digit||Stop|||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|character|1||part|A|B|||character|||||
|Automatically||(d1...dn)|||Automatically added||||||||
|added|||||||||||||
|(b) Concatenated code structure|||||||||||||
|Start|FNC|AI|Data|Check digit|FNC|AI|Data||Check digit||Check digit|Stop|
|character|1||part|A|1||part||A||B|character|
|Automatically||(d1...dn)|||||||||Automatically added||
|added|||||||||||||



- Transmit the data relevant to check digit A along with the application identifier (AI), from the host. 

- The start character number system character (CODE A, CODE B, CODE C), FNC1, check digit B (1 character), and stop character are added automatically. 

- The 4 special characters (SP, "(," ")," "*") are processed as shown in the table below. 

|■The 4 special characters (SP, "(," ")," "*") are processed as shown in the table below.|■The 4 special characters (SP, "(," ")," "*") are processed as shown in the table below.|■The 4 special characters (SP, "(," ")," "*") are processed as shown in the table below.|■The 4 special characters (SP, "(," ")," "*") are processed as shown in the table below.|
|---|---|---|---|
|||||
|**Special characters**||||
|**Character **|**Hex**|**Decimal**|**Processing**|
|SP|20|32|Afterd1, the first SP is processed as AI and the data part delimiter, and<br>a space is inserted for the HRI characters. Spaces are inserted for the<br>HRI characters for subsequent SP. In any case, SP does not constitute<br>encoded data.|
