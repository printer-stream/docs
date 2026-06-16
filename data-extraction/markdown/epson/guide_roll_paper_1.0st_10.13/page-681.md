## C O N F I D E N T I A L

## GS ( C

[Name]

Edit NV user memory

[Printers not featuring this command] TM-T20 , TM-T88IV , TM-T88V , TM-U230

[Description]

Edits the data in the NV user memory.

- Function code fn specifies the function.
- pL , pH specifies ( pL + pH × 256) as the number of bytes after pH ( m , fn , b , [c1 c2] , and [d1...dk] ).
- The other parameters are explained under each of the functions.
- ■ The command function is defined by the function code ( fn ). The command operation differs, depending on the function.
- ■ The NV user memory area is especially provided for storing character data in the non-volatile memory built into the printer.
- ■ The NV user memory data configuration is as follows: key code + data + terminator. This unit is called a record.
- A record is one data processing unit in the NV user memory. It is controlled by a key code.
- The key code is a 2-byte ID code used to identify records and is created with parameters c1 , c2 in the command (Character codes: Hexadecimal = 20H - 7EH/Decimal = 32 - 126.)

| fn    | Function No.   | Function name                                                |
|-------|----------------|--------------------------------------------------------------|
| 0, 48 | Function 0     | Delete the specified record                                  |
| 1, 49 | Function 1     | Store the data in the specified record                       |
| 2, 50 | Function 2     | Transmit the data in the specified record                    |
| 3, 51 | Function 3     | Transmit capacity of the NV user memory currently being used |
| 4, 52 | Function 4     | Transmit the remaining capacity of the NV user memory        |
| 5, 53 | Function 5     | Transmit the key code list                                   |
| 6, 54 | Function 6     | Delete all data in the NV user memory                        |

## [Notes]

EXECUTING + SETTING
