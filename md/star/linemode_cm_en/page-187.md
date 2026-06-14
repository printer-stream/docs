2. Separator character 1 (1 Byte) Sends “:” 

## 3. Data Type (1byte) 

Indicate printer status data; sends “B” (binary type). 

## 4. Status Length (2 bytes) 

- 2 byte value indicating printer status byte count. 

## 5. Printer Status (Variable length) 

Status sent by printer. Status differs according to the cause. 

See the command causes and automatic status for details on the content of statuses. 

## 6. Separator character 2 (1 Byte) 

Sends “;” 

3) Status Transmission Specification List 

|Status Cause<br>~~|~~|STAR ASB<br>||Length<br>~~LLL~~|StatusData<br>~~|~~<br>~~LLL~~|StatusData<br>~~|~~<br>~~LLL~~|StatusData<br>~~|~~<br>~~LLL~~|StatusData<br>~~|~~<br>~~LLL~~|StatusData<br>~~|~~<br>~~LLL~~|StatusData<br>~~|~~<br>~~LLL~~|StatusData<br>~~|~~<br>~~LLL~~|
|---|---|---|---|---|---|---|---|---|---|
||||StatusType<br>~~|~~<br>~~LLL~~||Separated<br>Character 1<br>~~|~~<br>~~LLL~~|Data<br>Type<br>~~|~~<br>~~LLL~~|Status<br>Length<br>~~|~~<br>~~LLL~~|Printer<br>Status<br>~~|~~<br>~~LLL~~|Separated<br>Character 2<br>~~|~~<br>~~LLL~~|
||||First/Second<br>Bytes<br>Cause<br>~~|~~<br>~~LLL~~|Third/Fourth<br>Bytes<br>n Parameter<br>~~|~~<br>~~LLL~~||||||
|ASB<br>Automatic Status<br>~~es~~|ASB|0x0000|--|--|--|--|--|--|--|
|ESC ACK SOH<br>Printer<br>Status<br>Request<br>~~es~~|ASB|0x0000|--|--|--|--|--|--|--|
|ENQ<br>Printer<br>Status<br>Request|ASB|0x0008|“01”|Omitted|“:”|“B”|0x0001|Status|“;”|
|EOT<br>Printer<br>Status<br>Request|ASB|0x0008|“02”|Omitted|“:”|“B”|0x0001|Status|“;”|
|ESC SYN 3 n<br>Presenter Counter<br>Request|ASB|0x0011|“13”|“00”≤<br> n≤<br> “01”<br>“30”≤<br> n≤<br> ”31”|“:”|“B”|0x0008|Status|“;”|
|ESC GS x I<br>PDF417<br>Information<br>Request|ASB|0x000C|“16”|Omitted|“:”|“B”|0x0005|Status|“;”|
|ESC GS y I QR<br>Code<br>Information<br>Request|ASB|0x000D|“19”|Omitted|“:”|“B”|0x0006|Status|“;”|
|ESC GS ETS n1 n2<br>Print End Counter<br>Request|ASB|0x000F|“20”|Omitted|“:”|“B”|0x0008|Status|“;”|



(*1) Automatic status is distributed to all hosts connected to the TCP#9,100 port. 

*  Installed MSW region is different depending on the model. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-15 
