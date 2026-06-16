## C O N F I D E N T I A L

(*1)  Response code

| ASCII   |   Hex |   Decimal | Request                      |
|---------|-------|-----------|------------------------------|
| ACK     |    06 |         6 | Send next data.              |
| NAK     |    15 |        21 | Resend previously sent data. |
| CAN     |    18 |        24 | Cancel send process.         |

- (*2)  Processing according to response (unsent data exists, identified by send data set 'Identification status')
- ■ Processing the codes except for ACK, NAK, and CAN performs the same processing as CAN .

| Response code   | Process                              |
|-----------------|--------------------------------------|
| ACK             | Start send processing for next data. |
| NAK             | Resend previously sent data.         |
| CAN             | End processing for this command.     |

(*3)  Processing according to response (no unsent data, identified by send data set 'Identification status')

| Response code   | Process                          |
|-----------------|----------------------------------|
| ACK, CAN        | End processing for this command. |
| NAK             | Resend previously sent data.     |
