Rev.2.52 

## **<Function 169> GS ( k pL pH cn fn m n  (cn=49, fn=69)** 

## Name 

Selects the error correction level for QR Code 

Code ASCII GS ( k pL pH cn fn m n Hex. 1D   28  6B  pL  pH cn fn m n Decimal   29   40  107  pL  pH cn fn m n Defined Region pL = 3, pH = 0 cn = 49, fn = 69 48 ≤ n ≤ 51 Initial Value n = 48 Function Selects  the error correction level for QR Code. 

|n1|Function|Reference: Approximate fgure for recovery|
|---|---|---|
|48|Select error correction level 0|<br>7 %|
|49|Select error correction level 1|15 %|
|50|Select error correction level 2|25 %|
|51|Select error correction level 3|30 %|



## **<Function 180> GS ( k pL pH cn fn m n  (cn=49, fn=80)** 

Name 

QR Code: Stores symbol data in the symbol storage area. 

Code ASCII GS ( k pL pH cn fn m d1...dk Hex. 1D   28  6B  pL  pH cn fn m d1...dk Decimal   29   40  107  pL  pH cn fn m d1...dk Defined Region 4 ≤ (pL + pH × 256) ≤ 7092 (0 ≤ pL ≤ 255, 0 ≤ pH ≤ 27) cn = 49, fn = 80, m =48 0 ≤ d ≤ 255 k = (pL + pH × 256) - 3 Function Stores symbol data (d1...dk) in the QR Code symbol storage area. 

ESC/POS Command Specifications 

116 
