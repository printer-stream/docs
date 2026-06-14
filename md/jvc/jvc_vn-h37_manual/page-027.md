## **Getting Enhance of a Scene File** 

## **Format  /api/param?camera.scene(number).image.enhance** 

## **Example of response  camera.scene(0).image.enhance=50&200 OK** 

**Interpretation** Acquire enhance setting. The enhance is equal to sharpness of image. Range of enhance is between 0 to 100, and it is mapped to 14 internal levels. The larger the value, the sharper will be the image. 

**Allowed users** admin, operator, user 

## **Setting Enhance of a Scene File** 

## **Format  /api/param?camera.scene(number).image.enhance=data** 

## **Example of setting a value  /api/param?camera.scene(0).image.enhance=50** 

## **Example of 1 step change  /api/param?camera.scene(0).image.enhance=+** 

## **Example of response  camera.scene(0).image.enhance&202 Accepted(camera.scene.status=save)** 

**Interpretation** Change enhance setting. The enhance is equal to sharpness of image. Specify 0 to 100, "+" or "-". The value is mapped to 14 internal levels. It becomes sharper 1 step by specifying "+", softer 1 step by specifying "-". The change of scene file 0 is saved by the API, camera.scene(0).status=save. If the change is not saved, the setting is restored by reboot. 

**Allowed users** admin, operator 

## **Getting 3DDNR of a Scene File** 

**Format  /api/param?camera.scene(number).image.3ddnr** 

## **Example of response  camera.scene(0).image.3ddnr=mid&200 OK** 

**Interpretation** Acquire 3DDNR (3 Dimension Digital Noise Reduction) setting. “off”, “low”, “mid” of “high”is 

returned. 

**Allowed users** admin, operator, user 

## **Setting 3DDNR of a Scene File** 

**Format  /api/param?camera.scene(number).image.3ddnr=data** 

## **Example of setting a value  /api/param?camera.scene(0).image.3ddnr=mid** 

## **Example of response  camera.scene(0).image.3ddnr&202 Accepted(camera.scene(0).status=save)** 

**Interpretation** Change 3DDNR setting. Specify “off”, “low”, “mid” of “high”. The change of scene file 0 is saved by the API, camera.scene(0).status=save. If the change is not saved, the setting is restored by reboot. 

**Allowed users** admin, operator 

## **Getting White Balance of a Scene File** 

**Format  /api/param?camera.scene(number).image.white_balance** 

**Example of response  camera.scene(0).image.white_balance=auto&200 OK** 

24 

Downloaded from www.Manualslib.com manuals search engine 
