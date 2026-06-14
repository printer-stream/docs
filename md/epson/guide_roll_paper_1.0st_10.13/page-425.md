## **C O N F I D E N T I A L** 

[Model-dependent variations] 

TM-J2000/J2100, TM-T90, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-U230, TM-U220. 

## **Program Example for all printers** 

PRINT #1, CHR$(&H10);CHR$(&H5);CHR$(2); 

## TM-J2000/J2100, TM-T90 

**BUSY condition is selected by memory switch [Msw1-3].** 

## TM-T88IV, TM-T88V, TM-T70 

**BUSY condition is selected by DIP switch 2-1.** 

## TM-L90 

TM-L90 **with Peeler:** 

**BUSY condition is selected by memory switch [Msw1-3].** 

**The settings of [Msw8-1] and [Msw8-2] affect the recovery operation from the paper layout error. See Function 3 of** GS ( E **.** 

|**[Msw8-1][Msw8-2] **|**Recovery operation from error**|
|---|---|
|**OFF**|**When the printer recovers from the error, paper layout is measured automatically and**<br>**paper is fed to the label print starting position and the paper layout stored in the non-**<br>**volatile memory is rewritten. Afterwards, the printer operates following the paper**<br>**layout automatically measured. When the peeling issuing mode is selected, the printer**<br>**is in the waiting status for a label to be removed when the paper layout is automatically**<br>**measured; therefore operators should remove the label.**|
|**ON**|**When the printer recovers from the error, paper is fed to the label print starting**<br>**position. Paper layout stored in the non-volatile memory is not changed. Change the**<br>**setting of the paper layout stored in the non-volatile memory so that it matches the**<br>**currently used paper layout. See function 49 of this command for setting the paper**<br>**layout.**|
