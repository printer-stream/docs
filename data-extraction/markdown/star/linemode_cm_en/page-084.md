<!-- image -->

## ESC ? LF NUL

[Name] [Code]

Reset printer (execute self print)

ASCII

ESC ? LF  NUL

Hex.

1B 3F 0A 00

Decimal

27 63 10 0

[Defined Area]

- - -

[Initial Value]

[Function]

- - -

Hardware resets the printer and executes on self print.

After sending this command, the next data is not sent until the printer is online (in a state wherein it can receive data).

When resetting the printer, the following processes are performed.

| I/F      | Mode          | Process         |
|----------|---------------|-----------------|
| Parallel | - - -         | BUSY output     |
| RS-232C  | DTR mode      | DTR mark output |
|          | Xon/Xoff mode | Xoff output     |

-----------------------------------------------------------------------------
