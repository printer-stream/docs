## **C O N F I D E N T I A L FS ( L** _<_ Function 66 > 

[Name] Feed paper to the cutting position [Format] ASCII FS ( L pL pH fn m Hex 1C 28 4C 02 00 42 m Decimal 28 40 76 2 0 66 m [Range] (pL + pH × 256) = 2 (pL = 2, pH = 0) m = 48, 49 fn = 66 

- [Description] Feeds paper to the cutting position. 

|m|**Function**|
|---|---|
|48|Feeds paper to the cutting position. However, if the paper is in standby at the<br>cutting position, the printer does not feed.|
|49|Feeds paper to the cutting position. However, if the paper is in standby at the<br>cutting position, the printer feeds paper to the next cutting position.|



- [Notes] ■ Please use this function by using “the first state of the line” in standard mode. 

   - This function is used when using “black mark paper.” 

   - The paper feed operation ends when no paper is detected in the paper feed to the cutting position. 

   - [Position information A] transmitted by Function 48 becomes (bit 1 = 1) when this function is used. Moreover, the print area of the label paper or black mark paper if there is a print start position right under the cutting position becomes “current label.” 

[Model-dependent variations] TM-L90, TM-P60 

## TM-L90 

TM-L90 **with Peeler does not support this function.** 
