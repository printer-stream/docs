After plotting the design, divide the grid into groups one dot wide and eight dots high.

<!-- image -->

The dots in each group have a value, as shown in the following diagram. The sum of each group is sent as a byte of data to the printer. Calculate the value for each byte as shown.

<!-- image -->

| 128   | 128 64        | 128 64   |
|-------|---------------|----------|
| 32    | 32 2 64 32 16 | 32 16 1  |
| 64 16 | 4 2           |          |
|       | 16 8 4        | 8 4 2    |
|       | 1 128         |          |
| 8     | 8             |          |
| 4     | 1             |          |
|       | 128 64        |          |
| 2     | 32 16         |          |
|       | 8 4           |          |
| 1     | 2             |          |
|       | 1             |          |
