## **ESC GS y S 0 n** 

[Name] Set QR code model [Code] ASCII ESC GS y S 0 n Hex. 1B 1D 79 53 30 n Decimal 27 29 121 83 48 n [Defined Area] 1 ≤ n ≤ 2 [Initial Value] n = 2 [Function] Sets the model. • Parameter details 

|n|SetModel|
|---|---|
|1|Model 1|
|2|Model 2|



## **ESC GS y S 1 n** 

[Name] Set QR code mistake correction level [Code] ASCII ESC GS y S 1 n Hex. 1B 1D 79 53 31 n Decimal 27 29 121 83 49 n [Defined Area] 0 ≤ n ≤ 3 [Initial Value] n = 0 [Function] Sets the mistake correction level. • Parameter details 

|n|Mistake Correction Level|Mistake Correction Rate (%)|
|---|---|---|
|0|L|7|
|1|M|15|
|2|Q|25|
|3|H|30|



## **ESC GS y S 2 n** 

[Name] Set QR code cell size [Code] ASCII ESC GS y S 2 n Hex. 1B 1D 79 53 32 n Decimal 27 29 121 83 50 n [Defined Area] 1 ≤ n ≤ 8 [Initial Value] n = 3 [Function] Sets the cell size. • Parameter details 

• n: Cell size (Units: Dots) 

• It is recommended that the specification using this command be 3 ≤ n. If n = 1 or 2, check by actually using. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-129 
