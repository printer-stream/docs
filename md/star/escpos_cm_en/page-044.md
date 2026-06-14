Rev.2.52 

## **ESC $ nL nH** 

|**ESC $ nL nH**||
|---|---|
|Name|Specify absolute position|
|Code|ASCII<br>ESC<br>$ nL<br>nH|
||Hex.<br>1B<br>24<br>nL<br>nH|
||Decimal<br>27<br>36<br>nL<br>nH|
|Defned Region|0≤nL≤255|
||0≤nH≤255|
|Function|Specifes the next printing starting position using an absolute position based on the left<br>margin position.  The next printing starting position is the position specifed by [(nL+nH×256)|
||× basic calculated pitch] from the left margin position.|
|Details|• Specifcations exceeding the print range are ignored.|
||• The basic calculated pitch is set by GSP (Set basic calculated pitch).|
||• If the calculation results in fractions, the pitch is corrected to a minimal mechanical pitch and|
||the rest is discarded.|
||• In standard mode, the basic calculated pitch (x) for the horizontal direction is used.|
||• In page mode, the basic calculated pitch that is used according to the starting point varies.|
||a. When the starting point is specifed to be upper left or lower right by the ESC T command|
||(Character print direction selection in page mode), the basic calculated pitch (x) for the|
||horizontal direction is used.|
||b. When the starting point is specifed to be upper right or lower left by the ESC T command|
||(Character print direction selection in page mode), the basic calculated pitch (y) for the|
||horizontal direction is used.|
|STAR|Top of line does not exist when this command is used to specify anything other than the left|
||margin position.  The top of the line is maintained only when the same position as the left<br>margin position is specifed.|
|Reference|ESC \ , GS $, GS \ , GS P|



ESC/POS Command Specifications 

44 
