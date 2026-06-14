**Allowed users** admin, operator, user 

## **Setting Sender Mail Address** 

## **Format  /api/param?application.smtp.mailfrom=data** 

## **Example  /api/param?application.smtp.mailfrom=somebody@somecompany.com** 

## **Example of Response  application.smtp.mailfrom&200 OK** 

**Interpretation** Change sender mail address setting. Maximum text number of sender mail address is 96. 

Alphanumeric and followings are available. 

! # $ % & ' * + - / = ? ^ _ ` { } | ~ 

POP user name is used as local part of sender mail address when sender mail address setting is blank. When 

POP user name is also blank, the local-part is set to "vn_h37@hostname". When the hostname is also blank, 

SMTP server decide sender mail address. 

**Allowed users** admin, operator 

## **Getting "POP before SMTP" Setting** 

## **Format  /api/param?application.smtp.type** 

## **Example of Response  application.smtp.type=pbs&200 OK** 

**Interpretation** Acquire the "POP before SMTP" setting. "simple" is returned when this is set to off. "pbs" is 

returned when this is set to on. 

**Allowed users** admin, operator, user 

## **Setting "POP before SMTP"** 

## **Format  /api/param?application.smtp.type=data** 

## **Example  /api/param?application.smtp.type=pbs** 

## **Example of Response  application.event.smtp.type&200 OK** 

**Interpretation** Change the "POP before SMTP" setting. Specify as "simple" when setting to off and "pbs" when setting to on. 

**Allowed users** admin, operator 

## **Getting POP Server Address Setting** 

## **Format  /api/param?application.pop.host** 

## **Example of Response  application.pop.host=192.168.0.200&200 OK** 

## **Response example when setting field is left blank  application.pop.host=&200 OK** 

**Interpretation** Acquire the address setting of the POP server. 

**Allowed users** admin, operator, user 

46 

Downloaded from www.Manualslib.com manuals search engine 
