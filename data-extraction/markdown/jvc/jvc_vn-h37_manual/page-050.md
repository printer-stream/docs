## Setting POP Server Address

Format  /api/param?application.pop.host=data

Example  /api/param?application.pop.host=192.168.0.200

Example of Response  application.pop.host&amp;200 OK

Interpretation Change the address setting of the POP server. Specify the IP address or FQDN. The maximum FQDN size is 63 bytes. Specify as 0.0.0.0 when the POP server is not set. It is also possible to leave the setting field blank as follows. /api/param?application.pop.host=%00

Allowed users admin, operator

## Getting POP Server Port Number Setting

Format  /api/param?application.pop.port

Example of Response  application.pop.port=110&amp;200 OK

Interpretation Acquire the port number setting of the POP server.

Allowed users admin, operator, user

## Setting POP Server Port Number

Format  /api/param?application.pop.port=data

Example  /api/param?application.pop.port=110

Example of Response  application.pop.port&amp;200 OK

Interpretation Change the port number setting of the POP server.

Allowed users admin, operator

## Getting POP Server User Name Setting

Format  /api/param?application.pop.user

Example of Response  application.pop.user=somename&amp;200 OK

Response example when setting field is left blank  application.pop.user=&amp;200 OK

Interpretation Acquire the user name setting of the POP server. The user name is used as local part of sender mail address when sender mail address setting is blank. When the user name is blank, the local-part is set to "vn\_h37".

Example of Response     application.pop.user=somename&amp;200 OK

Example of Mail Address  somename@somecompany.com

Allowed users admin, operator, user

## Setting POP Server User Name

Format  /api/param?application.pop.user=data

Example  /api/param?application.pop.user=somename
