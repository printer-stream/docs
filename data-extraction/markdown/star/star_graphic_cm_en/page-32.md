<!-- image -->

Rev. 2.31

## b n1 n2 data

| [Name]   | Transfer of raster data (automatic line feed)   | Transfer of raster data (automatic line feed)   | Transfer of raster data (automatic line feed)   | Transfer of raster data (automatic line feed)   | Transfer of raster data (automatic line feed)   | Transfer of raster data (automatic line feed)   | Transfer of raster data (automatic line feed)   | Transfer of raster data (automatic line feed)   |
|----------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|
| [Code]   | ASCII                                           | b                                               | n1                                              | n2                                              | d1                                              | d2                                              | ...                                             | dk                                              |
|          | Hex                                             | 62                                              | n1                                              | n2                                              | d1                                              | d2                                              | ...                                             | dk                                              |
|          | Decimal                                         | 98                                              | n1                                              | n2                                              | d1                                              | d2                                              | ...                                             | dk                                              |

[Defined Area]  0 ≦ n1 ≦ 255

0 ≦ n2 ≦ 255

0 ≦ d ≦ 255

k = n1 ＋ n2 x 256

1 ≦ k

---

Transfers the raster data.

Raster data is send at (n1 + n2 x 256) bytes binary data.

Raster data beyond the print area that is currently set is cut off.

The deployed position of the image buffer, after deploying the data to one dot column image buffer by this command, will one dot column automatic line feed, and move to the left margin of the next line position.

If it goes over page due to automatic line feed

- ・ Page length settings are in continuous print mode, if it exceeds the maximum page length (see ESC * r P n NUL command)
- ・ Page length set in the specified page length mode, and if it exceeds the specified page length, and print the data up to the end page, to process as the first line of data for the next page.

In addition, data expansion is performed by overwriting processing (OR processing) the current image buffer data.

For the set raster print color, the deployment image buffer is described below.

| Print color   | Deployment image buffer   |
|---------------|---------------------------|
| Black         | Black image buffer        |
| Cyan          | Colored image buffer      |
| Magenta       | Colored image buffer      |
| Yellow        | Colored image buffer      |

--------------------------------------------------------------------------------------

## [Initial Value] [Function]
