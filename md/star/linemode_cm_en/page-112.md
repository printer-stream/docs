## Specification B 

|n|Select/cancel 2colorprintmode|
|---|---|
|0, 48|Cancel 2-color printing mode<br>When in two-color print mode, this command cancels 2-color printing mode.<br>This command is ignored when the 2-color print mode is already cancelled.<br>The specification of this command is not cleared by ESC @, CAN.<br>The following processes are executed by canceling the 2-color print mode using this<br>command.<br>• Prints data in line buffer in 2-color print mode, if unprinted data exists in the line buffer.<br>• Waits to stop printing when printing in 2-color print mode.<br> •Recovers logo print setting to single color mode setting.|
|1, 49|Select 2-color printing mode<br>This command selects 2-color print mode, when in single color print mode.<br>This command is ignored already in the 2-color print mode.<br>The specification of this command is not cleared by ESC @, CAN.<br>The following processes are executed by selecting the 2-color print mode using this command.<br>• Prints data in line buffer in the single color print mode, if unprinted data exists in the line<br>buffer.<br>• Waits to stop printing when printing in single-color print mode.<br>• Initializes print color setting (2-color print mode setting)<br>•Setslogo print setting to2color mode setting.|



## Specification C 

|n|Specify printmode|
|---|---|
|0, 48|Single color print mode|
|1,49|2-colorprintmode|
|2, 50|Dot compatible2-color mode|
|16|Lowpowerconsumption mode|
|32|Doubleresolution mode|



- If set to the low power consumption mode using the DIP switches, this command is ignored. 

- This command is not cleared by ESC @, CAN. 

- When there is unprinted data in the line buffer, print the line buffer data. 

- This command is processed after ending the current print job. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-94 
