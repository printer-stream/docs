## _Error Status_ 

There are three possible error types: automatically recoverable errors, recoverable errors, and unrecoverable errors. 

Printing is no longer possible when automatically recoverable errors occur. They can be recovered easily, as described below. 

|Error|Error description|Error LED flash code|Recovery measure|
|---|---|---|---|
|Roll paper<br>cover open<br>error|The roll paper cover<br>was opened during<br>printing.|LED ON<br>LED OFF<br>Approx. 160 ms|Recovers automatically<br>when the roll paper<br>cover is closed.|
|Print head<br>temperature<br>error|A high temperature<br>outside the head drive<br>operating range was<br>detected.|LED ON<br>LED OFF<br>Approx. 160 ms|Recovers automatically<br>when the print head<br>cools.|



Printing is no longer possible when recoverable errors occur. They can be recovered easily by turning the power on again or sending an error recovery command from the driver after eliminating the cause of the error. 

|Error|Error description|Error LED flash code|Error LED flash code|Recovery measure|
|---|---|---|---|---|
|Autocutter<br>error|Autocutter does not<br>work correctly.|LED ON<br>LED OFF<br>Approx. 160 ms|Approx. 2560 ms|Remove the jammed<br>paper or foreign matter<br>in the printer, close the<br>roll paper cover, send<br>the error recovery<br>command, or turn the<br>power on to recover.|



The error recovery command is valid only if a recoverable error (excluding automatically recoverable errors) occurs. 

**20** 
