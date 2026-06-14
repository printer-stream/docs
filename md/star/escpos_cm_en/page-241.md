Rev.2.52 

## **<Function 48> ESC GS ) B pL pH fn m  (fn = 48)** 

Name Enable and disables text search Code ASCII ESC GS ) B pL pH fn m Hex. 1B 1D 29 42 pL pH fn m Decimal 27 29 41 66 pL pH fn m 

Defined Region pL = 2, pH = 0 fn = 48 m=0, 1 

Initial Value Depends on setting registered in the non-volatile memory (At the time of shipment: m = 0) Function Makes text searches valid or invalid. 

|akes text|searches valid or invalid.|
|---|---|
|m|Set|
|0|Invalid|
|1|Valid|



When text search is valid, determines whether a string registered in the printer in advance is in the print data. 

If it is included, run a text search macro that corresponds to that string before or after running the following trigger command. 

- Execute cuts by continous <LF>. 

• <GS> “V” 

- <ESC> “i" 

- <ESC> “m” 

No setting when the parameter is not a valid value. 

This setting is applied to printer operations when this command is processed. 

This setting is registered to non-volatile memory by the ESC GS ) B <Function 80) command. This command is ignored when the text search macro is running. 

Disabled in Page Mode. 

ESC/POS Command Specifications 

241 
