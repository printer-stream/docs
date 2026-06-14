## **30.1. Procedures** 

- 1) The client establishes a TCP connection to port number 80. 

## 2) The client sends out API. 

API has following structure. 

|GET|space|space|API Characters|API Characters|API Characters|space|space|HTTP/1.1|HTTP/1.1|0x0D 0x0A||
|---|---|---|---|---|---|---|---|---|---|---|---|
|Accept:||space||text/plain (or text/html)|||0x0D 0x0A|||||
|Host:|space||IP Address ofthe camera|||0x0D 0x0A||||||
|Authorization: Basic||||space|EncodedUser Name and Password||||0x0D 0x0A 0x0D 0x0A|||



Refer to Section 5 on details of the Accept and Authorization lines. 

The API characters are as follows. 

/api/receive?from=network&from.ip=data1&from.protocol=tcp_passive&from.ip_translate=on&to=audio 

Example 

/api/receive?from=network&from.ip=10.0.0.100&from.protocol=tcp_passive&from.ip_translate=on&to=audio 

Specify the client IP address for from.ip=. When from.ip_translate is set to off, the camera will standby to receive audio data from the IP address specified at from.ip. When from.ip_translate is set to on, the camera will ignore from.ip and standby to receive audio data from the source IP address of this API. 

## 2) The camera returns a response. 

HTTP/1.1 200 OK<CRLF> 

Connection: Keep-Alive<CRLF> 

Content-type: text/plain<CRLF> 

Date: Fri, 13 MAY 2005 07:33:12 GMT<CRLF> 

Server: VN-H57 Network Camera/1.0.0<CRLF> 

x-vnh57_response: 

from=network&from.ip=10.0.0.100&from.protocol=tcp_passive&from.ip_translate=on&to=audio<CRLF><CRLF> 200 OK<CRLF> 

The client may disconnect the TCP80 at this point of time. 

- 3) The client establishes a TCP connection to port number 49298. 

95 

Downloaded from www.Manualslib.com manuals search engine 
