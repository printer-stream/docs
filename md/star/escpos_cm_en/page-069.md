Rev.2.52 

## **ESC \ nL nH** 

|**ESC \ nL nH**||
|---|---|
|Name|Specify relative position|
|Code|ASCII<br>ESC<br>\<br>nL<br>nH|
||Hex.<br>1B<br>5C<br>nL<br>nH|
||Decimal<br>27<br>92<br>nL<br>nH|
|Defned Region|0≤nL≤255|
||0≤nH≤255|
|Function|• Specifes the next print starting position with a relative position based on the current position.|
||This sets the position from the current position to [(nL + nH x 256) x basic calculated pitch]|
||for the next print starting position.|
|Details|• Specifcations exceeding the print range are ignored.|
||• If the right direction of the current position is specifed for the character direction, specify a<br>positive number; if the left direction is specifed, a negative number is used.|



- Negative numbers is represented by the complement of 65536.  For example, when moving in the left direction n pitches, use: 

nL + nH × 256 = 65536-N 

- The basic calculated pitch is set by GSP (basic calculated pitch setting). • If there are fractions in the result, correct to the minimum mechanical pitch and discard. • Use the basic calculated pitch (x) for the horizontal direction in standard mode. 

- The following operations occur according to the starting point in page mode. 

- a. If the starting point is set to upper left or lower right by the ESC T (Select character print direction in page mode) command, specify the relative position of the vertical direction in the paper feed.  Use the basic calculated pitch (x) for the horizontal direction at this time. 

- b. If the starting point is set to upper right or lower left by the ESC T (Select character print direction in page mode) command, move the print position in the paper feed direction. Use the basic calculated pitch (y) for the horizontal direction at this time. 

Reference 

ESC $, GS P 

ESC/POS Command Specifications 

69 
