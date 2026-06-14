**<Function 64> ESC GS ) B pL pH fn m k d1…dk (fn = 64)** 

|[Name]|Define the text search string|Define the text search string||||||
|---|---|---|---|---|---|---|---|
|[Code]|ASCII|ESC GS<br>)<br>B<br>pL|pH<br>fn<br>n|m|k|d1|... dk|
||Hexadecimal<br>1B<br>1D<br>29<br>42<br>pL||pH<br>fn<br>n|m|k|d1|... dk|
||Decimal|27<br>29<br>41<br>66<br>pL|pH<br>fn<br>n|m|k|d1|... dk|
|[Defined Area]||4≤<br> (pL + pH x 256)≤<br> 65535  (0≤<br>|pL≤<br> 255, 0≤<br>|pH≤<br>|255)|||
|||fn = 64||||||
|||1≤<br> n≤<br> 100||||||
|||1≤<br> m≤<br> 100||||||
|||0≤<br> k≤<br> 32||||||
|||32≤<br>d≤<br> 255||||||
|[Initial Value]||Depends on setting registered in the non-volatile memory (At the time of shipment: no string|Depends on setting registered in the non-volatile memory (At the time of shipment: no string||||Depends on setting registered in the non-volatile memory (At the time of shipment: no string|
|||definition)||||||
|[Function]|[Function]|Defines the text search string for number n.||||||
|||If the text search string for number n is already defined, it is overwritten.||If the text search string for number n is already defined, it is overwritten.||||
|||M specifies the text search macro number to run.|M specifies the text search macro number to run.|||||
|||K specifies the size of the defined data in bytes.|K specifies the size of the defined data in bytes.|||||
|||D specifies the defined data.||||||
|||When the parameter has an invalid value, no definition.||||||
|||This definition is applied to printer operations when this command is processed.|This definition is applied to printer operations when this command is processed.|||||
|||This definition is registered to non-volatile memory by the ESC GS ) B <Function 80) command.||||||
|||This command is ignored when the text search macro is running.||This command is ignored when the text search macro is running.||||
|||Disabled in Page Mode.||||||



**<Function 65> ESC GS ) B pL pH fn m k1 k2 d1…dk (fn = 65)** 

|[Name]|Define the text search macro|Define the text search macro|||||||
|---|---|---|---|---|---|---|---|---|
|[Code]|ASCII|ESC<br>GS<br>)<br>B<br>pL<br>pH|fn<br>m|k1||k2|d1|... dk|
||Hexadecimal<br>1B<br>1D 29<br>42<br>pL<br>pH||fn<br>m|k1||k2|d1|... dk|
||Decimal|27<br>29 41<br>66<br>pL<br>pH|fn<br>m|k1||k2|d1|... dk|
|[Defined Area]||4≤<br> (pL + pH x 256)≤<br> 65535  (0≤<br> pL≤<br>|255, 0≤<br>|pH≤<br>|255)||||
|||fn = 65|||||||
|||1≤<br> m≤<br> 100|||||||
|||0≤<br> (k = k1 + k2 x 256)≤<br> 7680  (0≤<br> k1≤|≤<br> 255, 0≤|≤<br> k2≤|≤<br>|30)|||
|||(Size of defined area = 7,680 bytes)|||||||
|||0≤<br> d≤<br> 255|||||||
|[Initial Value]||Depends on setting registered in the non-volatile memory (At the time of shipment: no text|Depends on setting registered in the non-volatile memory (At the time of shipment: no text||||||
|||search macro definition)|||||||
|[Function]|[Function]|Defines the text search macro for number m.|||||||
|||If the text search macro for number m is already defined, it is overwritten.|If the text search macro for number m is already defined, it is overwritten.||||If the text search macro for number m is already defined, it is overwritten.||
|||(k = k1 + k2 x 256) specifies the size of the defined data in bytes.|||||(k = k1 + k2 x 256) specifies the size of the defined data in bytes.|(k = k1 + k2 x 256) specifies the size of the defined data in bytes.|
|||d specifies the defined data.|||||||
|||If the parameter has an invalid value, processing of this command ends at that point.|||||||
|||This definition is applied to printer operations when this command is processed.|||||||
|||This definition is registered to non-volatile memory by the ESC GS ) B <Function 80) command.|||||||
|||This command is ignored when the text search macro is running.||This command is ignored when the text search macro is running.||This command is ignored when the text search macro is running.||This command is ignored when the text search macro is running.|
|||Disabled in Page Mode.|||||||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-144 
