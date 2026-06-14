Rev.2.52 

## **ESC GS / 1 n** 

|**ESC GS / 1 n**||
|---|---|
|Name|Auto Logo Function On/Of Setting|
|Code|ASCII<br>ESC  GS<br>/<br>1<br>n|
||Hex.<br>1b<br>1d<br>2f<br>31<br>n|
||Decimal<br>27<br>29<br>47<br>49<br>n|
|Defned Region|0≤n≤2|
|Initial Value|n = 0|
|Function|Turns the Auto Logo function on and of.|
||This command is registered to the non-volatile memory by the “<ESC> <GS> / W” command.|
||When in page mode, the Auto Logo function is invalid.|
||This command is ignored when Auto Logo is being executed.|



|Initial Value<br> <br>Function<br> <br> <br> <br>|n = 0<br>Turns the Auto Logo function on and of.<br>This command is registered to the non-volatile memory by the “<ESC> <GS> / W” c<br>When in page mode, the Auto Logo function is invalid.<br>This command is ignored when Auto Logo is being executed.|
|---|---|
|n|Setting<br>|
|0|Auto Logo Function Of|
|1|<br>Standard Auto Logo Function ON<br><Operation Specifcations><br>1. Starts up the Auto Logo function using the current system cut command as a<br>trigger<br>2. Prints if there is print data in the image bufer<br>3. Executes user macro 1<br>4. Prints Auto Logo<br>5. Executes user macro 2|
|2|Simple Auto Logo Function ON<br><Operation Specifcations><br>1. Starts up the Auto Logo function using the current system cut command as a<br>trigger<br>2. Prints if there is print data in the image bufer<br>3. Execute center alignment<br>4. Print Logo 2 (When 2 color printing is set: Logo3)<br>5. Feed paper to cutting position and execute a partial cut<br>6. Print Logo 1<br>7. Recover position alignment setting<br>Note: • With this setting, user macro and command character are invalid.<br> (“/” isprinted as a character if the command character is set to “/” when setting.)|



The commands that are the triggers for the Auto Logo function are below. 

When the standard Auto Logo Function is turned on by n = 1, the following trigger commands function only as triggers and do not cut paper.  Therefore, it is necessary to register any cut command to the user macro 2. 

When the simple Auto Logo Function is turned on by n = 2, the following cut commands are executed and are the triggers for the simple Auto Logo function. 

•<GS> V m:  Cut command 

• <GS> V m n:  Cut command 

•<ESC> i:  Full cut command (not recommended) 

- •<ESC> m:  Partial cut command (not recommended) 

Reference ESC GS / W, ESC GS / C, ESC GS / 2, ESC GS / 3, ESC GS / 4, ESC GS / 5, ESC GS / 6 

ESC/POS Command Specifications 

210 
