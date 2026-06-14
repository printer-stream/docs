## **C O N F I D E N T I A L** 

## ■ [Position information B] is shown in the following. 

|■[Pos|ition information B] is shown in the following.||||
|---|---|---|---|---|
|**Bit**|**Function**|**Binary **|**Hex**|**Decimal**|
|0|The print start of the current label can operate.|0|00|0|
||The print start operation of the current label is impossible.|1|01|1|
|1|The print start of the next label can operate.|0|00|0|
||The print start of the next label is impossible.|1|02|2|
|2 to 5|(Reserved)|-|-|-|
|6|Fixed|1|40|64|
|7|Fixed|0|00|0|



   - Bits 0 and 1 always become “1” when the paper layout is “Receipt (without black mark)” and when the cover is open. 

   - “Present label” is a print area of the label paper or the black mark paper which corresponds to either of the following: 

      - a) “Print area where print start position exists right under label peeling position” right after executing <Function 65>. 

      - b) “Print area where print start position exists right under cutting position” right after executing <Function 66>. 

      - c) “Print area at print start position” right after executing <Function 67> and the print start operation. 

      - d) Print area with print position, except for the above-mentioned. 

   - “The next label” is “print area of the following label paper or the black mark paper of the present label. “ 

- See previous [Notes for transmission process] for description of transmission process. 

[Model-dependent variations] TM-L90, TM-P60 
