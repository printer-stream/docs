## C O N F I D E N T I A L

- Bits 0 and 2 indicate the following status:

| Bit   | Binary   | Hex   | Decimal   | Status for ASB                             |
|-------|----------|-------|-----------|--------------------------------------------|
| 0     | 0        | 00    | 0         | Not waiting for a label to be removed      |
| 0     | 1        | 01    | 1         | Waiting for a label to be removed          |
| 1     | -        | -     | -         | Reserved                                   |
| 2     | 0        | 00    | 0         | Paper present in label peeling detector    |
| 2     | 1        | 04    | 4         | No paper present in label peeling detector |
| 3     | -        | -     | -         | Reserved                                   |
| 4     | 0        | 00    | 0         | Not used. Fixed to Off.                    |
| 5,6   | -        | -     | -         | Reserved                                   |
| 7     | 0        | 00    | 0         | Not used. Fixed to Off.                    |

## ... how to use this table

- ■ Bit 0: When the continuous issuing is selected, this bit is always 0.
- ■ Bit 2: When the peeling issuing mode is selected, this bit is changed during paper feeding or when a label is in the peeling position. When the continuous issuing mode is selected, this bit is always 1.

The peeling issuing mode/continuous issuing mode is selected with the operation shown below.

- Selecting the peeling issuing mode

|   Step | Operation                                                               |
|--------|-------------------------------------------------------------------------|
|      1 | Press the cover open button, and open the peeler cover.                 |
|      2 | If the paper roll cover was open in Step 1, close the paper roll cover. |
|      3 | Press the peeler changeover lever. The peeler holder is raised.         |
|      4 | Close the peeler cover.                                                 |
