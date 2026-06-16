## C O N F I D E N T I A L

## DLE ENQ

[Name]

Send real-time request to printer

[Format]

ASCII

DLE ENQ n

Hex

10 05 n

Decimal

16 5 n

[Range]

TM-J2000/J2100 , TM-T90 , TM-L90 : 0 n 2 TM-T20 , TM-T88IV , TM-T88V : n = 1, 2

≤ ≤

TM-T70 : n = 1, 2 [Other than the following model]

n = 2 [Japanese model]

TM-P60 , TM-U220 : n = 2

TM-U230 : n = 0, 2

[Default]

None

[Printers not featuring this command] None

[Description]

Responds to a request in real time from the host computer, using n as follows:

|   n | Request                                                                                                                                                                                                    |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   0 | Recovers to online status when following online recovery waiting status. In the waiting status for the button to be pressed, the printer operates in the same way as when the FEED button is pressed once. |
|   1 | Recovers from a recoverable error and restarts printing from the line where the error occurred.                                                                                                            |
|   2 | Recovers from a recoverable error after clearing the receive and print buffers.                                                                                                                            |

[Notes]

- ■ This is a real-time command that the printer executes upon receiving it. Note the following when using this command.
- If this command is embedded within the code string of another command, it is processed as a parameter of the other command, and the print result is not correct.
- If another command (such as graphics data or defined data) has a code string in a parameter that is the same as this command, the printer starts processing this command.

EXECUTING COMMAND
