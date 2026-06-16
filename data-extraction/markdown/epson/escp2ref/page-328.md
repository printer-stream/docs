example 22: Code 128, CD: Host, HRI: none, using Data Character Set B

1B 28 42 10 00

; Barcode command and data length

06

; Barcode type k = Code 128

02

; Module width m = 2 dots / 180 inch

00

; Space adjustment value s = +0 dots / 360 inch

7D 00

; Bar length v1 , v2 = 125 / 180 inch

02

; Control flags c

42 32 33 40 61 42 63

; Barcode Data

44  5B 5D ;

<!-- image -->

example 23: Code 128, CD: Host, HRI: print, using Data Character Set C

1B 28 42 11 00

; Barcode command and data length

06

; Barcode type k = Code 128

02

; Module width m = 2 dots / 180 inch

00

; Space adjustment value s = +0 dots / 360 inch

7D 00

; Bar length v1 , v2 = 125 / 180 inch

00

; Control flags c

43 30 31 32 33 34 35

; Barcode Data

36 37 38 39 ;

123456789.0

<!-- image -->

example 24: Code 128, CD: Host, HRI: print, using Data Character Set C Next  example is of '0' added automatically, in the case of oddnumbered data.

1B 28 42 10 00

; Barcode command and data length

06

; Barcode type k = Code 128

02

; Module width m = 2 dots / 180 inch

00

; Space adjustment value s = +0 dots / 360 inch

7D 00

; Bar length v1 , v2 = 125 / 180 inch

00

; Control flags c

43 31 32 33 34 35

; Barcode Data

36 37 38 39 ;

<!-- image -->
