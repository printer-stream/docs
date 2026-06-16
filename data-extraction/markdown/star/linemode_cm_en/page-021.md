<!-- image -->

## 3.3.  Standard Command Details

## 3.3.1. Font style and Character Set

## ESC RS F n

[Name]

Select font

[Code]

ASCII

ESC RS F n

Hex.

1B 1E 46 n

Decimal

27 30 70 n

[Defined Region]

0 ≤ n ≤ 1, n = 16

[Initial Value]

n = 0

[Function]

Selects a font

|   n | Font                  |
|-----|-----------------------|
|   0 | Font-A (12 x 24 dots) |
|   1 | Font-B (9 x 24 dots)  |
|  16 | OCR-B (16 x 24 dots)  |

The following functions are disabled when OCR-B font is selected.

- Code page
- Blank code page
- International characters
- Slash zero

When using OCR-B font to read characters via a scanning operation, adornment, expansion and external characters are canceled.

OCR-B font should be checked by actually trying it first before use.

-----------------------------------------------------------------------------
