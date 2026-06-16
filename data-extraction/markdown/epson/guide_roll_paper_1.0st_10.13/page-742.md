## C O N F I D E N T I A L

- ■ (ARP) Reduction ratio of line spacing where extra line feeds are included (when a = 104))
- ■ ( ARP) Reduction ratio of bar code height (when a = 105)
- If the bar code height is less than 30 dots by using this function, the bar code is printed with the height of 30 dots.
- ■ Automatic replacement of Font A (when a = 111)
- ■ Automatic replacement of Font B (when a = 112)
- ■ Print density when printing in multiple tones (when a = 117)

|   ( nL + nH × 256) | Reduction ratio of line spacing where extra line feeds are included   |
|--------------------|-----------------------------------------------------------------------|
|                  0 | None                                                                  |
|                  1 | 25% reduction                                                         |
|                  2 | 50% reduction                                                         |
|                  3 | 75% reduction                                                         |

|   ( nL + nH × 256) | Reduction ratio of bar code height   |
|--------------------|--------------------------------------|
|                  0 | None                                 |
|                  1 | 25% reduction                        |
|                  2 | 50% reduction                        |
|                  3 | 75% reduction                        |

| ( nL + nH × 256)   | Automatic replacement of Font A   |
|--------------------|-----------------------------------|
| 0, 48              | Font A (Same as no replacement)   |
| 1, 49              | Font B                            |
| 97                 | Special font A                    |
| 98                 | Special font B                    |

| ( nL + nH × 256)   | Automatic replacement of Font B   |
|--------------------|-----------------------------------|
| 0, 48              | Font A                            |
| 1, 49              | Font B (Same as no replacement)   |
| 97                 | Special font A                    |
| 98                 | Special font B                    |
