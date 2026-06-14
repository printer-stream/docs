## **C O N F I D E N T I A L** 

|ESC T**start**<br>**position**|**Start position/end position**|**Horizontal and vertical motion units**<br>**used**|
|---|---|---|
|Top left or<br>bottom right|X: Vertical in relation to paper feed direction<br>(horizontal direction of characters)|X: Horizontal (vertical in relation to paper<br>feed direction)|
||Y: Paper feed direction (vertical direction of<br>characters)|Y: Vertical (paper feed direction)|
|Top right or<br>bottom left|X: Paper feed direction (horizontal direction<br>of characters)|X: Vertical (paper feed direction)|
||Y: Vertical in relation to paper feed direction<br>(vertical direction of characters)|Y: Horizontal (vertical in relation to paper<br>feed direction)|



■ If the line width is 2 dots or more, the line is thickened according to the rules shown in the table below, based on the relationship between the specified start coordinate and end coordinate. However, line data that exceeds the printing area is not saved in the print buffer. 

|**Condition 1**|**Condition 2**|**Line thickening method**|
|---|---|---|
|Y start position = Y end<br>position<br>(Lines horizontal in relation to<br>characters)|X start position < X end<br>position|Thickened downward as seen with the<br>start position at top left|
||X start position > X end<br>position|Thickened upward as seen with the start<br>position at top left|
|X start position = X end<br>position<br>(Lines vertical in relation to<br>characters)|Y start position < Y end<br>position|Thickened rightward as seen with the<br>start position at top left|
||Y start position > Y end<br>position|Thickened leftward as seen with the start<br>position at top left|



■ When this function is executed, the printing position does not change. 
