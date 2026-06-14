WindowsVista : Documents Windows7 : Documents Default: In case of VN-H37: VN-H37 In case of VN-H137: VN-H137 In case of VN-H237: VN-H237 In case of VN-H237VP: VN-H237VP In case of VN-H57: VN-H57 In case of VN-H157WP: VN-H157 In case of VN-H257: VN-H257 In case of VN-H257VP: VN-H257VP OpPassword Operator Password of the camera 

## **PTZ Control Client** 

|**PTZ Control Client**||
|---|---|
|Property|Meaning|
|IP|IP address of the camera<br>Default: 192.168.0.2|
|HttpPort|Port number of the camera<br>(1 - 65535）Default: 80|
|DispLang|Language of error messages<br>(0:Japanese,1: English)Default:0|
|OpPassword|Operatorpassword ofthe camera|
|PanTiltSpeed|Speed of manual pan/tilt control<br>(1 –8)Default: 4|
|FocusZoomSpeed|Speed of manual zoom control<br>(1 – 4)Default: 2|
|BlackAndWhiteMode|Easy Day and Night<br>(0: Auto, 3:Color,4: BlackandWhite)|
|WhiteBalance|White Balance<br>(0: ATW,2: AWC)|
|BLC|Back Light Compensation<br>(0:Off,1: Area1,2: Area2, 3: Area3,4: Area4)|
|AutoFunctionStatus|Status of current auto function<br>(0:stop,1:auto patrol isworking)|
|PositionTitle(n)|Getting the position title of registered preset position<br>n: Position Number(0– 19)|
|FocusAssistMode|Focus Assist Mode<br>(0:stopped,1: working)|



## **Audio Monitor/Audio Sending Client [VN-H57/VN-H157WP/VN-H257/VN-H257VP only]** 

|Property|Meaning|
|---|---|
|IP|[Audio Monitor]<br> IP address of the camera in case of unicast receiving<br> IP multicast address in case of multicast receiving<br>[Audio Sending Client]<br> IP address of the camera<br>Default: 192.168.0.2|
|Port<br>*Audio Monitor only|Port number of the camera in case of unicast receiving<br>Port number of multicast in case of multicast receiving<br>(1 –65535)Default:80|
|ApiPort<br>*Audio Sending<br> Client only|HTTP port number of the camera<br>(1 – 65535)  Default: 80|
|SoundPort<br>*Audio Sending<br> Client only|Destination port number of audio stream from PC to the camera<br>(1 – 65535)  Default: 49298|
|Result<br>*Audio Sending<br> Client only|Result of starting audio atream to the camera by “Play()” method.<br>(0: failed, 1: success)|
|Password|Operator password of the camera|



102 

Downloaded from www.Manualslib.com manuals search engine 
