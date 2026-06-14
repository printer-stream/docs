SETTING COMMAND 

## **C O N F I D E N T I A L** 

## **FS 2** 

[Name] Define user-defined Kanji characters [Format] ASCII FS 2 c1 c2 d1...dk Hex 1C 32 c1 c2 d1...dk Decimal 28 50 c1 c2 d1...dk 

## [Printers not featuring this command] None 

[Range] The ranges of c1 and c2 differ, depending on models and the character code system used. The ranges of c1 and c2 for each model are as follows. 

|**Models**|c1|c2|
|---|---|---|
|Japanese model (JIS code)|c1= 77H|21H≤ c2 ≤7EH|
|Japanese model (SHIFT JIS code)|c1= ECH|40H≤ c2 ≤7EH,<br>80H≤ c2 ≤9EH|
|Simplified Chinese model|c1= FEH|A1H≤ c2 ≤FEH|
|Traditional Chinese model|c1= FEH|A1H≤ c2 ≤FEH|
|Korean model|c1= FEH|A1H≤ c2 ≤FEH|



## 0 ≤ d ≤ 255 

## TM-J2000/J2100, TM-T90, TM-L90 **:** 

- k **= 72 [Simplified Chinese model / Traditional Chinese model]** 

- k **= 72 [Japanese model: Kanji Font A (24** × **24)** 

- k **= 60 [Japanese model: Kanji Font B (20** × **24)** 

- k **= 32 [Japanese model: Kanji Font C (16** × **16)** 

## TM-T20, TM-T88IV **:** 

## k **= 72** 

## TM-T88V **:** 

- k **= 72 [Simplified Chinese model / Traditional Chinese model]** 

- k **= 72 [Japanese model]** 

- k **= 72 [Korean model: Kanji Font A (24** × **24)** 

- k **= 32 [Korean model: Kanji Font B (16** × **16)** 
