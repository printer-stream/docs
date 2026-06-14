## **3.7. 2 Color Printing Command Details** 

The following commands control 2 color printing functions. 

The following commands are effective only when using a model handling 2 color printing. 

|**ESC RS c n**|**ESC RS c n**|**ESC RS c n**|**ESC RS c n**||
|---|---|---|---|---|
|[Name]|Set print color in 2 color print mode|Set print color in 2 color print mode|Set print color in 2 color print mode||
|[Code]|ASCII||ESC RS<br>c<br>n||
||Hex.||1B<br>1E<br>63<br>n||
||Decimal||Decimal<br>27<br>30<br>99<br>n||
|[Defined Area]|||0≤<br>n≤<br>1||
||||48≤<br>n≤<br>49 (”0”≤<br>n≤<br>”1”)||
|[Initial Value]|||n = 0, 48 (When in 2 color print mode)||
|[Function]|||Specifies print color in 2 color print mode.||
||||This command is ignored when not in the 2 color print mode.||
||||Specifies black for the print color when in 2 color print mode.||
||||This command is cleared only when the printer is reset.||
||||The specification of this command is not cleared by ESC @ CAN.||
||||However, print color is initialized to black by the ESC @ and CAN only when in the compatible 2|However, print color is initialized to black by the ESC @ and CAN only when in the compatible 2|
||||color print mode.||
|||n|Specifies2colorprintmode color||
||0,4|48|Black||
||1,4|49|Red||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-92 
