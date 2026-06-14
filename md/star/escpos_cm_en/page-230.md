Rev.2.52 

## **ESC GS y S 0 n** 

Name Set QR code model Code ASCII ESC GS y S 0 n Hex. 1B 1D 79 53 30 n Decimal 27 29 121 83 48 n 1 ≤ n ≤ 2 Defined Area Initial Value n = 2 Function Sets the model. • Parameter details n Set Model 1 Model 1 2 Model 2 

## **ESC GS y S 1 n** 

|Name|Set QR code mistake|Set QR code mistake|Set QR code mistake|correction level|correction level|correction level||
|---|---|---|---|---|---|---|---|
|Code|ASCII|ESC|GS|<br>Y|<br>S|1|n|
||Hex.|1B|1D|<br>79|<br>53|31|n|
||Decimal|27|29|121|<br>83|49|n|
|Defned Area|0≤n≤3|||||||
|Initial Value|n = 0|||||||
|Function|Sets the|mistake|correction||level.|||



• Parameter details 

||• Parameter details||
|---|---|---|
|n|Mistake Correction Level|Mistake Correction Rate(%)|
|0|L|7|
|1|M|15|
|2|Q|25|
|3|H|30|



## **ESC GS y S 2 n** 

|Name|Set QR code cell|size|||||
|---|---|---|---|---|---|---|
|Code|ASCII<br>ESC|GS|y|S|2|n|
||Hex.<br>1B|1D|79|53|32|n|
||Decimal<br>27|29|121|83|50|n|
|Defned Area|1≤n≤8||||||
|Initial Value|n = 3||||||
|Function|Sets the cell size.||||||
||• Parameter details||||||
||• n: Cell size (Units: Dots)||||||
||• It is recommended that the specifcation|||||using this command be 3≤n.|
||If n = 1 or 2, check by actually using.||||||



ESC/POS Command Specifications 

230 
