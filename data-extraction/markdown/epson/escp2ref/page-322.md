## example 4: EAN-8, CD: Host, HRI: print

1B 28 42 0E 00

; Barcode command and data length

01

; Barcode type k = EAN-8

02

; Module width m = 2 dots / 180 inch

00

; Space adjustment value s = +0 dots / 360 inch

7D 00

; Bar length v1 , v2 = 125 / 180 inch

00

; Control flags c

30 31 32 33 34 35 36 35

; Barcode Data

<!-- image -->

example 5: EAN-8, CD: Printer, HRI: none

1B 28 42 0D 00

; Barcode command and data length

01

; Barcode type k = EAN-8

02

; Module width m = 2 dots / 180 inch

00

; Space adjustment value s = +0 dots / 360 inch

7D 00

; Bar length v1 , v2 = 125 / 180 inch

03

; Control flags c

30 31 32 33 34 35 36

; Barcode Data

<!-- image -->

## example 6: Interleaved 2 of 5, CD: Host, HRI: print

1B 28 42 1A 00

; Barcode command and data length

02

; Barcode type k = Interleaved 2 of 5

02

; Module width m = 2 dots / 180 inch

00

; Space adjustment value s = +0 dots / 360 inch

7D 00

; Bar length v1 , v2 = 125 / 180 inch

00

; Control flags c

31 32 33 34 35 36 37

; Barcode Data

38 39 30 31 32 33 34 ;

35 36 37 38 39 30 ;

<!-- image -->
