| ESC/P 2   | ESC/P   | 9-Pin ESC/P   |
|-----------|---------|---------------|

Barcode print is available on DLQ-3000('96-), LQ-670, LQ-2070, LQ-2170, FX-2170 and later impact dot matrix models.

The ESC ( B command is used to print barcodes. The format of this command is as follows:

ESC ( B nL nH k m s v1 v2 c BarCodeData

nL nH

Specify the number of data bytes to follow, determined by the following equation:

(number of data bytes) = 6 bytes + BarCodeData bytes = ((nH × 256) + nL)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The parameter k specifies the barcode type.

|   k (Hex) | Bar code type    |
|-----------|------------------|
|        00 | EAN-13           |
|        01 | EAN-8            |
|        02 | Interleaved 2 of |
|        03 | UPC-A            |
|        04 | UPC-E            |
|        05 | Code 39          |
|        06 | Code 128         |
|        07 | POSTNET          |

The parameter

m

specifies the module width.

| m            | 24-pin printer (unit 1/180 inch)   | 9-pin printer (unit 1/120   |
|--------------|------------------------------------|-----------------------------|
| 02 (default) | 2 dots                             | 2 dots                      |
| 03           | 3 dots                             | 3 dots                      |
| 04           | 4 dots                             | 4 dots                      |
| 05           | 5 dots                             | 5 dots                      |

The parameter s specifies the space adjustment value.

| 24-pin printer   | -3 ≤ s ≤ 3 (unit 1/360 inch)   |
|------------------|--------------------------------|
| 9-pin printer    | -3 ≤ s ≤ 3 (unit 1/240 inch)   |

## The parameter v1 and v2 specifies the bar length.

| 24-pin printer   | bar length = v 1 + v 2 × 256 (unit 1/180   |
|------------------|--------------------------------------------|
| 9-pin printer    | bar length = v 1 + v 2 × 256 (unit 1/72    |

The limitation of bar length:

45/180 inch ≤ bar length ≤ 22 inch

: 24-pin printer

18/72 inch ≤ bar length ≤ 22 inch

:   9-pin printer

The v1 and v2 values are ignored when POSTNET is selected.

Long bar length of POSTNET is always 0.125 inch.

Short bar length of POSTNET is always 0.050 inch.
