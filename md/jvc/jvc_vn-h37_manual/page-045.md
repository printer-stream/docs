pin numbers. 

Specify sunday, monday, tuesday, wednesday, thursday, friday or saturday for WeekOfDay. 

Specify start time and end time in the format like hhmmss-hhmmss. Start time can be from 000000 to 235959. End time can be from 000001 to 240000. Start time must be earlier than end time. 

The changes to filter of alarm action is saved by /api/param?application.event(Number).status=restart. 

**Allowed users** admin, operator 

## **Getting Alarm Filter Type** 

## **Format  /api/param?application.event(Number).filter(WeekOfDay).type** 

**Example** When Getting Type of Sunday filter of Alarm No. 1 

## **/api/param?application.event(1).filter(sunday).type** 

## **Example of Response  application.event(1).filter(sunday).type=mask&200 OK** 

**Interpretation** Acquire filter type of the alarm action for the specified alarm number. Up to 5 alarm actions can be specified, periodic FTP is assigned to event No.6, and pre/post FTP assigned to No.7. Therefore the number of event(number) can be set between the range of 1 to 7. Note that alarm numbers are different from the alarm input pin numbers. 

Specify sunday, monday, tuesday, wednesday, thursday, friday or saturday for WeekOfDay. "mask" or "unmask" is returned. When the setting is mask, alarm action is disabled during the filter time. When the setting is unmask, alarm action is enabled during the filter time. 

**Allowed users** admin, operator 

## **Setting Alarm Filter Type** 

## **Format  /api/param?application.event(Number).filter(WeekOfDay).type=data** 

**Example** When setting Sunday filter type of Alarm No. 1 to be unmask 

## **/api/param?application.event(1).filter(sunday).type=unmask** 

## **Example of Response** 

## **application.event(1).filter(sunday).type&202 Accepted(application.event(1).status=restart)** 

**Interpretation** Set filter type of the alarm action for the specified alarm number. Up to 5 alarm actions can be specified, periodic FTP is assigned to event No.6, and pre/post FTP assigned to No.7. Therefore the number of 

event(number) can be set between the range of 1 to 7. Note that alarm numbers are different from the alarm input pin numbers. 

Specify sunday, monday, tuesday, wednesday, thursday, friday or saturday for WeekOfDay. 

Specify mask or unmask. When the setting is mask, alarm action is disabled during the filter time. When the setting is unmask, alarm action is enabled during the filter time. 

The changes to filter of alarm action is saved by /api/param?application.event(Number).status=restart. 

**Allowed users** admin, operator 

42 

Downloaded from www.Manualslib.com manuals search engine 
