## Getting H.264 or MPEG-4 bitrate

Format  /api/param?encode(number).bitrate

Example of response  encode(1).bitrate=4000000&amp;200 OK

Interpretation Acquire the bitrate setting of H.264 or MPEG-4. This API is valid when compression format is h264high, h264baseline or mpeg4.  If the response is 4000000 for example, the setting is 4Mbps.

Allowed users admin, operator, user

## Setting H.264 or MPEG-4 bitrate

Format  /api/param?encode(number).bitrate=Data

Example /api/param?encode(1).bitrate=2000000

Example of response  encode(1).bitrate&amp;202 Accepted(encode.status=save)

Interpretation Change the bitrate setting of H.264 or MPEG-4. This API is valid when compression format is h264high, h264baseline or mpeg-4. In case of H.264, specify from 64000 to 8000000. In case of MPEG-4, specify from 64000 to 3000000. The change of the first channel is availed by the API, encode(1).status=save.

Allowed users admin, operator

## Getting JPEG File Size Setting

Format  /api/param?encode(number).quality

Example of response  encode(1).quality=40k&amp;200 OK

Interpretation Acquire the file size setting of JPEG. This API is valid when compression format is jpeg. If the response is 40k for example, the setting is 40KB.

Allowed users admin, operator, user

## Setting JPEG File Size

Format  /api/param?encode(number).quality=Data

Example /api/param?encode(1).quality=30k

Example of response  encode(1).quality&amp;202 Accepted(encode.status=save)

Interpretation Change the file size setting of JPEG. This API is valid when compression format is jpeg. The unit

of set values is in KB.

Allowed users admin, operator

## Getting H.264 or MPEG-4 I-Frame Interval Setting

Format  /api/param?encode(number).iframeinterval

Example of response  encode(1).iframeinterval=15&amp;200 OK

Interpretation Acquire I-Frame interval of H.264 or MPEG-4 encoding.  This API is valid when compression format is h264high, h264baseline or mpeg4.
