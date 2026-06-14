structured JPEG. When framerate=0 is specified, Server Push is disabled even if server_push=on is specified. 

## **2.3. Response** 

## **When API with server_push=on is successfully received.** 

The camera will return 200 OK. The x-vnh37_response line indicates actual parameter. 

## **Example of VN-H137** 

HTTP/1.1 200 OK<CRLF> 

Content-Type: multipart/x-mixed-replace;boundary=foo<CRLF> 

Date: Tue, 06 Mar 2012 13:32:57 GMT<CRLF> 

Server: JVC VN-H137 Network Camera<CRLF> 

x-vnh37_response: encode=jpeg&framerate=5.0&framesize=1920x1080&server_push=on&ptz_info=off<CRLF> <CRLF> 

## **When API without server_push option is successfully received.** 

The camera will return 200 OK. The x-vnh37_response line indicates actual parameter. 

## **Example of VN-H137** 

HTTP/1.1 200 OK<CRLF> 

Connection: Keep-Alive<CRLF> 

Content-Type: image/jpeg<CRLF> 

Date: Tue, 06 Mar 2012 14:06:07 GMT<CRLF> 

Server: JVC VN-H137 Network Camera<CRLF> 

x-vnh37_response: encode=jpeg&framerate=5.0&framesize=1920x1080&server_push=off&ptz_info=off<CRLF> <CRLF> 

## **2.4. Restrictions** 

## **Access restriction** 

The camera has access restriction feature that enables to deny access from a specific IP address. If JPEG is 

requested from the IP address of access restriction, the camera disconnects the TCP connection after API is sent. 

## **Restriction by maximum bitrate of the camera.** 

The maximum bitrate of the camera is about 20 Mbps. 

## **Number of clients** 

The maximum number of clients that can get JPEG stream depends on encode settings and requests from client. 

9 

Downloaded from www.Manualslib.com manuals search engine 
