| Host:   | space   | IP Address of Camera   | 0x0D 0x0A 0x0D 0x0A   |
|---------|---------|------------------------|-----------------------|

Unlike APIs for getting/setting parameters, Accept line is not required. Basic authentication is also not necessary.

## Example

GET /api/video?encode=h264(1) HTTP/1.1&lt;CRLF&gt;

Host: 192.168.0.2&lt;CRLF&gt;&lt;CRLF&gt;

Parameter value is indicated using =. Do not insert space before and after =.

Example    encode=h264(1)

## Parameter Description

encode For specifying compression format. For example, specify as encode=h264(1) to get H.264 encoded by channel 1.  To know compression format of each channel, open Encoder setting page by IE described in INSTRUCTIONS manual,  or issue "encode" API described in later chapter of this document.

## 3.3. Response

## When API is successfully received.

The camera will return 200 OK. The x-vnh37\_response line indicates actual parameter.

## Example of VN-H137

HTTP/1.1 200 OK&lt;CRLF&gt;

Connection: Keep-Alive&lt;CRLF&gt;

Content-Type: video/mp4v-es&lt;CRLF&gt;

Date: Tue, 06 Mar 2012 15:10:55 GMT&lt;CRLF&gt;

Server: JVC VN-H137 Network Camera&lt;CRLF&gt;

x-vnh37\_response: encode=h264&amp;framesize=1920x1080&lt;CRLF&gt;

## 3.4. Restrictions

## Access restriction

The camera has access restriction feature that enables to deny access from a specific IP address. If H.264 is requested from the IP address of access restrictions, the camera disconnects the TCP connection after API is send.

## 3.5. H.264 Stream Format Send Out by the camera
