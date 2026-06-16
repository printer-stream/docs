## C O N F I D E N T I A L

## [Notes]

- ■ This function works both in user setting mode and during normal printer operation.
- ■ The printer transmits the data below ('Header to NUL') with this function:

| Transmit data     | Hex       | Decimal   | Data quantity   |
|-------------------|-----------|-----------|-----------------|
| Header            | 37H       | 55        | 1 byte          |
| Identifier        | 27H       | 39        | 1 byte          |
| Value number (*1) | 31H - 39H | 48 - 57   | 1 - 3 bytes     |
| Separation code   | 1FH       | 31        | 1 byte          |
| Setting (*2)      | 30H - 39H | 48 - 57   | 1 - 5 bytes     |
| NUL               | 00H       | 0         | 1 byte          |

## Example:

If the a is 118, the '118' (expressed hexadecimally as 31H, 31H, 38H. Decimally as 49, 49, 56) is converted to 3bytes data.

(*2)  The customized value is determined by the value defined in Function 5.

## Example:

When the customized value is 120, it is '120' expressed with 3 bytes of data (hex numbers: 31H, 32H, 30H / decimal numbers: 49, 50, 48).

- ■ Even if the combination of settings requested in Function 5 is not possible, the printer transmits the settings made with Function 5. Note that this will differ from the memory capacity used during actual operation. The capacity of memory In fact can be checked by the following commands.
- Capacity or unused capacity of NV user memory: GS ( C &lt;Function 3&gt;, &lt;Function 4&gt;
- Capacity or unused capacity of NV graphics domain: GS ( L &lt;Function 48&gt;, &lt;Function 51&gt;
- ■ See previous [Notes for transmission process] for process sending data group.

[Model-dependent variations]

TM-T90 , TM-T88IV , TM-L90 , TM-P60
