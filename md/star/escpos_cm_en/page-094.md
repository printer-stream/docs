Rev.2.52 

## **<Function 50> GS ( K pL pH fn m  (Fn=50)** 

Name Set printing speed Code ASCII GS ( K pL pH fn m Hex. 1D 28 4B pL pH fn m Decimal 29 40 75 pL pH fn m Defined Region {pL + (pH × 256) } = 2 (pL = 2, pH = 0) fn = 50 Spec.A 0 ≤ m ≤ 9, 48 ≤ m ≤ 57 Spec.B 0 ≤ m ≤ 3, 7 ≤ m ≤ 9, 48 ≤ m ≤ 51, 55 ≤ m ≤ 57 Initial Value m = 9 Function Sets printing speed. 

|m|PrintingSpeed|
|---|---|
|0,48|MSW Load Settings(default)|
|1,49|Slow speed|
|2,50|Slow speed|
|3,51|Slow speed|
|4,52|Mid-speed|
|5,53|Mid-speed|
|6,54|Mid-speed|
|7,55|High speed|
|8,56|High speed|
|9,57|High speed|



STAR The speed setting is disabled during reduced printing in the vertical direction. However, this command setting is enabled when reduced printing in the vertical direction is released. 

ESC/POS Command Specifications 

94 
