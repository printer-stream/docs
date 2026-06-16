<!-- image -->

ESC GS y D 2 a m1 n1L n1H d11 d12 · · ·  d1k m2 n2L n2H d21 d22 · · · d2k ml · · · dlk

| [Name]   | Set QR code cell size (Manual setting)   | Set QR code cell size (Manual setting)   | Set QR code cell size (Manual setting)   | Set QR code cell size (Manual setting)   | Set QR code cell size (Manual setting)   | Set QR code cell size (Manual setting)   | Set QR code cell size (Manual setting)   | Set QR code cell size (Manual setting)   | Set QR code cell size (Manual setting)   | Set QR code cell size (Manual setting)   | Set QR code cell size (Manual setting)   | Set QR code cell size (Manual setting)   | Set QR code cell size (Manual setting)   | Set QR code cell size (Manual setting)   |
|----------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|
| [Code]   | ASCII                                    | ESC                                      | GS                                       | y                                        | D                                        | 2                                        | a                                        | m1                                       | n1L                                      | n1H                                      | d11                                      | d12                                      | …                                        | d1K                                      |
|          | Hex.                                     | 1B                                       | 1D                                       | 79                                       | 44                                       | 32                                       | a                                        | m1                                       | n1L                                      | n1H                                      | d11                                      | d12                                      | …                                        | d1K                                      |
|          | Decimal                                  | 27                                       | 29                                       | 121                                      | 68                                       | 50                                       | a                                        | m1                                       | n1L                                      | n1H                                      | d11                                      | d12                                      | …                                        | d1K                                      |
|          | ASCII                                    | m2                                       | n2L                                      | n2H                                      | D21                                      | d22                                      | …                                        | d2K                                      | ml                                       | …                                        | dkl                                      |                                          |                                          |                                          |
|          | Hex.                                     | m2                                       | n2L                                      | n2H                                      | D21                                      | d22                                      | …                                        | d2K                                      | ml                                       | …                                        | dkl                                      |                                          |                                          |                                          |
|          | Decimal                                  | m2                                       | n2L                                      | n2H                                      | D11                                      | d22                                      | …                                        | d2K                                      | ml                                       | …                                        | dkl                                      |                                          |                                          |                                          |

## [Defined Area]

## [Initial Value] [Function]

1 ≤ a ≤ 255

1 ≤ m ≤ 4

0 ≤ nL ≤ 255, 0 ≤ nH ≤ 255

1 ≤ nL + nH x 256 ≤ 7089 (k = nL + nH x 256)

0 ≤ d ≤ 255

1 ≤ I ≤ 255

---

Specifies the bar code data type and sets the data.

- Parameter details
- a: Block count
- m: Input data type
- nL + nH x 256: Bar code data byte count
- dk: Bar code data (Max. 7089 bytes)
-  The  printer  receives  the  data  type  specified  by  m,  and  the  data  of  the  number  of  bytes  (k) specified by nL and nH, based on the block count specified by a.
- 1 block specified by a indicates m1, n1L, n1H, d11 · · · d1k (data type + data count + bar code data), and by continuously sending these a multiple of times, one bar code data can mix data types.
- It is possible to set a maximum of 255 blocks with one command transmission.
- nL and nH specify the number of bytes of the data, so when using Kanji, calculate that 1 character has 2 bytes.
-  If  this  command  is  outside  of  the  definition  region,  immediately  stop  the  command  analysis process.

|   m | Data Type          | Data Definition Region (d)                                       |
|-----|--------------------|------------------------------------------------------------------|
|   1 | Numbers            | '0' to '9'                                                       |
|   2 | English Characters | '', '$', '%' '*', '+', '-' '.' '/', ':', '0' to '9', 'A' to 'Z', |
|   3 | Binary             | 0x00 to 0xFF                                                     |
|   4 | Kanji (Shift JIS)  | 0x8140 to 0x9FFC, 0xE040 to 0xEBBF                               |
|     |                    | However, the lower 8 bits are 0x40 to 0x7E, and 0x80 to 0xFC     |

When doing so, the bar code data is cleared.

- This command data storage region is shared with the automatic setting command, so data is updated each time either command is executed.

-----------------------------------------------------------------------------
