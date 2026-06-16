<!-- image -->

## ESC GS y D 1 m nL nH d1 d2 … dk

| [Name]   | Set QR code cell size (Auto Setting)   | Set QR code cell size (Auto Setting)   | Set QR code cell size (Auto Setting)   | Set QR code cell size (Auto Setting)   | Set QR code cell size (Auto Setting)   |   Set QR code cell size (Auto Setting) | Set QR code cell size (Auto Setting)   | Set QR code cell size (Auto Setting)   | Set QR code cell size (Auto Setting)   | Set QR code cell size (Auto Setting)   | Set QR code cell size (Auto Setting)   | Set QR code cell size (Auto Setting)   | Set QR code cell size (Auto Setting)   |
|----------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|----------------------------------------|
| [Code]   | ASCII                                  | ESC                                    | GS                                     | y                                      | D                                      |                                      1 | m                                      | nL                                     | nH                                     | d1                                     | d2                                     | …                                      | dk                                     |
|          | Hex.                                   | 1B                                     | 1D                                     | 79                                     | 44                                     |                                     31 | m                                      | nL                                     | nH                                     | d1                                     | d2                                     | …                                      | dk                                     |
|          | Decimal                                | 27                                     | 29                                     | 121                                    | 68                                     |                                     49 | m                                      | nL                                     | nH                                     | d1                                     | d2                                     | …                                      | dk                                     |

[Defined Area]

[Initial Value] [Function]

m = 0 0 ≤ nL ≤ 255, 0 ≤ nH ≤ 255 1 ≤ nL + nH x 256 ≤ 7089 (k = nL + nH x 256) 0 ≤ d ≤ 255 ---

Automatically expands the data type of the bar code and sets the data.

- Parameter details
- nL + nH x 256: Byte count of bar code data
- dk: Bar code data (Max. 7089 bytes)
- When using this command, the printer receives data for the number of bytes (k) specified by nL and nH.  The data automatically expands to be set as the bar code data.
- Indicates the number bytes of data specified by the nL and nH.

Bar code data is cleared at this time.

- The data storage region of this command is shared with the manual setting command so data is updated each time either command is executed.

-----------------------------------------------------------------------------
