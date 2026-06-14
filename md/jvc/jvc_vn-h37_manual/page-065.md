home position and it is registered with default settings when initilized. Other positions are unregistered by initializing. 

**Allowed users** admin, operator 

## **Moving to Preset Position** 

## **Format  /api/param?camera.position(number).status=goto** 

## **Example of Response  camera.position(3).status&200 OK** 

**Interpretation** Move to specified preset position. Specify from 0 to 19 as position number. 

**Allowed users** admin, operator 

## **Getting Title of Preset Position** 

**Format  /api/param?camera.position(number).comment** 

**Example of response  camera.position(3).comment=entrance&200 OK** 

**Interpretation** Acquire title of specified preset position. Specify from 0 to 19 as position number. 

**Allowed users** admin, operator, user 

## **Setting Title to Preset Position** 

## **Format  /api/param?camera.position(number).comment=data** 

## **Example of Response  camera.position(3).status&200 OK** 

**Interpretation** Set tilte to specified preset position. Specify from 0 to 19 as position number. Maximum 

characters is 32. To erase title, specify %00, i.e. 0x25 0x30 0x30 in binary data. Use %20 to set space. 

**Allowed users** admin, operator 

## **15. JVC API for Auto Patrol** 

The APIs below are related to Auto Patrol. These are equivalent to the features on the AutoPatrol page of the WEB setting page. Refer to the instruction manual for details on the AutoPatrol page page. 

## **Start/Stop of Auto Patrol** 

**Format  /api/param?camera.motion.auto_patrol(0).status=data** 

**Example to start auto patrol   /api/param?camera.motion.auto_patrol(0).status=start** 

## **Example of Response    camera.motion.auto_patrol(0).status&200 OK** 

**Interpretation** Start/stop a mode of auto patrol. Specify start or stop. 

**Allowed users** admin, operator 

## **Getting Status of Auto Patrol** 

**Format  /api/param?camera.motion.auto_patrol(0).status** 

62 

Downloaded from www.Manualslib.com manuals search engine 
