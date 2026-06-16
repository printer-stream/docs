<!-- image -->

## GS	(	L	pL	pH	m	fn	[parameter] GS	8	L	p1	p2	p3	p4	m	fn	[parameter]

| Name   | Specify graphics data   | Specify graphics data   | Specify graphics data   | Specify graphics data   | Specify graphics data   | Specify graphics data   | Specify graphics data   | Specify graphics data   | Specify graphics data   | Specify graphics data   | Specify graphics data   | Specify graphics data   |
|--------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|
| Code   | ASCII                   | GS                      | (                       | L                       | pL                      | pH                      | m                       | fn                      | [parameter]             | [parameter]             | [parameter]             | [parameter]             |
|        | Hex.                    | 1D                      | 28                      | 4C                      | pL                      | pH                      | m                       | fn                      | parameter]              | parameter]              | parameter]              | parameter]              |
|        | Decimal                 | 29                      | 40                      | 76                      | pL                      | pH                      | m                       | fn                      | [parameter]             | [parameter]             | [parameter]             | [parameter]             |
| Code   | ASCII                   | GS                      | 8                       | L                       | p1                      | p2                      | p3                      | p4                      | m                       | fn                      | [parameter]             | [parameter]             |
|        | Hex.                    | 1D                      | 38                      | 4C                      | p1                      | p2                      | p3                      | p4                      | m                       | fn                      | [parameter]             | [parameter]             |
|        | Decimal                 | 1D                      | 29                      | 56                      | 76                      | p1                      | p2                      | p3                      | p4                      | m                       | fn                      | [parameter]             |

- (*) Use the GS ( L code to explain each function.
- GS ( L and GS 8 L are the same function.
- If [parameter] in each function exceeds 65533 bytes, use GS 8 L.

Runs the process related to the graphics data specified by the function code (fn).

## Function

| fn    | Code                                                                |   Function No. | Function                                      | For STAR            |
|-------|---------------------------------------------------------------------|----------------|-----------------------------------------------|---------------------|
| 0, 48 | GS ( L pL pH m fn                                                   |             48 | Send NV graphics memory capacity              | Supported           |
| 2, 50 | GS ( L pL pH m fn                                                   |             50 | Print raster graphics data                    | Receive and discard |
| 3, 51 | GS ( L pL pH m fn                                                   |             51 | Send remaining NV graph - ics memory capacity | Supported           |
| 64    | GS ( L pL pH m fn d1 d2                                             |             64 | Send NV graphics key code                     | Supported           |
| 65    | GS ( L pL pH m fn d1 d2 d3                                          |             65 | Batch all delete NV graph - ics data          | Supported           |
| 66    | GS ( L pL pH m fn kc1 kc2                                           |             66 | Delete the specified NV graphics data         | Supported           |
| 67    | GS ( L pL pH m fn a kc1 kc2 b xL xH yL yH [c d1...dk]1 [c d1...dk]b |             67 | Define NV graphics data                       | Supported           |
| 69    | GS ( L pL pH m fn a kc1 kc2 x y                                     |             68 | Print the specified NV graphics data          | Supported           |
| 112   | GS ( L pL pH m fn a bx by c xL xH yL yH d1...dk                     |            112 | Store raster graphics data                    | Supported           |
