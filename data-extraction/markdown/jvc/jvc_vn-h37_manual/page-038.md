## Getting Mike Power Supply setting

Format  /api/param?audio.input(1).powersupply.status

Example of response  audio.input(1).powersupply.status=on&amp;200 OK

Interpretation Acquire mike power supply setting. "on" or "off" is returned.

Allowed users admin, operator, user

## Setting Mike Power Supply

Format  /api/param?audio.input(1).powersupply.status=data

Example  /api/param?audio.input(1).powersupply.status=32

Example of response  audio.input(1).powersupply.status&amp;200 OK

Interpretation Change mike power supply setting. Specify "on" or "off".

Allowed users

admin, operator

## 11.  JVC API for Alarm

These APIs are related to alarm settings. Same functions are shown on the Alarm page of the WEB setting page.

Refer to the instruction manual for details on the Alarm page.

## Getting On/Off of Alarm Action

Format  /api/param?application.event(Number).status

Example When Getting the on/off status of alarm action No. 1

/api/param?application.event(1).status

Example of response  application.event(1).status=on&amp;200 OK

Interpretation Acquire the on/off status of the alarm action for the specified alarm action number. 5 alarm actions,

1 periodic FTP assigned to No.6, 1 pre/post FTP assigned to No.7, 1 SD Card constant recording assigned to No.8, and 1 SD Card alarm recording assigned to No.10 are available, so alarm action number can be 1 to 8 and 10. Note that alarm numbers are different from the alarm input pin numbers. Either on or off is returned.

Allowed users admin, operator

## Setting On/Off of Alarm Action, or Enabling Changes to Alarm Action

Format  /api/param?application.event(Number).status=data

Example When setting alarm action No. 1 to off

/api/param?application.event(1).status=off

Example of response  application.event(1).status&amp;200 OK

Interpretation Set the alarm action of the specified alarm action number to on/off, or enable changes to the alarm
