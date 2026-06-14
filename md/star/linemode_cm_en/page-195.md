## **5.5. Appendix 8 TSP828L Cut Command Specifications** 

<Line Mode> 

|<Line Mode>|<Line Mode>||||
|---|---|---|---|---|
|Command||Normal Thermal Paper|Label Paper||
||||Tear Bar|Peel Mode|
|<FF>||Form Feed|Label Gap Detection|Label Gap Detection<br>+<br>Peeling Position<br>Conveyance|
|<ESC> d n|n = 0, 48<br>n = 1, 49<br>n = 2, 50<br>n = 3, 51<br>n = 116<br>(“t”)|Tear<br>Bar<br>Position<br>Conveyance<br>Tear<br>Bar<br>Position<br>Conveyance|Label Gap Detection<br>+<br>Tear Bar Position<br>Conveyance<br>Label Gap Detection<br>+<br>Tear Bar Position<br>Conveyance|Label Gap Detection<br>+<br>Peeling Position<br>Conveyance<br>Label Gap Detection<br>+<br>Peeling Position<br>Conveyance|



<Raster Mode FF/EOT> 

|<Raster Mode FF/EOT>|<Raster Mode FF/EOT>||||
|---|---|---|---|---|
|Command||Normal Thermal Paper|Label Paper||
||||Tear Bar|Peel Mode|
|Form Feed|Valid<br>Invalid|Print<br>Print|Print<br>+<br>Label Gap Detection<br>Print<br>+<br>LabelGapDetection|Print<br>+<br>Label Gap Detection<br>Print<br>+<br>LabelGapDetection|
|Cut Feed|Valid<br>Invalid|Tear Bar Position<br>Conveyance<br>---|Tear Bar Position<br>Conveyance<br>---|Peeling Position<br>Conveyance<br>Peeling Position<br>Conveyance|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-23 
