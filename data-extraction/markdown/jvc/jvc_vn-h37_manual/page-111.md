- Set unique Multicast address and port number to each Multicast stream if multiple multicast streams are required in the system.
- Reload of ActiveX control is required to change Multicast property.

## 35.  PSIA

- PSIA Account

Default User Name: psia

Default Password: jvc

- RTSP URI See Chapter 4.

## 36.  FAQ

- (1) Low Frame rate due to long delay of network
- Causes of Low Frame Rate

During transmission via TCP, the camera sends out the following data by receiving the Ack of TCP. When network delay is long, reception of Ack will be delayed and sending rate will drop. This therefore leads to a drop in the frame rate.

- Countermeasure

This problem can be avoided by receiving via multicast. Multicast uses UDP and Ack does not exist. As such, the sender will be able to continue sending without being affected by network delays.
