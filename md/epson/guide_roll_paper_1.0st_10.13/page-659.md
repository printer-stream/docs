## **C O N F I D E N T I A L** 

- When (a = 49), b specifies the type of 2D composite element. 

|b|**2D composite element type**|**Symbol data (SP indicates a space)**|**Symbol data (SP indicates a space)**|**Symbol data (SP indicates a space)**|
|---|---|---|---|---|
|||**Data (k)**|**Characters**<br>**(ASCII)**|**Data (**d**)**|
|65|Automatic selection|1≤ **k** ≤2361|NUL ~ SP (7FH)|0≤ d ≤255|
|66|Fixed (CC-C)|1≤ **k** ≤2361|NUL ~ SP (7FH)|0≤ d ≤255|



## [Notes] 

- Data stored in the symbol storage area by this function is processed by Functions 481 and 482. The data in the symbol storage area are reserved after processing Function 481 or 482. 

## ■ k bytes of d1...dk are processed as symbol data. 

- To print Composite Symbology, this function must be executed twice. 

   - Specify (a = 48), and save the line element symbol data. 

   - Specify (a = 49), and save the 2D composite element symbol data. 

   - It does not matter whether the line element (a = 48) or 2D composite element (a = 49) is specified first. 

   - It is possible to change the symbol data of the 2D composite element (a = 49) without changing that of the line element (a = 48), and vice versa. 

- The line element symbol data in the symbol storage area is valid until any of <Function 080>, <Function 180>, <Function 280>, <Function 380>, and <Function 480: when (a = 48) is specified> of this command, ESC @, reset, or power off are executed. 

- The 2D composite element symbol data in the symbol storage area is valid until any of <Function 080>, <Function 180>, <Function 280>, <Function 380>, and <Function 480: when (a = 49) is specified> of this command, ESC @, reset, or power off are executed. 

## [Notes for EAN8, EAN13, and UPC-A] 

■ Transmit the data, except for the modular check character, from the host. 

## [Notes for UPC-E (0 omitted (6 digits) version)] 

- Transmit the data, except for the number system character (NSC) and modular check character, from the host. 
