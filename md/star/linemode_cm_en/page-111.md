|**ESC RS C n**|**ESC RS C n**|**ESC RS C n**|
|---|---|---|
|[Name]|Select/cancel 2 color print mode||
|[Code]|ASCII|ESC RS<br>C<br>n|
||Hex.|1B<br>1E<br>43<br>n|
||Decimal|27<br>30<br>67<br>n|
|[Defined Area]||Specification A|
|||0≤<br>n≤<br>2|
|||48≤<br>n≤<br>50 (”0”≤<br>n≤<br>”2”)|
|||Specification B|
|||0≤<br>n≤<br>1|
|||48≤<br>n≤<br>49 (”0”≤<br>n≤<br>”1”)|
|||Specification C|
|||0≤<br>n≤<br>2|
|||48≤<br>n≤<br>50 (”0”≤<br>n≤<br>”2”)|
|||n = 16, n = 32|
|[Initial Value]||n = 0, 48|
|[Function]||Specification A|
||n|Select/cancel 2colorprintmode|
||0, 48|Cancel 2-color printing mode|
|||When in two-color print mode, this command cancels 2-color printing mode.|
|||This command is ignored when the 2-color print mode is already cancelled.|
|||The specification of this command is not cleared by ESC @, CAN.|
|||The following processes are executed by canceling the 2-color print mode using this|
|||command.|
|||• Prints data in line buffer in 2-color print mode, if unprinted data exists in the line buffer.|
|||• Waits to stop printing when printing in 2-color print mode.|
|||• Recovers logo print setting to single color mode setting.|
||1, 49|Select 2-color printing mode|
|||This command selects 2-color print mode, when in single color print mode.|
|||This command is ignored already in the 2-color print mode.|
|||The specification of this command is not cleared by ESC @, CAN.|
|||The following processes are executed by selecting the 2-color print mode using this command.|
|||• Prints data in line buffer in the single color print mode, if unprinted data exists in the line|
|||buffer.|
|||• Waits to stop printing when printing in single-color print mode.|
|||• Initializes print color setting (2-color print mode setting)|
|||•Setslogo printsettingto2color mode setting.|



Invalid in page mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-93 
