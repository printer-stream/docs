## **C O N F I D E N T I A L** 

## **ESC –** 

SETTING COMMAND 

[Name] Turn underline mode on/off 

[Format] ASCII ESC – n Hex 1B 2D n Decimal 27 45 n [Range] TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV, TM-T88V, TM-T70,TM-L90, TM-P60, TM-U220 **: 0** ≤ n ≤ **2, 48** ≤ n ≤ **50** TM-U230 **:** n **= 0, 1, 48, 49** 

- [Default] n = 0 

- [Printers not featuring this command] None 

- [Description] Turns underline mode on or off using n as follows: 

|n|**Function**|
|---|---|
|0, 48|Turns off underline mode|
|1, 49|Turns on underline mode (1-dot thick)|
|2, 50|Turns on underline mode (2-dots thick)|



## [Notes] 

- The underline mode is effective for alphanumeric, Kana, Korean, and user-defined characters. 

- When underline mode is turned on, 90° clockwise rotated characters and white/black reverse characters cannot be underlined. 

- The color of underline is the same as that of the printing character. The printing character’s color is selected by GS ( N <Function 48>. 

- The printer cannot underline the space set by HT, ESC $, and ESC \. 

- Changing the character size does not affect the current underline thickness. 

- When underline mode is turned off, the following data cannot be underlined, but the thickness is maintained. 

- This command and bit 7 of ESC ! turn on and off underline mode in the same way. 

- Some of the printer models support the 2-dot thick underline (n = 2 or 5). 
