Rev.2.52 

## **ESC GS x P** 

Name Print PDF417 bar code Code ASCII ESC GS x P Hex. 1B 1D 78 50 Decimal 27 29 120 80 --Defined Area Initial Value --Function This command prints bar code data or expands it to the image buffer. 

Also, this command is ignored if the following errors occur. 

- When an error is generated when generating a bar code, due to the combination of the bar code setting commands 

- When the bar code data that is generated exceeds the printable size of PDF417 

- When the print data exceeds the currently set print region 

When a bar code is printed, always verify it by actual use. 

## Standard mode 

If there is unprinted data in the line buffer, after that data is printed, and this command is executed, the bar code is printed.  Therefore, it is not possible to print with other data (characters, bit images, or bar codes) existing in the same line. 

Page mode 

This command only expands bar code data to the image buffer. 

ESC/POS Command Specifications 

225 
