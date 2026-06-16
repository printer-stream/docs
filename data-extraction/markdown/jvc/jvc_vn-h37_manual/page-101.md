S-&gt;C

RTSP/1.0 200 OK

CSeq: 3

Session: 401875008

Status: pause

C-&gt;S

PLAY rtsp://192.168.0.20/PSIA/Streaming/tracks RTSP/1.0

CSeq: 4

Range: clock=20120518T135717Z

Session: 401875008

S-&gt;C

RTSP/1.0 200 OK

CSeq: 4

Session: 401875008

C-&gt;S

GET\_PARAMETER rtsp://192.168.0.20/PSIA/Streaming/tracks RTSP/1.0

CSeq: 5

Connection: Keep-Alive

Session: 401875008

S-&gt;C

RTSP/1.0 200 OK

CSeq: 5

Session: 401875008

Status: play

## 32.  Exporting H.264 data from SD Card to the PC

This section describes APIs for audio exporting H.264 data from SD card to the PC.

## Getting Total Number of Files and File Size

## Format

/api/copy?pseudo=on&amp;from.date.start=YYYYMMDDhhmmss&amp;from.date.end=YYYYMMDDhhmmss

Example of response

14&lt;CRLF&gt;

200 OK,(Completed)&lt;CRLF&gt;

&lt;CRLF&gt;

1f&lt;CRLF&gt;
