## **For Pre Duration  /api/param?application.object(7).prerec=2&200 OK** 

**For Post Duration  /api/param?application.object(7).postrec=2&200 OK** 

**For Encoder No.  /api/param?application.object(7).source=encode(1)&200 OK** 

**Interpretation** Acquire parameters for PrePost. 

**Allowed users** admin, operator, user 

## **Setting Parameters of Pre/Post Recording for FTP** 

## **Format** 

**To set Frame Rate  /api/param?application.object(7).framerate=5** 

**To set Pre Duration  /api/param?application.object(7).prerec=3** 

**To set Post Duration  /api/param?application.object(7).postrec=3** 

**To set Encoder No.  /api/param?application.object(7).source=encode(1)** 

## **Example of Response** 

**For Frame Rate      application.object(7).framerate&200 OK** 

**For Pre Duration  /api/param?application.object(7).prerec&200 OK** 

**For Post Duration  /api/param?application.object(7).postrec&200 OK** 

## **For Encoder No.  /api/param?application.object(7).source&200 OK** 

**Interpretation** Change parameters for PrePost. 

Specify 30, 15, 10, 7.5, 6, 5, 3, 2, or 1 for frame rate. Maximum Pre/Post duration is 60 seconds. Setting zero to 

Pre and Post duration is invalid. Specify encode(1), encode(2), or encode(3) for encoder No. Pre/Post Recording for FTP is valid when encode type is set to JPEG. 

**Allowed users** admin, operator 

## **13. JVC API for SD Card Record** 

The APIs below are related to SD Card Recording. These are equivalent to the features on the SD Card Record 

page of the WEB setting page. Refer to the instruction manual for details on the SD Card Record page. 

## **Getting SD Card Status** 

**Format  /api/param?storage.disk(1).status** 

**Example of Response  storage.disk(1).status=on&200 OK** 

**Interpretation** Acquire SD Card status. “on”, “empty”, “read_only”, “off”, “off_read_only”, or “off_empty” will be 

returned. 

|**Return value**|**Use / Disable**|**Status**|
|---|---|---|
|**off_empty**|**Disable**|**No SD card**|
|**off_read_only**|**Disable**|**LOCK switch is enabled**|
|**off**|**Disable**|**LOCK switch is disabled**|
|**empty**|**Use**|**No SD card**|



52 

Downloaded from www.Manualslib.com manuals search engine 
