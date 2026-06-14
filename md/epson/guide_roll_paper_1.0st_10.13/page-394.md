## **C O N F I D E N T I A L** 

■ The special characters ("(“,”)”) are processed as shown in the table below. **Special characters Character Hex Decimal Processing** ( 28 40 "(" is inserted for the HRI character. It can be used when you want the HRI characters that indicate AI to look nice when used with the pair of ")." . ) 29 41 After _**d1**_ , the first ")" is processed as AI and the data part delimiter, and ")" is inserted for the HRI characters. ")" are inserted for the HRI characters for subsequent ")" . ~~——~~ ■ Adds the guard pattern and finder pattern automatically. ■ When HRI characters are designated to be added, special character HRI characters are processed as follows. • The HRI character of function character (FNC1) is not printed. 

   - The HRI characters of special characters ("(", ")") are printed as the respective characters ("(", ")"). 

- The HRI characters of bar code data ["{" + ("(", ")")] are printed as the respective characters ("(", ")"). 

- ■ When the bar code height set with GS h is smaller than [34 times the module width], a bar code with a height (excluding the HRI characters) of [module width x 34] is printed, without reference to the GS h setting.) 

## **Program Example for all printers** 

## **Print Sample** 

PRINT #1, CHR$(&H1D);"h";CHR$(80); ← Set height PRINT #1, CHR$(&H1D);"k";CHR$(2); ← Print bar code PRINT #1, "496595707379";CHR$(0); PRINT #1, CHR$(&HA); PRINT #1, CHR$(&H1D);"k";CHR$(67);CHR$(12); PRINT #1, "496595707379"; ← Print bar code 
