## **C O N F I D E N T I A L** 

   - The quiet zone is not included in the printing data. Be sure to include the quiet zone when using this function. 

- [Description: Applied to GS1 DataBar Stacked and GS1 DataBar Stacked Omnidirectional] 

   - The data shown below is added automatically in encoding. 

      - Application identifier (AI): The AI is "01". 

      - Check digit (1 character) 

      - Guard pattern and separator pattern 

[Description: GS1 DataBar Expanded Stacked] 

- The data shown below is added automatically in encoding. 

   - Guard pattern, finder pattern and separator pattern 

- For encoding, the width of the symbol is decided by the setting value of <Function 371> of this command (nL + nH x 256) and the current printing area (the area from the current printing position to the edge of the printing area). 

   - When (nL + nH x 256) = 0, the width of the symbol is the current printing area. 

   - When (nL + nH x 256) ≠ 0 is specified and the setting value is greater than the current printing area, the width of the symbol is the current printing area. 

   - In cases other than above, (nL + nH x 256) is the width of the symbol. 

[Model-dependent variations] TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-P60 

## TM-T90, TM-T88IV, TM-T70, TM-L90 

## **This model does not support this Function.** 

## TM-T20, TM-T88V 

## **This printer supports this function.** 

## **In standard mode, symbols with height greater than 831 dots cannot be printed with this printer.** 

## TM-P60 

TM-P60 **with peeler supports this function.** 
