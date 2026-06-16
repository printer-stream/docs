## Setting Mode of FTP Server

Format  /api/param?application.ftp.mode=data

Example /api/param?application.ftp.mode=active

Example of Response application.ftp.mode&amp;200 OK

Interpretation Change the mode of FTP server that is used by alarm action. Set active or passive. Default is active.

active mode: Standard mode of FTP server. Also called PORT mode. TCP connection for data is established from 20 port of FTP server to 10020 port of the camera.

passive mode: TCP connection for data is established from the camera to FTP server. Port number depends on FTP server.

Allowed user admin, operator

## Getting Control Port Number of FTP Server

Format  /api/param?application.ftp.port

Example of Response  application.ftp.port=21&amp;200 OK

Interpretation Acquire port number for control of FTP server that is used by alarm action. Port number for data plus one is the port number for control.

Allowed users admin, operator, user

## Setting Control Port Number of FTP Server

Format  /api/param?application.ftp.port=data

Example  /api/param?application.ftp.port=21

Example of Response application.ftp.port&amp;200 OK

Interpretation Change port number for control of FTP server that is used by alarm action. Default is 21. Port number for data plus one is the port number for control.

Allowed user admin, operator

## Getting Port Number of RTSP Server

Format  /api/param?network.rtsp.port

Example of Response  network.rtsp.port=554&amp;200 OK

Interpretation Acquire port number for RTSP server.

Allowed users admin, operator, user

## Setting Port Number of RTSP Server

Format  /api/param?network.rtsp.port=data
