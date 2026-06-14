Rev.2.52 

## **ESC RS C n** 

|**ESC RS C n**|**ESC RS C n**|**ESC RS C n**|||||
|---|---|---|---|---|---|---|
|Name|||Print Mode Selection||||
|Code|||ASCII<br>ESC<br>RS<br>C||n||
||||Hex.<br>1B<br>1E<br>43||n||
||||Decimal<br>27|30<br>67|n||
|Defned Region|||<br>0≤n≤1<br>48|≤n≤49|||
||||n=16,n=32||||
|Initial||Value|---||||
|Function|||Selects print mode||||
|||n|Print Mode||||
|||0,48|Single color mode||||
|||1,49|2-color mode||||
|||16|Lowpower consumption mode||||
|||32|Double resolution mode||||
||||• This command is|ignored when low power consumption mode is selected.|||
||||• This command is|not cleared by ESC @.|||
||||• If there is unprinted data in the line bufer, the printing of the line bufer data will be executed.||||
||||• This command is|processed after the current printing has been completed.|||
||||• This command is|ignored when reduced printing in the vertical direction is setting.|||



ESC/POS Command Specifications 

187 
