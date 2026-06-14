**Allowed users** admin, operator 

## **Getting Timeout of Auto Return** 

## **Format  /api/param?camera.motion.auto_return.timeout** 

**Example of response  camera.motion.auto_return.timeout=60&200 OK** 

**Interpretation** Acquire timeout of Auto Return in seconds. 

**Allowed users** admin, operator, user 

## **Setting Timeout of Auto Return** 

## **Format  /api/param?camera.motion.auto_return.timeout=data** 

## **Example of Response  camera.motion.auto_return.timeout&202 Accepted(camera.status=save)** 

**Interpretation** Change timeout of Auto Return in seconds. Specify 60, 120, 180, 300, 600, 1200, 1800 or 3600. The change is saved by the API, camera.status=save. If the change is not saved, the setting is restored by reboot. **Allowed users** admin, operator 

## **Getting Auto Return Status** 

## **Format  /api/param?camera.motion.auto_return.status** 

## **Example of response  camera.motion.auto_return.status=on&200 OK** 

**Interpretation** Acquire status of Auto Return. "on" or "off" will be returned. 

**Allowed users** admin, operator, user 

## **Setting Auto Return Status** 

**Format  /api/param?camera.motion.auto_return.status=data** 

## **Example of Response  camera.motion.auto_return.status&202 Accepted(camera.status=save)** 

**Interpretation** Change status of Auto Return. Specify "on" or "off" to change the status. Specify "start" or "stop" 

for manual operation. "on" or "off" is saved by the API, camera.status=save. If the change is not saved, the setting is restored by reboot. 

**Allowed users** admin, operator 

## **Getting Speed of Going to Preset Position** 

**Format  /api/param?camera.motion.position.speed** 

## **Example of response  camera.motion.position.speed=100&200 OK** 

**Interpretation** Acquire speed of going to preset position. Value from 0 to 100 is returned. 100 is fastest. The 

speed is 4 steps internally. The speed is applied also to preset position of auto patrol. 

**Allowed users** admin, operator, user 

56 

Downloaded from www.Manualslib.com manuals search engine 
