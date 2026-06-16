<!-- image -->

## ESC GS = n1 n2 da1 da2...dak db1 db2...dbk

| [Name]   | Write blank code page data   | Write blank code page data   | Write blank code page data   | Write blank code page data   | Write blank code page data   | Write blank code page data   | Write blank code page data   | Write blank code page data   | Write blank code page data   | Write blank code page data   | Write blank code page data   | Write blank code page data   | Write blank code page data   | Write blank code page data   |
|----------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|
| [Code]   | ASCII                        | ESC                          | GS                           | =                            | n1                           | n2                           | da1                          | da2                          | ...                          | dak                          | db1                          | db2                          | dbk                          |                              |
|          | Hex.                         | 1B                           | 1D                           | 3D                           | n1                           | n2                           | da1                          | da2                          | ...                          | dak                          | db1                          | db2                          | dbk                          |                              |
|          | Decimal                      | 27                           | 29                           | 61                           | n1                           | n2                           | da1                          | da2                          | ...                          | dak                          | db1                          | db2                          | dbk                          |                              |

Spec. Aification

[Defined Area]

[Initial Value] [Function]

n1= 0

n2 = 48

1 ≤ (n1 + n2 x 256)

0 ≤ da ≤ 255      (Font-A data)

db = 0            (STAR mode is not installed with Font-B.)

k = (n1 + n2 x 256) ÷ 2

- - -

A  blank  code  page  indicates  a  character  code  table  where  character  codes  from  80h  to  FFh are all blank.

A blank code page can be selected using the ESC GS t n command n = 255.

The printer is reset when writing with this command is completed.

Font-A Data Format  Vertical 24 dots x Horizontal 12 dots]

<!-- image -->

-----------------------------------------------------------------------------
