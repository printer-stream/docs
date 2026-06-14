## **C O N F I D E N T I A L** 

## **GS ( k** 

EXECUTING + SETTING 

[Name] Set up and print the symbol 

[Printers not featuring this command] TM-J2000/J2100, TM-U230, TM-U220 

- [Description] Performs data processing related to 2-dimensional codes (PDF417, QR Code, MaxiCode, 2-dimensional GS1 DataBar, Composite Symbology). 

   - Symbol type is specified by cn 

   - Function code fn specifies the function. 

|cn|fn|**Function No. **|**Function name**|
|---|---|---|---|
|48|65|**Function 065**|PDF417: Set the number of columns in the data region|
||66|**Function 066**|PDF417: Set the number of rows|
||67|**Function 067**|PDF417: Set the width of the module|
||68|**Function 068**|PDF417: Set the row height|
||69|**Function 069**|PDF417: Set the error correction level|
||70|**Function 070**|PDF417: Select the options|
||80|**Function 080**|PDF417: Store the data in the symbol storage area|
||81|**Function 081**|PDF417: Print the symbol data in the symbol storage area|
||82|**Function 082**|PDF417: Transmit the size information of the symbol data in the symbol storage area|
|49|65|**Function 165**|QR Code: Select the model|
||67|**Function 167**|QR Code: Set the size of module|
||69|**Function 169**|QR Code: Select the error correction level|
||80|**Function 180**|QR Code: Store the data in the symbol storage area|
||81|**Function 181**|QR Code: Print the symbol data in the symbol storage area|
||82|**Function 182**|QR Code: Transmit the size information of the symbol data in the symbol storage<br>area|
