## **3.5. Black Mark Related Command Details** 

The following commands control top of form functions using black mark paper. The following commands are effective only when black mark is set to be effective. 

## **ESC d n** 

|[Name]|Auto cutter|Auto cutter||
|---|---|---|---|
|[Code]|ASCII|ESC<br>d|n|
||Hex.|1B<br>64|n|
||Decimal|27 100|n|
|[Defined Area]||0≤<br>d≤<br>3||
|||48≤<br>d≤<br>51 (”0”≤<br>d≤<br>”3”)||
|[Initial Value]||- - -||
|[Function]|[Function]|Executes the auto-cutter.|Executes the auto-cutter.|



After auto-cutter is executed, the printer considers that to be the top of the page. 

|n|Auto cutter||
|---|---|---|
|0, 48|Full cut at the current position.||
||Print data in line buffer is printed before a full cut.||
||This commandisignoredifthe printer isnot equippedwithanauto-cutter.||
|1, 49|Partial cut at the current position.||
||Print data in line buffer is printed before a partial cut.||
||This commandisignoredifthe printer isnot equippedwithanauto-cutter.||
|2, 50|After executing top of form, paper is fed to cutting position, then a full cut.||
||Print data in line buffer is printed before the operation described above.||
||This command is ignored if the printer is not equipped with an auto-cutter.||
|3, 51|After executing top of form, paper is fed to cutting position, then a partial cut.||
||Print data in line buffer is printed before the operation described above.||
||This commandisignoredif the printer isnotequippedwithanauto-cutter.||
||(*) The auto-cutter function operates in the following ways on models that only have a full cut or a|(*) The auto-cutter function operates in the following ways on models that only have a full cut or a|
||partial cut.||
||• Models that perform only a full cut:<br>Executes a full cut when for instructions calling||
||for a partial cut.||
||• Models that perform only a partial cut:<br>Executes a partial cut when there are for||
||instructions calling for a full cut.||
||(*) When connected with a presenter, executes a full cut when instructed for a partial cut.||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-87 
