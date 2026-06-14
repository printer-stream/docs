## **5.2.4 Prin ter status transmission specification when using Ethernet I/F and Wireless LAN I/F** 

The following describes printer status transmission specifications when using an Ethernet I/F and wireless LAN I/F. 

## 1) Transmission Format: 

• When transmitting only STAR ASB: ~~a~~ STAR ASB (Second Byte Bit 7 = 1) + Length (Length = 0x0000) 

## • When transmitting printer status other than STAR ASB: ~~7~~ STAR ASB (Second Byte Bit 7 = 1) + Length ~~6)~~ + Status Data 

## <Length Details> 

- 2 byte value indicating status data byte count (0x0000 ≤ Length ≤ 0x0200) 

- When the status data is 10 bytes: Length = 0x000a 

- Apply Length = 0x0000 to only transmit STAR ASB. 

- When STAR ASB Second Byte Bit-7 is applied with Length, set to Bit-7 = 1 

In analysis of printer statuses, the total number of bytes of the ASB according to the STAR ASB First byte is detected, and it is detected whether Length has been applied by the second byte Bit-7 of STAR ASB. Depending on the length, by acquiring subsequent status data byte counts, it is possible to analyze the status. 

## 2) ~~a~~ Status data transmission format 

~~PO~~ Status type + separator character 1 ~~SS~~ + data type + status length + _printer status_ + separator character 2 

1. Status Type (2byte or 4Byte) 

   - First and Second Bytes 

Indicate the cause to generate a printer status. • “00”: Reserved • “01” to ”09”: Star real-time status request command • ”10” to ”49”: Star status request command • “50”: Reserved • “51” to ”59”: Reserved • “60” to ”99”: Reserved • “A0” to “FF”: Reserved 

• Third and Fourth Bytes When a cause occurs, these indicate the command n parameter. If there is no n parameter, the third and fourth bytes can be omitted. <Ex.> When n = 0x31 using the ESC SYN 3 n command, the third and fourth bytes are “31.” 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-14 
