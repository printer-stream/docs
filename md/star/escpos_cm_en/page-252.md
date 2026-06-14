Rev.2.52 

## **4-3-16 Star Original Individual Logo Commands** 

## **ESC GS ) L pL pH fn [parameter]** 

Name Set graphics data Code ASCII ESC ) L pL pH fn [parameter] Hex. 1B 29 4C pL pH fn [parameter] Decimal 27 41 76 pL pH fn [parameter] 

Function Executes graphics data processing. 

• pL and pH specify the parameter count (pL + pH x 256) in bytes after fn. 

- See the function specifications for details on [parameter]. 

|fn|Function No|Function Name|
|---|---|---|
|48|Function 48|Send the registered individual logo CRC|
|49|Function 49|Send the registered individual NVgraphics memorycapacity|
|50|Function 50|Send all keycode of the registered NVgraphics|



ESC/POS Command Specifications 

252 
