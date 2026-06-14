## **C O N F I D E N T I A L GS ( k** <Function 065> 

- [Name] PDF417: Set the number of columns in the data region 

[Format] ASCII GS ( k pL pH cn fn n Hex 1D 28 6B 03 00 30 41 n Decimal 29 40 107 3 0 48 65 n [Range] (pL + pH × 256) = 3 (pL =3, pH =0) cn = 48 fn = 65 0 ≤ n ≤ 30 

- [Default] n = 0 

- [Description] Sets the number of columns in the data region for PDF417. 

      - When n = 0, specifies automatic processing 

      - When n is not 0, sets the number of columns in the data region to n codeword. 

- [Notes] ■ Settings of this function affect the processing of Functions 081 and 082. 

   - When auto processing (n = 0) is specified, the maximum number of columns in the data area is 30 columns. 

   - ■ The following data is not included in the number of columns: 

      - Start pattern and stop pattern 

      - Indicator codeword of left and right 

   - When automatic processing (n = 0) is specified, the number of columns is calculated by the print area when processing Functions 081, 082, module width (Function 067), and option setting (Function 070). 

   - Settings of this function are effective until ESC @ is executed, the printer is reset, or the power is turned off. 

[Model-dependent variations] 

## TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-P60 

## TM-T88IV, TM-T70 

**This function is not supported in the Japanese specification.** 
