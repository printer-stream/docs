## **C O N F I D E N T I A L** 

## [Notes for GS1 DataBar Expanded Stacked] 

■ Transmit the 2-byte data shown in the following table ([Hexadecimal = 7BH / Decimal = 123] + character code) from the host for the special character (FNC1) and symbol data "(", ")". ("+" in the table is not included in the transmission data) 

|**Data**|**Transmission data from host**|**Transmission data from host**|**Transmission data from host**|
|---|---|---|---|
||**ASCII**|**Hexadecimal**|**Decimal**|
|FNC1|{ + 1|7B + 31|123 + 49|
|(|{ + (|7B + 28|123 + 40|
|)|{ + )|7B + 29|123 + 41|



## [Notes for GS1-128] 

■ GS1-128 processes the following structures. 

## (a) Basic structure 

|Start|FNC|AI|Data|Check digit|Check digit|Check digit||Stop|||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|character|1||part|A|B|||character|||||
|Automatically||(d1...dk)|||Automatically added||||||||
|added|||||||||||||
|(b) Concatenated code structure|||||||||||||
|Start|FNC|AI|Data|Check digit|FNC|AI|Data||Check digit||Check digit|Stop|
|character|1||part|A|1||part||A||B|character|
|Automatically||(d1...dk)|||||||||Automatically added||
|added|||||||||||||



■ Transmit the data relevant to check digit A along with the application identifier (AI), from the host. 
