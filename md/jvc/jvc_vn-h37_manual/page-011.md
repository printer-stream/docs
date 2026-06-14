4) When the client wants to stop current JPEG transmission, the client disconnects TCP80. 

The camera does not accept further API via current TCP that is used for JPEG transmission. To change parameter, disconnect current TCP to stop the JPEG transmission, connect new TCP, and send API with new parameter. 

## **2.2. API Format** 

## **Structure** 

|GET|space|API|space|HTTP/1.1|0x0D 0x0A|0x0D 0x0A||
|---|---|---|---|---|---|---|---|
|Host:|space|IP Address of Camera|0x0D 0x0A 0x0D 0x0A|||||



Unlike APIs for getting/setting parameters, Accept line is not required. Basic authentication is also not necessary. 

## **Example** 

## **GET /api/video?encode=jpeg(1)&framerate=5&server_push=on HTTP/1.1<CRLF>** 

## **Host: 192.168.0.2<CRLF><CRLF>** 

Parameter value is indicated using =. Do not insert space before and after =. 

Example    framerate=1 

Parameters are segmented using &. Do not insert space before and after &. 

Example encode=jpeg&framerate=5 

There is no need to specify all parameters. Default values will be used for parameters that are not specified. 

## **Parameter Description** 

**encode** For specifying compression format with channel number. For example, specify as encode=jpeg(1) to get JPEG encoded by channel 1.  To know compression format of each channel, open Encoder setting page by IE described in INSTRUCTIONS manual,  or issue "encode" API described in later chapter of this document. **framerate** For specifying the frame rate. For example, specify as framerate=5 to get at 5 fps. Specify as framerate=-5 to get at 1/5 fps, or in other words, 1 frame in 5 seconds. Selection range for JPEG is as follows. 30, 15, 10, 7.5, 5, 3, 2, 1, 0, -2, -3, -5, -10, -15, -20, -30, -60 

When the parameter is specified as framerate=0, the camera sends 1 frame of JPEG data, and disconnect the TCP connection. 

**server_push** For specifying streaming structure. For example, specify as server_push=on to get Server Push 

8 

Downloaded from www.Manualslib.com manuals search engine 
