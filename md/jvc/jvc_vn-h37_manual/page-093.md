**Allowed users** admin, operator, user 

## **Getting Firmware Revisions** 

## **Format  /api/param?system.software.revision** 

## **Example of Response  system.software.revision=1.00&200 OK** 

**Interpretation** Acquire revisions of the firmware. 

**Allowed users** admin, operator, user 

## **Getting Software ID** 

## **Format  /api/param?system.software.programid** 

**Response** Return software ID. 

Response examples 

## **system.software.programid=SPL0123&200 OK** 

**Interpretation** Acquire the software ID. 

**Allowed user** admin 

## **28. JVC API for Others** 

These are APIs of features not found on the WEB setting page. 

## **Getting Alarm Input Status  (VN-H57/157/257)** 

**Format  /api/param?peripheral.input_pin.pin(Number).status** 

## **Example of Response  peripheral.input_pin.pin(1).status=make&200 OK** 

**Interpretation** Acquire the current alarm input status. Specify 1 or 2 to Number. Either make or break will be 

returned. 

**Allowed users** admin, operator, user 

## **Getting Mode of FTP Server** 

## **Format  /api/param?application.ftp.mode** 

## **Example of Response  application.ftp.mode=active&200 OK** 

**Interpretation** Acquire the mode of FTP server that is used by alarm action. Either active or passive is returned. active mode: Standard mode of FTP server. Also called PORT mode. TCP connection for data is established from 20 port of FTP server to 10020 port of the camera. 

passive mode: TCP connection for data is established from the camera to FTP server. Port number depends on FTP server. 

**Allowed users** admin, operator, user 

90 

Downloaded from www.Manualslib.com manuals search engine 
