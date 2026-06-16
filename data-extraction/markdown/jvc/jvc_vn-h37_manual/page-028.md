Interpretation Acquire white balance setting. "autoW", "autoN",  or "manual" is returned.

Allowed users admin, operator, user

## Setting White Balance of a Scene File

Format  /api/param?camera.scene(number).image.white\_balance=data

Example  /api/param?camera.scene(0).image.white\_balance=auto

Example of response  camera.scene(0).image.white\_balance&amp;202 Accepted(camera.scene.status=save)

Interpretation Change white balance setting. Specify  "autoW", "autoN",  or "manual". If "op\_auto" is specified,

one push auto white balance control is done, and setting becomes "manual". The change of scene file 0 is saved

by the API, camera.scene(0).status=save. If the change is not saved, the setting is restored by reboot.

Allowed users admin, operator

## Getting R-Gain of White Balance of a Scene File

Format  /api/param?camera.scene(number).image.white\_balance.r

Example of response  camera.scene(0).image.white\_balance.r=s85&amp;200 OK

Interpretation Acquire R-gain of white balance setting. s0 to s255 is returned. The s before number means

"step". Default value is s85.

Allowed users admin, operator, user

## Setting R-Gain of White Balance of a Scene File

Format  /api/param?camera.scene(number).image.white\_balance.r=data

Example  /api/param?camera.scene(0).image.white\_balance.r=s100

Example of response

camera.scene(0).image.white\_balance.r&amp;202 Accepted(camera.status=save)

Interpretation Change R-gain white balance setting. Specify s0 to s255. The s before number means "step".

Default value is s85. The change of scene file 0 is saved by the API, camera.scene(0).status=save. If the change

is not saved, the setting is restored by reboot.

Allowed users

admin, operator

## Getting B-Gain of White Balance of a Scene File

Format  /api/param?camera.scene(number).image.white\_balance.b

Example of response  camera.scene(0).image.white\_balance.b=s219&amp;200 OK

Interpretation Acquire B-gain of white balance setting. s0 to s255is returned. The s before number means "step".

Default value is s219.

Allowed users admin, operator, user
