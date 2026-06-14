## **C O N F I D E N T I A L** 

## **GS ( L** _**pL pH m fn kc1 kc2** <_ Function 82 > 

[Name] Delete the specified download graphics data. 

- [Format] ASCII GS ( L pL pH m fn kc1 kc2 Hex 1D 28 4C 04 00 30 52 kc1 kc2 Decimal 29 40 76 4 0 48 82 kc1 kc2 

- [Range] (pL + pH × 256) = 4 (pL = 4, pH = 0) m = 48 fn = 82 

   - 32 ≤ kc1 ≤ 126 

   - 32 ≤ kc2 ≤ 126 

- [Description] Deletes the downloaded graphics data defined by the key codes (kc1 and kc2). 

      - Deleted areas are designated “Unused areas.” 

      - Deleted key codes are designated as undefined. 

- [Notes] ■ Use this function at the beginning of the line when the standard mode is selected. 

■ This function is incompatible with macros, so be sure to avoid including it when defining macros. [Model-dependent variations] TM-T90, TM-T88IV, TM-T70, TM-L90, TM-P60 

TM-T90, TM-T88IV, TM-T70,  TM-L90, TM-P60 

**This printer does not support this function.** 
