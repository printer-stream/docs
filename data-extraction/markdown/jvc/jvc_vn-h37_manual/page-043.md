Alarm action of event number 7 is "PrePostRecording + FTP". Specify recftp, FTP number and the object for PrePostRecording+FTP. The FTP number is fixed as ftp01 at all times. The object is fixed as object(7). Parameters of FTP can be set by other APIs, application.ftp and application.object. Ensure to set the FTP server (/api/param?application.ftp.host, /api/param?application.object.framerate etc.) before setting PrePostRecording+FTP.

Setting Example  /api/param?application.event(7).action=recftp/ftp01/object(7)

Alarm action of event number 8 is 'SD Card constant recording'. Specify rec, SD Card number and the object for SD Card constant recording. The SD Card number is fixed as sd01 at all times. The object is fixed as object(8). Parameters of SD Card recording can be set by other APIs, application.object.

Setting Example  /api/param?application.event(8).action=rec/sd01/object(8)

Alarm action of event number 10 is 'SD Card alarm recording'. Specify rec, SD Card number and the object for SD Card alarm recording. The SD Card number is fixed as sd01 at all times. The object is fixed as object(10). Parameters of SD Card recording can be set by other APIs, application.object.

Setting Example  /api/param?application.event(10).action=rec/sd01/object(10)

Allowed users admin, operator

## Getting Alarm Filter Setting

Format  /api/param?application.event(Number).filter(WeekOfDay).status

Example When Getting Setting of Sunday filter of Alarm No. 1

/api/param?application.event(1).filter(sunday).status

Example of Response  application.event(1).filter(sunday).status=off&amp;200 OK

Interpretation Acquire filter setting of the alarm action for the specified alarm number. Up to 5 alarm actions can be specified, periodic FTP is assigned to event No.6, and pre/post FTP assigned to No.7. Therefore the number of event(number) can be set between the range of 1 to 7. Note that alarm numbers are different from the alarm input pin numbers.

Specify sunday, monday, tuesday, wednesday, thursday, friday or saturday for WeekOfDay.

When the filter is enabled, on will be returned. When the filter is disabled, off will be returned.

Allowed users admin, operator

## Setting Alarm Filter

Format  /api/param?application.event(Number).filter(WeekOfDay).status=data
