<!-- image -->

## 6-3 Appendix-3	Blank	Page	Configuration

Blank code pages are code tables that are empty from character code 80H to FFH.  They can be specified using the command below.

- ESC t n (n=255)
- ESC GS t  n (n=255)

Also, it is possible to write data to the blank code page area using the command below.

- ESC GS = . . . . .
1. Example configuration of Font-A data.  (12 x 24 font)

<!-- image -->

<!-- image -->

| MSB   | MSB   | MSB   | MSB   |   LSB | LSB   |   LSB |
|-------|-------|-------|-------|-------|-------|-------|
| d2    |       |       |       |     0 | 0 0   |     0 |
| d4    |       |       |       |     0 | 0 0   |     0 |
| d6    | •     | •     |       |     0 | 0 0   |     0 |
| d8    | •     | •     |       |     0 | 0 0   |     0 |
| d10   |       | •     | •     |     0 | 0 0   |     0 |
| d12   |       | •     | •     |     0 | 0 0   |     0 |
| d14   |       | •     | •     |     0 | 0 0   |     0 |
| d16   |       | •     | •     |     0 | 0 0   |     0 |
| d18   | •     | •     |       |     0 | 0 0   |     0 |
| d20   | •     | •     |       |     0 | 0 0   |     0 |
| d22   | •     |       |       |     0 | 0 0   |     0 |
| d24   |       |       |       |     0 | 0 0   |     0 |
| d26   |       |       |       |     0 | 0 0   |     0 |
| d28   |       |       |       |     0 | 0 0   |     0 |
| d30   |       |       |       |     0 | 0 0   |     0 |
| d32   |       |       |       |     0 | 0 0   |     0 |
| d34   |       |       |       |     0 | 0 0   |     0 |
| d36   |       |       |       |     0 | 0 0   |     0 |
| d38   |       |       |       |     0 | 0 0   |     0 |
| d40   | •     | •     | •     |     0 | 0 0   |     0 |
| d42   | •     | •     | •     |     0 | 0 0   |     0 |
| d44   |       |       |       |     0 | 0 0   |     0 |
| d46   |       |       |       |     0 | 0 0   |     0 |
| d48   |       |       |       |     0 | 0 0   |     0 |
