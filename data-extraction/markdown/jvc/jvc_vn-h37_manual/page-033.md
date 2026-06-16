## 9.  JVC API for Encode

These APIs are related to camera settings. Same functions are shown on the Encode page of the WEB setting page. Refer to the instruction manual for details on the Encode page.

Though multiple encode is available, there are limitations to set multiple encode channels. If VMS does not get multiple streams from a camera, setting only first channel is recommended that can simplify such limitations. Refer the Encode page of the camera to see those limitations.

## Getting Compression Format

Format  /api/param?encode(number).type

Example of response  encode(1).type=jpeg&amp;200 OK

Interpretation Acquire compression format of the encode channel. Encode channel is from encode(1) to encode(3).

Allowed users admin, operator, user

## Setting Compression Format

Format   /api/param?encode(number).type=data

Example  /api/param?encode(1).type=h264high

Example of response   encode(1).type&amp;202 Accepted(encode.status=save)

Interpretation Change compression format of the encode channel.  Set "jpeg", "h264high", "h264baseline",

'mpeg4'or "off". The change of the first encode channel is availed by the API, encode(1).status=save.

Example When Changing Compression Format from H.264 to JPEG,

it is necessary that rate control setting is specified to 'afs' or 'vfs'.

/api/param?encode(1).type=jpeg&amp;encode(1).cbr\_mode=afs

/api/param?encode(1).status=save

Example When Changing Compression Format from JPEG to H.264,

it is necessary that rate control setting is specified to 'cbr' or 'vbr'.

/api/param?encode(1).type=h264high&amp;encode(1).cbr\_mode=cbr

/api/param?encode(1).status=save

Caution: In case of multiple resolution, 3 channels are available at the maximum. In case of multiple encoding, 2 channels are available at the maximum, i.e. 3rd channel is not available.

Allowed users admin, operator

## Getting Resolution (Frame Size)

Format  /api/param?encode(number).framesize

Example of response  encode(1).framesize=1920x1080&amp;200 OK
