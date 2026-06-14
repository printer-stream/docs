## **3.3.2. Character Expansion Settings** 

**ESC i n1 n2** [Name] Set/cancel the double wide/high [Code] ASCII ESC i n1 n2 Hex. 1B 69 n1 n2 Decimal 27 105 n1 n2 [Defined Area] 0≤n1≤5 48≤n1≤53 (”0”≤n1≤”5”) 0≤n2≤5 48≤n2≤53 (”0”≤n2≤”5”) [Initial Value] n1 = 0 (Double high cancelled) n2 = 0 (Double wide cancelled) [Function] Specifies/cancels double high/wide for ANK characters and Kanji characters. This command is ignored if either n1 or n2 is outside of the defined area. 

|n1|Expandedhigh|
|---|---|
|0,48|Cancels expandedhigh|
|1, 49|Specifies 2x high expansion|
|2, 50|Specifies 3x highexpansion|
|3, 51|Specifies4x highexpansion|
|4, 52|Specifies 5x highexpansion|
|5, 53|Specifies 6x highexpansion|
|||
|n2|Expandedwide|
|0,48|Cancels expandedwide|
|1, 49|Specifies 2x wide expansion|
|2, 50|Specifies 3x wide expansion|
|3, 51|Specifies4x wide expansion|
|4, 52|Specifies 5x wide expansion|
|5, 53|Specifies 6x wide expansion|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-12 
