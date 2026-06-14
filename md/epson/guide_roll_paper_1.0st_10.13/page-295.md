## **C O N F I D E N T I A L** 

## **GS ( L** _**pL pH m fn a bx by c xL xH yL yH d1...dk**_ <Function 113> 

## **GS 8 L** _**1 2 3 4 m fn a bx b c xL xH L H d1...dk p p p p y y y**_ 

- [Name] Store the graphics data in the print buffer (column format). 

[Format] ASCII GS ( L pL pH m fn a bx by c xL xH yL yH d1...dk Hex 1D 28 4C pL pH 30 71 30 bx by c xL xH yL yH d1...dk Decimal 29 40 76 pL pH 48 113 48 bx by c xL xH yL yH d1...dk ASCII GS 8 L p1 p2 p3 p4 m fn abx by c xL xH yL yH d1...dk Hex 1D 38 4C p1 p2 p3 p4 30 71 30bx by c xL xH yL yH d1...dk Decimal 29 56 76 p1 p2 p3 p4 48 113 48bx by c xL xH yL yH d1...dk 

[Range] **11** ≤ **(** pL **+** pH × **256)** ≤ **65535 (0** ≤ pL ≤ **255, 0** ≤ pH ≤ **255)** 

**[When using** GS 8 L **: 11** ≤ **(** p1 **+** p2 × **256 +** p3 × **65536 +** p4 × **16777216)** ≤ **4294967295]** m **= 48,** fn **= 113,** a **= 48** 

- **0** ≤ d ≤ **255** 

## k **= (** xL **+** xH × **256)** × **(int((** yL **+** yH × **256) + 7)/8)** 

   - TM-J2000/J2100 **: 49** ≤ c ≤ **51 (TM-J2100 [two-color printing model])** 

         - c **= 49 (TM-J2000 [single-color printing model])** 

         - **1** ≤ **(** xL **+** xH × **256)** ≤ **2048 (0** ≤ xL ≤ **255, 0** ≤ xH ≤ **8)** 

         - **1** ≤ **(** yL **+** yH × **256)** ≤ **128 (1** ≤ yL ≤ **128,** yH **= 0)** 

- [Description] Stores the graphics data (column format) in the print buffer. 

      - Users have the option of specifying horizontal bx × vertical by size settings for the selected data. 

      - c specifies the color of the stored data. 

|c|**Color specifications**|
|---|---|
|49|Color 1|
|50|Color 2|
|51|Color 3|



- xL and xH specify the number of dots in the horizontal direction as (xL + xH × 256). 
