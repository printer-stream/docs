## **3.16. Page Mode Command Details** 

## **ESC GS P 0** 

|**ESC GS P 0**|**ESC GS P 0**|**ESC GS P 0**||
|---|---|---|---|
|[Name] Selects page mode|[Name] Selects page mode|||
|[Code]|ASCII|ESC GS|P<br>0|
||Hexadecima<br>1B<br>1D||50<br>30|
||l|||
||Decimal|27<br>29|80<br>48|
|[Function]||Switches from standard mode to page mode.|Switches from standard mode to page mode.|
|||• Valid only when input at the top of the line.||
|||• Invalid when input in page mode.||
|||• Returns to standard mode after running this command.||
|||• ESC GS P 1 (selects standard mode)|• ESC GS P 1 (selects standard mode)|
|||• ESC GS P 7 (prints in page mode and recovers)|• ESC GS P 7 (prints in page mode and recovers)|
|||• The character expansion position uses the starting point specified by ESC GS P2 (selection of||
|||character print direction in page mode) in the print region specified by ESC GS P 3 (set print|character print direction in page mode) in the print region specified by ESC GS P 3 (set print|
|||region in page mode).|region in page mode).|
|||• Switches the following command setting values that have independent values for both page and|• Switches the following command setting values that have independent values for both page and|
|||standard modes to the setting values of page mode.||
|||• Set space amount:<br>ESC SP , ESC : , ESC M, ESC P, ESC g, ESC p, ESC s, ESC t||
|||• Set the line feed amount:<br>ESC z, ESC 0, ESC 1, ESC 2,||
|||• Set horizontal tab:<br>ESC D||
|||• The following commands are invalid in page mode.||
|||• VT:|Vertical tab|
|||• FF:|Form feed|
|||• ESC GS c:|Reduced Printing|
|||• ESC GS ) B:|• ESC GS ) B:<br>Text Search|
|||• ESC RS m:|BM setting|
|||• ESC RS A:|Printing Region Setting|
|||• ESC GS M:|Maintenance counter control|
|||• ESC GS r:|Get CRC|
|||• ESC GS %:|User ID|
|||• ESC GS *:|Print Mark|
|||• ESC RS C:|Set printing mode|
|||• ESC * r:|Related to raster mode|
|||• ESC RS r:|Set print speed|
|||• ESC RS L:|Lump print of logos|
|||• ESC FS p:|Print logo|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-135 
