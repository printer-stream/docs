## C O N F I D E N T I A L

- When operating with a serial interface, make sure that the host PC is able to receive data before executing this function.
- When operating with a parallel interface, change the host PC to the reverse mode for confirming any responses.
- ■ Offline response is the 'header to NUL' data shown below:
- ■ When transmitting an offline response occurs at the same time that an untransmitted offline response is being stored, the printer transmits the latest offline response only.
- ■ You can get detailed information of offline occurrences by using the combination of ASB status and offline response with offline cause.
- ■ When specifying offline response by this function, execute response confirmation processing on the host PC for the responses from the printer.
- ■ See program example and print sample for ESC i and ESC m for description of response transmission process.

| Send data          | Hex       | Decimal   | Data quantity   |
|--------------------|-----------|-----------|-----------------|
| Header             | 37H       | 55        | 1 byte          |
| Identifier         | 23H       | 35        | 1 byte          |
| Offline cause (*1) | 40H ~ 7FH | 64 ~ 127  | 0 ~ 10 byte     |
| NUL                | 00H       | 0         | 1 byte          |

[Model-dependent variations]

TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-L90 , TM-P60
