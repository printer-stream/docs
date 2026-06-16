<!-- image -->

- 2) Transmission Format Status Data

Status type

+

Separator character 1

1. Status Type (2byte or 4Byte)
- First and Second Bytes

Indicate the cause to generate a printer status.

- '00'    Reserved
- '01' to '09' Reserved
- '10' to '49'

Status Original Status Request Command

- '50'

ESC/POS ASB

- '51' to '59' ESC/POS Real-time Status Request Command
- '60' to 'A0' ESC/POS Status Request Command
- 'A1' ESC/POS [Header to NUL ] Block Status Request Command
- 'A2' to 'FF'  Reserved
- Third and Fourth Bytes

When a cause occurs, these indicate the command n parameter.

If there is no n parameter, the third and fourth bytes can be omitted.

&lt;Ex.&gt; When n = 0x31 using the ESC SYN 3 n command, the third and fourth bytes are '31.'

- 2 Separator character 1 (1 byte)

Sends ':'

- 3 Data Type (1byte)

Indicates printer status data; sends 'B' (binary type).

- 4 Status Length (2 bytes)

2 byte value indicating printer status byte count.

- 5 Printer Status (Variable length)

Status sent by printer.

Status differs according to the cause.

See the command causes and automatic status for details on the content of statuses.

- 6 Separator character 2 (1 byte)

Sends ';'

+

Data type

+

Status length

+

Printer status

+

Separator character 2
