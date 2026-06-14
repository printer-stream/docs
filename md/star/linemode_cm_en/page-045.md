## **3.3.6. Ho rizontal Direction Printing Position** 

**ESC l n** [Name] Set left margin [Code] ASCII ESC l n Hex. 1B 6C n Decimal 27 108 n [Defined Area] 0≤n≤255 [Initial Value] n = 0 [Function] Uses the left edge as a standard to set the left margin as (current ANK character pitch x n). Character pitch includes the space between characters and expansion settings are enabled. The left margin set using this command is unaffected by changing the character pitch. This command is ignored if settings are for a printing region less than 36 mm. Specification A Setting this command partway will take affect from the next line. Specification B This command is enabled only when at the top of the line. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-27 
