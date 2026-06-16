<!-- image -->

## 1.2.  Parallel Interfaces (Amphenol 36 pins)

## 1.2.1. Specifications (Conforming to IEEE1284)

Rating:

Conforms to IEEE 1284

Mode:

Compatibility Mode/Nibble Mode/Byte Mode

Data transfer speed: 1000 to 6000 CPS

Synch method:

According to externally supplied strobe pulse

Handshake:

According to ACK and BUSY signals

Logic level:

Compatible to TTL

## 1.2.2. Signal array and explanations according to interface connector pin

## &lt;Signal Array and Functions&gt;

| Pin No.   | Compatibility Mode Signal Name   | Nibble Mode Signal Name   | Byte Mode Signal Name   |
|-----------|----------------------------------|---------------------------|-------------------------|
| 1         | nStrobe                          | HostClk                   | HostClk                 |
| 2 to 9    | Data0 to 7                       | Data0 to 7                | Data0 to 7              |
| 10        | nAck                             | PtrClk                    | PtrClk                  |
| 11        | Busy                             | PtrBusy/Data3,7           | PtrBusy                 |
| 12        | PError                           | AckDataReq/Data2,6        | AckDataReq              |
| 13        | Select                           | Xflag/Data1,5             | Xflag                   |
| 14        | N/C                              | HostBusy                  | HostBusy                |
| 15        | N/C                              | -                         | -                       |
| 16        | Signal GND                       | Signal GND                | Signal GND              |
| 17        | Frame GND                        | Frame GND                 | Frame GND               |
| 18        | +5V                              | +5V                       | +5V                     |
| 19 to 30  | Twisted Pair Return              | Twisted Pair Return       | Twisted Pair Return     |
| 31        | nInit                            | nInit                     | nInit                   |
| 32        | nFault                           | nDataAvail/Data0,4        | nDataAvail              |
| 33        | External GND                     | -                         | -                       |
| 34        | N/C                              | -                         | -                       |
| 35        | N/C                              | -                         | -                       |
| 36        | nSelectIn                        | 1284Active                | 1284Active              |

-----------------------------------------------------------------------------
