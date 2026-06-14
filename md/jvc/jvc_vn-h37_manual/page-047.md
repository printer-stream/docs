## **application.event(1).trigger&202 Accepted(application.event(1).status=restart)** 

**Interpretation** Set Trigger of the alarm action for the specified alarm number. Up to 5 alarm actions can be specified, and periodic FTP is assigned to event No.6, pre/post FTP assigned to No.7, SD Card constant recording is assigned to event No.8 and SD Card alarm recording is assigned to event No.10. Therefore the number of event(number) can be set between the range of 1 to 8 and 10. Note that alarm numbers are different from the alarm input pin numbers. 

The changes to settings of alarm action become valid by /api/param?application.event(Number).status=restart. When setting only 1 Trigger: 

Specify m1 in the case of Make for alarm input 1. **[VN-H57/157WP/257/257VP Only]** Specify b1 in the case of Break for alarm input 1. **[VN-H57/157WP/257/257VP Only]** Specify m2 in the case of Make for alarm input 2. **[VN-H57/157WP/257/257VP Only]** Specify b2 in the case of Break for alarm input 2. **[VN-H57/157WP/257/257VP Only]** Specify camera.position(num).status for preset position. "num" is from 0 to 19. 

Specify v1 for motion detection of video. 

Specify audio_detect1 for audio detection 1. **[VN-H57/157WP/257/257VP Only]** Specify audio_detect2 for audio detection 2. **[VN-H57/157WP/257/257VP Only]** 

Specify tampering_detect for tampering detect of video. 

Specify ncbwe for IR Filter ON. 

Specify ncbws for IR Filter OFF. Specify i(second) for periodic FTP trigger. Specify time/hhmmss for time trigger. 

## **Setting Example /api/param?application.event(1).trigger=v1** 

Interval can be set to periodic ftp assigned to event(6). Set "i1500" for interval 1500 seconds. 

## **Setting Example /api/param?application.event(6).trigger=i1500** 

When setting Trigger upon combining 2 alarm inputs, specify as m1(50)b2. The example above indicates that trigger will be activated when break is invoked at alarm input 2 within 50 seconds after make is invoked at alarm input 1. Additionally, combination is only allowed for alarm inputs and not motion detect nor IR Filter. And same alarm can not be combined. For example, m1(50)m1 is not available. 

## **Setting Example  /api/param?application.event(1).trigger=m1(100)b2** 

**Allowed users** admin, operator 

## **12. JVC API for Alarm Environment** 

The APIs below are related to alarm environment setting. These are equivalent to the features on the Alarm 

Environment page of the WEB setting page. Refer to the instruction manual for details on the Alarm Environment 

page. 

44 

Downloaded from www.Manualslib.com manuals search engine 
