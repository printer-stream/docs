Alarm action of event number 10 is “SD Card alarm recording”. When “SD Card alarm recording” is enabled, rec, SD Card number, and the attached object number will be returned. Segments are indicated by /. The SD Card number is fixed as sd01 at all times. The object number is fixed as object(10). Parameters of SD Card recording can be gotten by other APIs, application.object. 

## **Example of Response  application.event(10).action=rec/sd01/object(10)&200 OK** 

**Allowed users** admin, operator 

## **Setting Alarm Action** 

## **Format  /api/param?application.event(Number).action=Data** 

**Example** When setting action of Alarm No. 1 

## **/api/param?application.event(1).action=mailto/somebody@somecompany.com/none/Message** 

## **Example of Response** 

## **application.event(1).action&202 Accepted(application.event(1).status=restart)** 

**Interpretation** Set the alarm action of the specified alarm number. 5 alarm actions, 1 periodic FTP assigned to No.6, 1 pre/post FTP assigned to No.7 are available, 1 SD Card constant recording assigned to No.8 and 1 SD Card alarm recording assigned to No.10 so alarm action number can be 1 to 8 and 10. Note that alarm numbers are different from the alarm input pin numbers. A separate API 

(/api/param?application.event(Number).status=off) is used to set the alarm action to off. 

The action will be activated by setting the alarm trigger. The API for setting the alarm trigger is /api/param?application.event(Number).trigger. 

The changes to settings of alarm action become valid by /api/param?application.event(Number).status=restart. 

Specify mailto, mail address, JPEG attach and the character string to be sent when sending via mail. Segments are indicated by /. The maximum number of characters for the mail address is 95. To attach JPEG, specify object(Number). If none is specified instead of object(Number), JPEG is not attached to the mail. Number of the character string is from 1 to 127 bytes. To use following characters, specify by hexadecimal number after %. 

## space  &  /  <  >  #  %  "  {  }  |  \  ^  [  ]  ` 

For example, specify 3 characters %20 when inserting a space in the character string. For example, to send the character string "This is alarm.", specify as "This%20is%20alarm.".  %09 and %0D are not available. 

## **Setting Example** 

## **/api/param?application.event(1).action=mailto/somebody@somecompany.com/object(1)/Message%20O** 

## **N** 

The character string "Alarm from VN-H37" will be stored in the title field of the mail. 

38 

Downloaded from www.Manualslib.com manuals search engine 
