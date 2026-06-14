Rev.2.52 

## **6-2-5 Printer Status Transmission Specification When Using Ethernet and Wireless I/F** 

With a wireless LAN I/F, the printer status sending specifications are Star Original Expanded Status Specifications (*2). 

See the table below for printer status sending specifications for Ethernet I/F. 

|(1)<br>Spec.|Printer Status SendingSpecifcations|Printer Status SendingSpecifcations|Automatic Status SendingDestination Specifcations|Automatic Status SendingDestination Specifcations|
|---|---|---|---|---|
||Star Original Expanded ASB Specifcations(*2)||Distributes to All Hosts Connected to the Communication Port||
|||Printer Status Sending<br>Specifcations<br>Automatic Status Sending Destination<br>Specifcations<br>Star Original Expanded Status<br>Specifcations<br>(*2)<br>Distributes to All Hosts Connected to<br>the Communication Port<br>ESC/POS Standard Status<br>Compatibility Specifcations<br>(*1)<br>Sends Only to Host for Print Session|||
|(2)<br>Spec.|Ethernet I/F Used|Printer Status Sending<br>Specifcations||Automatic Status Sending Destination<br>Specifcations|
||IFBD-HE05/06<br>F/W Version (Main) Ver.<br>1.0.1|Star Original Expanded Status<br>Specifcations<br>(*2)||Distributes to All Hosts Connected to<br>the Communication Port|
||IFBD-HE05/06<br>F/W Version (Main) Ver.<br>1.1.0|ESC/POS Standard Status<br>Compatibility Specifcations<br>(*1)||Sends Only to Host for Print Session|



(*1) ESC/POS Standard Status Compatibility Specifications 

In the same way as serial, parallel and USB, ASB is standard 4 bytes for ESC/POS, and the status using ESC/POS inquiry commands (DLE EOT, GS r, GS I, ESC v, ESC u etc.) is 1 byte for ESC/POS. 

NSB function is fixed at invalid (does not send automatic status to the connected host), and ASB function can be set to valid/invalid. 

(*2) Star Original Expanded Status Specifications 

The following describes the Star Original Expanded Status Specifications. 

With these specifications, ESC/POS standard status (ASB or other statuses) are sent embedded in expanded status data attached to Star ASB. 

See the STAR Line Mode Command Specifications for details on STAR ASB specifications. 

NSB function is fixed at valid (sends automatic status to the connected host), and ASB function is fixed at valid. 

The following will describe printer status transmission specifications for using an Ethernet interface and a wireless LAN interface. 

See the Star Line Mode Command Specifications foe details on Star’s ASB specifications. 

## 1) Transmission Format 

• For transmitting only STAR ASB STAR ASB (Second Byte Bit 7 = 1) + Length (Length = 0x0000) • For transmitting printer status other than STAR ASB STAR ASB (Second Byte Bit 7 = 1) + Length + Status Data 

## <Length Details> 

- 2 byte value indicating status data byte count (0x0000 ≤ Length ≤ 0x0200) 

- When the status data is 10 bytes: Length = 0x000a 

- Apply Length = 0x0000 to only transmit STAR ASB. 

- When STAR ASB Second Byte B-7 is applied with Length, set to Bit-7 = 1 

Status analysis detects the total byte count of ASB using the first byte of STAR ASB, and detects whether Length is appended using the second byte bit-7 of STAR ASB. It is also possible to analyze the status by getting the byte count of subsequent byte counts. 

ESC/POS Command Specifications 

272 
