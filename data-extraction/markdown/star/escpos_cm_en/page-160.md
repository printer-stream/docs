<!-- image -->

## GS w n

Name

Set bar code horizontal size

Code

ASCII

GS w n

Hex.

1D 77 n

Decimal

29 119 n

Defined Region

1 ≤ n ≤ 6

Initial Value

n = 3

Function

Sets the bar code horizontal size.

|    | Multi-level Bar Code Module Width [mm]   | Binary Level Bar Code   | Binary Level Bar Code    |
|----|------------------------------------------|-------------------------|--------------------------|
| n  | Multi-level Bar Code Module Width [mm]   | Fine Element Width [mm] | Thick Element Width [mm] |
| 1  | 0.141                                    | 0.141                   | 0.423                    |
| 2  | 0.282                                    | 0.282                   | 0.706                    |
| 3  | 0.423                                    | 0.423                   | 1.129                    |
| 4  | 0.564                                    | 0.564                   | 1.411                    |
| 5  | 0.706                                    | 0.706                   | 1.834                    |
| 6  | 0.847                                    | 0.847                   | 2.258                    |

## Details

- Multi-level bar codes specify the follow bar code types. UPC-A, UPC-E, JAN13 (EAN13), JAN8 (EAN8), CODE 93, CODE 128

- Binary level bar codes specify the follow bar code types.

- CODE39, ITF, CODABAR

## STAR

- The bar codes that are printed do not conform to each standard, so you should confirm before actual use.

Particularly, if n = 1 is specified, the bar code is not guaranteed.

- The following are the module widths on STAR printers.

|    | Multi-level Bar Code Module Width [mm]   | Binary Level Bar Code   | Binary Level Bar Code    |
|----|------------------------------------------|-------------------------|--------------------------|
| n  | Multi-level Bar Code Module Width [mm]   | Fine Element Width [mm] | Thick Element Width [mm] |
| 1  | 0125                                     | 0.125                   | 0.375                    |
| 2  | 0.25                                     | 0.25                    | 0.625                    |
| 3  | 0.375                                    | 0.375                   | 1.125                    |
| 4  | 0.5                                      | 0.5                     | 1.375                    |
| 5  | 0.625                                    | 0.625                   | 1.75                     |
| 6  | 0.75                                     | 0.75                    | 2.25                     |

Reference GS k
