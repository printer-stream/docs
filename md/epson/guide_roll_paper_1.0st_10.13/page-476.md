## **C O N F I D E N T I A L** 

## **Program Example** 

PRINT #1, CHR$(&H1D); Ó (G Ó ;CHR$(3);CHR$(0);CHR$(49);CHR$(48); CHR$(1); ← specifies the offline response [function 48] PRINT #1, Ó AAAAA Ó ;CHR$(&HA); ← Print data on paper PRINT #1, CHR$(&H1D); Ó (G Ó ;CHR$(2);CHR$(0);CHR$(82);CHR$(48); ← Pre-process for cut sheet insertion ends [function 82] PRINT #1, CHR$(&H1D);Ó(HÓ;CHR$(6);CHR$(0);CHR$(48);CHR$(48);Ó0001Ó ← Specifies process ID    [function 48] PRINT #1, Ó BBBBB Ó ;CHR$(&HA); ← Print data on paper PRINT #1, CHR$(&H1D);Ó(HÓ;CHR$(6);CHR$(0);CHR$(48);CHR$(48);Ó0002Ó ← Specifies process ID    [function 48] PRINT #1, CHR$(&H1D); Ó (V Ó ;CHR$(66);CHR$(0); ← Cutting paper 

## **Print Example** 

|Print sample|||
|---|---|---|
|AAAAA|←|The process ID response (0001)|
|BBBBB|←|The process ID response (0002)|
||←|Paper cutting|



## [Model-dependent variations] TM-T90, TM-L90, TM-T20, TM-T88IV, TM-T88V,TM-T70, TM-P60 

## TM-T90, TM-L90 

**The printer supports all functions.** 

## TM-T20, TM-T88IV, TM-T70, TM-T88V,TM-P60 

**The printer supports function 48.** 
