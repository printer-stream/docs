<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The number of bytes required for each dot column shown below.

<!-- formula-not-decoded -->

You must specify the vertical and horizontal dot density of graphics when sending the ESC * command. The dot densities available are shown in the table below.

Dot density

| Parameter m in ESC * command   | Horizontal density   | Vertical density   | Vertical density   | Vertical density   | Adjacent dot printing   | Dots per column   | Bytes per column   |
|--------------------------------|----------------------|--------------------|--------------------|--------------------|-------------------------|-------------------|--------------------|
| Parameter m in ESC * command   | Horizontal density   | 9 pin              | 24 pin             | 48 pin             | Adjacent dot printing   | Dots per column   | Bytes per column   |
| 0                              | 60                   | 72                 | 60                 | 60                 | Yes                     | 8                 | 1                  |
| 1                              | 120                  | 72                 | 60                 | 60                 | Yes                     | 8                 | 1                  |
| 2                              | 120                  | 72                 | 60                 | 60                 | No                      | 8                 | 1                  |
| 3                              | 240                  | 72                 | 60                 | 60                 | No                      | 8                 | 1                  |
| 4                              | 80                   | 72                 | 60                 | 60                 | Yes                     | 8                 | 1                  |
| 5                              | 72                   | 72                 | N/A                | N/A                | Yes                     | 8                 | 1                  |
| 6                              | 90                   | 72                 | 60                 | 60                 | Yes                     | 8                 | 1                  |
| 7                              | 144                  | 72                 | N/A                | N/A                | Yes                     | 8                 | 1                  |
| 32                             | 60                   | N/A                | 180                | 180                | Yes                     | 24                | 3                  |
| 33                             | 120                  | N/A                | 180                | 180                | Yes                     | 24                | 3                  |
| 38                             | 90                   | N/A                | 180                | 180                | Yes                     | 24                | 3                  |
| 39                             | 180                  | N/A                | 180                | 180                | Yes                     | 24                | 3                  |
| 40                             | 360                  | N/A                | 180                | 180                | No                      | 24                | 3                  |
| 64                             | 60                   | N/A                | N/A                | 360                | Yes                     | 48                | 6                  |
| 65                             | 120                  | N/A                | N/A                | 360                | Yes                     | 48                | 6                  |
| 70                             | 90                   | N/A                | N/A                | 360                | Yes                     | 48                | 6                  |
| 71                             | 180                  | N/A                | N/A                | 360                | Yes                     | 48                | 6                  |
| 72                             | 360                  | N/A                | N/A                | 360                | No                      | 48                | 6                  |
| 73                             | 360                  | N/A                | N/A                | 360                | Yes                     | 48                | 6                  |
