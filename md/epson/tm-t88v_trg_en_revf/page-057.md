Chapter 4   Advanced Usage 

4 

## Transmission Speed (DIP Switches 1-7/1-8) 

|Transmission speed (bps: bits per second)|SW 1-7|SW 1-8|
|---|---|---|
|Depends on the memory switches (customized value) settings.*|ON|ON|
|4800|OFF|ON|
|9600 (default)|ON|OFF|
|19200|OFF|OFF|



## bps: bits per second 

* The default value of transmission speed set with memory switches (customized value) is 38400 

bps. (See "Setting the Memory Switches (Customized Value)" on page 63.) 

Depending on print conditions, such as print duty, print head temperature, and data transmission speed, print speed is automatically adjusted, which can cause white lines due to intermittent print (the motor sometimes stops). To avoid this, set the transmission speed higher or keep the print speed constant by setting it lower. 

## DIP Switch Bank 2 

|SW|Function|ON|OFF|Default<br>setting|
|---|---|---|---|---|
|2-1|Handshaking (BUSY condition)|Receive buffer full|• Offline<br>• Receive buffer full|OFF|
|2-2|Reser ved (Do not change<br>setting)|Fixed to OFF||OFF|
|2-3∼<br>2-4|Selects print density|See"Selecting the Print Density (DIP Switches<br>2-3/2-4)" on page 62.||OFF|
|2-5|Sets the release condition of the<br>receive buffer BUSY state. (This<br>function is effective when DIP<br>Switch 1-2 is set to off.)|Releases the BUSY<br>state<br>when<br>the<br>remaining capacity<br>of the receive buffer<br>reaches 138 bytes.|Releases the BUSY<br>state<br>when<br>the<br>remaining capacity<br>of the receive buffer<br>reaches 256 bytes.|OFF|
|2-6|Reser ved (Do not change<br>setting)|Fixed to OFF||OFF|
|2-7|I/F pin 6 reset signal|Enabled|Disabled|OFF|
|2-8|IF pin 25 reset signal|Enabled|Disabled|OFF|



- For DIP Switch 2-1 (BUSY condition), see also "Selecting the BUSY Status" on page 62. 

- When you use the APD, change the setting of DIP switch 2-1 (BUSY condition) to ON. 

**57** 
