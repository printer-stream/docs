## **3.3.13. Prin t Settings** 

## **ESC RS d n** 

[Name] Set print density [Code] ASCII ESC RS d n Hex. 1B 1E 64 n Decimal 27 30 100 n 

[Defined Area] 0≤n≤ 6 48≤n≤57 (”0”≤n≤”6”) [Initial Value] Memory switch setting [Function] Sets print density. This command executes after stopping the printing operation. When in 2-color mode, only print density for red printing can be set by this command. When in low peak current mode, print density using this command is invalid. 

## Spec. A. 

|[Function]<br>Spec. A.pec. A.ec. A.|Sets print density.<br>This command executes after stopping the printing operation.<br>When in 2-color mode, only print density for red printing can be set by this command.<br>When in low peak current mode, print density using this command is invalid.|
|---|---|
|n|Print Density<br>Single Color Printing Mode<br>Two Color Printing Mode  Red Print Density<br>Double Resolution Mode<br>(*) Installed print mode depends on the<br>model.|
|0,48|Print density1.3<br>Print density1.2|
|1, 49<br>~~a~~|Print density 1.2<br>Print density 1.2<br>~~a~~|
|2, 50|Print density1.1<br>Print density1.0|
|3, 51<br>~~a~~|Print density1.0<br>Print density1.0<br>~~a~~|
|4, 52|Print density 0.9<br>Print density1.0|
|5, 53<br>~~a~~|Print density 0.8<br>Print density 0.8<br>~~a~~|
|6, 54|Print density 0.7<br>Print density 0.8|



Spec. B. 

|Spec. B.pec. B.ec. B.||
|---|---|
|n|Print Density<br>Single Color Printing Mode<br>2-color Printing Mode  Red Print Density<br>Double Resolution Mode<br>*1|
|0, 48<br>~~a~~|Print density+3<br>Print density+1<br>~~a~~|
|1,49<br>~~|~~|Print density+ 2<br>Print density+ 1<br>~~|~~|
|2, 50|Print density+ 1<br>Standard print density (Standard)|
|3, 51<br>~~a~~|Standard print density (Standard)<br>Standard print density (Standard)<br>~~a~~|
|4, 52|Print density- 1<br>Standard print density (Standard)|
|5, 53<br>~~A~~|Print density- 2<br>Print density-1<br>~~A~~|
|6, 54<br>~~A~~|Print density-3<br>Print density- 1<br>~~A~~|



*1) See the appropriate printer specifications manual for details on the print modes that are available. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-51 
