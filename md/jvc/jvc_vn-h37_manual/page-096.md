,,, 

Structure of 12 bytes header is as below. First 4 bytes is payload type for u-Law. 

0x00000080 Volume of payload (512 for u-Law) Time stamp in 8kHz 

5) When the client wants to stop current audio transmission, the client disconnects TCP80. 

The camera does not accept further API via current TCP that is used for audio transmission. To change parameter, dsconnect current TCP to stop the audio transmission, connect new TCP, and send API with new parameter. 

## **29.2. API Format** 

## **Structure** 

|GET|space|API|space|HTTP/1.1|0x0D 0x0A|0x0D 0x0A||
|---|---|---|---|---|---|---|---|
|Host:|space|IP Address ofthe camera|0x0D 0x0A 0x0D 0x0A|||||



Unlike APIs for getting/setting parameters, Accept line is not required. Basic authentication is also not necessary. 

## **Example** 

## **GET /api/audio?assured=1&lowdelay=1 HTTP/1.1<CRLF>** 

## **Host: 192.168.0.2<CRLF><CRLF>** 

Parameter value is indicated using =. Do not insert space before and after =. 

Example    assured=1 

Parameters are segmented using &. Do not insert space before and after &. 

Example assured=1&lowdelay=0 

There is no need to specify all parameters. Default values will be used for parameters that are not specified. 

## **Parameter Description** 

**assured** Recent audio data is stored in internal buffer of the camera. Specify as assured=0 to request for the newest data in the buffer and assured=1 to request for the oldest data in the buffer. Specify as assured=0 to 

93 

Downloaded from www.Manualslib.com manuals search engine 
