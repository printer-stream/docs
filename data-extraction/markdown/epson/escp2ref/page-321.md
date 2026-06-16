## Examples:

example 1: EAN-13, CD: Host, HRI: print, Flag Char.: center

(CD: Check digit, HRI: Human Readable character)

1B 28 42 13 00

; Barcode command and data length

00

; Barcode type k = EAN-13

02

; Module width m = 2 dots / 180 inch

00

; Space adjustment value s = +0 dots / 360 inch

7D 00

; Bar length v1 , v2 = 125 / 180 inch

00

; Control flags c

30 31 32 33 34 35 36

; Barcode Data

37 38 39 30 31 32 ;

<!-- image -->

example 2: EAN-13, CD: Printer, HRI: print, Flag Char.: under

1B 28 42 12 00

; Barcode command and data length

00

; Barcode type k = EAN-13

02

; Module width m = 2 dots / 180 inch

00

; Space adjustment value s = +0 dots / 360 inch

7D 00

; Bar length v1 , v2 = 125 / 180 inch

05

; Control flags c

31 32 33 34 35 36

; Barcode Data

37 38 39 30 31 32

<!-- image -->

example 3: EAN-13, CD: Printer, HRI: none, Flag Char.: under

1B 28 42 12 00

; Barcode command and data length

00

; Barcode type k = EAN-13

02

; Module width m = 2 dots / 180 inch

00

; Space adjustment value s = +0 dots / 360 inch

7D 00

; Bar length v1 , v2 = 125 / 180 inch

03

; Control flags c

31 32 33 34 35 36

; Barcode Data

37 38 39 30 31 32

<!-- image -->
