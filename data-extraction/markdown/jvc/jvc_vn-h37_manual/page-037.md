## Example of response  video.output.status&amp;200 OK

Interpretation Change monitor out status. Specify on to enable the monitor out, off to disable the monitor out.

Allowed users admin, operator

## 10.  JVC API for Audio (VN-H57/157WP/257/257VP)

These APIs are related to audio settings. Same functions are shown on the Audio page of the WEB setting page.

Refer to the instruction manual for details on the Audio page.

## Getting Audio Duplex Mode

Format  /api/param?audio.input(1).halfduplex

Example of response  audio.input(1).halfduplex=on&amp;200 OK

Interpretation Acquire audio duplex mode. "on" or "off" is returned. When the setting is "on", audio from the camera is muted during a client is sending audio to the camera. By setting "on", howling/echo can be suppressed.

Allowed users admin, operator, user

## Setting Audio Duplex Mode

Format  /api/param?audio.input(1).halfduplex=data

Example  /api/param?audio.input(1).halfduplex=on

Example of response  audio.input(1).halfduplex&amp;200 OK

Interpretation Change audio duplex mode. Specify "on" or "off". When the setting is "on", audio from the camera is muted during a client is sending audio to the camera. By setting "on", howling/echo can be suppressed.

Allowed users admin, operator

## Getting Mike Gain

Format  /api/param?audio.input(1).gain

Example of response  audio.input(1).gain=32&amp;200 OK

Interpretation Acquire mike gain. "0", "20", "26", "32" or "auto" is returned. "32" measn 32 dB.

Allowed users admin, operator, user

## Setting Mike Gain

Format  /api/param?audio.input(1).gain=data

Example  /api/param?audio.input(1).gain=32

Example of response  audio.input(1).gain&amp;200 OK

Interpretation

Change mike gain. Specify "0", "20", "26", "32" or "auto". "32" measn 32 dB.

Allowed users admin, operator
