## **Getting SMTP Server Address Setting** 

**Format  /api/param?application.smtp.host** 

## **Example of Response  application.smtp.host=192.168.0.200&200 OK** 

## **Response example when setting field is left blank  application.smtp.host=&200 OK** 

**Interpretation** Acquire the address setting of the SMTP server. 

**Allowed users** admin, operator, user 

## **Setting SMTP Server Address** 

**Format  /api/param?application.smtp.host=data** 

## **Example  /api/param?application.smtp.host=192.168.0.200** 

## **Example of Response  application.smtp.host&200 OK** 

**Interpretation** Change the address setting of the SMTP server. Specify the IP address or FQDN. The maximum 

FQDN size is 63 bytes. Specify as 0.0.0.0 when the SMTP server is not set. It is also possible to leave the setting 

field blank as follows. **/api/param?application.smtp.host=%00** 

**Allowed users** admin, operator 

## **Getting SMTP Server Port Number Setting** 

**Format  /api/param?application.smtp.port** 

## **Example of Response  application.smtp.port=25&200 OK** 

**Interpretation** Acquire the port number setting of the SMTP server. 

**Allowed users** admin, operator, user 

## **Setting SMTP Server Port Number** 

**Format  /api/param?application.smtp.port=data** 

**Example  /api/param?application.smtp.port=25** 

## **Example of Response  application.smtp.port&200 OK** 

**Interpretation** Change the port number setting of the SMTP server. 

**Allowed users** admin, operator 

## **Getting Sender Mail Address Setting** 

## **Format  /api/param?application.smtp.mailfrom** 

## **Example of Response  application.smtp.mailfrom=somebody@somecompany.com&200 OK** 

**Interpretation** Acquire sender mail address setting. POP user name is used as local part of sender mail address when sender mail address setting is blank. When POP user name is also blank, the local-part is set to 

"vn_h37@hostname". When the hostname is also blank, SMTP server decide sender mail address. 

45 

Downloaded from www.Manualslib.com manuals search engine 
