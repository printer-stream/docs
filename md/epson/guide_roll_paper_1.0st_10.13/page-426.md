## **C O N F I D E N T I A L** 

**Request of (** n **=0) can be used when** GS ^ **is executed or when the printer is in one of the following status conditions when the peeling issuing mode is selected:** 

■ **Waiting for the paper feed button to be pressed when the cover is closed.** 

■ **Waiting for the paper feed button to be pressed to remove a label (when the label peeling detector cannot detect paper due to sunlight).** 

TM-L90 **models without Peeler:** 

**BUSY condition is selected by memory switch [Msw1-3].** 

**The setting of [Msw8-2] affects the recovery operation from the paper layout error. See Function 3 of** GS ( E **.** 

|**[Msw8-2]**|**Recovery operation from error**|
|---|---|
|**OFF**|**When the printer recovers from the error, paper layout is measured automatically and**<br>**paper is fed to the label print starting position and the paper layout stored in the non-**<br>**volatile memory is rewritten. Afterwards, the printer operates following the paper**<br>**layout automatically measured.**|
|**ON**|**When the printer recovers from the error, paper is fed to the label print starting**<br>**position. Paper layout stored in the non-volatile memory is not changed. Change the**<br>**setting of the paper layout stored in the non-volatile memory so that it matches the**<br>**currently used paper layout. See function 49 of this command for setting the paper**<br>**layout.**|



## TM-U230, TM-U220 

**BUSY condition for the parallel interface is selected by DIP switch 1-8.** 
