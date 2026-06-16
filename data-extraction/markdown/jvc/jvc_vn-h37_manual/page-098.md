## 30.1.  Procedures

- 1) The client establishes a TCP connection to port number 80.
- 2) The client sends out API.

API has following structure.

Accept:

User Name and Password

Refer to Section 5 on details of the Accept and Authorization lines.

The API characters are as follows.

space HTTP/1.1

0x0D 0x0A

GET

space API Characters

/api/receive?from=network&amp;from.ip=data1&amp;from.protocol=tcp\_passive&amp;from.ip\_translate=on&amp;to=audio

Example Authorization: Basic text/plain (or text/html) the camera Encoded

space

Host:

space IP Address of

0x0D 0x0A

space

0x0D 0x0A 0x0D 0x0A

0x0D 0x0A

/api/receive?from=network&amp;from.ip=10.0.0.100&amp;from.protocol=tcp\_passive&amp;from.ip\_translate=on&amp;to=audio

Specify the client IP address for from.ip=. When from.ip\_translate is set to off, the camera will standby to receive audio data from the IP address specified at from.ip. When from.ip\_translate is set to on, the camera will ignore from.ip and standby to receive audio data from the source IP address of this API.

- 2) The camera returns a response.

HTTP/1.1 200 OK&lt;CRLF&gt;

Connection: Keep-Alive&lt;CRLF&gt;

Content-type: text/plain&lt;CRLF&gt;

Date: Fri, 13 MAY 2005 07:33:12 GMT&lt;CRLF&gt;

Server: VN-H57 Network Camera/1.0.0&lt;CRLF&gt;

x-vnh57\_response:

from=network&amp;from.ip=10.0.0.100&amp;from.protocol=tcp\_passive&amp;from.ip\_translate=on&amp;to=audio&lt;CRLF&gt;&lt;CRLF&gt; 200 OK&lt;CRLF&gt;

The client may disconnect the TCP80 at this point of time.

- 3) The client establishes a TCP connection to port number 49298.
