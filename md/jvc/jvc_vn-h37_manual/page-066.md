## **Example of response  camera.motion.auto_patrol(0).status=moving&200 OK** 

**Interpretation** Acquire current status of auto patrol. "moving" or "stop" is returned. 

**Allowed users** admin, operator, user 

## **Getting Preset Postion Number of Auto Patrol** 

**Format  /api/param?camera.motion.auto_patrol(0).position(number)** 

## **Example to get preset position number of patrol nuber 3** 

## **/api/param?camera.motion.auto_patrol(0).position(3)** 

## **Example of response  camera.motion.auto_patrol(0).position(3)=5&200 OK** 

**Interpretation** Acquire preset position number of specified patrol number of auto patrol. Patrol number is from 0 

to 19. Preset position number from 0 to 19 is returned. 

**Allowed users** admin, operator, user 

## **Setting Preset Postion Number of Auto Patrol** 

**Format  /api/param?camera.motion.auto_patrol(0).position(number)=data** 

**Example of Response   camera.motion.auto_patrol(0).position(3)&202** 

## **Accepted(camera.motion.auto_patrol.status=save)** 

**Interpretation** Set preset position number of specified patrol number of auto patrol. Patrol number is from 0 to 19. 

Specify preset position number from 0 to 19. The change is saved by the API, 

camera.motion.auto_patrol.status=save. If the change is not saved, the setting is restored by reboot. 

**Allowed users** admin, operator 

## **Getting Duration of Auto Patrol** 

**Format  /api/param?camera.motion.auto_patrol(0).position(number).duration** 

**Example to get duration of patrol nuber 3** 

## **/api/param?camera.motion.auto_patrol(0).position(3).duration** 

## **Example of response  camera.motion.auto_patrol(0).position(3).duration=30&200 OK** 

**Interpretation** Acquire duration of specified patrol number of auto patrol. Patrol number is from 0 to 19. 0, 10, 20, 

30, 45, 60, or 120 is returned. 0 means skip. 10 means 10 seconds. 

**Allowed users** admin, operator, user 

## **Setting Duarion of Auto Patrol** 

**Format  /api/param?camera.motion.auto_patrol(0).position(number).duration=data** 

## **Example of Response   camera.motion.auto_patrol(0).position(3).duration&202** 

## **Accepted(camera.motion.auto_patrol.status=save)** 

**Interpretation** Set duration of specified patrol number of auto patrol. Patrol number is from 0 to 19. Specify 0, 10, 

63 

Downloaded from www.Manualslib.com manuals search engine 
