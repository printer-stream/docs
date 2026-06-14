20, 30, 45, 60, or 120. 0 means skip. 10 means 10 seconds. The change is saved by the API, 

camera.motion.auto_patrol.status=save. If the change is not saved, the setting is restored by reboot. 

**Allowed users** admin, operator 

## **Getting Speed of Auto Patrol** 

**Format  /api/param?camera.motion.auto_patrol(0).position(number).speed** 

**Example to get speed of patrol nuber 3** 

## **/api/param?camera.motion.auto_patrol(0).position(3).speed** 

## **Example of response  camera.motion.auto_patrol(0).position(3).speed=30.00&200 OK** 

**Interpretation** Acquire speed of specified patrol number of auto patrol. Patrol number is from 0 to 19. 

**Allowed users** admin, operator, user 

## **Setting Speed of Auto Patrol** 

**Format  /api/param?camera.motion.auto_patrol(0).position(number).speed=data** 

**Example to set maximum speed from patrol nuber 3 to 4** 

## **/api/param?camera.motion.auto_patrol(0).position(3).speed=100.00** 

**Example of Response   camera.motion.auto_patrol(0).position(3).speed&202** 

## **Accepted(camera.motion.auto_patrol.status=save)** 

**Interpretation** Set speed of specified patrol number of auto patrol. Patrol number is from 0 to 19. Specify from 

0.00 to 100.00. 0 means skip. The change is saved by the API, camera.motion.auto_patrol.status=save. If the 

change is not saved, the setting is restored by reboot. 

**Allowed users** admin, operator 

## **Saving Preset Position Number/Duarion of Auto Patrol** 

**Format  /api/param?camera.motion.auto_patrol(0).status=save** 

**Example of Response   camera.motion.auto_patrol(0).status&202** 

**Accepted(camera.motion.auto_patrol.status=save)** 

**Interpretation** Save preset position number and duration of auto patrol. 

**Allowed users** admin, operator 

## **16. JVC API for Privacy Masking** 

The APIs below are related to privacy masking. These are equivalent to the features on the Privacy Masking page of the WEB setting page. Refer to the instruction manual for details on the Privacy Masking page. 

## **Getting Privacy Masking On/Off Status** 

64 

Downloaded from www.Manualslib.com manuals search engine 
