system.session.sending\_count=2&amp;200 OK system.session.sending\_max=5&amp;200 OK system.session.sending(01).bitrate=326k&amp;200 OK system.session.sending(01).to.ip=10.0.0.100&amp;200 OK system.session.sending(01).to.port=1536&amp;200 OK system.session.sending(01).to.protocol=tcp\_passive&amp;200 OK system.session.sending(01).to.session=http&amp;200 OK system.session.sending(01).from.encode=jpeg&amp;200 OK system.session.sending(01).from.framerate=1&amp;200 OK system.session.sending(01).from.framesize=vga&amp;200 OK

In case of H.264, system.session.sending(01).from.encode=h264baseline or h264high is returned. In case of multicast, system.session.sending(01).to.ip becomes multicast IP address.

Interpretation Acquire the sending status of the camera. Starting and stopping stream can be occurred in random order, so it can happen that sending(01) is vacant though sending(02) has information.

Allowed users admin, operator, user

## Getting Log

Format  /api/param?system.log

Response Return the following information. These information will be initialized upon turning off the power of the camera.

Number of seconds after startup, Alarm input, Motion detect, Error

Response examples

system.log=&amp;200 OK

system alive time: 2142sec &lt;----- No. of seconds after startup

Dec 19 14:35:32 vn-h37 user.info evman: Motion Detect    &lt;----- Motion detect

Dec 19 14:36:03 vn-h37 user.info evman: Alarm Detect (m1)   &lt;----- Alarm input 1ch (make)

Dec 19 14:36:04 vn-h37 user.info evman: Alarm Detect (b2)  &lt;----- Alarm input 2ch (break)

Dec 19 14:35:18 vn-h37 user.info evman: Motion Detect      &lt;----- Motion detect

Interpretation Acquire the the camera log. Maximum size is 10KB.

Allowed user admin

## Getting Model Name

Format  /api/param?system.model

Example of Response  system.model=VN-H37&amp;200 OK

Interpretation Acquire the model name.
