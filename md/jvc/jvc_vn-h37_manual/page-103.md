**C800<CRLF>** 

Data(2) size of file1 

data(2) of file1 (50 kB) ... **C800<CRLF>** Data(1) size of file2 data(1) of file2 (50 kB) **C800<CRLF>** Data(2) size of file2 

data(2) of file2 (50 kB) ... **0<CRLF>** End of file 

**Interpretation** Specify start time and end time, then CHUNKED HTTP response and H.264 elementary stream 

data will be returned. 

**Allowed users** admin, operator 

## **33. List of Protocols and Port Numbers Used** 

The camera uses the following protocols and port numbers. 

|**Protocol / Port Number**|**Use**|
|---|---|
|TCP  20,21|FTP|
|TCP  25|SMTP(MailbyAlarm Action)|
|TCP  80|WEB setting page, API for Getting status and changing<br>settings,video/audio streaming by JVC protocol|
|UDP80|Search forthe camera|
|TCP  110|POP(MailbyAlarm Action)|
|UDP  123|SNTP|
|TCP554|RTSP|
|UDP9131|AMX DeviceDiscoveryProtocol|
|TCP  10020,10021,10023|reservedfor internaluse|
|TCP32040|Alarmserver|
|TCP  49298|Audio sendingfroma client to the camera|
|TCPUserSetting|Alarmon TCP|
|UDPUserSetting|AlarmonUDP|
|UDPUserSetting|Multicast Streaming|



## **34. Customizing Built-in Viewer** 

The built-in viewer of the camera consists of five ActiveX controls. These ActiveX controls are available for 

customized viewer. 

## **34.1. List of ActiveX** 

- JPEG/H.264 Viewer 

- PTZ Control Client 

It can show JPEG and H.264 video, and save still image. It can control digital ptz. 

- Audio Monitor It can playback audio. 

100 

Downloaded from www.Manualslib.com manuals search engine 
