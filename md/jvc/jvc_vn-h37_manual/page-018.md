Unlike APIs for getting/setting parameters, Accept line is not required. Basic authentication is also not necessary. 

## **Example** 

## **GET /api/video?encode=mpeg4 HTTP/1.1<CRLF>** 

## **Host: 192.168.0.2<CRLF><CRLF>** 

Parameter value is indicated using =. Do not insert space before and after =. 

Example    encode=h264 

## **Parameter Description** 

**encode** For specifying compression format. 

## **4.3. Response** 

## **When API is successfully received.** 

The camera will return 200 OK. The x-vnh37_response line indicates actual parameter. 

## **Example of VN-H137** 

HTTP/1.1 200 OK<CRLF> 

Connection: Keep-Alive<CRLF> 

Content-Type: video/mp4v-es<CRLF> 

Date: Tue, 06 Mar 2012 15:10:55 GMT<CRLF> 

Server: JVC VN-H137 Network Camera<CRLF> 

x-vnh37_response: encode=mpeg4&framesize=640x480<CRLF> 

## **4.4. Restrictions** 

## **Access restriction** 

The camera has access restriction feature that enables to deny access from a specific IP address. If MPEG-4 is 

requested from the IP address of access restrictions, the camera disconnects the TCP connection after API is send. 

## **4.5. MPEG-4 Stream Format Send Out by the camera** 

MPEG-4 stream form the camera is MPEG-4 Part2 (ISO/IEC 14496-2) compliant, level3 of simple profile. Its is a sequence of I-VOPs, or I-VOPs and P-VOPs. 

I-VOP:  Inter frame compressed data 

P-VOP: Inter frame compressed data with previous frame 

15 

Downloaded from www.Manualslib.com manuals search engine 
