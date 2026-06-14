Rev.2.52 

## **ESC GS / 5 n** 

|**ESC GS**|**ESC GS**|**/ 5 n**|||
|---|---|---|---|---|
|Name|||Set command character switching method||
|Code|||ASCII<br>ESC<br>GS<br>/<br>5<br>n||
||||Hex.<br>1b<br>1d<br>2f<br>35<br>n||
||||Decimal<br>27<br>29<br>47<br>53<br>n||
|Defned Region<br>|||0≤n≤1||
|Initial Value<br>|||n = 0||
|Function||<br>|Sets the Auto Logo function command character switching method.||
||||This command is registered to the non-volatile memory by the “<ESC> <GS> / W” command.||
||||This command is ignored when Auto Logo is being executed.||
|||n|Setting||
|||0|Does notprint the command character and the followinglogo number||
|||1|Switches the command character and the following logo number into a space<br>character(0 x 20)||
||||When “/” is specifed as the command character, the “/2” embedded in the print data is not a||
||||character string, but processed as a command.||
||||At this time, “/2” is processed as a command is not printed.||
||||However, by specifying n = 1 in this command, it is possible to switch “/2” to a space.||
|Reference<br>|||ESC GS / W, ESC GS / C, ESC GS / 1, ESC GS / 2, ESC GS / 3, ESC GS / 4, ESC GS / 6||



ESC/POS Command Specifications 

214 
