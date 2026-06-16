## Format

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Parameter range

0 ≤ nL ≤ 255

<!-- formula-not-decoded -->

## Function

Prints dot-graphics in 8, 24, or 48-dot columns, depending on the following parameters:

m

Specifies the dot density (see table below)

nL, nH

Specifies the total number of columns of graphics data that follow

(number of dot columns) = ((nH × 256) + nL)

<!-- formula-not-decoded -->

d1 . . . d k Bytes of graphics data; k is determined by multiplying the total number of columns times the number of bytes required for each column (see the table below)
