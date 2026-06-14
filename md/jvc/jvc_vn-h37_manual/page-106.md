## **34.3. Method of ActiveX Control** 

## **JPEG /H.264 Viewer** 

|Method|Meaning|
|---|---|
|Play()|Start playback|
|Stop()|Stop playback|
|Capture()<br>*JPEG only|Save still image of JPEG<br>(Saved folder is specified by “Folder Name” of property)|



## **PTZ Control Client** 

|**PTZ Control Client**||
|---|---|
|Method|Meaning|
|Initialize()|Initialize PTZ Control Client<br>*Itmust be called before using ptzcontrol|
|Destroy()|Finalizing PTZ Control Client<br>*Itmust be calledwhenthe applicationusingActiveXcontrol is closed.|
|ManualCtrl(n)|Start Pan/Tilt according to specified direction<br>**Direction**  **Number of  “n”**<br>upper-left    up      upper-right                         7  8  9<br>left                         right                                   4  5  6<br>under-left   down   under-right                        1  2  3|
|ZoomCtrl(n)|Start Zoom-In/Zoom-Out<br>(n =0: Zoom-In,n = 1: Zoom-Out)|
|Stop()|StopPan/Tilt/Zoom|
|SetAutoFunction(n)|Control Auto Patrol<br>(n =0:stop auto patrol,n = 2:start auto patrol)|
|OnePushAWC()|Issue one push AWC|
|SetPosition(n, str)|Register current position as preset position<br>n: Position Number (0 – 19)<br>str: Position Title (0-32characters)|
|DeletePosition(n)|Unregister specified preset position<br>n: Position Number(1 – 19) *Cannot unregister HomePosition|
|MovePosition(n)|Move to specified preset position<br>n: Position Number (0 – 19)|



## **Audio Monitor/Audio Sending Client** 

|Method|Meaning|
|---|---|
|Play()|[Audio Monitor]<br> Start playback<br>[Audio Sending Client]<br>Start audio stream<br> *Result ofstarting audio stream is storedin “Result”ofproperty|
|Stop()|[Audio Monitor]<br> Stop playback<br>[Audio Sending Client]<br> Stop audio stream|
|Destroy()<br>*Audio Sending<br>  Client only|Finalize Audio Sending Client<br>*It must be called when the application using ActiveX control is closed.|



## **34.4. How to use ActiveX Control by HTML** 

If write the next code in <Body> of HTML source code, It comes to be able to use ActiveX in HTML. 

103 

Downloaded from www.Manualslib.com manuals search engine 
