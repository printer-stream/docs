## **C O N F I D E N T I A L** 

## **GS w** 

SETTING COMMAND 

[Name] Set bar code width [Format] ASCII GS w n Hex 1D 77 n Decimal 29 119 n 

[Range] TM-J2000/J2100 **: 2** ≤ n ≤ **6, 68** ≤ n ≤ **76** TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-P60: **2** ≤ n ≤ **6** 

[Default] TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-P60 **:** n **= 3** [Printers not featuring this command] TM-U230, TM-U220 

[Description] Sets the horizontal size of a bar code. 

      - n specifies the bar code module width. 

- [Notes] ■ The units for n depend on the printer model. 

   - This command setting is effective until performing of ESC @, reset or power-off. 

   - Bar code types are Multi level bar code [UPC-A, UPC-E, JAN13 / EAN13, JAN8 / EAN8, CODE93, CODE128, GS1-128, GS1 DataBar Omnidirectional, GS1 DataBar Truncated, GS1 DataBar Limited, and GS1 DataBar Expanded] and Binary level bar code [CODE39, ITF, CODABAR(NW-7)]. 
