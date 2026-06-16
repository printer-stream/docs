<!-- image -->

- The printer receives the data type specified by m, and the data of the number of bytes (k) specified by nL and nH, based on the block count specified by a.
- 1 block specified by a indicates m1, n1L, n1H, d11 · · · d1k (data type + data count + bar code data), and by continuously sending these a multiple of times, one bar code data can mix data types.
- It is possible to set a maximum of 255 blocks with one command transmission.
- nL and nH specify the number of bytes of the data, so when using Kanji, calculate that 1 character has 2 bytes.
- If this command is outside of the definition region, immediately stop the command analysis process.

When doing so, the bar code data is cleared.

- This command data storage region is shared with the automatic setting command, so data is updated each time either command is executed.
- When the data type is specified as the  English Characters (m=2) and 'a' to 'z' are transmitted, these are converted to the upper-case 'A' to 'Z' and the bar code are generated.
