Rev.2.52 

For 3: 

|m|Bar Code Type|Defned region of n|Defned region of d|
|---|---|---|---|
|65|UPC-A|<br>11≤n≤12|<br>48≤d≤57|
|66|UPC-E|11≤n≤12|48≤d≤57|
|67|JAN13(EAN13)|12≤n≤13|48≤d≤57|
|68|JAN8(EAN8)|7≤n≤8|48≤d≤57|
|69|CODE39|1≤n≤255|48≤d≤57, 65≤d≤90,32, 36, 37, 43, 45, 46, 47<br>42(d1,dk)|
|70|ITF|2≤n≤255(Even number)|48≤d≤57|
|71|CODABAR|1≤n≤255|48≤d≤57,65≤d≤68,36,43,45,46,47,58|
|72|CODE93|1≤n≤255|0≤d≤127|
|73|CODE128|2≤n≤255|0≤d≤127|
|74|GS1-128|2≤n≤255|0≤d≤127|
|75|GS1 DataBar<br>Omnidirectional|n=13|48≤d≤57|
|76|GS1 DataBar<br>Truncated|n=13|48≤d≤57|
|77|GS1 DataBar<br>Limited|n=13|48≤d≤57[However, 48≤d1≤49]|
|78|GS1 DataBar<br>Expanded|2≤n≤255|32≤d≤34, 37≤d≤63, 65≤d≤90, d = 95,<br>97≤d≤122, d = 123<br>[However, d1 = 40, 48≤d2≤57, 48≤d3≤57,<br>or 48≤d1≤57, 48≤d2≤57]|



## Details 

## For 1: 

- This command is quit by the NULL code. 

- For UPC-A and UPC-E, a bar code is printed when 12 bytes of bar code data are input. Subsequent data is processed as normal data. 

- For JAN13 (EAN13), a bar code is printed when 13 bytes of bar code data are input. Subsequent data is processed as normal data. 

- For JAN8 (EAN8), a bar code is printed when 8 bytes of bar code data are input. Subsequent data is processed as normal data. 

- •The data count for ITF bar codes is always even numbered.  If the data count is odd numbered, the last data is ignored. 

ESC/POS Command Specifications 

151 
