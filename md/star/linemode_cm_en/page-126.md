|**ESC GS* 0  n  m1  m2  m3 … mk**|**ESC GS* 0  n  m1  m2  m3 … mk**|**0  n  m1  m2  m3 … mk**||
|---|---|---|---|
|[Name]|Print mark|||
|[Code]|ASCII|ESC GS<br>*<br>0<br>n<br>m1<br>m2|m3<br>…<br>mk|
||Hex.|1B<br>1D<br>2A<br>30<br>n<br>m1<br>m2|m3<br>…<br>mk|
||Decimal|Decimal<br>27<br>29<br>42<br>48<br>n<br>m1<br>m2|m3<br>…<br>mk|
|[Defined Area]||“001”≤<br> n≤<br> ”255”||
|||“0”≤<br> m≤<br> ”9”||
|||k = n||
|[Initial Value]||- - -||
|[Function]|[Function]|Prints the mark number specified by m, based on the mark format (mark height, mark line feed||
|||amount, each mark color, and each mark horizontal width) that is preset.|amount, each mark color, and each mark horizontal width) that is preset.|
|||n indicates the number of marks to print; If the number of marks is 10 (m1 to m10), n = “010.”||
|||m specifies the mark number to print.||
|||n and m are ASCII character strings that are represented by decimals; They are composed of||
|||character codes “0” to “9.”||
|||This command is ignored if there is print data in the image buffer. Therefore, other characters||
|||cannot be included (characters, bit images, bar codes, etc.).||
|||If there is no mark specified in the remaining print region, the number of bytes specified by n are||
|||discarded.||
|||Also, if the value of n is out of the defined range, subsequent data are processed as normal data.|is out of the defined range, subsequent data are processed as normal data.|
|||This command is affected by position alignment, left margin, moved position, positions such as||
|||horizontal tab and upside down printing.||
|||Invalid in page mode.||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-108 
