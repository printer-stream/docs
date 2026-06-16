## Example of Response  camera.motion.pan.mode&amp;200 OK

Interpretation Set direction of pan operation. Specify left or right.

Allowed users

admin, operator

## Setting Speed of Pan Operation

Format  /api/param?camera.motion.pan.speed=data

Example to set maximum speed   /api/param?camera.motion.pan.speed=100

Example of Response  camera.motion.pan.speed&amp;200 OK

Interpretation Set speed of pan operation. Specify 0 to 100. The speed is 8 steps internally.

Allowed users admin, operator

## Getting Pan Operation Status

Format  /api/param?camera.motion.pan.status

Example of Response  camera.motion.pan.status=moving&amp;200 OK

Interpretation Acquire current pan status. "moving" or "stop" is returned.

Allowed users admin, operator, user

## Getting Tilt Position

Format  /api/param?camera.motion.tilt

Example of response  camera.motion.tilt=s45&amp;200 OK

Interpretation Acquire current tilt position, top edge of current area, in pixels. Value from 0 to 958 is returned. "s"

is added before the value.

Allowed users admin, operator, user

## Moving to Specified Tilt Position

Format  /api/param?camera.motion.tilt=data

Example to move to absolute 100 pixels   /api/param?camera.motion.tilt=s100

Example to move to relative 45 degrees   /api/param?camera.motion.tilt=+s45

Example of Response  camera.motion.tilt&amp;200 OK

Interpretation Move to specified tilt position, top edge of target area, in pixels. To move to absolute position,

specify from 0 to 958 with "s". Moved position can be adjusted automatically to prevent showing invalid area.

Allowed users admin, operator

## Tilt Operation

Format  /api/param?camera.motion.tilt.status=data

Example to start pan   /api/param?camera.motion.tilt.status=start
