Appendix 

|Pin|Source||Compatibility<br>Mode||Nibble Mode||Byte Mode|
|---|---|---|---|---|---|---|---|
|28|||GND||GND||GND|
|29|||GND||GND||GND|
|30|||GND||GND||GND|
|31|Host||Init||Init||Init|
|32|Printer||Fault||DataAvail/Data0,4||DataAvail|
|33|||GND||ND||ND|
|34|Printer||DK_STATUS||ND||ND|
|35|Printer||+5V||ND||ND|
|36|Host||SelectIn||1284-Active||1284-Active|



NC: Not Connected 

ND: Not Defined 

|•|A signal name with a rule above it indicates an “L” active signal.|
|---|---|
|•|Bidirectional communications cannot take place, unless all signal names for both sides|
|CAUTION|correspond to each other.|
|•|Connect all signal lines using a twisted-pair cable. Connect the return side to the signal|
||ground level.|
|•|Make sure the signals satisfy electrical characteristics.|
|•|Set the leading edge and trailing edge times to 0.5ms or less.|
|•|Do not ignore Ack<br>or BUSY signals during a data transfer. Ignoring such signals may|
||result in data corruption.|
|•|Make the interface cables as short as possible.|



**109** 
