## **ESC Q n** 

[Name] Set right margin [Code] ASCII ESC Q n Hex. 1B 51 n Decimal 27 81 n 

[Defined Area] 0≤n≤255 [Initial Value] - - - [Function] Uses the left edge as a standard to set the print region as (current ANK character pitch x n). Character pitch includes the space between characters and expansion settings are enabled. The right margin set using this command is unaffected by changing the character pitch. This command is ignored if settings are for a printing region less than 36 mm. 

Specification A Setting this command partway will take affect from the next line. Specification B This command is enabled only when at the top of the line. 

Printable Region Left Margin                       Print Region Right Margin 

## **HT** 

[Name] Move horizontal tab [Code] ASCII HT Hex. 09 Decimal 9 

[Defined Area] - - - [Initial Value] - - - [Function] Move print position to next horizontal tab position. 

This command is ignored with under the following conditions. 

• When there is no horizontal tab set. 

• When the current position is the same as the furthest right horizontal tab position or to the right of it. 

There is no initial value for the horizontal tab. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-28 
