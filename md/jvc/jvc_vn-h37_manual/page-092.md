## **system.session.sending_count=2&200 OK** 

**system.session.sending_max=5&200 OK** 

**system.session.sending(01).bitrate=326k&200 OK** 

**system.session.sending(01).to.ip=10.0.0.100&200 OK** 

**system.session.sending(01).to.port=1536&200 OK** 

**system.session.sending(01).to.protocol=tcp_passive&200 OK** 

**system.session.sending(01).to.session=http&200 OK** 

**system.session.sending(01).from.encode=jpeg&200 OK** 

**system.session.sending(01).from.framerate=1&200 OK** 

**system.session.sending(01).from.framesize=vga&200 OK** 

In case of H.264, system.session.sending(01).from.encode=h264baseline or h264high is returned. In case of 

multicast, system.session.sending(01).to.ip becomes multicast IP address. 

**Interpretation** Acquire the sending status of the camera. Starting and stopping stream can be occurred in 

random order, so it can happen that sending(01) is vacant though sending(02) has information. 

**Allowed users** admin, operator, user 

## **Getting Log** 

## **Format  /api/param?system.log** 

**Response** Return the following information. These information will be initialized upon turning off the power of the 

camera. 

Number of seconds after startup, Alarm input, Motion detect, Error 

Response examples 

## **system.log=&200 OK** 

**system alive time: 2142sec** <----- No. of seconds after startup 

**Dec 19 14:35:32 vn-h37 user.info evman: Motion Detect    <----- Motion detect** 

**Dec 19 14:36:03 vn-h37 user.info evman: Alarm Detect (m1)   <----- Alarm input 1ch (make)** 

**Dec 19 14:36:04 vn-h37 user.info evman: Alarm Detect (b2)  <----- Alarm input 2ch (break)** 

**Dec 19 14:35:18 vn-h37 user.info evman: Motion Detect      <----- Motion detect** 

**Interpretation** Acquire the the camera log. Maximum size is 10KB. 

**Allowed user** admin 

## **Getting Model Name** 

**Format  /api/param?system.model** 

## **Example of Response  system.model=VN-H37&200 OK** 

**Interpretation** Acquire the model name. 

89 

Downloaded from www.Manualslib.com manuals search engine 
