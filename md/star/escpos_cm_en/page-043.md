Rev.2.52 

## **ESC !  n** 

Batch specify print mode 

Name Batch specify print mode Code ASCII ESC ! n Hex. 1B 21 n Decimal 27 33 n 

0 ≤ n ≤ 255 Defined Region Initial Value n = 0 Function Specifies batch print mode 

|Bit|Function|“0”|“1”|
|---|---|---|---|
|7|Underline|OFF|ON|
|6|Undefned|--|--|
|5|<br>Double wide expanded|OFF|ON|
|4|Double tall expanded|OFF|ON|
|3|Emphasizedprinting.|OFF|ON|
|2|Undefned||--|
|1|Undefned|--|--|
|0|<br>Character Fonts|Font-A|Font-B|



- Details • Quadruple-size characters are printed by specifying both double-tall (bit 4 = 1) and doublewide (bit 5 = 1) modes. 

   - An underline is applied to the entire character width, including the ESC SP (character right space amount).  However, underlines are not applied to portions that have been skipped using HT (horizontal tab) or ESC V (character 90 degree rotation). 

   - The thickness of the underline is set by ESC - (specify/cancel underlines) regardless of the character. 

   - The base line for characters is the same when there are characters having different vertical direction ratios in the same line. 

   - The setting of the last received command is effective even when emphasized printing is executed by the ESC E (specify/cancel emphasized printing) command. 

   - The setting of the last received command is effective even when underlines are executed by the (ESC -) Specify/cancel underline command. 

   - The setting of the last received command is effective even when character size is executed by the GS! command. 

   - Emphasized printing (bit 3) is effective for ANK and Chinese characters.  Other printing modes are effective only on ANK characters.  • Specifications using this command are ignored in HRI characters. 

## STAR 

The following are the font configurations on STAR printers. 

|Character Fonts|Horizontal Dots x Vertical Dots|
|---|---|
|Font A|12 x 24 Dots|
|Font B|9 x 24 Dots|
|Chinese Character Fonts|24 x 24 Dots|



Reference ESC -, ESC E, GS ! 

ESC/POS Command Specifications 

43 
