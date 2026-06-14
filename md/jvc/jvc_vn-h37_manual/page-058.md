## **To set recording quality to Mid** 

**/api/param?encode(3).type=h264high** 

- **/api/param?encode(3).framesize=1280x720** 

- **/api/param?encode(3).framerate=5** 

**/api/param?encode(3).bitrate=768000** 

**/api/param?encode(3).cbr_mode=cbr** 

- **/api/param?encode(3).iframeinterval=5** 

**To set recording quality to Low** 

- **/api/param?encode(3).type=h264high** 

**/api/param?encode(3).framesize=640x360** 

- **/api/param?encode(3).framerate=5** 

**/api/param?encode(3).bitrate=128000** 

- **/api/param?encode(3).cbr_mode=cbr** 

- **/api/param?encode(3).iframeinterval=5** 

**Allowed users** admin, operator 

## **14. JVC API for Digital PTZ** 

The APIs below are related to digital PTZ control. These are equivalent to the features on the PTZ page of the 

WEB setting page. Refer to the instruction manual for details on the PTZ page. 

Basic authentication is required for JVC API explained in Section 7 or later. This section provides general 

explanation of those APIs. The API is valid when the resolution is 640x360 or 640x480. 

## (1) Settings for PTZ Control 

## **Getting Auto Return Mode** 

**Format  /api/param?camera.motion.auto_return.mode** 

**Example of response  camera.motion.auto_return.mode=home&200 OK** 

**Interpretation** Acquire Auto Return mode. "home" or "auto_patrol(0)" will be returned. 

**Allowed users** admin, operator, user 

## **Setting Auto Return Mode** 

**Format  /api/param?camera.motion.auto_return.mode=data** 

**Example of Response  camera.motion.auto_return.mode&202 Accepted(camera.status=save)** 

**Interpretation** Change Auto Return mode. Specify "home" or "auto_patrol(0)". The change is saved by the API, 

camera.status=save. If the change is not saved, the setting is restored by reboot. 

55 

Downloaded from www.Manualslib.com manuals search engine 
