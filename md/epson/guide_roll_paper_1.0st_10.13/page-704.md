## **C O N F I D E N T I A L** 

## **GS ( E** _**pL pH fn d1 d2 d3**_ <Function 2> 

[Name] End the user setting mode session 

[Format] ASCII GS ( E pL pH fn d1 d2 d3 Hex 1D 28 45 04 00 02 4F 55 54 Decimal 29 40 69 4 0 2 79 85 84 [Range] (pL + pH × 256) = 4 (pL = 4, pH = 0) fn = 2 d1 = 79 d2 = 85 d3 = 84 

- [Description] Ends the user setting mode, and performs a software reset. 

- [Notes] 

- This function is performed when the printer is in user setting mode. 

- After the software reset, the printer goes into the power on state. 

- Executing this function enables setting values set in user setting mode (such as memory switch or customize value). 

- Be sure to execute this function after changing all the setting values. 
