returned. Segments are indicated by /.

Example of Response application.event(1).action=udpto/10.0.0.100/20000/Message&amp;200 OK

When switch scene file is specified, scene file number will be returned.

Example of Response when scene file number is 7

application.event(1).action=camera.image.scene(7).status/goto&amp;200 OK

When preset position is specified, position number will be returned.

Example of Response when position number is 2

application.event(1).action=camera.position(2).status/goto&amp;200 OK

[VN-H57/157WP/257/257VP Only] When audio file playback is specified, audio file number will be returned. A separate API (/api/param?application.audioplay) is used to get/set parameters of audio file playback.

Example of Response when audio file number is 2

application.event(1).action=audioplay/audiofile02/ch01&amp;200 OK

[VN-H57/157WP/257/257VP Only] When alarm output is specified, pinout, distinction between make/break (m1 or b1) and output time (millisecond) will be returned. Segments are indicated by /.

Example of Response  application.event(1).action=pinout/m1/1500&amp;200 OK

Alarm action of event number 6 is periodic FTP. Response to the API has ftpto, FTP number, and the attached object number. Segments are indicated by /. The FTP number is fixed as ftp01 at all times. The object number is fixed as object(6). Parameters of FTP can be gotten by another API, application.ftp.

Example of Response  application.event(6).action=ftpto/ftp01/object(6)&amp;200 OK

Alarm action of event number 7 is "PrePostRecording + FTP".  When "PrePostRecording + FTP" is enabled, recftp, FTP number, and the attached object number will be returned. Segments are indicated by /. The FTP number is fixed as ftp01 at all times. The object number is fixed as object(7). Parameters of FTP can be gotten by other APIs, application.ftp and application.object.

Example of Response  application.event(7).action=recftp/ftp01/object(7)&amp;200 OK

Alarm action of event number 8 is 'SD Card constant recording'. When 'SD Card constant recording' is enabled, rec, SD Card number, and the attached object number will be returned. Segments are indicated by /. The SD Card number is fixed as sd01 at all times. The object number is fixed as object(8). Parameters of SD Card recording can be gotten by other APIs, application.object.

Example of Response  application.event(8).action=rec/sd01/object(8)&amp;200 OK
