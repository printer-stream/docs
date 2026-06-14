SETTING COMMAND 

## **C O N F I D E N T I A L** 

## **GS 0 g** 

- [Name] Initialize maintenance counter 

- [Format] ASCII GS g 0 m nL nH Hex 1D 67 30 00 nL nH Decimal 29 103 48 0 nL nH 

- [Printers not featuring this command] TM-U230, TM-U220 

- [Range] m = 0 

   - TM-J2000/J2100 **:   30** ≤ ( nL **+** nH × **256)** ≤ **34,** ( nL **+** nH × **256) = 50, 70** TM-T90, TM-T88IV, TM-T70, TM-P60 **: (** nL **+** nH × **256) = 20, 21, 50, 70** TM-T20,TM-T88V **: (** nL **+** nH × **256) = 20, 21, 22, 50, 70 (** nL **= 20, 21, 22, 50, 70,** nH **= 0)** TM-L90 **: (** nL **+** nH × **256) = 20, 21, 70 [** TM-L90 **with Peeler]** 

   - TM-L90 **: (** nL **+** nH × **256) = 20, 21, 50, 70 [** TM-L90 **models without Peeler]** 

- [Description] Sets the resettable maintenance counter specified by (nL + nH × 256) to 0. 

|(nL+nH ×256)|**Counter**|
|---|---|
|10 ~ 19|Serial impact head|
|20 ~ 29|Thermal head|
|30 ~ 39|Ink jet head|
|40 ~ 49|Shuttle head|
|50 ~ 59|Devices that conform to the normal specification|
|60 ~ 69|Optional devices|
|70 ~ 79|Time|



## [Notes] 

- In standard mode, this command is effective only when processed in the beginning of a line. 

- Unsupported counter numbers cannot be specified. 

- Do not use this command while a macro is being defined, because the command cannot be included in the macro. 
