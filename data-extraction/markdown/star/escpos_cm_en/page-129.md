<!-- image -->

Name

Set counter print mode

Code

ASCII

GS C 0 n m

Hex.

1D 43 30 n m

Decimal

29 67 48 n m

Defined Region

0 ≤ n ≤ 5

0 ≤ m ≤ 2, 48 ≤ m ≤ 50

Initial Value

n = 0

m = 0

Function

Sets the serial number counter print mode.

| m     | Printing Position   | Processing of Counter Value Less than Set Digit Count   |
|-------|---------------------|---------------------------------------------------------|
| 0, 48 | Align Right         | Applies a space to the left side                        |
| 1, 49 | Align Right         | Applies a 0 to the left side                            |
| 2, 50 | Align Left          | Applies a space to the right side                       |

## Details

- n specifies the digits to print.
- When n = 0, the printer prints only the actual number of digits of the counter value.
- Sets the print digit count when n ≠ 0.
- m sets the serial number counter printing position in the set digit count.
- If the counter value is larger than the n set digit count, the printer prints n digits below the counter value.

Reference

GS C 1, GS C 2, GSC ;, GS c

&lt;n = 3, m = 0&gt;

&lt;n = 3, m = 1&gt;

&lt;n = 3, m = 2&gt;

ΔΔ1

001

1ΔΔ

Δ=Space
