Vertical

24 Dots

<!-- image -->

3.3.7. Do wnload

## ESC &amp; c1 c2 n d1…d48

| [Name]   | Register 12 x 24 dot font download characters   | Register 12 x 24 dot font download characters   | Register 12 x 24 dot font download characters   | Register 12 x 24 dot font download characters   | Register 12 x 24 dot font download characters   | Register 12 x 24 dot font download characters   | Register 12 x 24 dot font download characters   | Register 12 x 24 dot font download characters   |
|----------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|
| [Code]   | ASCII                                           | ESC                                             | &                                               | c1                                              | c2                                              | n d1                                            | ...                                             | d48                                             |
|          | Hex.                                            | 1B                                              | 26                                              | c1                                              | c2                                              | n d1                                            | ...                                             | d48                                             |
|          | Decimal                                         | 27                                              | 38                                              | c1                                              | c2                                              | n d1                                            | ...                                             | d48                                             |

[Defined Area]

[Initial Value] [Function]

c1 = 1, 49

c2 = 1, 49

32 ≤ n ≤ 127

0 ≤ d ≤ 255

- - -

Registers 12 x 24 dot font download characters to the nth address.

Download characters can be registered to &lt;20&gt;H to &lt;7F&gt;H.

If one has been already registered to an address, it is overwritten.

When parameters c1 and c2 and n are outside of the defined area, subsequent data is handled as normal data.

Horizontal 12 Dots

| d1 ●   | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d2   | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
|--------|-----|-----|-----|-----|-----|-----|-----|------|-----|-----|-----|-----|-------|-----|-----|
| d3 ●   | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d4   | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d5 ●   | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d6   | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d7 ●   | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d8   | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d9 ●   | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d10  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d11 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d12  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d13 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d14  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d15 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d16  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d17 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d18  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d19 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d20  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d21 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d22  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d23 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d24  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d25 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d26  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d27 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d28  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d29 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d30  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d31 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d32  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d33 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d34  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d35 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d36  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d37 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d38  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d39 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d40  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d41 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d42  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d43 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d44  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d45 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d46  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |
| d47 ●  | ●   | ●   | ●   | ●   | ●   | ●   | ●   | d48  | ●   | ●   | ●   | ●   | ○ ○   | ○   | ○   |

bit7

bit6

bit5

bit4

bit3

● : Font data

○ : Invalid data

-----------------------------------------------------------------------------

bit2

bit1

Bit0

bit7 bit6 bit5 bit4 bit3 bit2 bit1 bit0
