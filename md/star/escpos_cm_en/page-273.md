Rev.2.52 

## **6-2-4 ASB Status Specifications** 

This ASB status applies to the following I/F.  The STAR mode ASB status is sent with a USB I/F.  (Refer to the “STAR Line Mode Command Specifications Manual” for details regarding the STAR mode ASB status.) 

- USB 

With the USB I/F on the models below, Star Mode ASB status is sent. 

(See the Star Line Mode Command Specifications for details on the Star Mode ASB status.) 

TSP600/TSP700/TSP800/TUP900/TSP1000/TSP700II Ver. 1.0 to 1.4/TSP650 Ver. 1.0 to 1.4/ 

TUP500 Ver. 1.0 

- RS-232C 

- Parallel 

- Ethernet (See section 6-2-5 Printer Status Transmission Specification When Using Ethernet and Wireless I/F for details.) 

- Wireless LAN (See section 6-2-5 Printer Status Transmission Specification When Using Ethernet and Wireless I/F for details.) 

- Bluetooth 

## 1. First Byte (Printer Information) 

|Bit|Contents|Status|Status|Targeted Status n|Targeted Status n|Targeted Status n|Targeted Status n|Targeted Status n|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|CompatibilityPer Model|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||“0”|“1”|Bit7|Bit3|Bit2|Bit1|Bit0|TSP600|TSP700|TSP800|TUP900|TSP1000|TSP700II|TSP650|TUP500|TSP800II|FVP10|BSC10|TSP043|TSP650II|TSP650IISK|
|7|Fixed at “0”||||||||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|6|Paper SW input|No SW<br>Input|SW<br>Input||||○||○|○|○|○|○|○|○|○|○|○|○|○|○|○|
|5|Cover Status|Closed|Open||||○||○|○|○|○|○|○|○|○|○|○|○|○|○|○|
|4|Fixed at “1”||||||||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|3|ONLINE/OFFLINE<br>Status|ONLINE|OFFLINE||||○||○|○|○|○|○|○|○|○|○|○|○|○|○|○|
|2|Drawer kick<br>connectorpin #3|“L”|“H”|||||○|○|○|○|x|x|○|○|x|○|○|○|○|○|○|
||Presenter Cover|Closed|Open||||○||x|x|x|x|x|x|x|x|x|x|x|x|x|x|
|1|Undefned(“0”)||||||||-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|0|Undefned (“0”)||||||||-|-|-|-|-|-|-|-|-|-|-|-|-|-|



Bit-2:  Drawer kick connector #3 pin status is allocated for models not equipped with a presenter; presenter cover status is allocated to those models equipped with a presenter.  TUP900 and TUP500 are provided with a present er, but this bit is invalid because it does not have a presenter cover. 

ESC/POS Command Specifications 
