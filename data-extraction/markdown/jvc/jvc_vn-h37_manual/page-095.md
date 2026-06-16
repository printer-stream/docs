Example  /api/param?network.rtsp.port=554

Example of Response network.rtsp.port&amp;202 Accepted(network.rtsp(configuration).status=restart)

Interpretation Change port number of RTSP server. Default is 554.

Allowed user

admin, operator

## 29.  Getting Audio from the Camera via HTTP (VN-H57/157WP/257/257VP)

## 29.1.  Basic Procedures

- 1) The client establishes a TCP connection to port number 80.
- 2) The client sends out API.

## Example

GET /api/audio?lowdelay=1 HTTP/1.1&lt;CRLF&gt;

Host: 192.168.0.2&lt;CRLF&gt;&lt;CRLF&gt;

Note &lt;CRLF&gt; denotes the line feed code (0x0D, 0x0A).

- 3) The camera returns HTTP response.

## Example

HTTP/1.1 200 OK&lt;CRLF&gt;

Connection: close&lt;CRLF&gt;

Content-type: audio/ulaw&lt;CRLF&gt;

Date: Tue, 02 Oct 2007 07:33:12 GMT&lt;CRLF&gt;

Server: JVC VN-H57 Network Camera&lt;CRLF&gt;

x-vnh57\_response: encode=ulaw&amp;lowdelay=1&amp;assured=1&lt;CRLF&gt;&lt;CRLF&gt;

- 4) The camera sends out audio data after returning HTTP response.

Audio data with 12 bytes header will be sent out continuously after HTTP response. HTTP Response and audio data sent out by the camera are as follows.

HTTP Response

header (12 bytes)

u-Law data (512 bytes)

header (12 bytes)

u-Law data (512 bytes)
