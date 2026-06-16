<!-- image -->

Rev. 2.31

## 4. APPENDIX

## 4-1) Appendix-1 Standard Status

Standard status, is a status group which is returned from the printer to the query from the host. Standard status is structured with "Header 1" + "Header 2" + "multiple-byte Printer Status", and is returned continuously to the host. Host will, for every 1 byte received, according to the identification method, execute data identification. Standard status, is always replying to inquiries from the host.

## Header 1

Header 1 is a 1-byte length information that is sent to the head of a standard status.

The structure of header 1 is as indicated in the following chart. Header 1, displays the sent bit number for the overall status that includes bit 1 to bit 3, and bit 5bit and header 1. Host acquires the sent byte number information and always receives the status data for the sent byte number. For reference, the relationship between the transmission bit count and header 1 is as shown in the chart below. This data, because the header 1 to indicate it is bit 0 is always 1 (the second and subsequent bytes always 0), so when detecting the header 1 just confirm that bit 0 = 1 and bit 4 = 0. In addition, bit 6 for future expansion, is ignored by host-side processing.

## &lt; Header 1 (the first byte) &gt;

|   Bit |                              | Condition   | Condition   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   |
|-------|------------------------------|-------------|-------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|       |                              | '0'         | '1'         | U        | PU       | IIU      | GT       | LAN      | IIIW     | IIILAN   | IIIBI    | IIIU     |
|     7 | Fixed at '0'                 |             | -           | 0        | 0        | 0        | 0        | 0        | 0        | 0        | 0        | 0        |
|     6 | Reserved (0 fixed)           |             | -           | 0        | 0        | 0        | 0        | 0        | 0        | 0        | 0        | 0        |
|     5 | Print status number of bytes |             |             | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
|     4 | Fixed at '0'                 |             | -           | 0        | 0        | 0        | 0        | 0        | 0        | 0        | 0        | 0        |
|     3 | Print status number of bytes |             |             | 0        | 0        | 0        | 0        | 0        | 0        | 0        | 0        | 0        |
|     2 | Print status number of bytes |             |             | 0        | 0        | 0        | 0        | 0        | 0        | 0        | 0        | 0        |
|     1 | Print status number of bytes |             |             | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |
|     0 | Fixed at '1'                 | -           |             | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        | 1        |

The actual number of bytes sent and the support table for header 1

|   Number of bytes sent n (7 ≦ n ≦ 15) | Header 1           |
|---------------------------------------|--------------------|
|                                     7 | 00001111B (0F Hex) |
|                                     8 | 00100001B (21 Hex) |
|                                     9 | 00100011B (23 Hex) |
|                                    10 | 00100101B (25 Hex) |
|                                    11 | 00100111B (27 Hex) |
|                                    12 | 00101001B (29 Hex) |
|                                    13 | 00101011B (2B Hex) |
|                                    14 | 00101101B (2D Hex) |
|                                    15 | 00101111B (2F Hex) |

--------------------------------------------------------------------------------------
