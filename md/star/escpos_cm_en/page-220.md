Rev.2.52 

The settings above are set individually, so the errors described below may be generated even if there is no particular problem in those settings.  In such case, if the bar code is generated the (3) print command (<ESC> <GS> “x” “P”) is ignored. 

- Error is generated when generating a bar code, due to the combination of the bar code setting commands. 

- The bar code data that is generated exceeds the printable size of PDF417. 

- Print data exceeds the currently set print region. 

It is recommended to use (4) Bar code expansion information acquisition (<ESC> <GS> “x” “I”) as a means for checking these errors prior to printing. 

## **(2) Bar code data setting command** 

This command sets the print data of the bar code. 

## **(3) Bar code print command** 

- Standard mode 

This command prints the bar code according to the settings of (1) and (2). 

- Page mode 

This command expands to the bar code image buffer according to the settings of (1) and (2). 

## **- Precautions for use of commands -** 

- Unless the following operations are performed, the setting values are maintained for (1) and (2). This setting value is held between both the standard mode and the page mode. 

   - Sending of new setting commands 

   - Sending an initializing command (<ESC> @, <CAN>) 

   - The power is turned off 

- Sent each time for (3). 

- Printing 

• When printing, position shifting according to the horizontal tab, absolute position specification, relative position specification, and position alignment is valid. 

   - Upside-down printing and two-color printing are possible. 

- When a bar code is printed, always verify it by actual use. 

Send the command transmission example last. 

- = ESC/POS standard mode = 

1. Bar code type setting 

<ESC> <GS> “x” “S” “0” 0 2 3: Sets the bar code size to USE_LIMITS = 2:3 <ESC> <GS> “x” “S” “1” 3: Sets ECC level to 3 <ESC> <GS> “x” “S” “2” 3: Sets the module X direction size to 3 dots <ESC> <GS> “x” “S” “3” 3: Sets module aspect ratio to 3 

2. Bar code data setting 

   - <ESC> <GS> “x” “D” 10 0 “0123456789”: Sets the bar code data 

## 3. Printing bar code 

To verify whether printing is possible with the current settings, check the bar code expansion information <ESC> <GS> “x” “I”: Bar code expansion information check <ESC> <GS> “x” “P”: Print 

ESC/POS Command Specifications 

220 
