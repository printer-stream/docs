Rev.2.52 

## **ESC T n** 

Select character print direction in page mode 

Name Select character print direction in page mode Code ASCII ESC T n Hex. 1B 54 n Decimal 27 84 n Defined Region 0 ≤ n ≤ 3, 48 ≤ n ≤ 51 Initial Value n = 0 Function Selects the character printing direction and starting point in page mode. 

|n<br>Print Direction<br>StartingPoint<br>0,48<br>Left to Right<br>Upper Left(A in the figure below)<br>1,49<br>Bottom to Top<br>Lower Left(B in the figure below)<br>2,50<br>Right to Left<br>Lower Right(C in the Figure below)<br>3,51<br>Topto Bottom<br>Upper Right(D in the figure below)|Print Region<br>D<br>C<br>B<br>A|Paper Feed Direction|
|---|---|---|



Details • Executes only a printer internal flag operation when this command is input in standard mode. The command does not affect printing in standard mode. 

- The character expansion starting point is in the print region specified by ESC W (Set print region in page mode). 

- The basic calculated pitch (x or y) used with the following commands differs according to the starting point. 

- a. If the starting point is upper left or lower right (feeds paper and expands characters in the vertical direction) 

Commands using x : ESC SP, ESC $, ESC \, FS S Commands using y : SC 3, ESC J, GS $, GS \ b. If the starting point is upper right or lower left Commands using x : ESC 3, ESC J, GS $, GS \ Commands using y : ESC SP, ESC $, ESC \, FS S Reference ESC $, ESC L, ESC W, ESC \, GS $, GS P, GS\ 

ESC/POS Command Specifications 

65 
