## Getting Auto Exposure Reference of a Scene File

Format  /api/param?camera.scene(number).auto\_exposure.reference

Example of response  camera.scene(0).auto\_exposure.reference=0&amp;200 OK

Interpretation Acquire auto exposure reference. A number from -5 to 5 is returned. When the number is bigger, image becomes brighter.

Allowed users admin, operator, user

## Setting Auto Exposure Reference of a Scene File

Format  /api/param?camera.scene(number).auto\_exposure.reference=data

Example  /api/param?camera.scene(0).auto\_exposure.reference=0

Example of response  camera.scene(0).auto\_exposure.reference&amp;202

Accepted(camera.scene.status=save)

Interpretation Change auto exposure reference. Specify a number from -5 to 5, or "+", "-". When the number is bigger, image becomes brighter. The change of scene file 0 is saved by the API, camera.scene(0).status=save. If the change is not saved, the setting is restored by reboot.

Allowed users admin, operator

## Getting Color Level of a Scene File

Format  /api/param?camera.scene(number).image.color

Example of response  camera.scene(0).image.color=50&amp;200 OK

Interpretation Acquire color level value. Range of color level is between 0 to 100. The value is mapped to 11

internal levels. The larger the value, the stronger will be the color.

Allowed users admin, operator, user

## Setting Color Level of a Scene File

Format  /api/param?camera.scene(number).image.color=data

Example of setting a value  /api/param?camera.scene(0).image.color=50

Example of 1 step change  /api/param?camera.scene(0).image.color=+

Example of response

camera.scene(0).image.color&amp;202 Accepted(camera.scene.status=save)

Interpretation Change color level value. Specify 0 to 100, "+" or "-". The value is mapped to 11 internal levels. The larger the value, the stronger will be the color. It becomes stronger 1 step by specifying "+", softer 1 step by specifying "-". The change of scene file 0 is saved by the API, camera.scene(0).status=save. If the change is not saved, the setting is restored by reboot.

Allowed users admin, operator
