Rev.2.52 

## **ESC V n** 

Name Specify/cancel character 90 degree clockwise rotation Code ASCII ESC V n Hex. 1B 56 n Decimal 27 86 n Defined Region 0 ≤ n ≤ 1, 48 ≤ n ≤ 49 Initial Value n = 0 Function Specifies or cancels character 90 degree clockwise rotation. 

||**n**|**Function**||
|---|---|---|---|
||**0, 48**|**Cancels 90 degree clockwise rotation**||
||**1, 49**|**Specifes 90 degree clockwise rotation**||
|Details||• Underlines are not applied to characters rotated 90 degrees clockwise even when ESC !,||
|||ESC – or FS – commands are given.||



   - If 90 degree clockwise rotation is specified, double-wide and double-tall commands in the 90 rotation mode enlarges characters in the opposite directions to double-wide and double-tall commands. 

   - This command only affects printing in standard mode. 

   - In page mode, this command is only effective for the setting. 

   - This command is effective for ANK and Chinese characters. 

- STAR • Characters are rotated as shown below when printing 90 degree clockwise rotation characters. 

Vertical 1 Horizontal 2 Mags Right Space Vertical 1 Horizontal 1 Mag M 90 Degree Clockwise Rotation Vertical 1 Horizontal 2 Mags Right Space Vertical 1 Horizontal 1 Mag 

Reference ESC !, ESC - 

ESC/POS Command Specifications 

66 
