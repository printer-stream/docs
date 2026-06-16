## C O N F I D E N T I A L

- ■ The basic ASB statuses, corresponding to each bit for n are as follows:

| n   | n                                 | ASB status                           | ASB status                                      |
|-----|-----------------------------------|--------------------------------------|-------------------------------------------------|
| Bit | Function                          | Bit                                  | Status                                          |
| 0   | Drawer kick-out connector status. | Bit 2 of the first byte              | Drawer kick-out connector pin 3 status.         |
| 1   | Online/offline status.            | Bit 3 of the first byte              | Online/ offline status.                         |
| 1   | Online/offline status.            | Bit 5 of the first byte              | Cover status.                                   |
| 1   | Online/offline status.            | Bit 6 of the first byte              | Paper is being fed by paper feed button status. |
| 1   | Online/offline status.            | Bit 0 of the second byte             | Waiting for online recovery status.             |
|     |                                   | Bit 0 and 1 of the third byte [Note] | Roll paper near-end sensor status.              |
|     |                                   | Bit 2 and 3 of the third byte [Note] | Roll paper end sensor status.                   |
| 2   | Error status.                     | Bit 2 of the second byte             | Recoverable error status.                       |
| 2   | Error status.                     | Bit 3 of the second byte             | Autocutter error status.                        |
| 2   | Error status.                     | Bit 5 of the second byte             | Unrecoverable error status.                     |
| 2   | Error status.                     | Bit 6 of the second byte             | Automatically recoverable error status.         |
| 3   | Roll paper sensor status.         | Bits 0 and 1 of the third byte       | Roll paper near-end sensor status.              |
| 3   | Roll paper sensor status.         | Bits 2 and 3 of the third byte       | Roll paper end sensor status.                   |
| 6   | Panel switch status.              | Bit 1 of the second byte             | Paper feed status                               |

... how to use this table
