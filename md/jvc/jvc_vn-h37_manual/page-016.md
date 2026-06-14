H.264 stream form the camera is sequence of I Picture and P Picture. Ratio of I Picture and P Picture depends on 

I-Frame interval setting. Encode page of Web has the setting. 

## **Example of H.264 Stream** 

HTTP response Sequence Parameter Set Picture Parameter Set User data I Picture User data P Picture ~ User data I Picture 

There are Sequence Parameter Set, Picture Parameter Set, and User data before each I Picture and there is User data before each P Picture. 

The following information is stored in the User data. Each item has a fixed length. 

|Item|Size|Example|Note|
|---|---|---|---|
|Start code|4|0x00000001|Start code ofUserdatain H.264stream.|
|NALunit type|1|0x66|NALunit type ofUserdatain H.264stream.|
|Payload type|1|0x05|Payload type ofUserdatain H.264stream.|
|Userdata size|1|0xf0|Size ofUserdatain H.264stream.|
|Reserved|16|0x030303030303030<br>30303030303030303|－|
|Model Name|18|type=VN-H137|Product Name|
|Time Stamp|70|timestamp<br>=<br>2012030623341253<br>8UTC|<br>This<br>is<br>made<br>up<br>of<br>the<br>year/month/day,<br>hour/minute/second, millisecond and timezone code.|
|Camera ID|50|camera= input01|Camera ID that user can define|
|Motion Detect Result|7|md = 1|Specified as 1 if motion is detected at the time when<br>datais created.|
|Tampering Detect<br>Result|14|tampering = 0|Specified as 1 if tampering is detected at the time when<br>datais created.|



13 

Downloaded from www.Manualslib.com manuals search engine 
