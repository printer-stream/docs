## **ESC GS P 4 nL nH** 

|**ESC GS P 4 nL nH**|**ESC GS P 4 nL nH**|**ESC GS P 4 nL nH**|
|---|---|---|
|[Name] Specify character vertical direction absolute position in page mode|[Name] Specify character vertical direction absolute position in page mode||
|[Code]|ASCII|ESC GS<br>P<br>4|
||Hexadecima<br>1B<br>1D<br>50<br>34||
||l||
||Decimal|Decimal<br>27<br>29<br>80<br>52|
|[Defined Area]|[Defined Area]|0≤<br> nL≤<br> 255, 0≤<br> nH≤<br> 255|
|[Initial Value]||- - -|
|[Function]||Specify the position for character vertical direction of the data expansion starting position in page|
|||mode with the absolute position that uses the starting point as a reference.|
|||The position of the character vertical direction of the starting position for subsequent data|
|||expansion uses the position from the starting point [(nL + nH x 256) x 1/8]mm.|
|||• This command is ignored when page mode is not selected.|
|||• Absolute position specifications that exceed the specified print region are ignored.|
|||• The position of the character horizontal direction of the data expansion starting position does not|
|||move.|
|||• Specify the reference starting point using ESC GS P 2.|
|||• The following operations will occur depending on the starting point of ESC GS P 2|
|||(select character print direction in page mode).|
||a. When the starting point is “upper left” or “bottom right,” specify the absolute position of the paper feed||
||direction.||
||b. When the starting point is “upper right” or “bottom left,” specify the absolute position of the|b. When the starting point is “upper right” or “bottom left,” specify the absolute position of the|
||perpendicular direction to the paper feed.||



• If the calculated results is a fraction, that is corrected to the minimum mechanical pitch and excess is discarded. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-139 
