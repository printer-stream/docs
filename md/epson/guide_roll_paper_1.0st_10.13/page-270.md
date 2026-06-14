## **C O N F I D E N T I A L** 

## **GS ( L** _**pL pH m fn d1 d2 d3** <_ Function 81> 

[Name] Delete all download graphics data. 

- [Format] ASCII GS ( L pL pH m fn d1 d2 d3 Hex 1D 28 4C 05 00 30 51 43 4C 52 Decimal 29 40 76 5 0 48 81 67 76 82 

- [Range] (pL + pH × 256) = 5 (pL = 5, pH = 0) 

   - m = 48 

   - fn = 65 

   - d1 = 67 

   - d2 = 76 d3 = 82 

- [Description] Deletes all downloaded graphics data that has been defined using Functions 83 and 84. 

      - Deleted areas are designated “Unused areas.” 

      - All key codes are designated as undefined. 

- [Notes] 

   - Use this function at the beginning of the line when the standard mode is selected. 

   - This function is incompatible with macros, so be sure to avoid including it when defining macros. 

   - When downloaded graphics data is being shared by multiple applications, executing this function will delete all data being used by all applications. Caution is required when using this function. 

- [Model-dependent variations] TM-T90, TM-T88IV, TM-T70, TM-L90, TM-P60 

## TM-T90, TM-T88IV, TM-T70, TM-L90, TM-P60 

**This printer does not support this function.** 
