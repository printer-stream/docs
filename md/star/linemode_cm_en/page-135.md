|**ESC GS /  3  nL  nH  d1 d2 … dk**|**ESC GS /  3  nL  nH  d1 d2 … dk**|**ESC GS /  3  nL  nH  d1 d2 … dk**|**ESC GS /  3  nL  nH  d1 d2 … dk**|**ESC GS /  3  nL  nH  d1 d2 … dk**||||
|---|---|---|---|---|---|---|---|
|[Name]|Set user macro 1|||||||
|[Code]|ASCII|ESC GS<br>/|3<br>nL<br>nH|d1|d2|...|dk|
||Hex.|1b<br>1d<br>2f|33<br>nL<br>nH|d1|d2|...|dk|
||Decimal<br>27<br>29<br>47||51<br>nL<br>nH|d1|d2|...|dk|
|[Defined Area]||1≤<br> n≤<br>64||||||
|||nH = 0||||||
|||1≤<br> (nL + nH x 256)≤<br>|64|||||
|||dk = (nL + nH x 256)|dk = (nL + nH x 256)|||||
|||0≤<br> d≤<br>255||||||
|[Initial Value]||No user macro 1 setting||||||
|[Function]||Sets the user macro 1 of the Auto Logo function.|Sets the user macro 1 of the Auto Logo function.|||||
|||This command is registered to the non-volatile memory by the “<ESC> <GS> / W” command.|||||This command is registered to the non-volatile memory by the “<ESC> <GS> / W” command.|
|||This command is ignored when Auto Logo is being executed.||||This command is ignored when Auto Logo is being executed.||
|||Registers print data in user macro 1.|Registers print data in user macro 1.|||||
|||A maximum of 64 bytes of data can be registered.||||||
|||Note that it is prohibited to register Auto Logo command characters in a user macro.||||||



|**ESC GS /  4  nL  nH  d1 d2 … dk**|**ESC GS /  4  nL  nH  d1 d2 … dk**|**ESC GS /  4  nL  nH  d1 d2 … dk**|**ESC GS /  4  nL  nH  d1 d2 … dk**|**ESC GS /  4  nL  nH  d1 d2 … dk**||||
|---|---|---|---|---|---|---|---|
|[Name]|Set user macro 2|||||||
|[Code]|ASCII|ESC GS<br>/|4<br>nL<br>nH|d1|d2|...|dk|
||Hex.|1b<br>1d<br>2f|34<br>nL<br>nH|d1|d2|...|dk|
||Decimal<br>27<br>29<br>47||52<br>nL<br>nH|d1|d2|...|dk|
|[Defined Area]||1≤<br> nL≤<br> 64||||||
|||nH = 0||||||
|||1≤<br> (nL + nH x 256)≤<br>|64|||||
|||dk = (nL + nH x 256)|dk = (nL + nH x 256)|||||
|||0≤<br> d≤<br>255||||||
|[Initial Value]||No user macro 2 setting||||||
|[Function]||Sets the user macro 2 of the Auto Logo function.|Sets the user macro 2 of the Auto Logo function.|||||
|||This command is registered to the non-volatile memory by the “<ESC> <GS> / W” command.|||||This command is registered to the non-volatile memory by the “<ESC> <GS> / W” command.|
|||This command is ignored when Auto Logo is being executed.||||This command is ignored when Auto Logo is being executed.||
|||Registers print data in user macro 2.|Registers print data in user macro 2.|||||
|||A maximum of 64 bytes of data can be registered.||||||
|||Note that it is prohibited to register Auto Logo command characters in a user macro.||||||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-117 
