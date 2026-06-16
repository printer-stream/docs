<!-- image -->

## ESC * r E n NUL

[Name]

Set raster EOT mode

[Code]

ASCII

ESC

*

r

E

n

NUL

Hex.

1B 2A 72 45 n 00

Decimal

27 42 114 69 n 0

[Defined Area]

n = 0, 1, 2, 3, 8, 9, 12, 13, 36, 37

[Initial Value]

Models handling full cut: n = 9

Models connected with a presenter: n = 37

[Function]

Sets the raster EOT mode.

The EOT mode operates to execute using the raster document quit command (ESC FF EOT). n is a decimal description (max. 255 digits) using ASCII characters. Invalid in page mode.

## Specification A &lt;EOT mode setting format&gt;

|   n | FormFeed       | Cut Feed       | Cutter         | Presenter      |
|-----|----------------|----------------|----------------|----------------|
|   0 | Set To Default | Set To Default | Set To Default | Set To Default |
|   1 | ○              | --             | --             | --             |
|   2 | ○              | ○              | --             | --             |
|   3 | ○              | TearBar        | --             | --             |
|   8 | ○              | --             | Full Cut       | --             |
|   9 | ○              | ○              | Full Cut       | --             |
|  12 | ○              | --             | Partial Cut    | --             |
|  13 | ○              | ○              | Partial Cut    | --             |
|  36 | ○              | --             | Full Cut       | Eject          |
|  37 | ○              | ○              | Full Cut       | Eject          |

## Specification B &lt;EOT mode setting format&gt;

|   n | FormFeed       | Cut Feed       | Cutter         | Presenter      |
|-----|----------------|----------------|----------------|----------------|
|   0 | Set To Default | Set To Default | Set To Default | Set To Default |
|   1 | ○ (*1)         | --             | --             | --             |
|   2 | ○ (*1)         | ○              | --             | --             |
|   3 | ○ (*1)         | TearBar        | --             | --             |
|   8 | ○ (*1)         | --             | Full Cut       | --             |
|   9 | ○ (*1)         | ○              | Full Cut       | --             |
|  12 | ○ (*1)         | --             | Partial Cut    | --             |
|  13 | ○ (*1)         | ○              | Partial Cut    | --             |
|  36 | ○ (*1)         | --             | Full Cut       | Eject          |
|  37 | ○ (*1)         | ○              | Full Cut       | Eject          |

When the printer is a model handling BM and is set for BM to be effective, the set raster mode page length is ignored and BM detecting is performed.

-----------------------------------------------------------------------------
