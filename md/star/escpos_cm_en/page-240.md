Rev.2.52 

## < Text search functional overview > 

The following gives an example of command transmission used to set the printer to print the “first logo” at the end of receipt when the print data contains a character string “Cheese burger”. 

|~~a~~|~~ee es~~|~~es~~||
|---|---|---|---|
|~~a~~|~~ee es~~|Function No.<br>~~es~~|Contents|
|1<br>~~a~~<br>~~a~~|1C 71 ..<br>~~ee es~~|--<br>~~es~~|Register the logo as the first logo(see FSq).|
|2|1B 1D 29 42 02 00 51 00|Function 81|Initialize the settings and definitions of functions 48, 49, 50,<br>64,65,and 66.|
|3<br>~~a~~|1B 1D 29 42 02 00 30 01|Function 48|Enable text searching.|
|4<br>~~a~~|1B 1D 29 42 02 00 31 00<br>~~GO~~|Function 49<br>~~GO~~|Set the text search macro to run once.<br>~~GO~~|
|5|1B 1D 29 42 02 00 32 00|Function 50|Configure the print setting for the matched text string such<br>that the matched text stringisprinted.|
|6|1B 1D 29 42 11 00 40 01<br>01 0D 43 68 65 65 73 65<br>20 62 75 72 67 65 72|Function 64|Set the text search string with string number 1 to “Cheese<br>burger,” and set the text search macro that is executed<br>when this stringis included to text search macro 1.|
|7|1B 1D 29 42 08 00 41 01<br>04 00 1C 70 01 00|Function 65|Define text search macro 1 as a command to print logo 1<br>(see FSp).|
|8|1B 1D 29 42 03 00 42 01<br>01|Function 66|Set the execution time for the text search macro that is ex-<br>ecuted when text search string 1 is included (text search<br>macro 1 in this case)to immediatelybefore cutting.|
|9|1B 1D 29 42 02 00 60 00|Function 96|Print the settings and definitions of functions 48, 49, 50, 64,<br>65,and 66. Check the settings and definitions.|
|10|1B 1D 29 42 02 00 61 01|Function 97|Check the settings and definitions. Make sure the macro<br>runsproperly.|
|11|.. 43 68 65 65 73 65 20<br>62 75<br>72 67 65 72 .. 0A 1D 56<br>42 00|--|Send print data that includes a string such as that shown in<br>fig. 1 (“Cheese burger”) and a trigger command, and check<br>to make sure that the printed result is similar to fig. 2.|
|12|1B 1D 29 42 02 00 50 00|Function 80|Register the text search settings and definitions to non-<br>volatile memory. After you make sure that everything works<br>properly, use this command to register the text search set-<br>tings and definitions to non-volatile memory. Afterward,<br>even if you do not send commands 1 to 10, you can obtain a<br>printed result such as that shown in fig. 2 simply by sending<br>print data such as that shown in fig. 1.|



Before setting the text search 

After setting the text search 

The first logo is printed becuase the data contains the string “Cheese burger”. 

ESC/POS Command Specifications 

240 
