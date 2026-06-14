## **C O N F I D E N T I A L** 

## **GS ( E** _**pL pH fn d1 d2 d3**_ <Function 48> 

[Name] Delete the paper layout 

[Format] ASCII GS ( E pL pH fn d1 d2 d3 Hex 1D 28 45 04 00 30 d1 d2 d3 Decimal 29 40 69 4 0 48 d1 d2 d3 [Range] (pL + pH × 256) = 4 (pL = 4, pH = 0) fn = 48 d1 = 67, d2 = 76, d3 = 82 

- [Description] Deletes all the setting value for the paper layout (no paper layout is set). 

- [Notes] 

- This function works in user setting mode. 

- With this command, layout setting values stored in the non-volatile memory are canceled due to one of the following processes: 

   - Execution of Function 49 of this command 

   - Execution of GS ( A   (m = 64) 

   - Executing “Automatic paper layout setting mode function” by panel operation when turning on the power 

   - Recovery from a paper layout error 

[Model-dependent variations] 

TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-P60, TM-U220 

## TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-P60, TM-U220 

**This printer does not support this function.** 

## TM-L90 

**Recovery from a paper layout error can be set the DIP switches below. See the printer information of Function 3 of** GS ( E **for details.** 

TM-L90 **with Peeler: [Msw8-1] and [Msw8-2]** TM-L90 **models without Peeler: [Msw8-2]** 
