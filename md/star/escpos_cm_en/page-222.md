Rev.2.52 

## **ESC GS x S 0 n p1 p2** 

Name Set PDF417 bar code size Code ASCII ESC GS x S 0 n p1 p2 Hex. 1B 1D 78 53 30 n p1 p2 Decimal 27 29 120 83 48 n p1 p2 Defined Area n = 0, 1 When n = 0: 1 ≤ p1 ≤ 99, 1 ≤ p2 ≤ 99 

Name 

When n = 1: p1 = 0 or 3 ≤ p1 ≤ 90, p2 = 0 or 1 ≤ p2 ≤ 30  (However, this excludes p1 = p2 = 0) Initial Value n = 0, p1 = 1, p2 = 2 Function Parameter details 

|n<br>(SpecifyMethod to SpecifyBar Code Size)|n<br>(SpecifyMethod to SpecifyBar Code Size)|p1, p2<br>(Size Specifcation)|
|---|---|---|
|0|USE_LIMITS<br>(Specify ratio of bar code horizontally and<br>vertically)|p1:  p2:  Proportions of Vertical (p1) and Horizontal (p2)<br>However, p1:  p2 = 1:  99 to 10 : 1 (p1/p2 = 0.01 to 10)|
|1|USE_FIXED<br>(Specifes number of lines and number of<br>columns of bar code.)|p1:  Number of lines (0, 3 to 90), p2: Number of columns<br>(0, 1 to 30)<br>However, p1 * p2≤928<br>When either p1 or p2 specifes 0, it indicates that that<br>settingvalue is variable.|



Setting the bar code size using this command specifies the general size of the bar code.  The size will automatically be corrected according to the other settings. 

## **ESC GS x S 1 n** 

Name Set PDF417 ECC (security level) Code ASCII ESC GS x S 1 n Hex. 1B 1D 78 53 31 n Decimal 27 29 120 83 49 n 0 ≤ n ≤ 8 Defined Area Initial Value n = 1 Function Parameter details • n: ECC level (0 to 8) 

ESC/POS Command Specifications 

222 
