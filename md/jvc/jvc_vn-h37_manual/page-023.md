When an error occurs, an error code will be returned instead of indicating a value in the body of HTTP response. Example: 

## **ParamA.ParamB.ParamC&401 Unauthorized** 

When multiple APIs for getting are performed at one time, a response will be returned for each setting. 

## **ParamA.ParamB.ParamC&200 OK<CRLF>** 

**ParamA.ParamB.ParamD&200 OK<CRLF>** 

## **7.3. Setting Parameter** 

Specify API in GET line according to the format below when setting a parameter for the camera. 

## **/api/param?ParamA.ParamB.ParamC=Data** 

Parameter values are indicated using =. Do not insert space before and after =. 

It is possible to perform multiple settings at a time. Connect parameters with &. Do not insert space before and after &. 

## **/api/param?ParamA.ParamB.ParamC=Data&ParamA.ParamB.ParamD=Data** 

The upper limit of this character string is 1024 bytes. The maximum number of parameters that can be set at a 

time is 15.  Status settings, i.e. network.interface.status, network.dns.status, network.ntp.status, etc., can not be acquired at a time. 

Response will be in the following format. 

## **ParamA.ParamB.ParamC&200 OK** 

An error code will be returned when setting is not properly performed. Example: 

## **ParamA.ParamB.ParamC&401 Unauthorized** 

When multiple settings are performed at one time, a response will be returned for each setting. 

## **ParamA.ParamB.ParamC&200 OK<CRLF>** 

**ParamA.ParamB.ParamD&200 OK<CRLF>** 

## **8. JVC API for Camera** 

These APIs are related to camera settings. Same functions are shown on the Camera page of the WEB setting page. Refer to the instruction manual for details on the Camera page. 

## **Getting Camera ID** 

20 

Downloaded from www.Manualslib.com manuals search engine 
