## **ESC * r F n NUL** 

[Name] Set raster FF mode [Code] ASCII ESC * r F n NUL Hex. 1B 2A 72 46 n 00 Decimal 27 42 114 70 n 0 

[Defined Area] n = 0, 1, 2, 3, 8, 9, 12, 13, 36, 37 [Initial Value] Models handling full cut: n = 9 

Models connected with a presenter: n = 37 [Function] Sets raster FF mode. 

The FF mode operates to execute using the raster document quit command (ESC FF NUL). n is a decimal description (max. 255 digits) using ASCII characters. Invalid in page mode. 

|n<br>~~a~~<br>~~es~~|FormFeed<br>~~es~~<br>~~eG~~|Cut Feed<br>~~Df~~<br>~~eG~~|Cutter<br>~~Df~~|Presenter|
|---|---|---|---|---|
|0<br>~~a ~~<br>~~es~~<br>~~es~~|SetToDefault<br> ~~es~~<br>~~eG~~<br>~~GG~~|SetToDefault<br>~~Df~~<br>~~eG~~<br>~~GG~~|SetToDefault<br>~~Df~~<br>~~GG~~|SetToDefault<br>~~GG~~|
|1<br>~~es~~<br>~~es~~<br>~~ee~~|○<br>~~eG~~<br>~~GG~~<br>~~ee~~|--<br>~~eG~~<br>~~GG~~<br>~~GG~~|--<br>~~GG~~<br>~~GG~~|--<br>~~GG~~|
|2<br>~~es~~<br>~~ee~~<br>~~Rs~~<br>~~a~~|○<br>~~GG~~<br>~~ee~~<br>~~GD~~|○<br>~~GG~~<br>~~GG~~<br>~~GD~~|--<br>~~GG~~<br>~~GG~~<br>~~GD~~<br>~~QO~~|--<br>~~GG~~<br>~~GD~~|
|3<br>~~ee~~<br>~~Rs~~<br>~~a~~|○<br>~~ee~~<br>~~GD~~|TearBar<br>~~GG~~<br>~~GD~~|--<br>~~GG~~<br>~~GD~~<br>~~QO~~|--<br>~~GD~~|
|8<br>~~Rs~~<br>~~a~~|○<br>~~GD~~|--<br>~~GD~~|FullCut<br>~~GD~~<br>~~QO~~|--<br>~~GD~~|
|9<br>~~a~~<br>~~a eG~~<br>~~es~~|○<br>~~eG~~<br>~~GG~~|○<br>~~eG~~<br>~~GG~~|FullCut<br>~~QO~~<br>~~eG~~<br>~~GG~~|--<br>~~eG~~<br>~~GG~~|
|12<br>~~es~~<br>~~ee~~|○<br>~~GG~~<br>~~ee~~|--<br>~~GG~~<br>~~GG~~|PartialCut<br>~~GG~~<br>~~GG~~|--<br>~~GG~~|
|13<br>~~es~~<br>~~ee~~|○<br>~~GG~~<br>~~ee~~|○<br>~~GG~~<br>~~GG~~|PartialCut<br>~~GG~~<br>~~GG~~|--<br>~~GG~~|
|36<br>~~ee~~<br>~~a~~|○<br>~~ee~~<br>|--<br>~~GG~~<br>|FullCut<br>~~GG~~<br>|Eject<br>|
|37<br>~~GF~~|○<br>~~GF~~|○<br>~~GF~~|FullCut<br>~~GF~~|Eject<br>~~GF~~|



Specification B <FF mode setting format> 

|n<br>~~a~~<br>~~Rs~~|FormFeed<br>~~se~~|CutFeed<br>~~se~~|Cutter<br>~~se~~|Presenter<br>~~se~~|
|---|---|---|---|---|
|0<br>~~Rs~~|SetToDefault|SetToDefault|SetToDefault|SetToDefault|
|1<br>~~Rs~~<br>~~a~~|○(*1)<br>~~eG~~|--<br>~~eG~~|--<br>~~eG~~|--<br>~~eG~~|
|2<br>~~a eG~~<br>~~es~~|○(*1)<br>~~eG~~<br>~~GG~~|○<br>~~eG~~<br>~~GG~~|--<br>~~eG~~<br>~~GG~~|--<br>~~eG~~<br>~~GG~~|
|3<br>~~es~~<br>~~ee~~|○(*1)<br>~~GG~~<br>~~ee~~|TearBar<br>~~GG~~<br>~~GG~~|--<br>~~GG~~<br>~~GG~~|--<br>~~GG~~|
|8<br>~~es~~<br>~~ee~~|○(*1)<br>~~GG~~<br>~~ee~~|--<br>~~GG~~<br>~~GG~~|FullCut<br>~~GG~~<br>~~GG~~|--<br>~~GG~~|
|9<br>~~ee~~<br>~~a~~|○(*1)<br>~~ee~~|○<br>~~GG~~|FullCut<br>~~GG~~|--|
|12<br>~~a~~|○(*1)<br>~~eG~~|--<br>~~eG~~|PartialCut<br>~~eG~~|--<br>~~eG~~|
|13<br>~~es~~|○(*1)<br>~~GG~~|○<br>~~GG~~|Partial Cut<br>~~GG~~|--<br>~~GG~~|
|36<br>~~es~~<br>~~es~~|○(*1)<br>~~GG~~<br>~~GG~~|--<br>~~GG~~<br>~~GG~~|FullCut<br>~~GG~~<br>~~GG~~|Eject<br>~~GG~~<br>~~GG~~|
|37<br>~~es~~<br>~~es~~|○(*1)<br>~~GG~~<br>~~GG~~|○<br>~~GG~~<br>~~GG~~|FullCut<br>~~GG~~<br>~~GG~~|Eject<br>~~GG~~<br>~~GG~~|



When the printer is a model handling BM and is set for BM to be effective, the set raster mode page length is ignored and BM detecting is performed. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-74 
