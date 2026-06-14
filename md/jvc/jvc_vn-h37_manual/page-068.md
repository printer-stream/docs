## **Format  /api/param?camera.private_mask.status** 

## **Example of response  camera.private_mask.status=on&200 OK** 

**Interpretation** Acquire the on/off status of privacy masking. 

**Allowed users** admin, operator, user 

## **Setting Privacy Masking to On/Off** 

## **Format  /api/param?camera.private_mask.status=data** 

## **Example of Response  camera.private_mask.status&202 Accepted(camera.status=save)** 

**Interpretation** Change the on/off status of privacy masking. The change is saved by the API, 

camera.status=save. If the change is not saved, the setting is restored by reboot. 

**Allowed users** admin, operator 

## **Getting Privacy Masking Color** 

## **Format  /api/param?camera.private_mask.color** 

## **Example of response  camera.private_mask.color=ffffff&200 OK** 

**Interpretation** Acquire the color of privacy masking. RGB values are returned as hexadecimal number. For 

exmaple, ffffff is white, ff0000 is red, 00ff00 is green, and 0000ff is blue. 

**Allowed users** admin, operator, user 

## **Setting Privacy Masking Color** 

## **Format  /api/param?camera.private_mask.color=data** 

## **Example of Response  camera.private_mask.color&202 Accepted(camera.status=save)** 

**Interpretation** Change the color of privacy masking. Specify RGB values by hexadecimal number. For exmaple, ffffff for white, ff0000 for red, 00ff00 for green, and 0000ff for blue.The change is saved by the API, 

camera.status=save. If the change is not saved, the setting is restored by reboot. 

**Allowed users** admin, operator 

## **Getting Privacy Masking Area** 

## **Format  /api/param?camera.private_mask.area** 

## **Example of response  camera.private_mask.area=ffffff,,,f&200 OK** 

**Interpretation** Acquire the area of privacy masking. 510 characters are returned as hexadecimal number that show bitmap. A bit for privacy masking is 32x32 pixels block, and 1920x1080 is divided to 60x34 blocks. For example, f means 8 blocks are masked. 

**Allowed users** admin, operator, user 

## **Setting Privacy Masking Color** 

65 

Downloaded from www.Manualslib.com manuals search engine 
