Interpretation Change LED setting. Specify "on" or "off". If "on" is set, LED becomes off after restarting. To validate the change, use "camera.status=save" API.

Allowed users admin, operator

## Getting LED blinking mode

Format  /api/param?camera.identify

Example of Response  camera.identify=off&amp;200 OK

Interpretation Acquire LED blinking setting. "on" or "off" is returned. If thie is "on", LED is blinking.

Allowed users admin, operator, user

## Setting LED blinking mode

Format  /api/param?camera.identify=data

Example  /api/param?camera.identify=on

Example of Response

camera.identify&amp;202 Accepted(camera.status=save)

Interpretation Change LED blinking setting. Specify "on" or "off". If "on" is set, LED starts blinking. To validate the change, use "camera.status=save" API.

Allowed users

admin, operator

## 27.  JVC API for Getting Status

The APIs below are related to status acquisition. These are equivalent to the features on the Operation/Settings page of the WEB setting page. Refer to the instruction manual for details on the Operation/Settings page.

## Getting Sending Status

Format  /api/param?system.session

Response Return the total transmission bit rate, and status of each sending operation. Transmission is not carried out in the following examples.

system.session=&amp;200 OK

system.session.total\_bitrate=0k&amp;200 OK

system.session.sending\_count=0&amp;200 OK

system.session.sending\_max=20&amp;200 OK

In the examples below, 1 JPEG stream of TCP is being sent.

system.session=&amp;200 OK

system.session.total\_bitrate=388k&amp;200 OK
