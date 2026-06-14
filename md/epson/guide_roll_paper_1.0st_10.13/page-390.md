## **C O N F I D E N T I A L** 

|(|28|40|"(" is inserted for the HRI character. It can be used when you want the<br>HRI characters that indicate AI to look nice when used with the pair of<br>")."  ")." does not constitute encoded data.|
|---|---|---|---|
|)|29|41|Afterd1, the first ")" is processed as AI and the data part delimiter,<br>and ")" is inserted for the HRI characters. ")" are inserted for the HRI<br>characters for subsequent ")" .  In any case, SP does not constitute<br>encoded data.|
|*|2A|42|Check digit A (1 character), calculated with modulus 10 is added as the<br>data part at the position of *. "*" is not an HRI character, but check<br>digits are inserted for HRI characters.|



- Examples of bar code data using special characters (SP, "(," ")," "*") are shown below. 

   - Example:  When [AI = 01/data = 9501234567890/Specify to add check digit A/enclose AI in ()] GS k 74 18 "(01)9501234567890*" 

When HRI characters are designated to be added, the HRI characters are [(01)95012345678903]. 

- Example:  When [AI = 01/data = 9501234567890/Specify to add check digit A/enclose AI in (), and insert a space between the data] 

GS k 74 18 "(01)9501234567890*" 

When HRI characters are designated to be added, the HRI characters are [(01)95012345678903]. 

   - Example:  When linking [AI = 01/data = 9501234567890/Specify to add check digit A/enclose AI in ()] and [AI=3102/data = 000400/enclose AI in ()], and separating the HRI characters between the link with a space 

      - GS k 74 33 "(01)9501234567890* {1(3102)000400" 

      - When HRI characters are designated to be added, the HRI characters are [(01)95012345678903 (3102)000400]. 

- When HRI characters are designated to be added, (d1...dn) is printed as HRI characters. Automatically added data is not treated as HRI characters. 

The HRI characters of special characters are processed as follows. (“SP” indicates a space) 

- The HRI character of the start character (CODE A, CODE B, CODE C) is not printed. 

- The HRI characters of the function characters (FNC1, FNC3) and the control characters (Hexadecimal = 00H - 1FH, 7FH / Decimal = 0 - 31, 127) are printed as spaces. 
