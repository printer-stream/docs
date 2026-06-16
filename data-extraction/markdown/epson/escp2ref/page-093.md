## Format

The format for this command depends on whether you are defining draft characters or NLQ characters.

## Draft:

| ASCII   | ESC   |   & |   NUL | n   | m   | [a   | d 1   | d 2   | . . .   | d k   |
|---------|-------|-----|-------|-----|-----|------|-------|-------|---------|-------|
| Hex     | 1B    |  26 |    00 | n   | m   | [a   | d 1   | d 2   | . . .   | d k ] |
| Decimal | 27    |  38 |     0 | n   | m   | [a   | d 1   | d 2   | . . .   | d k ] |

## NLQ:

| ASCII   | ESC   |   & |   NUL | n   | m   |   0 | [a   |   0 | d 1   | d 2   | . . .   | d k ]   |
|---------|-------|-----|-------|-----|-----|-----|------|-----|-------|-------|---------|---------|
| Hex     | 1B    |  26 |    00 | n   | m   |   0 | [a   |   0 | d 1   | d 2   | . . .   | d k ]   |
| Decimal | 27    |  38 |     0 | n   | m   |   0 | [a   |   0 | d 1   | d 2   | . . .   | d k ]   |

## Parameter range

| Draft (FX):   | Draft (LX):   |
|---------------|---------------|
| 0 ≤ a ≤ 255   | 0 ≤ a ≤ 255   |
| 0 ≤ m ≤ 255   | 58 ≤ m ≤ 63   |
| 0 ≤ n ≤ 255   | 58 ≤ n ≤ 63   |
| m ≤ n         | m ≤ n         |
| 0 ≤ d ≤ 255   | 0 ≤ d ≤ 255   |

## NLQ:

0 ≤ a ≤ 12

58 ≤ m ≤ 63

58 ≤ n ≤ 63

m ≤ n

0 ≤ d ≤ 255

## Function

Sets the parameters for user-defined characters and then sends the data for those characters, as described below:

n

Character code of the first character to be user-defined

| m           | Character code of the last character to be user-defined   |
|-------------|-----------------------------------------------------------|
| a           | Sets parameters for characters to be user-defined         |
| d 1 . . . d | Character data                                            |
