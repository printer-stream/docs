## **ESC GS x S 0 n p1 p2** 

[Name] Set PDF417 bar code size [Code] ASCII ESC GS x S 0 n p1 p2 Hex. 1B 1D 78 53 30 n p1 p2 Decimal 27 29 120 83 48 n p1 p2 [Defined Area] n = 0, 1 

When n = 0: 1 ≤ p1 ≤ 99, 1 ≤ p2 ≤ 99 When n = 1: p1 = 0 or 3 ≤ p1 ≤ 90, p2 = 0 or 1 ≤ p2 ≤ 30 (However, this excludes p1 = p2 = 0) 

[Initial Value] n = 0, p1 = 1, p2 = 2 [Function] Parameter details 

|n<br>(SpecifyMethod to SpecifyBar Code Size)|p1, p2<br>(Size Specification)|
|---|---|
|0<br>USE_LIMITS<br>(Specify<br>ratio<br>of<br>bar<br>code<br>horizontallyand vertically)|p1:  p2:  Proportions of Vertical (p1) and Horizontal (p2)<br>However, p1:  p2 = 1:  99 to 10 : 1 (p1/p2 = 0.01 to 10)|
|1<br>USE_FIXED<br>(Specifies number of lines and<br>number of columns of bar code.)|p1:  Number of lines (0, 3 to 90), p2: Number of columns (0, 1<br>to 30)<br>However, p1 * p2≤<br> 928<br>When either p1 or p2 specifies 0, it indicates that that setting<br>value is variable.|



Setting the bar code size using this command specifies the general size of the bar code.  The size will automatically be corrected according to the other settings. 

## **ESC GS x S 1 n** 

[Name] Set PDF417 ECC (security level) [Code] ASCII ESC GS x S 1 n Hex. 1B 1D 78 53 31 n Decimal 27 29 120 83 49 n [Defined Area] 0 ≤ n ≤ 8 [Initial Value] n = 1 [Function] Parameter details • n: ECC level (0 to 8) 

## **ESC GS x S 2 n** 

[Name] Set PDF417 module X direction size [Code] ASCII ESC GS x S 2 n Hex. 1B 1D 78 53 32 n Decimal 27 29 120 83 50 n 

[Defined Area] 1 ≤ n ≤ 10 [Initial Value] n = 2 [Function] Parameter details 

• n: Sets the module X direction size (x-dim). Units: Dots It is recommended that 2 ≤ n when specifying using this command. When using with n = 1, check by actual use. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-122 
