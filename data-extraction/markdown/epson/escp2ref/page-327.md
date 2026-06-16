## example 19: Code 39, CD: Printer, HRI: none

1B 28 42 0D 00

; Barcode command and data length

05

; Barcode type k = Code 39

02

; Module width m = 2 dots / 180 inch

00

; Space adjustment value s = +0 dots / 360 inch

7D 00

; Bar length v1 , v2 = 125 / 180 inch

03

; Control flags c

31 32 41 42 24 25 2E

; Barcode Data

<!-- image -->

example 20: Code 128, CD: Printer, HRI: print, using Data Character Set A

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

01

; Control flags c

41 32 33 40 41 21 43

; Barcode Data

44 5B 5D ;

<!-- image -->

example 21: Code 128, CD: Printer, HRI: print, using Data Character Set B

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

01

; Control flags c

42 32 33 40 61 42 63

; Barcode Data

44  5B 5D ;

<!-- image -->

23aaBedCi1a
