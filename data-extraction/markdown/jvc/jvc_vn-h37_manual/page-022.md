## admin:jvc

Base64 encoding of this string yields YWRtaW46anZj. Enter this in the Authorization line. Default password for each username is jvc.

3) The camera returns a response to the client. In the following example, current subnet mask is 255.0.0.0. In addition, 255.0.0.0 is followed by &amp; and 200 OK, indicating that getting parameter is successful.

## Example

HTTP/1.1 200 OK&lt;CRLF&gt;

Connection: close&lt;CRLF&gt;

Content-Length: 80&lt;CRLF&gt;

Content-type: text/plain&lt;CRLF&gt;

Date: Fri, 13 MAY 2011 07:33:12 GMT&lt;CRLF&gt;

Server: JVC VN-H37 API Server&lt;CRLF&gt;

network.interface.subnetmask=255.0.0.0&amp;200 OK&lt;CRLF&gt;

- 4) The client disconnects TCP80 to end the use of API.

Note:  APIs for getting/setting parameters are not restricted by the access restriction function.

## 7.2. Getting Parameter

Specify API in GET line according to the format below when getting a parameter from the camera.

/api/param?ParamA.ParamB.ParamC

It is possible to get multiple parameters at a time. Connect parameters with &amp;. Do not insert space before and after &amp;.

/api/param?ParamA.ParamB.ParamC&amp;ParamA.ParamD.ParamE

The upper limit of this character string is 1024 bytes. The maximum number of parameters that can be acquired at a time is 15. Status settings, i.e. network.interface.status, network.dns.status, network.ntp.status, etc., can not be acquired at a time.

When acquisition is successfully completed, values will be shown in the body of HTTP response, followed by "&amp;200 OK" message.

Example:

ParamA.ParamB.ParamC=Data&amp;200 OK
