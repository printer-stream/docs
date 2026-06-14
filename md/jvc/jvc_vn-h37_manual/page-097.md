shorten the audio delay time. To enable stable playback in a network where jitter occurs, it is recommended that this be specified as assured=1. Default value is 1. 

**lowdelay** Specifying as lowdelay=1 disables the Nagle algorithm of TCP, and audio delay time will be shortened. When lowdelay=0 is specified, the Nagle algorithm is enabled and audio delay time will be prolonged. However, transmission overhead will be enhanced. Default value is 1. 

## **29.3. Response** 

## **When API is successfully received** 

The camera will return 200 OK. There is no Content-length field in the HTTP response. The x-vnh57_response 

line indicates actual parameter. 

**Example** 

## **HTTP/1.1 200 OK<CRLF>** 

## **Connection: close<CRLF>** 

**Content-type: audio/ulaw<CRLF>** 

**Date: Tue, 02 Oct 2007 07:33:12 GMT<CRLF>** 

**Server: JVC VN-H57 Network Camera<CRLF>** 

## **x-vnh57_response: encode=ulaw&lowdelay=1&assured=1<CRLF><CRLF>** 

## **29.4. Restrictions** 

## **Access restriction** 

The camera has access restriction feature that enables to deny access from a specific IP address. If audio is 

requested from the IP address of access restriction, the camera disconnects the TCP connection after API is sent. 

## **Restriction by maximum bitrate** 

The maximum bitrate of the camera is about 20 Mbps. 

## **Number of clients** 

The maximum number of audio stream is 2, 2 TCP streams or 1 TCP stream and 1 multicast stream. When 2 

streams are sent from the camera, new request for audio is disconnected. 

## **30. Sending Audio to the Camera  (VN-H57/157WP/257/257VP)** 

This section describes APIs for audio sending from a client to the camera. Make use of the APIs explained in this section in the way as mentioned in Section 7. 

94 

Downloaded from www.Manualslib.com manuals search engine 
