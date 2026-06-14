## **C O N F I D E N T I A L** 

## **When origin of layout (** sa **) is “Bottom of a label”:** 

|**n of layout (**sa**) is “Bottom of a label”:**||
|---|---|
|**Parameter of Paper layout**|**Setting value**|
|**Bottom of a label ~ bottom of the next label (**sb**)**|**Measured value**|
|**Bottom of a label ~ top of the next label (**sc**)**|**Measured value**|
|**Layout in the vertical direction (**sd**) ~ (**sf**)**|**Fixed value**|
|**The layout in the horizontal direction (**sg**), (**sh**)**|**Fixed value**|



**If the installed paper is label paper with black mark in procedure 5, the printer may not recognize it correctly. In this case, the origin of layout is set to “none.”** GS ( E **<Function 49> is recommended for label paper with black mark.** 

## **Recommended procedure of exchanging paper:** 

|**Procedure **|**Processing for host PC**|**Performing of the printer**|
|---|---|---|
|**1.**|**Transmit**GS ( E**<Function 1> to the printer. **|**Entering user setting mode.**|
|**2.**|**Operator’s operation: exchange the paper.**|**—**|
|**3.**|**Transmit**GS ( E**<Function 49> to the**<br>**printer.**|**Specifying the paper layout to “None (does not use**<br>**paper layout).“**|
|**4.**|**Transmit**GS ( E**<Function 2> to the printer. **|**Executing software reset, and close user setting**<br>**mode.**|
|**5.**|**Transmit**GS ( A**(**m**= 64) to the printer.**|**Executing automatic setting of paper layout.**|



**Note: If you skip procedure 1, an error may occur.** 

**Paper layout setting value can be changed in the automatic setting mode of paper layout by panel operation when the printer power is turned on. However, if paper to be used is a label (with a black mark), the automatic setting mode cannot be used. Paper layout needs to be set by Function 49 of** GS ( E **. Recovery from a paper layout error can be set by memory switches as below. See Function 3 of** GS ( E **of the model dependent variation for details.** 

TM-L90 **with Peeler: [Msw8-1] and [Msw8-2]** TM-L90 **models without Peeler: [Msw8-2]** 
