## C O N F I D E N T I A L

## GS ( H p L p H fn m d1 d2 d3 d4 &lt;Function 48&gt;

```
[Format] ASCII GS ( H pL pH  fn  m d1 d2 d3 d4 Hex 1D 28 48 06 00 30 30 d1 d2 d3 d4 Decimal 29 40 72 6 0 48 48 d1 d2 d3 d4 [Range] ( pL + pH × 256) = 6( pL = 6, pH = 0) fn = 48 m = 48 32 ≤ d1 ≤ 126 32 ≤ d2 ≤ 126 32 ≤ d3 ≤ 126 32 ≤ d4 ≤ 126
```

## [Description]

[Notes]

Saves the specified process ID related to the processed data just before this function.

- ( d1 , d2, d3, d4 ) specifies the process ID. The process ID is able to be related to printing data and any command data without a real-time command.
- When the related data is processed, the process ID is transmitted to the host PC.
- ■ The time when the response is transmitted differs depending on the related data.
- When the related data is printing data, the process ID response is transmitted when the printing is completed.
- When the related data is any data without the commands described above, the process ID response is transmitted at the time of processing the data.
