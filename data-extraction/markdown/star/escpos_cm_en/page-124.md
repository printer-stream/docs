<!-- image -->

a = 49

|   b | Type of Symbol                                            | Data (k)     | Data (d)     |
|-----|-----------------------------------------------------------|--------------|--------------|
|  65 | CC-A, CC-B, CC-C Automatic distinction by a digit number. | 3 ≤ k ≤ 2361 | 32 ≤ d ≤ 127 |
|  66 | fixing to CC-C                                            | 3 ≤ k ≤ 2361 | 32 ≤ d ≤ 127 |

Note

Data stored in the symbol saving region by this function is processed using function 481.

After processing functions 481, data in the saving region is maintained.

k bytes for d1...dk are processed as symbol data.

This setting is valid until this function is reset, ESC@ is executed, the printer is reset, or the power is off.

Reference

GS ( k Function 481, ESC @
