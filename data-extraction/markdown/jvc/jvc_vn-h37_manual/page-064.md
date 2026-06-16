Example to move (958, 534) to center (pixel)

/api/param?camera.motion.clickoncenter=s958-s534

Example to move (958, 534) to center (percentage)

/api/param?camera.motion.clickoncenter=50.00-50.00

Interpretation Moving specified position to center of image. To move to X position, specify from s0 to s1918 or 0.00 to 100.00. To move to Y position, specify from s0 to s1078 or 0.00 to 100.00.

Allowed users admin, operator

## (3) Preset Position

## Getting Current Preset Position

Format  /api/param?camera.status

Example of response  camera.status=3&amp;200 OK

Interpretation Acquire current preset position after moving to preset position. "none" is returned after moved

from preset position.

Allowed users admin, operator, user

## Getting Status of Specified Preset Position

Format  /api/param?camera.position(number).status

Example of response  camera.position(3).status=unregistered&amp;200 OK

Interpretation Acquire current status of specified preset position. Specify from 0 to 19 as position number.

"unregistered" or "registered" is returned.

Allowed users admin, operator, user

## Register Current Position as Preset Position

Format  /api/param?camera.position(number).status=save

Example of Response  camera.position(3).status&amp;200 OK

Interpretation Save current position as preset position. Specify from 0 to 19 as position number.

Allowed users admin, operator

## Initialize Preset Position

Format  /api/param?camera.position(number).status=initialize

Example of Response  camera.position(3).status&amp;200 OK

Interpretation Initialize specified preset position. Specify from 0 to 19 as position number. Position number 0 is
