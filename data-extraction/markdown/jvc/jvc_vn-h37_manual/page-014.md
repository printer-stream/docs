Example:  When width=640, the 13-byte area will be written as follows.

| w   | i   | d   | t   | h   | =   | 6   | 4   | 0   | 0x00   | 0x00   |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|--------|--------|

## 3.  JVC Protocol: H.264 Streaming

## 3.1. Basic Procedures

- 1) The client establishes a TCP connection to port number 80.
- 2) The client sends out API.

Example to get H.264 high profile stream encoded by first channel of  the camera

GET /api/video?encode=h264(1) HTTP/1.1&lt;CRLF&gt;

Host: 192.168.0.2&lt;CRLF&gt;&lt;CRLF&gt;

Note &lt;CRLF&gt; denotes the line feed code (0x0D, 0x0A).

- 3) The camera returns HTTP response and H.264 stream.

HTTP Response and H.264 stream sent out by the camera are as follows.

| HTTP Response                     |
|-----------------------------------|
| I Picture of H.264 (First Frame)  |
| P Picture of H.264 (Second Frame) |
| ,,,                               |

- 4) When the client wants to stop current H.264 transmission, the client disconnects TCP80.

The camera does not accept further API via current TCP that is used for H.264 transmission. To change parameter, disconnect current TCP to stop the H.264 transmission, connect new TCP, and send API with new parameter.

## 3.2. API Format

## Structure

| GET   | space   | API   | space   | HTTP/1.1   | 0x0D 0x0A   |
|-------|---------|-------|---------|------------|-------------|
