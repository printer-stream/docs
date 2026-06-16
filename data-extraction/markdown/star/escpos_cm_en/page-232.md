<!-- image -->

## ESC	GS	y	D	2	a	m1	n1L	n1H	d11	d12	·	·	·		d1k	m2	n2L	n2H	d21	d22	·	·	·	d2k	ml	·	·	·	dlk

Name

Set QR code cell size (Manual setting)

Code

ASCII

ESC

GS

y

D

2

a

m1

n1L

n1H

d11

d12

…

d1K

Hex.

1B

1D

79

44

32

a

m1

n1L

n1H

d11

d12

…

d1K

Decimal

27

29

121

68

50

a

m1

n1L

n1H

d11

d12

…

d1K

ASCII

m2

n2L

n2H

D21

d22

…

d2K

ml

…

dl k

Hex.

m2

n2L

n2H

D21

d22

…

d2K

ml

…

dl k

Decimal

m2

n2L

n2H

D11

d22

…

d2K

ml

…

dl k

Defined Area

1 ≤ a ≤ 255

1 ≤ m ≤ 4

0 ≤ nL ≤ 255, 0 ≤ nH ≤ 255

1 ≤ nL + nH x 256 ≤ 7089 (k = nL + nH x 256)

0 ≤ d ≤ 255

1 ≤ I ≤ 255

Initial Value

---

Function

Specifies the bar code data type and sets the data.

- Parameter details

- a: Block count

- m: Input data type

- nL + nH x 256: Bar code data byte count

- dk: Bar code data (Max. 7089 bytes)

|   m | Data Type          | Data Definition Region (d)                                                  |
|-----|--------------------|-----------------------------------------------------------------------------|
|   1 | Numbers            | '0' to '9'                                                                  |
|   2 | English Characters | '', '$', '%' '*', '+', '-' '.' '/', ':', '0' to '9', 'A' to 'Z', 'a' to 'z' |
|   3 | Binary             | 0x00 to 0xFF                                                                |
|   4 | Kanji (Shift JIS)  | 0x8140 to 0x9FFC, 0xE040 to 0xEBBF                                          |
|     |                    | However, the lower 8 bits are 0x40 to 0x7E, and 0x80 to 0xFC                |
