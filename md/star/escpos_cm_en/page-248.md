Rev.2.52 

## **<Function 81> ESC GS ) B pL pH fn m  (fn = 81)** 

|Name|Initialize text search settings|Initialize text search settings|Initialize text search settings|and defnitions|and defnitions|and defnitions|||
|---|---|---|---|---|---|---|---|---|
|Code|ASCII<br>ESC|GS|)|B|pL|pH|fn|m|
||Hex.<br>1B|1D|29|42|pL|pH|fn|m|
||Decimal<br>27|29|41|66|pL|pH|fn|m|
|Defned Region|pL = 2, pH = 0||||||||
||fn = 81||||||||
||m = 0||||||||
|Initial Value|---||||||||
|Function|Initialize text search settings|||and defnitions|||||
||The following shows the||contents to initialize.||||||



|Function No|Contents|Initial Value|
|---|---|---|
|Function 48|Enable and disables text search|Invalid|
|Function 49|Set the number of times to run the text search macro|1 time|
|Function 50|Set toprint the stringthat matches in the text search|Prints the string|
|Function 64|Defne the text search string|No text search stringdefnition|
|Function 65|Defne the text search macro|No text search macro defnition|
|Function 66|Defne the timingof the text search macro execution|soon after cutting|



This setting is applied to printer operations when this command is processed. 

This setting is registered to non-volatile memory by the ESC GS ) B <Function 80) command. This command is ignored when the text search macro is running. Disabled in Page Mode. 

ESC/POS Command Specifications 

248 
