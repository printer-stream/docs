## C O N F I D E N T I A L

| Transmit data          | Hex       | Decimal   | Data        |
|------------------------|-----------|-----------|-------------|
| Vertical layout (sc)   | 30H ~ 39H | 48 ~ 57   | 0 ~ 5 bytes |
| Separator              | 1FH       | 31        | 1 byte      |
| Vertical layout (sd)   | 30H ~ 39H | 48 ~ 57   | 0 ~ 5 bytes |
| Separator              | 1FH       | 31        | 1 byte      |
| Vertical layout (se)   | 30H ~ 39H | 48 ~ 57   | 0 ~ 5 bytes |
| Separator              | 1FH       | 31        | 1 byte      |
| Vertical layout (sf)   | 30H ~ 39H | 48 ~ 57   | 0 ~ 5 bytes |
| Separator              | 1FH       | 31        | 1 byte      |
| Horizontal layout (sg) | 30H ~ 39H | 48 ~ 57   | 0 ~ 5 bytes |
| Separator              | 1FH       | 31        | 1 byte      |
| Horizontal layout (sh) | 30H ~ 39H | 48 ~ 57   | 0 ~ 5 bytes |
| Separator              | 1FH       | 31        | 1 byte      |
| NUL                    | 00H       | 0         | 1 byte      |

(*1) 'Type of information' transmits the value n converted into character data expressed by decimal numbers from the high order end. Example: When the setting of 'Type of information' is ( n = 64), it is 2-byte data of '64' [Hexadecimal = 36H, 34H/Decimal = 54, 52]. When the setting of 'Type of information' is ( n = 80), it is 2-byte data of '80' [Hexadecimal = 38H, 30H/Decimal = 56, 48].

(*2) 'Layout information' is transmitted sequentially, converting the character data into decimal data.

Example: When 'Layout basis' is '64,' it is 2-byte of  '64' [Hexadecimal = 36H, 34H/Decimal = 54, 52]

|                           | Transmit data   | Transmit data   | Transmit data   |
|---------------------------|-----------------|-----------------|-----------------|
| Type of information ( n ) | Hex             | Decimal         | Data            |
| Setting value ( n = 64)   | 36H, 34H        | 54, 52          | 2 bytes         |
| Effect value ( n = 80)    | 38H, 30H        | 56, 48          | 2 bytes         |

■ Setting value ( n = 64) is specified as the type of information, transmit data are as follows:
