Rev.2.52 

**<Function 80> ESC GS ) B pL pH fn m  (fn = 80)** Name Register text search settings and definitions in the non-volatile memory Code ASCII ESC GS ) B pL pH fn m Hex. 1B 1D 29 42 pL pH fn m Decimal 27 29 41 66 pL pH fn m 

Defined Region pL = 2, pH = 0 fn = 80 

m = 0 

Initial Value --Function Registers the text search setting to non-volatile memory. 

The following shows the contents to register. 

|Function No|Contents|
|---|---|
|Function 48|Enable and disables text search|
|Function 49|Set the number of times to run the text search macro|
|Function 50|Set toprint the stringthat matches in the text search<br>|
|Function 64|Defne the text search string<br>|
|Function 65|<br>Defne the text search macro<br>|
|Function 66|<br>Defne the timingof the text search macro execution<br>|
|Function 81|<br>Initialize text search settings and defnitions|



After registration ends, resets the printer. 

The printer operates by reading the setting registered using this command the next time the printer power is turned on. 

This command is ignored when the text search macro is running. 

Consider the life of the non-volatile memory and avoid over-sue of this command. 

Disabled in Page Mode. 

ESC/POS Command Specifications 

247 
