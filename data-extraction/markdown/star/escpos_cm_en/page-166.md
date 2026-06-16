<!-- image -->

Name

Define external character

Code

ASCII

FS 2 c1 c2  d1...dk

Hex.

1C 32 c1 c2  d1...dk

Decimal

28 50 c1 c2  d1...dk

Defined Region

• c1 and c2 differ according to specifications and code type.  See below.

| Specifications                                      | c1     | c2                            |
|-----------------------------------------------------|--------|-------------------------------|
| Japanese Kanji Specifications (JIS code type)       | c1=77H | 21H ≤ c2 ≤ 7EH                |
| Japanese Kanji Specifications (SHIFT-JIS code type) | c1=ECH | 40H ≤ c2 ≤ 7EH 80H ≤ c2 ≤ 9EH |
| Chinese Kanji Specifications                        | c1=FEH | A1H ≤ c2 ≤ FEH                |
| Taiwanese Kanji Specifications                      | c1=FEH | A1H ≤ c2 ≤ FEH                |
| Korean Kanji Specifications                         | c1=FEH | A1H ≤ c2 ≤ FEH                |

- 0 ≤ d ≤ 255
- k = 72

All spaces

Defines the external character pattern of the Chinese character to a character code specified by c1 and c2.

- c1 and c2 indicate the Chinese character code that defines the external character; c1 is the first byte; c2 is the second byte.
- d specifies defined data. Bits that correspond to the dots to print are 1, and the bits that correspond to the dots that are not printed are 0.
- Defined data is cleared by ESC @.
- This command is ignored when the memory switch location of use is specified as SBCS (single byte countries).
- External character registration of JIS codes and SHIFT-JIS codes for Japanese characters uses the same region.

FS C

Initial Value

Function

Details

STAR

Reference
