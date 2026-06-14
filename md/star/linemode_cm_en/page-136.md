## **ESC GS / 5  n** 

|[Name]|Set command character switching method|Set command character switching method|Set command character switching method|Set command character switching method|Set command character switching method|Set command character switching method|
|---|---|---|---|---|---|---|
|[Code]|ASCII||ESC GS|ESC GS||ESC GS<br>/<br>5<br>n|
||Hex.||1b|1d||1d<br>2f<br>35<br>n|
||Decimal||27|29||29<br>47<br>53<br>n|
|[Defined Area]||0≤<br>|n≤<br>1||||
|[Initial Value]||n = 0|n = 0||||
|[Function]||Sets the Auto Logo function command character switching method.|||Sets the Auto Logo function command character switching method.||
|||This command is registered to the non-volatile memory by the “<ESC> <GS> / W” command.|||||
|||This command is ignored when Auto Logo is beingexecuted.|||||
|||n||||Setting|
|||0||||Does not print the command character and the following logo number|
|||1||||Switches the command character and the following logo number into a space|
|||||||character(0x 20)|



When “/” is specified as the command character, the “/2” embedded in the print data is not a character string, but processed as a command. 

At this time, “/2” is processed as a command is not printed. 

However, by specifying n = 1 in this command, it is possible to switch “/2” to a space. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-118 
