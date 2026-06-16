<!-- image -->

## 1-2-4 Data	Reception	Timing	(Compatibility	Mode)

<!-- image -->

(*1) Memory Switch Setting: ACK Pulse Width

|                          |         | Standards        | Standards    |
|--------------------------|---------|------------------|--------------|
|                          |         | Minimum [ns]     | Maximum [ns] |
| Data Hold Time (host)    | tHold-1 | -                | 500          |
| Data Hold Time (printer) | tHold-2 | -                | -            |
| Data Setup Time          | tSetup  | -                | 500          |
| STROBE Pulse Width       | tSTB    | -                | 500          |
| READY Cycle Idle Time    | tReady  | -                | -            |
| BUSY Output Delay Time   | tBUSY   | 0                | 500          |
| Data Processing Time     | tReply  | 0                | ∞            |
| ACKNLG Pulse Width       | tACK    | 1usec/9usec (*1) | -            |
| BUSY Cancel Time         | tnBUSY  | 0                | ∞            |
| ACK Cycle Idle Time      | tNext   | -                | 0            |

ON    = 9usec

OFF = 1usec (Default)
