structured JPEG. When framerate=0 is specified, Server Push is disabled even if server\_push=on is specified.

## 2.3. Response

## When API with server\_push=on is successfully received.

The camera will return 200 OK. The x-vnh37\_response line indicates actual parameter.

## Example of VN-H137

HTTP/1.1 200 OK&lt;CRLF&gt;

Content-Type: multipart/x-mixed-replace;boundary=foo&lt;CRLF&gt;

Date: Tue, 06 Mar 2012 13:32:57 GMT&lt;CRLF&gt;

Server: JVC VN-H137 Network Camera&lt;CRLF&gt;

x-vnh37\_response: encode=jpeg&amp;framerate=5.0&amp;framesize=1920x1080&amp;server\_push=on&amp;ptz\_info=off&lt;CRLF&gt; &lt;CRLF&gt;

## When API without server\_push option is successfully received.

The camera will return 200 OK. The x-vnh37\_response line indicates actual parameter.

## Example of VN-H137

HTTP/1.1 200 OK&lt;CRLF&gt;

Connection: Keep-Alive&lt;CRLF&gt;

Content-Type: image/jpeg&lt;CRLF&gt;

Date: Tue, 06 Mar 2012 14:06:07 GMT&lt;CRLF&gt;

Server: JVC VN-H137 Network Camera&lt;CRLF&gt;

x-vnh37\_response: encode=jpeg&amp;framerate=5.0&amp;framesize=1920x1080&amp;server\_push=off&amp;ptz\_info=off&lt;CRLF&gt; &lt;CRLF&gt;

## 2.4. Restrictions

## Access restriction

The camera has access restriction feature that enables to deny access from a specific IP address. If JPEG is requested from the IP address of access restriction, the camera disconnects the TCP connection after API is sent.

## Restriction by maximum bitrate of the camera.

The maximum bitrate of the camera is about 20 Mbps.

## Number of clients

The maximum number of clients that can get JPEG stream depends on encode settings and requests from client.
