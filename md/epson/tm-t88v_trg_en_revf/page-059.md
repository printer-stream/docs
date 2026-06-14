Chapter 4   Advanced Usage 

4 

When using the serial or parallel interface, it is not necessary to change the DIP switch setting but their function changes. For the details, see "For Serial Interface" on page 56 and "For Parallel Interface" on page 58. 

## DIP Switch Bank 1 

|SW|Function|ON|OFF|Default<br>setting|
|---|---|---|---|---|
|1-1|Auto line feed|Always enabled|Always disabled|OFF|
|1-2|Receive buffer capacity|45 bytes|4 KB|OFF|
|1-3∼<br>1-6|Undefined|—||OFF|
|1-7|Undefined|—||*|
|1-8|Setting of USB power-saving<br>function|Disabled|Enabled|OFF|



* Varies depending on the interfaces. 

## DIP Switch Bank 2 

|SW|Function|ON|OFF|Default<br>setting|
|---|---|---|---|---|
|2-1|Handshaking (BUSY condition)|Receive buffer full|• Offline<br>• Receive buffer full|OFF|
|2-2|Reser ved (Do not change<br>setting)|Fixed to OFF||OFF|
|2-3∼<br>2-4|Selects print density|See"Selecting the Print Density (DIP Switches<br>2-3/2-4)" on page 62.||OFF|
|2-5|Sets the release condition of the<br>receive buffer BUSY state. (This<br>function is effective when DIP<br>Switch 1-2 is set to off.)|Releases the BUSY<br>state<br>when<br>the<br>remaining capacity<br>of the receive buffer<br>reaches 138 bytes.|Releases the BUSY<br>state<br>when<br>the<br>remaining capacity<br>of the receive buffer<br>reaches 256 bytes.|OFF|
|2-6∼<br>2-7|Reser ved (Do not change<br>settings)|Fixed to OFF||OFF|
|2-8|Reserved|—||*|



* Varies depending on the interfaces. 

For DIP Switch 2-1 (BUSY condition), see also "Selecting the BUSY Status" on page 62. 

**59** 
