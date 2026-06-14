## **C O N F I D E N T I A L** 

## **ESC U** 

SETTING COMMAND 

[Name] Turn unidirectional print mode on/off [Format] ASCII ESC U n Hex 1B 55 n Decimal 27 85 n [Range] 0 ≤ n ≤ 255 [Default] n = 0 

- [Printers not featuring this command] TM-T90, TM-T20, TM-T88IV, TM-T88V,  TM-T70, TM-L90,  TM-P60 [Description] Turns unidirectional print mode on or off. 

      - When the LSB of n is 0, unidirectional print mode is turned off. 

      - When the LSB of n is 1, unidirectional print mode is turned on. 

- [Notes] ■ This mode can be set independently in standard mode and in page mode. 

      - When this command is used in standard mode, the printer sets the mode for standard mode. 

      - When this command is used in page mode, the printer sets the mode for page mode. 

   - When unidirectional print mode is turned off, bidirectional print mode is automatically turned on. 

   - When page mode is selected, the printer performs unidirectional printing for all data that is to be collectively printed using FF or ESC FF. 

   - Unidirectional print mode can be turned on when printing double-height characters or graphics or bit image or two dimension code to ensure that the top and bottom of the printing patterns are aligned. 

   - The settings of this command are effective until ESC @ is executed, the printer is reset, or the power is turned off. 

[Model-dependent variations] 

None 

## **Program Example for all printers** 

PRINT #1, CHR$(&H1B);"U";CHR$(1); ← Unidirectional print mode turned on 
