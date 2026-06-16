<!-- image -->

## GS I n

Name

Transmission of Printer ID

Code

ASCII GS I n

Hex.

1D 49 n

Decimal

29 73 n

Defined Region

Spec. A 1 ≤ n ≤ 3, 49 ≤ n ≤ 51, 65 ≤ n ≤ 69

Spec. B

1 ≤ n ≤ 4, 49 ≤ n ≤ 51, 65 ≤ n ≤ 69, 111 ≤ n ≤ 113

Function

Sends the specified printer ID.

Spec. A

| n     | Printer ID Type   | Specifications                     |
|-------|-------------------|------------------------------------|
| 1, 49 | Model ID          | TM-T88II = 0 x 20 BA-T500 = 0 x 27 |
| 2, 50 | Type ID           | (See table below; Type ID)         |
| 3, 51 | ROM Version ID    | Depends on the ROM version         |

## Spec. B

| n     | Printer ID Type             | Specifications                                                                                                            |
|-------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------|
| 1, 49 | Model ID                    | See the models below.                                                                                                     |
| 2, 50 | Type ID                     | (See <Type ID> in the table below.)                                                                                       |
| 3, 51 | ROM version ID              | Depends on the ROM version                                                                                                |
| 65    | Firmware Version            | Depends on the Firmware Version                                                                                           |
| 66    | Manufacturers Name          | STAR                                                                                                                      |
| 67    | Model Name                  | See the models below.                                                                                                     |
| 68    | Serial Number               | '0000000000000000'                                                                                                        |
| 69    | Double bytes Character Type | Japanese Kanji : KANJI JAPANESE Chinese Character : CHINA GB2312 or CHINA GB18030 Taiwan Chinese Character : TAIWAN BIG-5 |

## &lt;Type ID&gt;

|   Bit | Function                              | '0'   | '1'   |
|-------|---------------------------------------|-------|-------|
|     7 | Fixed at '0'                          |       |       |
|     6 | Undefined                             | ---   | ---   |
|     5 | Undefined                             | ---   | ---   |
|     4 | Fixed at '0'                          |       |       |
|     3 | MICR Reader                           | None  | Yes   |
|     2 | Direct connection to customer display | None  | Yes   |
|     1 | Auto-cutter                           | None  | Yes   |
|     0 | 2 Byte Code Handling                  | None  | Yes   |
