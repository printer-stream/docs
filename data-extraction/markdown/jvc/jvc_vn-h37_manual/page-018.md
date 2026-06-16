Unlike APIs for getting/setting parameters, Accept line is not required. Basic authentication is also not necessary.

## Example

GET /api/video?encode=mpeg4 HTTP/1.1&lt;CRLF&gt;

Host: 192.168.0.2&lt;CRLF&gt;&lt;CRLF&gt;

Parameter value is indicated using =. Do not insert space before and after =.

Example    encode=h264

## Parameter Description

encode For specifying compression format.

## 4.3. Response

## When API is successfully received.

The camera will return 200 OK. The x-vnh37\_response line indicates actual parameter.

## Example of VN-H137

HTTP/1.1 200 OK&lt;CRLF&gt;

Connection: Keep-Alive&lt;CRLF&gt;

Content-Type: video/mp4v-es&lt;CRLF&gt;

Date: Tue, 06 Mar 2012 15:10:55 GMT&lt;CRLF&gt;

Server: JVC VN-H137 Network Camera&lt;CRLF&gt;

x-vnh37\_response: encode=mpeg4&amp;framesize=640x480&lt;CRLF&gt;

## 4.4. Restrictions

## Access restriction

The camera has access restriction feature that enables to deny access from a specific IP address. If MPEG-4 is requested from the IP address of access restrictions, the camera disconnects the TCP connection after API is send.

## 4.5. MPEG-4 Stream Format Send Out by the camera

MPEG-4 stream form the camera is MPEG-4 Part2 (ISO/IEC 14496-2) compliant, level3 of simple profile. Its is a sequence of I-VOPs, or I-VOPs and P-VOPs.

I-VOP:  Inter frame compressed data

P-VOP: Inter frame compressed data with previous frame
