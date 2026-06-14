## **3.3.11. Cu tter Control** 

## **ESC d n** 

[Name] Auto-cutter [Code] ASCII ESC d n Hex. 1B 64 n Decimal 27 100 n 

[Defined Area] 0≤d≤3 48≤d≤51 (”0”≤d≤”3”) [Initial Value] - - - [Function] Executes the auto-cutter. 

After auto-cutter is executed, the printer considers that to be the top of the page. 

|n|Auto cutter|
|---|---|
|0, 48|Full cut at the current position.<br>Print data in line buffer is printed before a full cut.<br>This command is ignored if the printer is not equipped with an auto-cutter.|
|1, 49|Partial cut at the current position.<br>Print data in line buffer is printed before a partial cut.<br>This commandisignoredifthe printer isnot equippedwithanauto-cutter.|
|2, 50|Paper is fed to cutting position, then a full cut.<br>Print data in line buffer is printed before the operation described above.<br>This commandisignoredifthe printer isnot equippedwithanauto-cutter.|
|3, 51|Paper is fed to cutting position, then a partial cut.<br>Print data in line buffer is printed before the operation described above.<br>This commandisignoredifthe printer isnot equippedwithanauto-cutter.|



(*) When connected with a presenter, executes a full cut when instructed for a partial cut. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-44 
