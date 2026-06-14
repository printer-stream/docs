## **C O N F I D E N T I A L** 

## (*3)[Error information] indicates mainly detailed information when [Other information] is [Unprintable]. 

|**Error**<br>**information**|**Error content**|**Solution**|
|---|---|---|
|"0000"|No error (printing is possible)|-|
|"1001"|The line element symbol data is invalid|Transmit vaild data (Function 480)|
|"1002"|The 2D composite element symbol data is<br>invalid|Transmit valid data (Function 480)|
|"1003"|There is too much 2D composite element data<br>When something other than GS1-128 is<br>specified for line element, and when<br>“automatic selection“ is specified for 2D<br>composite element and the 2D composite<br>element data exceeds 399 bytes|Reduce the amount of 2D composite<br>element data (Function 480)<br>Change the line element to GS1-128<br>(Function 480)|
|"1005"|The combination of line element and 2D<br>composite element is invalid<br>When something other than GS1-128 is<br>specified for line element, and “Fixed (CC-C)“<br>is specifed for the 2D composite element|Change the line element to GS1-128<br>(Function 480)<br>Change the 2D composite element to<br>“automatic selection“ (when the amount<br>of data is 338 bytes or less) (Function 480)|
|"1006"|There is no data in the symbol storage area|Transmit data (Function 480)|
|"2001"|When the standard mode is selected, there is<br>data in the print buffer|Empty the print buffer (GS Tor the print<br>command [LF,CR,ESC J, etc.])|
|"2002"|The symbol size is bigger than the current<br>printing area<br>The symbol is bigger than the printing area<br>The symbol is bigger than the <Function 471><br>maximum width|Make the module size smaller (Function<br>467)<br>Make the <Function 471> maximum width<br>bigger<br>Make the printing area bigger (GS W,ESC<br>W,ESC $etc)|



■ The quiet zone is not included in the size information. 
