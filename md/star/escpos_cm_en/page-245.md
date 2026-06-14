Rev.2.52 

## **<Function 65> ESC GS ) B pL pH fn m k1 k2 d1…dk (fn = 65)** 

|Name|Defne the text search macro||||||
|---|---|---|---|---|---|---|
|Code|ASCII<br>ESC<br>GS<br>)<br>B<br>pL<br>pH<br>fn<br>m|k1|k2|d1|...|dk|
||Hex.<br>1B<br>1D<br>29<br>42<br>pL<br>pH<br>fn<br>m|k1|k2|d1|...|dk|
||Decimal<br>27<br>29<br>41<br>66<br>pL<br>pH<br>fn<br>m|k1|k2|d1|...|dk|
|Defned Region|4≤(pL + pH x 256)≤65535  (0≤pL≤255, 0≤pH≤255)||||||
||fn = 65||||||
||1≤m≤100||||||
||0≤(k = k1 + k2 x 256)≤7680  (0≤k1≤255, 0≤k2≤30)||||||
||(Size of defned area = 7,680 bytes)||||||
||0≤d≤255||||||
|Initial Value|Depends on setting registered in the non-volatile memory (At the time of shipment: no text<br>search macro defnition)||||||
|Function|Defnes the text search macro for number m.||||||
||If the text search macro for number m is already defned, it is overwritten.||||||
||(k = k1 + k2 x 256) specifes the size of the defned data in bytes.||||||
||d specifes the defned data.||||||
||If the parameter has an invalid value, processing of this command||ends at that||point.||
||This defnition is applied to printer operations when this command||is processed.||||
||This defnition is registered to non-volatile memory by the ESC GS ) B <Function 80)||||||
||command.||||||
||This command is ignored when the text search macro is running.||||||
||Disabled in Page Mode.||||||



ESC/POS Command Specifications 

245 
