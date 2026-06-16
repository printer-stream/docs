## Example of Response  application.pop.user&amp;200 OK

Interpretation Change the user name setting of the POP server. The maximum user name size is 64 bytes. Set as follows when this is to be left blank.

/api/param?application.pop.user=%00

The user name is used as local part of sender mail address when sender mail address setting is blank. When the user name is blank, the local-part is set to "vn\_h37". When POP before SMTP is disabled, it is not necessary to set POP server settings other than POP user name setting.

Example of setting            /api/param?application.pop.user=somename

Example of Mail Address      somename@somecompany.com

Following characters must not be used in user name.

<!-- formula-not-decoded -->

Allowed users admin, operator

## Setting POP Server Password

Format  /api/param?application.pop.password=data

Example  /api/param?application.pop.password=someword

Example of Response  application.pop.password&amp;200 OK

Interpretation Change the password setting of the POP server. The maximum password size is 32 bytes. Set as follows when this is to be left blank. /api/param?application.pop.password=%00

Allowed users admin, operator

(Note: There is no API for reading passwords.)

## Getting FTP Server Address Setting

Format  /api/param?application.ftp.host

Example of Response  application.ftp.host=192.168.0.200&amp;200 OK

Response example when setting field is left blank  application.ftp.host=&amp;200 OK

Interpretation Acquire the FTP server address setting used for FTP transmission via alarm.

Allowed users admin, operator, user

## Setting FTP Server Address

Format  /api/param?application.ftp.host=data

Example  /api/param?application.ftp.host=10.0.0.200

Example of Response  application.ftp.host&amp;200 OK

Interpretation Change the FTP server address setting used for FTP transmission via alarm. Specify the IP address or FQDN. The maximum FQDN size is 63 bytes. Specify as 0.0.0.0 when the FTP server is not set. It is also possible to leave the setting field blank as follows. /api/param?application.ftp.path=%00
