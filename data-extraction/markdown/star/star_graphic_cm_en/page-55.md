<!-- image -->

Rev. 2.31

## 4-3) Appendix-3 Device Status Specification (USB Interface Only)

Device Status is a 1-byte status which is returned for the GET\_PORT\_STATUS request from the USB host.

## Device status specification

| Bit    | Field       | 1           | 0               |
|--------|-------------|-------------|-----------------|
| 7 .. 6 | Reserved    | -           |                 |
| 5      | Paper Empty | Paper Empty | Paper Not Empty |
| 4      | Select      | Selected    | Not Selected    |
| 3      | Not Error   | Not Error   | Error           |
| 2 .. 0 | Reserved    | -           |                 |

--------------------------------------------------------------------------------------
