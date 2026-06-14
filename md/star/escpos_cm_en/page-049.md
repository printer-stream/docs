Rev.2.52 

## **ESC * m nL nH d1…dk** 

Name Specify bit image mode Code ASCII ESC * m nL nH d1...dk Hex. 1B 2A m nL nH d1...dk Decimal 27 42 m nL nH d1...dk Defined Region m = 0,1,32,33 0 ≤ nL ≤ 255 Spec.A 0 ≤ nH ≤ 3 Spec.B 0 ≤ nH ≤ 7 

0 ≤ d ≤ 255 

Function Selects a bit-image mode in mode _m_ for the number of dots specified by _nL_ and _nH_ . 

|Funct|ion<br>Selects a bit-im|age mode in mode|_m_for the numb|er of dots specifed|by_nL _and_nH_.|
|---|---|---|---|---|---|
|m|Mode|Number of Vert.<br>Dir. Dots|Number of<br>Hor. Dir. Dots|Density of Hor.<br>Dir. Dots|Data Count (k)|
|0|8-dot single density|8|60 DPI|90 DPI|nL+nH×256|
|1|8-dot double density|8|60 DPI|180 DPI|nL+nH×256|
|32|24-dot single density|24|180 DPI|90 DPI|(nL+nH×256)×3|
|33|24-dot double density|24|180 DPI|180 DPI|(nL+nH×256)×3|



- Details • If the value of m is out of the specified range, nL and subsequent data are processed as normal data. 

   - nL and nH indicate the number of dots in the bit image in the horizontal direction to print. The number of dots is calculated by (nL + nH x256). 

   - If the bit-image data input exceeds the number of dots that can be printed on one line, the excess data is discarded. 

   - d indicates the bit-image data. Bits that correspond to the dots to print are 1, and the bits that correspond to the dots that are not printed are 0. 

   - After processing bit images, the printer returns to normal data processing. 

   - Excluding upside-down printing, print modes (emphasized printing, double printing, underlines, character sizes and black/white inverted printing) are unaffected. 

   - For details on the bit image expansion position in the page mode, see section 2. Explanations of the Page Mode. 

## STAR 

- Dot density (when the STAR printer head = 203 DPI) on STAR printers. 

|**m**|Mode|Densityof Vert. Direction Dots|Densityof Hor. Direction Dots|
|---|---|---|---|
|**0**|8-dot single density|67 DPI|101 DPI|
|**1**|8-dot double density|67 DPI|203DPI|
|**32**|24-dot single density|203DPI|101 DPI|
|**33**|24-dot double density|203DPI|203DPI|



- Fonts A and B and Chinese characters can be used together. 

ESC/POS Command Specifications 

49 
