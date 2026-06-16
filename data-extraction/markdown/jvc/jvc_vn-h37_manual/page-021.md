waits 0-0.7 second before sending response to avoid too many responses are sent in short period from many cameras.

Response Example        system.id=VN-H37(192.168.0.2/24)&amp;200 OK&lt;CRLF&gt;

## 7.  Using API that Requires Basic Authentication

Basic authentication is required for JVC API explained in Section 7 or later. This section provides general explanation of those APIs.

## 7.1. Procedure

- 1) The client establishes a TCP connection to port number 80.
- 2) The client sends API.

API has following structure.

Accept:

text/plain (or text/html)

space

space

HTTP/1.1

0x0D 0x0A

Host:

space

IP Address of Camera

0x0D 0x0A

Authorization: Basic

space

Encoded User Name and Password

0x0D 0x0A 0x0D 0x0A

GET

space

API Characters

0x0D 0x0A

The following is an example of API for Getting subnet mask of the camera.

## Example

GET /api/param?network.interface.subnetmask HTTP/1.1&lt;CRLF&gt;

Accept: text/plain&lt;CRLF&gt;

Host: 192.168.0.2&lt;CRLF&gt;

Authorization: Basic YWRtaW46anZj&lt;CRLF&gt;&lt;CRLF&gt;

Specify the response format by Accept line. Plain text response is returned when this is specified as text/plain. HTML response is returned when text/html is specified. HTML response is returned when Accept is not specified. These APIs for getting/setting parameters are protected by basic authentication. Authorization line needs to include encoded username and password. There are 3 types of usernames, namely admin, operator and user. Available APIs are different for each username. Join the user name and the password using a colon, Base64 encode this character string and enter this in the Authorization line.

For example, when

User name   admin

Password    jvc

then the character string joining the user name and the password with a colon is:
