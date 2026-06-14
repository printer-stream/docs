## **C O N F I D E N T I A L** 

   - When HRI characters are designated to be added, special character HRI characters are processed as follows. 

      - The HRI character of function character (FNC1) is not printed. 

      - The HRI characters of special characters ("(", ")") are printed as the respective characters ("(", ")"). 

      - The HRI characters of bar code data ["{" + ("(", ")")] are printed as the respective characters ("(", ")"). 

- [Note for GS1 DataBar Expanded Stacked] 

   - The data shown below is added automatically in encoding. 

      - Guard pattern, finder pattern and separator pattern 

   - For encoding, the width of the symbol is decided by the setting value of <Function 471> of this command (nL + nH × 256) and the current printing area (the area from the current printing position to the edge of the printing area). 

      - When (nL + nH × 256) = 0, the width of the symbol is the current printing area. 

      - When (nL + nH × 256) ≠ 0 is specified and the setting value is greater than the current printing area, the width of the symbol is the current printing area. 

      - In cases other than above, (nL + nH × 256) is the width of the symbol. 

   - Even when HRI characters are designated to be added, HRI characters are not added to this symbol. 

## [Note for GS1-128] 

■ GS1-128 processes the following structures. 

## (a) Basic structure 

|Start<br>character|FNC<br>1|AI|Data<br>part|Check digit<br>A|Check digit<br>B|Stop<br>character|
|---|---|---|---|---|---|---|
|Automatically<br>added||<Function 480 (d1...dn)>|||Automatically added||
