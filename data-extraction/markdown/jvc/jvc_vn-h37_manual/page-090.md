WEB setting page. Refer to the instruction manual for details on the Maintenance page.

## Restart the Camera

Format  /api/param?system.status=restart

Example of Response  system.status&amp;200 OK

Interpretation

Restarts the camera.

Allowed users admin

## Initialization

Format  /api/param?system.status=initialize

Example of Response  system.status&amp;200 OK

Interpretation Restore all the camera settings to factory defaults. Upon doing so, all transmission services that are in progress will be terminated. Initializing takes a few minutes. Response is returned after initializing. Do not power off during initializing.

Allowed user admin

## Firmware Update

Version upgrading is not possible using API. To do so, use the Version Upgrade feature on the Maintenance page of the WEB setting page.

## 26.  JVC API for LED Setting

The APIs below are related to LED. These are equivalent to the features on the LED page of the WEB setting page. Refer to the instruction manual for details on the LED page.

## Getting LED mode

Format  /api/param?camera.stealth

Example of Response  camera.stealth=off&amp;200 OK

Interpretation Acquire LED setting. "on" or "off" is returned. If thie is "on", LED becomes off after restarting.

Allowed users admin, operator, user

## Setting LED mode

Format  /api/param?camera.stealth=data

Example  /api/param?camera.stealth=on

Example of Response

camera.stealth&amp;202 Accepted(camera.status=save)
