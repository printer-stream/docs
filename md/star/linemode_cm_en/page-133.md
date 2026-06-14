**ESC GS / 1  n** [Name] Auto Logo Function On/Off Setting [Code] ASCII ESC GS / 1 n Hex. 1b 1d 2f 31 n Decimal 27 29 47 49 n 

[Defined Area] 0 ≤ n ≤ 2 [Initial Value] n = 0 [Function] Turns the Auto Logo function on and off. 

This command is registered to the non-volatile memory by the <ESC> <GS> / W command. When in raster mode, the Auto Logo function is invalid. 

This command is ignored when Auto Logo is being executed. 

|n|Setting|
|---|---|
|0|AutoLogoFunctionOFF|
|1|Standard Auto Logo Function ON<br><Operation Specifications><br>1. Start up the Auto Logo function using the current system cut command<br>as a trigger<br>2. Prints if there is print data in the image buffer<br>3. Executes user macro 1<br>4. Prints the Auto Logo<br>5. Executes user macro 2|
|2|Simple Auto Logo Function ON<br><Operation Specifications><br>1. Start up the Auto Logo function using the current system cut command<br>as a trigger<br>2. Prints if there is print data in the image buffer<br>3. Execute center alignment<br>4. Print Logo 2 (When 2 color printing is set: Logo3)<br>5. Feed paper to cutting position and executes a partial cut<br>6. Print Logo 1<br>7. Recover position alignment setting<br>Note:<br>• With this setting, user macro and command character are invalid.<br>(“/” is printed as a character if the command character is set to “/” when<br>setting.)|



The commands that are the triggers for the Auto Logo function are below. 

When the standard Auto Logo Function is turned on by n = 1, the following trigger commands function only as triggers and do not cut paper. Therefore, it is necessary to register any cut command to the user macro 2. When the simple Auto Logo Function is turned on by n = 2, the following cut commands are executed and are the triggers for the simple Auto Logo function. 

- <ESC> d n: Cut command 

- <FF>: When allocated to the cutting function 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-115 
