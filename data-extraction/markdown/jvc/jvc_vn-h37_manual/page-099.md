- 4) The client continues to send 512 bytes of u-Law data with a 12-byte header.
- 5) To end, disconnect TCP49298.

| 0x00000080                        |
|-----------------------------------|
| Volume of payload (512 for u-Law) |
| Time stamp in 8kHz                |
| u-Law data (512 bytes)            |

## 30.2. Restrictions

## Restrictions on Number of Clients

Only 1 client is allowed to send audio data to the camera. the camera will return an error for this API and TCP will be disconnected when this function is currently in use by another client.

## Timing of Data Sending

512 bytes, or in other words, 64 msec of audio data may be sent during each transmission. Send audio data at intervals as evenly as possible. A part of the data may be lost if audio data exceeding 2 seconds are sent to the camera at one time.

## 31.  Getting SD Card data from the Camera via RTSP/RTP

RTSP of the camera is RFC2326 compliant.

## 31.1. URI

URI for RTSP is

rtsp://ipaddress/PSIA/Streaming/tracks

## 31.2. Playback control

For Playback control, the messages is used as below,

| Control command   | Method        | Header   | Example                       |
|-------------------|---------------|----------|-------------------------------|
| Play              | PLAY          | Range    | Range: clock=20120518T135717Z |
| Pause             | PAUSE         | -        |                               |
| KeepAlive         | GET_PARAMETER | -        |                               |

Specify start time by request header 'Range'.

For keep-alive control, issue the GET\_PARAMETER method in 3 seconds during receiving data.

Keep the message interval is longer than 200 milliseconds.
