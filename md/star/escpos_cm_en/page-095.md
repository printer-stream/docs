Rev.2.52 

## **GS ( L pL pH m fn [parameter] GS 8 L p1 p2 p3 p4 m fn [parameter]** 

|Name|Specify graphics|Specify graphics|data||||||||
|---|---|---|---|---|---|---|---|---|---|---|
|Code|ASCII|GS|(|L|pL|pH|m|fn|[parameter]||
||Hex.|1D|28|4C|pL|pH|m|fn|parameter]||
||Decimal|29|40|76|pL|pH|m|fn|[parameter]||
|Code|ASCII|GS|8|L|p1|p2|p3|p4|m<br>fn<br>[parameter]||
||Hex.|1D|38|4C|p1|p2|p3|p4|m<br>fn<br>[parameter]||
||Decimal|1D|29|56|76|p1|p2|p3|p4<br>m<br>fn|[parameter]|



- (*) Use the GS ( L code to explain each function. 

• GS ( L and GS 8 L are the same function. 

• If [parameter] in each function exceeds 65533 bytes, use GS 8 L. 

Function Runs the process related to the graphics data specified by the function code (fn). 

|fn|Code|Function<br>No.|Function|For STAR|
|---|---|---|---|---|
|0, 48|GS ( L pL pH m fn|48|Send NV graphics memory<br>capacity|Supported|
|2, 50|GS ( L pL pH m fn|50|Print raster graphics data|Receive and discard|
|3, 51|GS ( L pL pH m fn|51|Send remaining NV graph-<br>ics memorycapacity|Supported|
|64|GS ( L pL pH m fn d1 d2|64|Send NV graphics key<br>code|Supported|
|65|GS ( L pL pH m fn d1 d2 d3|65|Batch all delete NV graph-<br>ics data<br>|Supported|
|66|GS ( L pL pH m fn kc1 kc2|66|Delete the specifed NV<br>graphics data<br>|Supported|
|67|GS ( L pL pH m fn a kc1 kc2 b xL<br>xHyLyH[c d1...dk]1[c d1...dk]b|67|Defne NV graphics data<br>|Supported|
|69|GS ( L pL pH m fn a kc1 kc2 x y|68|Print the specifed NV<br>graphics data|Supported|
|112|GS ( L pL pH m fn a bx by c xL xH<br>yLyH d1...dk|112|Store raster graphics data|Supported|



ESC/POS Command Specifications 

95 
