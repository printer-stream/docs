Rev.2.52 

## **FS 2 c1 c2 d1 … dk** 

Name Define external character 

Code ASCII FS 2 c1 c2 d1...dk Hex. 1C 32 c1 c2 d1...dk Decimal 28 50 c1 c2 d1...dk 

|Name<br>Defne external character<br>Code<br>ASCII<br>FS<br>2<br>c1<br>c2 d1...dk<br>Hex.<br>1C<br>32<br>c1<br>c2 d1...dk<br>Decimal<br>28<br>50<br>c1<br>c2 d1...dk|Name<br>Defne external character<br>Code<br>ASCII<br>FS<br>2<br>c1<br>c2 d1...dk<br>Hex.<br>1C<br>32<br>c1<br>c2 d1...dk<br>Decimal<br>28<br>50<br>c1<br>c2 d1...dk|Name<br>Defne external character<br>Code<br>ASCII<br>FS<br>2<br>c1<br>c2 d1...dk<br>Hex.<br>1C<br>32<br>c1<br>c2 d1...dk<br>Decimal<br>28<br>50<br>c1<br>c2 d1...dk|
|---|---|---|
|Defned Region<br>• c1 and c2 difer according to specifcations and code type.  See below.<br>|||
|Specifcations<br>|c1|c2|
|Japanese Kanji Specifcations(JIS code type)|c1=77H|21H≤c2≤7EH|
|<br>Japanese Kanji Specifcations (SHIFT-JIS code type)|c1=ECH|40H≤c2≤7EH<br>80H≤c2≤9EH|
|Chinese Kanji Specifcations|c1=FEH|A1H≤c2≤FEH|
|Taiwanese Kanji Specifcations|c1=FEH|A1H≤c2≤FEH|
|Korean Kanji Specifcations|c1=FEH|A1H≤c2≤FEH|



- 0 ≤ d ≤ 255 

- k = 72 

Initial Value All spaces 

Function Defines the external character pattern of the Chinese character to a character code specified by c1 and c2. 

- Details • c1 and c2 indicate the Chinese character code that defines the external character; c1 is the first byte; c2 is the second byte. 

   - d specifies defined data. Bits that correspond to the dots to print are 1, and the bits that correspond to the dots that are not printed are 0. 

   - Defined data is cleared by ESC @. 

- STAR • This command is ignored when the memory switch location of use is specified as SBCS (single byte countries). 

   - External character registration of JIS codes and SHIFT-JIS codes for Japanese characters uses the same region. 

Reference 

FS C 

ESC/POS Command Specifications 

166 
