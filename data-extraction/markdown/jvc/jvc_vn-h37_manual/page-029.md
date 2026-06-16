## Setting B-Gain of White Balance of a Scene File

Format  /api/param?camera.scene(number).image.white\_balance.b=data

Example  /api/param?camera.scene(0).image.white\_balance.b=s100

Example of response

camera.scene(0).image.white\_balance.b&amp;202 Accepted(camera.status=save)

Interpretation Change B-gain white balance setting. Specify s0 to s255. The s before number means "step".

Default value is s219. The change of scene file 0 is saved by the API, camera.scene(0).status=save. If the change is not saved, the setting is restored by reboot.

Allowed users admin, operator

## Getting AGC of a Scene File

Format  /api/param?camera.scene(number).image.brightness

Example of response  camera.scene(0).image.brightnesss=autoL&amp;200 OK

Interpretation Acquire AGC setting. "manual", "autoM" or "autoH" is returned.

Allowed users admin, operator, user

## Setting AGC of a Scene File

Format  /api/param?camera.scene(number).image.brightness=data

Example  /api/param?camera.scene(0).image.brightness=auto

Example of response  camera.scene(0).image.brightness&amp;202 Accepted(camera.scene.status=save)

Interpretation Change AGC setting. Specify "manual",  "autoM" or "autoH". The change of scene file 0 is saved

by the API, camera.scene(0).status=save. If the change is not saved, the setting is restored by reboot.

The AGC setting is limited by Day and Night setting. Change Day and Night first,  then change AGC setting.

Allowed users admin, operator

## Getting Limit of Sense Up of a Scene File

Format  /api/param?camera.scene(number).image.senseup\_limit

Example of response  camera.scene(0).image.senseup\_limit=0&amp;200 OK

Interpretation Acquire limit of sense up. 0, 2, 4, 8, 16, 32 or 60 is returned. 0 means sense up is disabled. Other

numbers mean frame number of sense up.

Allowed users admin, operator, user

## Setting Limit of Sense Up of a Scene File

Format  /api/param?camera.scene(number).image.senseup\_limit=data

Example  /api/param?camera.scene(0).image.senseup\_limit=4

Example of response  camera.scene(0).image.senseup\_limit&amp;202 Accepted(camera.status=save)
