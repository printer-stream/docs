Specify tcpto, IP address, port number, none or object(Number), and the character string to be sent when sending via TCP. Segments are indicated by /. The number of character string is from 1 to 127 bytes. To use following characters, specify by hexadecimal number after %.

<!-- formula-not-decoded -->

For example, specify 3 characters %20 when inserting a space in the character string. For example, to send the character string "This is alarm.", specify as "This%20is%20alarm.".  %09 and %0D are not available.

Setting Example /api/param?application.event(1).action=tcpto/10.0.0.100/20000/none/Message To add JPEG, specify object(Number) instead of 'none'.

Setting Example /api/param?application.event(1).action=tcpto/10.0.0.100/20000/object(1)/Message

Specify udpto, IP address, port number and the character string to be sent when sending via UDP. Segments are indicated by /. The number of character string is from 1 to 127 bytes. To use following characters, specify by hexadecimal number after %.

<!-- formula-not-decoded -->

For example, specify 3 characters %20 when inserting a space in the character string. For example, to send the character string "This is alarm.", specify as "This%20is%20alarm.".  %09 and %0D are not available.

Setting Example /api/param?application.event(1).action=udpto/10.0.0.100/20000/Message

Specify scene file number when switch scene file is specified.

Setting Example /api/param?application.event(1).action=camera.image.scene(7).status/goto

Specify preset position number when preset position is specified.

Setting Example  /api/param?application.event(1).action=camera.position(2).status/goto

[VN-H57/157WP/257/257VP Only] Specify audio file number when audio file playback is specified. The audio file number can be from 01 to 05.

Setting Example  /api/param?application.event(1).action=audioplay/audiofile02/ch01

[VN-H57/157WP/257/257VP Only] Specify pinout, distinction between make/break (m1 or b1) and the time (millisecond) when alarm output is specified. Segments are indicated by /. The time is 0 or from 100 to 5000. When the time is 0, alarm output does not come back to previous state.

Setting Example  /api/param?application.event(1).action=pinout/m1/1500

Alarm action of event number 6 is periodic FTP. Other Event number can not be set to periodic FTP. Parameters of FTP can be set by another API, application.ftp.

Setting Example  /api/param?application.event(6).action=ftpto/ftp01/object(6)
