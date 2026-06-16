## Format     /api/param?camera.id

Example of response    camera.id=VN-H37&amp;200 OK

Response example when setting field is left blank    camera.id=&amp;200 OK

Interpretation Acquire Camera ID comment. This comment is stored in comment segment of JPEG. The

Camera ID is used as sender's display name of alarm mail. If you want to set sender's mail address, see "Setting Sender Mail Address".

## Example of response  camera.id=Camera01&amp;200 OK

## Sender               Camera01&lt;somename@somecompany.com&gt;

Allowed users admin, operator, user

## Setting Camera ID

Format   /api/param?camera.id=data

Example  /api/param?camera.id=Camera01

Example when setting as blank   /api/param?camera.id=%00

Example of response    camera.id&amp;202 Accepted(camera.status=save)

Interpretation Change the camera ID stored in comment segment of JPEG. Maximum size is 40 bytes.

To use following characters, specify by hexadecimal number after %.

<!-- formula-not-decoded -->

To set as blank, specify as %00(0x25, 0x30, 0x30).

To use space, specify as %20(0x25, 0x32, 0x30). If you want to set "Comment In JPEG" for example, specify

as follows. /api/param?camera.id=Comment%20In%20JPEG

The Camera ID is used as sender's display name of alarm mail. If you want to set sender's mail address, see "Setting Sender Mail Address".

Example of setting    /api/param?camera.id=Camera01

## Sender               Camera01&lt;somename@somecompany.com&gt;

The change is saved by the API, camera.status=save. If the change is not saved, the setting is restored by reboot.

Allowed users admin, operator

## Getting Current Scene File Number

Format  /api/param?camera.scene.status

Example of response  camera.scene.status=0&amp;200 OK

Interpretation Acquire current scene file number. A number from 0 to 7 is returned.

A scene file is a set of preset parameters below.

auto\_exposure.reference, color, monitortype, pedestal, gamma, enhance, white\_balance, brightness,

white\_balance, white\_balance.r, white\_balance.b, senseup\_limit, brightness.highgain, true\_daynight, blc,

auto\_exposure.priority, shutter
