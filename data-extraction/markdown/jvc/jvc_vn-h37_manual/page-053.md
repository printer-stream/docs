## Setting FTP Server Password

Format  /api/param?application.ftp.password=data

Example  /api/param?application.ftp.password=someword

Example of Response  application.ftp.password&amp;200 OK

Interpretation Change the FTP server password setting used for FTP transmission via alarm. The maximum password size is 32 bytes. Set as follows when this setting is to be left blank.

/api/param?application.ftp.password=%00

Allowed users admin, operator

(There is no API for Getting passwords.)

## Getting File Naming of Periodic FTP

Format  /api/param?application.ftp.naming

Example of Response  application.ftp.naming=default&amp;200 OK

Interpretation Acquire file naming of periodic FTP. "default", "type1" or "type2" is returned. When default is set,

the file name is as YYYYMMDDHHMMSS-NNN-2.jpg.

Example

20060207201315-001-2.jpg

When type1 is set, the file name is as ***YYYMMDDHHMMSSNNN.jpg. "***" can be gotten by another API,

/api/param?application.ftp.naming\_option.

File Name Example

Camera\_20060207201315001.jpg

When type2 is set, the file name is as ***.jpg. "***" can be gotten by another API,

/api/param?application.ftp.naming\_option.

File Name Example

Camera.jpg

Allowed users

admin, operator

## Setting File Naming of Periodic FTP

Format  /api/param?application.ftp.naming=data

Example  /api/param?application.ftp.naming=type1

Example of Response  application.ftp.naming&amp;200 OK

Interpretation Change file naming of periodic FTP. Specify "default", "type1" or "type2". When default is set, the

file name is as YYYYMMDDHHMMSS-NNN-2.jpg.

Example

20060207201315-001-2.jpg

When type1 is set, the file name is as ***YYYYMMDDHHMMSSNNN.jpg. "***" can be set by another API, /api/param?application.ftp.naming\_option.

File Name Example

Camera\_20060207201315001.jpg

When type2 is set, the file name is as ***.jpg. "***" can be set by another API,
