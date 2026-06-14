## **1. INTERF ACE CONFIGURATION** 

## **1.1. RS-232 Serial Interface** 

**1.1.1. Sp ecifications (Conforming to RS-232)** Rating: RS-232C Synch method: Start-Stop synchronization method Handshake: DTR mode Baud rates: 4800, 9600, 19200, 38400 bps (Set by DIP switches) Bit length: 7, 8 bits (Set by DIP switches) Parity: Yes/No (Set by DIP switches) Parity bit: Odd/even (Set by DIP switches) Stop bit: 1 bit (Fixed) Signal polarity: Mark    = logic 1 (-3 to -15 V) Space = logic 0  (+3 to +15 V) 

## **1.1.2. Signal array and explanations according to interface connector pin** 

<Signal Array and Functions> 

|Pin<br>No.<br>~~a~~|Signal Name<br>~~A~~|Signal<br>Direction<br>~~Cn~~|Remarks|
|---|---|---|---|
|1<br>~~a~~|FG<br>~~A~~|-<br>~~Cn~~|Frame ground|
|2<br>~~a ~~<br>~~a~~|TXD<br> ~~A~~|OUT<br>~~Cn~~|Transmissiondata|
|3<br>~~a ~~|RXD<br> ~~A~~|IN|Reception data|
|4<br>~~aA~~|RTS<br>~~aA~~|OUT<br>~~aA~~|Same as DTR|
|5<br>~~a~~|N.C<br>~~aSC~~|-<br>~~SC~~|Not used|
|6<br>~~a~~|DSR<br>~~SC~~|IN<br>~~SC~~|Not used|
|7<br>~~a~~|SG<br>~~SC~~|-<br>~~SC~~|Signal ground|
|8-19<br>~~aA~~|N.C<br>~~aA~~|-<br>~~aA~~|Not used|
|20|DTR|OUT|Data terminal ready signal  (SPACE: printer is ready to receive.)<br>1)  When in DTR mode:<br>When printer is ready to receive data: SPACE<br>2)  When in XON/XOFF mode:<br>Always SPACE except in the following conditions.<br>1. Until communication is possible after a reset.<br>2. When test printing|
|21-24|N.C||Signal ground|
|25<br>~~a~~|/INIT<br>~~a~~<br>~~A~~|IN|Signalground|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

1-1 
