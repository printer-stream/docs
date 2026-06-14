Rev.2.52 

## **ESC { n** 

Name Specify/cancel upside-down printing Code ASCII ESC { n Hex. 1B 7B n Decimal 27 123 n 0 ≤ n ≤ 255 Defined Region Initial Value n = 0 Function Specifies or cancels upside-down printing. 

   - Cancels upside-down printing when n = <*******0>H. 

   - Specifies upside-down printing when n = <*******1>H. 

- Details • n is effective only when it is the lowest bit. 

   - This command is effective only when input at the top of the line when standard mode is being used. 

   - This command has no affect in page mode.  In page mode, this command is only effective for the setting. 

   - Upside-down printing rotates line data 180 degrees. 

- STAR • The characters that are printed in upside-down printing are reversed, but the order of the lines that are printed are not in reverse. 

When upside-down printing is specified 

When upside-down printing is canceled 

**==> picture [351 x 84] intentionally omitted <==**

**----- Start of picture text -----**<br>
ABCDEF<br>012345<br>Paper Feed Cirection<br>ABCDEF<br>012345<br>**----- End of picture text -----**<br>


•Upside-down printing is enabled for the following images. a. ESC * : Specify bit image mode b. GS /: Print download bit images c. FS P: Print NV bit image mode 

ESC/POS Command Specifications 

77 
