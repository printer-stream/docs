## **C O N F I D E N T I A L GS ( k** <Function 471> 

- [Name] Composite Symbology: GS1 DataBar Expanded Stacked maximum width setting 

- [Format] ASCII GS ( k pL pH cn fn nL nH Hex 1D 28 6B 04 00 34 47 nL nH Decimal 29 40 107 4 0 52 71 nL nH 

- [Range] **(** pL **+** pH × **256) = 4 (** pL **=4,** pH **=0)** 

   - cn **= 52** 

## fn **= 71** 

   - TM-P60 **,** TM-T20 **,** TM-T88V **: 106** ≤ (nL + nH × **256)** ≤ **3952,** (nL + nH × **256) = 0 (0** ≤ nL ≤ **255, 0** ≤ nH ≤ **15)** 

- [Default] TM-T20 **,** TM-P60 **:** (nL + nH × **256)** = **160 (** nL = **160,** nH = **0)** 

   - TM-T88V **:** (nL + nH × **256)** = **141(** nL = **141,** nH = **0)** 

- [Description] Sets the maximum width of the GS1 DataBar Expanded Stacked (the line element of Composite Symbology) to (nL + nH x 256) dots. 

      - When (nL + nH x 256) = 0, maximum width does not set. 

   - Settings of this function affect the processing of Functions 481 and 482. 

   - When (nL + nH x 256) = 0 is specified, the width of the symbol changes according to the printing area when <Function 381> and <Function 382> are processed. 

   - Settings of this function are effective until ESC @ is executed, the printer is reset, or the power is turned off. 

- [Model-dependent variations] TM-T90,TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-P60 

## TM-T90, TM-T88IV, TM-T70, TM-L90 

## **This model does not support this function.** 

## TM-T20 

## **TM-T20 supports this function.** 

**The setting unit is 1 dot. The width is set in units of 0.125mm {1/203 inch}.** 
