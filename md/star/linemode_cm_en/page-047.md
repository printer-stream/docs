## **ESC D n1 n2…nk NUL** 

|[Name]|Set horizontal tab|Set horizontal tab|
|---|---|---|
|[Code]|ASCII|ESC<br>D<br>n1<br>n2<br>...<br>nk NUL|
||Hex.|1B<br>44<br>n1<br>n2<br>...<br>nk<br>00|
||Decimal|27<br>68<br>n1<br>n2<br>...<br>nk<br>0|
|[Defined Area]||1≤<br>n≤<br>255|
|||0≤<br>k≤<br>16|
|[Initial Value]||- - -|
|[Function]|[Function]|Uses the left edge as a standard to set the horizontal tab to the position of (current ANK character|
|||pitch x n).|
|||The horizontal tab reference point is the right edge of the paper, regardless of the left margin.|
|||ANK character pitch includes the right space and expansion settings are enabled.|
|||All other horizontal tabs set before setting the horizontal tab using this command are cancelled|
|||A maximum of 16 horizontal tabs can be set.|
|||However, the tab position must satisfy the following conditions.|
|||If the following conditions are not met, data up to the NUL code is discarded.|
|||Normal tabs that meet the conditions below are set and tabs after errors occur are not set.|
|||• 1<n1 < n2... < nk|
|||• nk≤<br> Printable region|
|||The horizontal tab set using this command is unaffected by changing the character pitch.|
|||Horizontal tabs set using the ESC D NUL command are cleared.|
|||There is no initial value for the horizontal tab.|



Standard mode and page mode can be set independently of each other. 

## **ESC D NUL** 

[Name] Clear horizontal tab [Code] ASCII ESC D NUL Hex. 1B 44 00 Decimal 27 68 0 

[Defined Area] - - - [Initial Value] - - - [Function] Clears the currently set horizontal tab. 

Standard mode and page mode can be set independently of each other. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-29 
