## **Setting Speed of Going to Preset Position** 

## **Format  /api/param?camera.motion.position.speed=data** 

## **Example to set horizontal   /api/param?camera.motion.position.speed=100** 

## **Example of Response  camera.motion.position.speed&202 Accepted(camera.status=save)** 

**Interpretation** Set speed of going to preset position. Specify from 0 to 100. 5 is horizontal. 100 is fastest. The 

speed is 4 steps internally. The speed is applied also to preset position of auto patrol. The change is saved by the API, camera.status=save. If the change is not saved, the setting is restored by reboot. 

**Allowed users** admin, operator 

## (2) PTZ Control 

## **Getting Pan Position** 

**Format  /api/param?camera.motion.pan** 

## **Example of response  camera.motion.pan=s100&200 OK** 

**Interpretation** Acquire current pan position, left edge of current area,  in pixels. Value from 0 to 1278 is returned. 

"s" is added before the value. 

**Allowed users** admin, operator, user 

## **Moving to Specified Pan Position** 

**Format  /api/param?camera.motion.pan=data** 

## **Example to move to absolute 100 pixels   /api/param?camera.motion.pan=s100** 

## **Example to move to relative 45 pixels    /api/param?camera.motion.pan=+s45** 

## **Example of Response  camera.motion.pan&200 OK** 

**Interpretation** Move to specified pan position, left edge of target area, in pixels. To move to absolute position, 

specify from 0 to 1278 with "s". Moved position can be adjusted automatically to prevent showing invalid area. 

**Allowed users** admin, operator 

## **Pan Operation** 

**Format  /api/param?camera.motion.pan.status=data** 

**Example to start pan   /api/param?camera.motion.pan.status=start** 

## **Example of Response  camera.motion.pan.status&200 OK** 

**Interpretation** Start or stop pan operation. Specify start or stop. 

**Allowed users** admin, operator 

## **Setting Direction of Pan Operation** 

**Format  /api/param?camera.motion.pan.mode=data** 

**Example to set to left   /api/param?camera.motion.pan.mode=left** 

57 

Downloaded from www.Manualslib.com manuals search engine 
