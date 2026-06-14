## **1.2. Parallel Interfaces (Amphenol 36 pins)** 

## **1.2.1. Specifications (Conforming to IEEE1284)** 

Rating: Conforms to IEEE 1284 Mode: Compatibility Mode/Nibble Mode/Byte Mode Data transfer speed: 1000 to 6000 CPS Synch method: According to externally supplied strobe pulse Handshake: According to ACK and BUSY signals Logic level: Compatible to TTL 

## **1.2.2. Signal array and explanations according to interface connector pin** 

<Signal Array and Functions> 

|Pin No.|Compatibility Mode Signal Name|Nibble Mode Signal Name|Byte Mode Signal Name|
|---|---|---|---|
|1<br>2 to 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19 to 30<br>31<br>32<br>33<br>34<br>35<br>36|nStrobe<br>Data0 to 7<br>nAck<br>Busy<br>PError<br>Select<br>N/C<br>N/C<br>Signal GND<br>Frame GND<br>+5V<br>Twisted Pair Return<br>nInit<br>nFault<br>External GND<br>N/C<br>N/C<br>nSelectIn|HostClk<br>Data0 to 7<br>PtrClk<br>PtrBusy/Data3,7<br>AckDataReq/Data2,6<br>Xflag/Data1,5<br>HostBusy<br>-<br>Signal GND<br>Frame GND<br>+5V<br>Twisted Pair Return<br>nInit<br>nDataAvail/Data0,4<br>-<br>-<br>-<br>1284Active|HostClk<br>Data0 to 7<br>PtrClk<br>PtrBusy<br>AckDataReq<br>Xflag<br>HostBusy<br>-<br>Signal GND<br>Frame GND<br>+5V<br>Twisted Pair Return<br>nInit<br>nDataAvail<br>-<br>-<br>-<br>1284Active|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 1-4 
