<!-- image -->

Name

Specify Kanji mode

Code

ASCII

FS &amp;

Hex.

1C 26

Decimal

28 38

Function

Specifies Kanji mode.

Details

- &lt; Japanese Kanji Specifications &gt;

- Kanji mode specification using this command is enabled only when using JIS codes.
- If the Kanji mode is specified, all character codes are handled as 2 byte Chinese character codes.
- Kanji codes are processed in the order first byte, second byte.
- Kanji mode is cancelled as the default setting.
- It is possible to select the Kanji code type using FS C.
- &lt; Chinese Kanji Specifications/ Taiwanese Kanji Specifications/ Korean Kanji Specifications&gt;
- If Kanji mode is specified, the first byte that follows processing of the character code equivalent to the first byte of the Kanji code is processed as the second byte of the Kanji code.
- Kanji codes are processed in the order first byte, second byte.
- Kanji mode is specified as the default setting.
- This command is ignored when the memory switch location of use is specified as SBCS (single byte countries).
- ANK adornment commands are possible for Kanji enhancement (ESC E) and black/white inversion (GS B)  However, if the Kanji is enlarged over three times, enhancement is ignored.
- The following shows the 2 byte code defined area.

Specifications A:

Enhancement of Kanji is ignored for those characters rotated 90 degrees to the right (ESC V) .

Specifications B:

Enhancement of Kanji is effective for those characters rotated 90 degrees to the right (ESC V).

| Specifications                           | Defined Area              | Defined Area   |
|------------------------------------------|---------------------------|----------------|
|                                          | Upper Bytes               | Lower Bytes    |
| Japanese Kanji Characters JIS Type       | 0x21 to 0x7E              | 0x21 to 0x7E   |
| Japanese Kanji Characters/Shift JIS Type | 0x81 to 0x9F 0xE0 to 0xEF | 0x40 to 0xFE   |
| Chinese Kanji characters                 | 0xA1 to 0xFD              | 0xA1 to FE (*) |
| Taiwanese Kanji characters               | 0xA1 to 0xFD              | 0x40 to FE     |
| Korean Kanji characters                  | 0xA1 to 0xFD              | 0xA1 to FE     |

(*) Bit - 7 of the lower bytes of the Chinese Kanji is always processed as MASK (0xA1A1 → 0xA121)

Reference

FS., FS C

STAR
