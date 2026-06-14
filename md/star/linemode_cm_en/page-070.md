## **ESC RS r n** 

[Name] Set print speed [Code] ASCII ESC RS r n Hex. 1B 1E 72 n Decimal 27 30 114 n 

[Defined Area] 0≤n≤3 48≤n≤51 (”0”≤n≤”3”) [Initial Value] Memory switch setting [Function] Sets print speed. This command stops printing to be executed. 

Because two-color print mode, low peak current mode, and double resolution mode print in one speed, the speed settings with this command are invalid. 

This command setting becomes valid when returned from the two-color print mode, low peak current mode, and double resolution mode to the single color print mode. Invalid in page mode. 

Spec. A 

**==> picture [411 x 117] intentionally omitted <==**

**----- Start of picture text -----**<br>
|||||||
|---|---|---|---|---|---|
|n|Print Speed|
|Single Color Printing Mode|Two Color Printing Mode|
|Low Peak Current Mode|
|Double Resolution|
|(*) Installed print mode depends on the|
|model.|
|a|0, 48|High speed|Each print mode speed|
|a|1, 49|Mid-speed|Each print mode|speed|
|a|2,|50|Slow speed|Each print mode|speed|
|3, 51|Option-speed|Each print mode speed|
|(*) Print|speed|depends|on the model.|

**----- End of picture text -----**<br>


## Spec. B 

**==> picture [411 x 110] intentionally omitted <==**

**----- Start of picture text -----**<br>
|||||||
|---|---|---|---|---|---|
|n|Print Speed|
|Single Color Printing Mode|Two Color Printing Mode|
|Low Peak Current Mode|
|Double Resolution|
|(*) Installed print mode depends on the|
|model.|
|0, 48|Standard|Each print mode speed|
|a|1, 49|Mid-speed|Each print mode|speed|
|a|2,|50|Slow speed|Each print mode|speed|
|3,|51|High speed|Each print mode|speed|
|Rs|

**----- End of picture text -----**<br>


――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-52 
