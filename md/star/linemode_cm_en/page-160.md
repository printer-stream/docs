## **3.17. Text Search Command Details** 

## **ESC GS ) B pL pH fn [parameter]** 

[Name] Set text search [Code] ASCII ESC ) B pL pH fn [parameter] Hexadecimal 1B 29 42 pL pH fn [parameter] Decimal 27 41 66 pL pH fn [parameter] [Function] Runs processes related to text search. 

• pL and pH specify the parameter count (pL + pH x 256) in bytes after fn. 

- See the function specifications for details on [parameter]. 

|fn|Function No.|Function Name|
|---|---|---|
|48|Function 48|Enable and disables text search|
|49|Function 49|Set the number of times to run the text search macro|
|50|Function 50|Set toprint the stringthat matches in the text search|
|64|Function 64|Define the text search string|
|65|Function 65|Define the text search macro|
|80|Function 80|Register text search settings and definitions in the non-volatile memory|
|81|Function 81|Initialize text search settings and definitions|
|96|Function 96|Print the text search settings and definitions|
|97|Function 97|Run the text search macro|



## **<Function 48> ESC GS ) B pL pH fn m  (fn = 48)** 

|[Name]|Enable and disables text search|Enable and disables text search|Enable and disables text search|Enable and disables text search||||||
|---|---|---|---|---|---|---|---|---|---|
|[Code]|ASCII|ESC GS||)|B|pL|pH|fn|m|
||Hexadecimal||1B<br>1D|29|42|pL|pH|fn|m|
||Decimal||27<br>29|41|66|pL|pH|fn|m|
|[Defined Area]||pL = 2, pH = 0|pL = 2, pH = 0|||||||
|||fn = 48|fn = 48|||||||
|||m = 0, 1|m = 0, 1|||||||
|[Initial Value]||Depends on setting registered in the non-volatile memory (At the time of shipment: m = 0)|||||Depends on setting registered in the non-volatile memory (At the time of shipment: m = 0)|Depends on setting registered in the non-volatile memory (At the time of shipment: m = 0)||
|[Function]|[Function]|Makes text searches valid or invalid.|Makes text searches valid or invalid.|||Makes text searches valid or invalid.||Makes text searches valid or invalid.||



m Set 0 Invalid 1 Valid When text search is valid, determines whether a string registered in the printer in advance is in the print data. If it is included, run a text search macro that corresponds to that string after running the following trigger command. • Execute cuts by continous <LF>. • <ESC> “d” No setting when the parameter is not a valid value. This setting is applied to printer operations when this command is processed. This setting is registered to non-volatile memory by the ESC GS ) B <Function 80) command. This command is ignored when the text search macro is running. Disabled in Page Mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-142 
