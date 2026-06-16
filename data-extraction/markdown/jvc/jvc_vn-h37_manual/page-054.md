/api/param?application.ftp.naming\_option.

File Name Example Camera.jpg

Allowed users

admin, operator

## Getting User Define Name of File Naming

Format  /api/param?application.ftp.naming\_option

Example of Response  application.ftp.naming\_option=abc&amp;200 OK

Interpretation Acquire user define name for file naming of periodic FTP. The maximum size is 16 bytes. When /api/param?application.ftp.naming\_option is set to "type1", the file name is as ***YYYMMDDHHMMSSNNN.jpg,

and "***" can be gotten by this API.

File Name Example Camera\_20060207201315001.jpg

When /api/param?application.ftp.naming\_option is set to "type2", the file name is as ***.jpg and "***" can be gotten by this API.

File Name Example Camera.jpg

Allowed users admin, operator

## Setting User Define Name of File Naming

Format  /api/param?application.ftp.naming\_option=data

Example of Response  application.ftp.naming\_option&amp;200 OK

Interpretation Change user define name for file naming of periodic FTP. The maximum size is 16 bytes. When /api/param?application.ftp.naming\_option is set to "type1", the file name is as ***YYYMMDDHHMMSSNNN.jpg,

and "***" can be set by this API.

File Name Example Camera\_20060207201315001.jpg

When /api/param?application.ftp.naming\_option is set to "type2", the file name is as ***.jpg and "***" can be set by this API.

File Name Example Camera.jpg

Allowed users

admin, operator

## Getting Parameters of Pre/Post Recording for FTP

## Format

To get Frame Rate  /api/param?application.object(7).framerate

To get Pre Duration  /api/param?application.object(7).prerec

To get Post Duration  /api/param?application.object(7).postrec

To get Encoder No.  /api/param?application.object(7).source

Example of Response

For Frame Rate      application.object(7).framerate=10&amp;200 OK
