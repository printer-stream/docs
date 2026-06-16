Allowed users admin, operator

## Getting FTP Server Path Setting

Format  /api/param?application.ftp.path

Example of Response  application.ftp.path=subdir1&amp;200 OK

Response example when setting field is left blank  application.ftp.path=&amp;200 OK

Interpretation Acquire the FTP server directory setting used for FTP transmission via alarm.

Allowed users admin, operator, user

## Setting FTP Server Path

Format  /api/param?application.ftp.path=data

Example  /api/param?application.ftp.path=subdir1

Example of Response  application.ftp.path&amp;200 OK

Interpretation Change the FTP server directory setting used for FTP transmission. It is possible to set FTP transmission to a directory under the FTP server home directory by specifying that directory name. Use %2F to segment the directory. ("2F" is ASCII code of "/".) The maximum directory name size is 63 bytes.

Example  /api/param?application.ftp.path=subdir1%2Fsubdir2

By leaving the setting blank as follows, FTP transmission will be set to the FTP server home directory.

/api/param?application.ftp.path=%00

Allowed users admin, operator

## Getting FTP Server User Name Setting

Format  /api/param?application.ftp.user

Example of Response  application.ftp.user=somename&amp;200 OK

Response example when setting field is left blank  application.ftp.user=&amp;200 OK

Interpretation Acquire the FTP server user name setting used for FTP transmission via alarm.

Allowed users admin, operator

## Setting FTP Server User Name

Format  /api/param?application.ftp.user=data

Example  /api/param?application.ftp.user=somename

Example of Response  application.ftp.user&amp;200 OK

Interpretation Change the FTP server user name setting used for FTP transmission via alarm. The maximum user name size is 32 bytes. Set as follows when this setting is to be left blank.

/api/param?application.ftp.user=%00

Allowed users

admin, operator
