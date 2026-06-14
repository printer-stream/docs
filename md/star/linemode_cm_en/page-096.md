## **b  n1 n2 data** 

[Name] Send raster data (auto line feed) [Code] ASCII b n1 n2 d1 d2 ... dk Hex. 62 n1 n2 d1 d2 ... dk Decimal 98 n1 n2 d1 d2 ... dk 

[Defined Area] 0≤n1≤255 0≤n2≤255 0≤d≤255 k= n1+n2 x 256 1≤k 

[Initial Value] - - - [Function] Sends raster data (auto line feed). 

Raster data is sent in (n1 + n2 x 256) byte counts as binary data. Raster data exceeding the print area currently set is discarded. 

The image buffer expanded position is automatically line fed one dot row and moved to the left margin on the next line after expanded the image buffer data 1 dot row using this command. Also, data expansion is duplicated on the data in the current image buffer (OR process). The following shows expanded image buffer for the set raster print color. n is a decimal description (max. 255 digits) using ASCII characters. Invalid in page mode. 

|Print color|Expandedimage buffer|
|---|---|
|Black|Image buffer for black|
|Cyan|Image buffer forcolor|
|Magenta|Image buffer forcolor|
|Yellow|Image buffer forcolor|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-78 
