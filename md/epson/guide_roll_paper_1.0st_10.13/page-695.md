## **C O N F I D E N T I A L** 

## **GS ( C** _**pL pH m fn b d1 d2 d3**_ <Function 6> 

- [Name] Delete all data in the NV user memory 

[Format] ASCII GS ( C pL pH m fn b d1 d2 d3 Hex 1D 28 43 06 00 00 fn 00 43 4C 52 Decimal 29 40 67 6 0 0 fn 0 67 76 82 [Range] (pL + pH × 256) = 6 (pL = 6, pH = 0) m = 0 fn = 6, 54 b = 0 

   - d1 = 67 d2 = 76 d3 = 82 

- [Description] Deletes all data in the NV user memory. 

      - All area is changed to unused area. 

      - All key codes are designated as undefined. 

- [Notes] ■ In standard mode, this command is effective only at the beginning of the line. 

   - In page mode, this command is ignored. 

   - This command cannot include macros; therefore, do not use this command when defining macros. 
