If a data-length counter is received, the printer prints the specified number of bytes. The next byte following the data is treated as a counter.

Prints next 5 bytes as data

<!-- formula-not-decoded -->

Since the printer evaluates each counter separately, you can include both kinds of counters in the same ESC . 1 command sequence. However, the total amount of print data must match the length and height of the graphics band.

## Note:

If your image has consecutive blank spaces, use the repeat counter to send repetitive bytes of NUL data (bytes with value of 0). This can greatly reduce the amount of data necessary for printing some images.

During compressed mode, divide the image grid into bytes just as with full graphics mode. However, you then separate repetitive data bytes from nonrepetitive bytes. Shaded areas indicate repetitive data bytes.

The ESC . 1 command would be as follows for the example above.

|   60 |   90 |   30 |   128 |   37 |   79 |   42 |   15 |   53 |
|------|------|------|-------|------|------|------|------|------|
|   14 |   99 |  155 |   155 |   63 |   97 |   22 |    0 |    0 |
|    0 |    0 |   60 |    15 |   15 |   15 |   15 |   15 |  128 |
|   32 |    9 |   27 |    34 |  173 |   91 |   92 |    8 |    0 |
|    0 |    0 |    0 |     0 |    0 |    0 |    0 |    0 |    0 |
|    0 |    0 |   37 |    14 |   16 |   88 |  103 |   77 |   61 |
|   13 |   25 |  155 |   155 |   63 |   97 |   22 |   31 |   97 |
|   44 |  110 |  109 |    15 |   15 |   15 |   15 |   15 |    0 |

ESC . 1 10 10 8 72 0

After sending the following data (shaded data bytes are counters), send a CR or LF command.

|   15 |   60 |   90 |   30 |   128 |   37 |   79 |   42 |
|------|------|------|------|-------|------|------|------|
|   15 |   53 |   14 |   99 |   155 |  155 |   63 |   97 |
|   22 |   -3 |    0 |    0 |    60 |   -4 |   15 |    8 |
|  128 |   32 |    9 |   27 |    34 |  173 |   91 |   92 |
|    8 |  -11 |    0 |   18 |    37 |   14 |   16 |   88 |
|  103 |   77 |   61 |   13 |    25 |  155 |  155 |   63 |
|   97 |   22 |   31 |   97 |    44 |  110 |  109 |   -4 |
|   15 |    0 |    0 |      |       |      |      |      |
