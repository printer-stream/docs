<!-- image -->

## ESC GS t n

[Name] [Code]

Select code page

ASCII

ESC

GS

t

n

Hex.

1B 1D 74 n

Decimal

27 29 116 n

[Defined Region]

0 ≤ n ≤ 21

32 ≤ n ≤ 34

64 ≤ n ≤ 79

[Initial Value]

Memory switch setting

When installed with Japanese language characters and DBCS setting: Fixed at n=2

[Function]

Specifies code page

When installed with Japanese and Chinese language characters and DBCS setting, this command is ignored.

|   n | Code Page                         |
|-----|-----------------------------------|
|   0 | Normal*                           |
|   1 | CodePage437 (USA, Std. Europe)    |
|   2 | Katakana                          |
|   3 | CodePage437 (USA, Std. Europe)    |
|   4 | Codepage 858 (Multilingual)       |
|   5 | Codepage 852 (Latin-2)            |
|   6 | Codepage 860 (Portuguese)         |
|   7 | Codepage 861 (Icelandic)          |
|   8 | Codepage 863 (Canadian French)    |
|   9 | Codepage 865 (Nordic)             |
|  10 | Codepage 866 (Cyrillic Russian)   |
|  11 | Codepage 855 (Cyrillic Bulgarian) |
|  12 | Codepage 857 (Turkey)             |
|  13 | Codepage 862 (Israel (Hebrew) )   |
|  14 | Codepage 864 (Arabic)             |
|  15 | Codepage 737 (Greek)              |
|  16 | Codepage 851 (Greek)              |
|  17 | Codepage 869 (Greek)              |
|  18 | Codepage 928 (Greek)              |
|  19 | Codepage 772 (Lithuanian)         |
|  20 | Codepage 774 (Lithuanian)         |
|  21 | Codepage 874 (Thai)               |

|   n | Code Page                        |
|-----|----------------------------------|
|  32 | Codepage 1252 (Windows Latin-1)  |
|  33 | Codepage 1250 (Windows Latin-2)  |
|  34 | Codepage 1251 (Windows Cyrillic) |
|  64 | Codepage 3840 (IBM-Russian)      |
|  65 | Codepage 3841 (Gost)             |
|  66 | Codepage 3843 (Polish)           |
|  67 | Codepage 3844 (CS2)              |
|  68 | Codepage 3845 (Hungarian)        |
|  69 | Codepage 3846 (Turkish)          |
|  70 | Codepage 3847 (Brazil-ABNT)      |
|  71 | Codepage 3848 (Brazil-ABICOMP)   |
|  72 | Codepage 1001 (Arabic)           |
|  73 | Codepage 2001 (Lithuanian-KBL)   |
|  74 | Codepage 3001 (Estonian-1)       |
|  75 | Codepage 3002 (Estonian-2)       |
|  76 | Codepage 3011 (Latvian-1)        |
|  77 | Codepage 3012 (Latvian-2)        |
|  78 | Codepage 3021 (Bulgarian)        |
|  79 | Codepage 3041 (Maltese)          |
| 255 | User Setting Blank Code Page     |

-----------------------------------------------------------------------------
