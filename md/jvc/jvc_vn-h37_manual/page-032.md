by the API, camera.scene(0).status=save.  If the change is not saved, the setting is restored by reboot. 

The AGC setting is limited by Day and Night setting. Change Day and Night first, then change AGC setting. 

**Allowed users** admin, operator 

## **Getting Back Light Compensation of a Scene File** 

## **Format  /api/param?camera.scene(number).image.blc** 

## **Example of response  camera.scene(0).image.blc=off&200 OK** 

**Interpretation** Acquire Back Light Compensation setting. "off", "a", "b", "c" or "d" is returned. Refer the instruction manual for detailed information of "a", "b", "c" and "d". 

**Allowed users** admin, operator, user 

## **Setting Back Light Compensation of a Scene File** 

**Format  /api/param?camera.scene(number).image.blc=data** 

## **Format of setting ON  /api/param?camera.scene(0).image.blc=a** 

## **Example of response  camera.scene(0).image.blc&202 Accepted(camera.scene.status=save)** 

**Interpretation** Change Back Light Compensation setting. Specify "off", "a", "b", "c" or "d". Refer the instruction 

manual for detailed information of "a", "b", "c" and "d". The change of scene file 0 is saved by the API, 

camera.scene(0).status=save. If the change is not saved, the setting is restored by reboot. 

**Allowed users** admin, operator 

## **Getting CLVI of a Scene File** 

**Format  /api/param?camera.scene(number).image.clvi** 

## **Example of response  camera.scene(0).image.clvi=off&200 OK** 

**Interpretation** Acquire CLVI (Clear Logic Video Intelligence) setting. "on" or  "off" is returned. 

**Allowed users** admin, operator, user 

## **Setting CLVI of a Scene File** 

**Format  /api/param?camera.scene(number).image.clvi=data** 

## **Format of setting ON  /api/param?camera.scene(0).image.clvi=on** 

## **Example of response  camera.scene(0).image.clvi&202 Accepted(camera.scene.status=save)** 

**Interpretation** Change CLVI (Clear Logic Video Intelligence) setting. Specify "on" or "off". The change of scene file 0 is saved by the API, camera.scene(0).status=save. If the change is not saved, the setting is restored by reboot. 

**Allowed users** admin, operator 

29 

Downloaded from www.Manualslib.com manuals search engine 
