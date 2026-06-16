## C O N F I D E N T I A L

## GS ( H

[Name]

Request transmission of response or status

[Printers not featuring this command] TM-J2000/J2100 , TM-U230 , TM-U220

[Description]

## [Notes]

Various process are performed as the response.

- pL , pH specifies ( pL + pH × 256) as the number of bytes after pH ( fn and m ).
- Function code fn specifies the type of response control.
- ■ Do not use this command in a system in which the printer is used with the OPOS driver and Java POS driver that are provided by Seiko Epson Corporation.
- ■ The function of this command is defined by function code fn and the operation differs depending on the function selected.
- ■ 'Response' is a data block to inform the host of the processing status. There are three kinds of 'Response' as shown in the following table. Untransmitted multi-kind responses are stored in the printer and transmitted in the order of priority shown in the following table, ignoring the order of occurrence.

|   fn | Function    |                                    |
|------|-------------|------------------------------------|
|   48 | Function 48 | Specifies the process ID response. |
|   49 | Function 49 | Specifies the offline response.    |

| Kind of Response    | Related Command               |   Priority |
|---------------------|-------------------------------|------------|
| Process ID response | <Function 48> of this command |          1 |
| Offline response    | <Function 49> of this command |          2 |
| Clear response 25   | DLE DC4 ( fn = 8)             |          3 |

EXECUTING COMMAND
