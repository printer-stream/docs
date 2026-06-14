## **5.2.3. A utomatic Status** 

Automatic status is a group of states that are automatically returned from the printer to the host when the printer’s status has changed.  Automatic status is composed of “Header – 1,” “Header – 2” and “plurality of bytes of the printer status and is continuously returned to the host.  The host always uses an identifying method to identify the data for every byte received. 

(It is possible that Xon/Xoff codes are exceptionally mixed in the automatic status in the Xon/Xoff mode (when using a serial I/F), so it is necessary to consider that on the receiving side.) 

The valid/invalid conditions of the automatic status abide by the DIPSW settings for the initial values. It is possible to change the conditions using the ESC RS a n command after turning ON the power. Also, it is possible to get the automatic status using the ESC ACK SOH command, regardless of the valid/invalid conditions. 

## 1. Header – 1 

Header – 1 is the 1 byte length information transmitted at the head of the automatic status. 

The table below shows the composition of the Header – 1.  Header – 1 represents the entire status transmission byte count, including Header – 1, using bit 1 to bit 3 and bit 5.  The host gets the transmission byte information and always receives the status data for that amount transmission bytes.  For reference, the table below shows the relationship of actual transmission bytes and the Header – 1.  Because the bit 0 that indicates that this is the Header – 1 is normally 1 (the second byte and beyond is 0), to detect the Header – 1, it is acceptable to verify that bit 0 is 1 and bit 4 = 0 for this data.  Note that bit 6 is for future expansion and is ignored in host-side processes. 

<Header – 1 (First Byte)> 

|Bit<br>~~ee~~|Contents<br>~~ee~~|Status<br>~~ee~~|Status<br>~~ee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||“0”<br>~~ee~~<br>~~ee~~|“1”<br>~~ee~~<br>~~ee~~|TSP800<br>~~ee~~<br>~~ee~~|TSP700<br>~~ee~~<br>~~ee~~|TSP600<br>~~ee~~<br>~~ee~~|TUP900<br>~~ee~~<br>~~ee~~|TSP1000 <br>~~ee~~<br>~~ee~~|TSP828L <br>~~ee~~<br>~~ee~~|TSP700II T<br>~~ee~~<br>~~ee~~|II TSP650<br>~~ee~~<br>~~ee~~|TUP500T<br>~~ee~~<br>~~ee~~<br>~~ee~~|TSP800II<br>~~ee~~<br>~~ee~~<br>~~eee~~|FVP10<br>~~ee~~<br>~~ee~~<br>~~eee~~|
|7<br>~~ee~~<br>~~po~~<br>~~pot~~|Fixed at “0”<br>~~ee ~~<br>~~po~~<br>~~pot~~|~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~ee ~~<br>~~po~~|-<br>~~ee~~<br> ~~eee~~<br>~~po~~|-<br>~~ee~~<br>~~eee~~<br>~~po~~|
|6<br>~~pot~~<br>~~poof~~|Reserved(Fixed at “0”)<br>~~pot~~<br>~~poof~~||-|-|-|-|-|-|-|-|-|-|-|-|
|5<br>~~pot~~<br>~~poof~~<br>~~poof~~|PrinterStatusByte Count<br>~~pot~~<br>~~poof~~<br>~~poof~~|||OK<br>~~Ge~~|OK|OK|OK|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK|
|4<br>~~poof~~<br>~~eG~~<br>~~poof~~|Fixed at “0”<br>~~poof~~<br>~~eG~~<br>~~poof~~|~~eG~~|-<br>~~eG~~|-<br>~~eG~~<br>~~Ge~~|-<br>~~eG~~|-<br>~~eG~~|-<br>~~eG~~|-<br>~~eG~~<br>~~OO~~|-<br>~~eG~~<br>~~OO~~|-<br>~~eG~~<br>~~OO~~|-<br>~~eG~~<br>~~OO~~|-<br>~~eG~~<br>~~OO~~|-<br>~~eG~~<br>~~OO~~|-<br>~~eG~~|
|3<br>~~poof~~<br>~~pot~~|Printer Status  Byte Count<br>~~poof~~<br>~~pot~~|||OK<br>~~Ge~~|OK|OK|OK|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK|
|2<br>~~poof~~<br>~~pot~~<br>~~pot~~|PrinterStatusByte Count<br>~~poof~~<br>~~pot~~<br>~~pot~~|||OK<br>~~Ge~~|OK|OK|OK|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK|
|1<br>~~pot~~<br>~~pot~~|PrinterStatusByte Count<br>~~pot~~<br>~~pot~~|||OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
|0<br>~~pot~~<br>~~pot~~|Fixed at “1”<br>~~pot~~<br>~~pot~~|-<br>~~pot~~|~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|



Actual transmission byte count and header – 1 table 

|Transmission Byte Count n<br>(7 ≤<br>n ≤<br>15)|Header – 1|
|---|---|
|(7 ≤<br>15)<br>7|00001111B (0F Hex)|
|8|00100001B (21 Hex)|
|9|00100011B (23 Hex)|
|10|00100101B (25 Hex)|
|11|00100111B (27 Hex)|
|12|00101001B (29 Hex)|
|13|00101011B (2B Hex)|
|14|00101101B (2D Hex)|
|15|00101111B (2F Hex)|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-7 
