## **ESC W n** 

[Name] Specify/cancel expanded wide [Code] ASCII ESC W n Hex. 1B 57 n Decimal 27 87 n [Defined Area] 0≤n≤5 48≤n≤53 (”0”≤n≤”5”) [Initial Value] n = 0 (Double wide cancelled) [Function] Specifies/cancels double wide for ANK characters and Kanji characters. 

||n|Expandedwide|
|---|---|---|
|0, 48|0, 48|Cancels expanded wide|
|1,4|49|Specifies2x wide expansion|
|2,|50|Specifies 3x wide expansion|
|3,|51|Specifies4x wide expansion|
|4,|52|Specifies 5x wide expansion|
|5,|53|Specifies 6x wide expansion|



## **ESC h n** 

[Name] Specify/cancel expanded high [Code] ASCII ESC h n Hex. 1B 68 n Decimal 27 104 n 

[Defined Area] 0≤n≤5 48≤n≤53 (”0”≤n≤”5”) [Initial Value] n = 0 (Double high cancelled) [Function] Specifies/cancels double high for ANK characters and Kanji characters. 

|n|Expandedhigh|
|---|---|
|0,48|Cancels expandedhigh|
|1, 49|Specifies 2x expansion|
|2, 50|Specifies 3xexpansion|
|3, 51|Specifies4xexpansion|
|4, 52|Specifies 5xexpansion|
|5, 53|Specifies 6xexpansion|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-13 
