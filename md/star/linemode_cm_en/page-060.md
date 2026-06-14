## **3.3.10. Bar Code** 

## **ESC b n1 n2 n3 n4 d1...dk RS** 

[Name] [Code] ASCII ESC b n1 n2 n3 n4 d1 ... dk RS Hex. 1B 62 n1 n2 n3 n4 d1 ... dk 1E Decimal 27 98 n1 n2 n3 n4 d1 ... dk 30 [Defined Area] 0≤n1≤8,  48≤n1≤56 (”0≤n1≤”8”) 1≤n2≤4,  49≤n2≤52 (”1”≤n2≤”4”) 1≤n4≤255 n3 (bar code mode), d (bar code data), k (bar code data count) definitions differ according to the type of bar code. [Initial Value] - - - [Function] Bar code printing is executed according to the following parameters. 

If n1, n2, n3 and n4 are acquired and detected to be out of the defined area, data up to RS is discarded. 

• n1 bar code type selection 

|n1|Barcode type|
|---|---|
|0,48|UPC-E|
|1,49|UPC-A|
|2, 50|JAN/EAN8|
|3, 51|JAN/EAN13|
|4, 52|Code39|
|5, 53|ITF|
|6, 54|Code128|
|7, 55|Code93|
|8, 56|NW-7|



• n2 Under-bar character selection and added line feed selection 

|n2|Under-barcharacterselectionand addedlinefeed selection|
|---|---|
|1, 49|No added under-bar characters Executes line feed after printing a bar code|
|2, 50|Adds under-barcharacters<br>Executeslinefeed afterprinting a barcode|
|3, 51|No added under-barcharactersDoesnot executelinefeed afterprinting a barcode|
|4, 52|Adds under-barcharacters<br>Doesnot executelinefeed afterprinting a barcode|



• n3 bar code mode selection 

|~~a~~|~~**e**ee~~|~~**e**ee~~|~~**e**ee~~|
|---|---|---|---|
|n3<br>~~a~~|Bar code type<br>~~**e**ee~~<br>~~e~~|||
||UPC-E, UPC-A, JAN/EAN8<br>JAN/EAN13, Code128, Code93<br>~~**e**ee~~|Code39, NW-7<br>~~e~~|ITF<br>~~e~~|
|1, 49<br>~~a ~~<br>~~eG~~|Minimum module 2 dots<br> ~~**e**ee~~<br>~~eG~~|Narrow: Wide=2:6 dots<br>~~eG~~|Narrow: Wide=2:5 dots<br>~~eG~~|
|2, 50<br>~~a~~|Minimum module 3 dots|Narrow: Wide=3:9 dots|Narrow: Wide= 4:10 dots|
|3, 51<br>~~a~~|Minimum module4dots<br>|Narrow: Wide= 4:12dots<br>|Narrow: Wide=6:15 dots<br>|
|4, 52<br>~~eG~~<br>~~es~~|- - -<br>~~eG~~<br>|Narrow: Wide= 2:5 dots<br>~~eG~~<br>|Narrow: Wide= 2:4dots<br>~~eG~~<br>|
|5, 53<br>~~es~~|- - -<br>|Narrow: Wide=3:8 dots<br>|Narrow: Wide=4:8 dots<br>|
|6, 54<br>~~essD~~|- - -<br>~~sD~~|Narrow: Wide= 4:10 dots<br>~~sD~~|Narrow: Wide=6:12dots<br>~~sD~~|
|7, 55<br>~~a~~|- - -|Narrow: Wide= 2:4dots|Narrow: Wide= 2:6 dots|
|8, 56<br>~~a~~<br>~~a~~|- - -|Narrow: Wide=3:6 dots|Narrow: Wide=3:9 dots|
|9, 57<br>~~a~~|- - -|Narrow: Wide= 4:8 dots|Narrow: Wide= 4:12dots|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-42 
