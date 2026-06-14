**Interpretation** Change LED setting. Specify "on" or "off". If "on" is set, LED becomes off after restarting. To validate the change, use "camera.status=save" API. 

**Allowed users** admin, operator 

## **Getting LED blinking mode** 

## **Format  /api/param?camera.identify** 

## **Example of Response  camera.identify=off&200 OK** 

**Interpretation** Acquire LED blinking setting. "on" or "off" is returned. If thie is "on", LED is blinking. 

**Allowed users** admin, operator, user 

## **Setting LED blinking mode** 

**Format  /api/param?camera.identify=data** 

**Example  /api/param?camera.identify=on** 

## **Example of Response** 

## **camera.identify&202 Accepted(camera.status=save)** 

**Interpretation** Change LED blinking setting. Specify "on" or "off". If "on" is set, LED starts blinking. To validate the change, use "camera.status=save" API. 

**Allowed users** admin, operator 

## **27. JVC API for Getting Status** 

The APIs below are related to status acquisition. These are equivalent to the features on the Operation/Settings page of the WEB setting page. Refer to the instruction manual for details on the Operation/Settings page. 

## **Getting Sending Status** 

## **Format  /api/param?system.session** 

**Response** Return the total transmission bit rate, and status of each sending operation. Transmission is not carried out in the following examples. 

## **system.session=&200 OK** 

## **system.session.total_bitrate=0k&200 OK** 

## **system.session.sending_count=0&200 OK** 

## **system.session.sending_max=20&200 OK** 

In the examples below, 1 JPEG stream of TCP is being sent. 

## **system.session=&200 OK** 

## **system.session.total_bitrate=388k&200 OK** 

88 

Downloaded from www.Manualslib.com manuals search engine 
