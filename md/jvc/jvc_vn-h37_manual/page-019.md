Ratio of I-VOP and P-VOP depends on I-Frame interval setting. Encode page of Web has the setting. 

First VOP can be I-VOP or P-VOP. If client want to decode from I-VOP, please skip P-VOP and wait first I-VOP. 

## **Example of MPEG-4 Stream** 

HTTP response P-VOP P-VOP P-VOP VOL I-VOP P-VOP ~ 

There are VOL, Userdata1, GOV and Userdata2 before each I-VOP. 

Data structure before I-VOP 

|Data structure before I-VOP||
|---|---|
|Item|Note|
|VOL|VOL of MPEG-4 Video|
|Userdata1|Reserved|
|GOV|GOVof MPEG-4 Video|
|Userdata2|Userdata|



Data structure of Userdata2 

|Item|Size|Example|Note|
|---|---|---|---|
|Start code|4|0x000001B2|Start code ofUserdatain MPEG-4stream.|
|Model Name|18|type=VN-H137|Product Name|
|Time Stamp|70|timestamp<br>=<br>2012030623341253<br>8UTC|<br>This<br>is<br>made<br>up<br>of<br>the<br>year/month/day,<br>hour/minute/second, millisecond and timezone code.|
|Camera ID|50|camera= input01|Camera ID that user can define|
|Motion Detect Result|7|md = 1|Specified as 1 if motion is detected at the time when<br>datais created.|
|Tampering Detect<br>Result|14|tampering = 0|Specified as 1 if tampering is detected at the time when<br>datais created.|
|Pan position|16|digipan=123|Indicates pan position in pixels from 0 to 1278.|
|Tilt position|17|digitilt= 123|Indicates tilt position inpixelsfrom0 to 958.|
|Zoom position|17|digizoom=1.23|Indicates zoom value from 1.00 to 8.00.|
|Preset Posision<br>Number|15|position = 19|Indicates preset position number after moving to<br>preset position. Inothercases, position = NA.|



16 

Downloaded from www.Manualslib.com manuals search engine 
