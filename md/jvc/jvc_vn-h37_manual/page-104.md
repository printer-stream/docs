- Audio Sending Client It can send audio from PC to the camera. 

## How to download ActiveX controls: 

- i) Please input URL below in Internet Explorer’s url form. 

http://(IP Address)/ IntegratedViewer.cab 

- Ex.) When IP address of the camera is “192.168.0.2”: 

http://192.168.0.2/IntegratedViewer.cab 

ii) Download dialog box is showed. Please click save button and copy to some folder in the PC. 

## **34.2. Properties of ActiveX** 

**JPEG /H.264 Viewer** 

|Property|Meaning|
|---|---|
|IP|IP Address of the camera: Required when RcvMode is unicast.<br>Default: 192.168.0.2|
|HttpPort|Port Number of the camera: Required when RcvMode is unicast.<br>(1 - 65535）Default: 80|
|MultiIP|IP Address of multicast: Required when RcvMode is multicast.<br>Default: 225.0.1.1|
|MultiPort|Port Number of multicast: Required when RcvMode is multicast.<br>(1 -65535)Default: 49152|
|RcvMode|Desired stream<br>(0:unicast,1: multicast)|
|FrameRate<br>*JPEG only|Frame Rate of JEPG<br>To specify a frame rate lower than 1fps, use “-“. For example, specify -5 for 1/5 fps.<br>(15,  10, 7.5, 6, 5, 3, 2, 1, -2, -3, -5, -10, -15, -20, -30, -60)<br>Default:5|
|DispWidth|Width of Display<br>When the size is different from original frame size, the image is scaled.<br>Default:640|
|DispHeight|Height of Display<br>When the size is different from original frame size, the image is scaled.<br>Default:360|
|DispTitle|Display of Camera ID<br>(0: hide,1:display)Default:0|
|DispMotion<br>*JPEG only|Display of Motion Detection<br>(0: hide,1:display)Default:0|
|DispPosTitle|Display of Position Title<br>(0: hide,1:display)Default:0|
|DispTimeCode|Display of Time Code<br>(0: hide, 1: display)  Default: 0|
|TimeFormat|Format of Time Code<br>( 0:  YYYY/MM/DD HH:MM:SS.mm<br>1:  YYYY/MM/DD HH:MM:SS<br>2:  DD/MM/YYYY HH:MM:SS<br>3:  MM/DD/YYYY HH:MM:SS<br>4:  MM/DD HH:MM:SS<br>5:  HH:MM:SS<br>6:  HH:MM)<br>*Y: Year  M: Month  D: Day  H: Hour  M: Minute  S: Second  m: milli second<br>Default: 1|
|FolderName<br>*JPEG only|Folder Name of saving still images.<br>This folder is created in<br> WindowsXP<br>: MyDocuments|



101 

Downloaded from www.Manualslib.com manuals search engine 
