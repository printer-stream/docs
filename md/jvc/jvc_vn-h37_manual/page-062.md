**Example of Response  camera.motion.tilt.status&200 OK** 

**Interpretation** Start or stop tilt operation. Specify start or stop. 

**Allowed users** admin, operator 

## **Setting Direction of Tilt Operation** 

**Format  /api/param?camera.motion.tilt.mode=data** 

**Example to set to up   /api/param?camera.motion.tilt.mode=up** 

## **Example of Response  camera.motion.tilt.mode&200 OK** 

**Interpretation** Set direction of tilt operation. Specify up or down. 

**Allowed users** admin, operator 

## **Setting Speed of Tilt Operation** 

**Format  /api/param?camera.motion.tilt.speed=data** 

**Example to set maximum speed   /api/param?camera.motion.tilt.speed=100** 

## **Example of Response  camera.motion.tilt.speed&200 OK** 

**Interpretation** Set speed of tilt operation. Specify 0 to 100. The speed is 8 steps internally. 

**Allowed users** admin, operator 

## **Getting Tilt Operation Status** 

**Format  /api/param?camera.motion.tilt.status** 

**Example of Response  camera.motion.tilt.status=moving&200 OK** 

**Interpretation** Acquire current tilt status. "moving" or "stop" is returned. 

**Allowed users** admin, operator, user 

## **Getting Zoom Position** 

**Format  /api/param?camera.motion.zoom** 

## **Example of response  camera.motion.zoom=x2.00&200 OK** 

**Interpretation** Acquire current zoom multiple. Value from 1.00 to 8.00 is returned with "x". The API is valid when 

the resolution is 640x360 or 640x480. 

**Allowed users** admin, operator, user 

## **Moving to Specified Zoom Position** 

**Format  /api/param?camera.motion.zoom=data** 

**Example to move to absolute multiple, x2.0   /api/param?camera.motion.zoom=x2.00** 

**Example to move to relative multiple,  1.5 Tele   /api/param?camera.motion.zoom=+x1.5** 

59 

Downloaded from www.Manualslib.com manuals search engine 
