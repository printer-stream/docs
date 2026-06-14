Rev.2.52 

## **<Function 64> ESC GS ) B pL pH fn m k d1…dk (fn = 64)** 

|Name|Defne the text search string||||||||
|---|---|---|---|---|---|---|---|---|
|Code|ASCII<br>ESC<br>GS<br>)<br>B<br>pL<br>pH|fn|n|m|k|d1|...|dk|
||Hex.<br>1B<br>1D<br>29<br>42<br>pL<br>pH|fn|n|m|k|d1|...|dk|
||Decimal<br>27<br>29<br>41<br>66<br>pL<br>pH|fn|n|m|k|d1|...|dk|
|Defned Region|4≤(pL + pH x 256)≤65535  (0≤pL≤255, 0≤pH≤255)||||||||
||fn = 64||||||||
||1≤n≤100||||||||
||1≤m≤100||||||||
||0≤k≤32||||||||
||32≤d≤255||||||||
|Initial Value|Depends on setting registered in the non-volatile<br>defnition)|memory (At the time of||||shipment: no string|||
|Function|Defnes the text search string for number n.||||||||
||If the text search string for number n is already defned,||it is overwritten.||||||
||M specifes the text search macro number to run.||||||||
||K specifes the size of the defned data in bytes.||||||||
||d specifes the defned data.||||||||
||When the parameter has an invalid value, no defnition.||||||||
||This defnition is applied to printer operations when this||command is processed.||||||
||This defnition is registered to non-volatile memory by the ESC GS ) B <Function 80)||||||||
||command.||||||||
||This command is ignored when the text search macro is running.||||||||
||Disabled in Page Mode.||||||||



ESC/POS Command Specifications 

244 
