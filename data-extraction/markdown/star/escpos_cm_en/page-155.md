<!-- image -->

- &lt;When using GS1-128 (m = 74)&gt;
- Be sure to note the following points when sending bar code data for GS1-128 bar code printing.

## The following four special characters operate as shown below.

| Special Characters   |      |         |                                                                                                                                                                  |
|----------------------|------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Special Characters   | Hex. | Decimal |                                                                                                                                                                  |
| SP                   | 20   | 32      | The first SP after d1 is the data division identifier for identifying (AI). The SP is reflected by the HRI but is not included in the encoding data.             |
| (                    | 28   | 40      | ''(' is reflected by the HRI. This is useful when using '(',')' to highlight the AI. It is not included in encoding data.                                        |
| )                    | 29   | 41      | The first ')' after d1 is the data division identifier for identifying (AI). The ')' is reflected by the HRI but is not included in the encoding data.           |
| *                    | 2A   | 42      | The check digit calculated by modulus 10 is inserted automatically at the position specified in '*'. The check digit is reflected in the HRI instead of the '*'. |

Also the following characters are expressed as 2 bytes.

| Special Characters   | Transmission Data   | Transmission Data   | Transmission Data   |
|----------------------|---------------------|---------------------|---------------------|
| Special Characters   | ASCII               | Hex.                | Decimal             |
| FNC1                 | {1                  | 7B, 31              | 123, 49             |
| FNC3                 | {3                  | 7B, 33              | 123, 51             |
| '('                  | {(                  | 7B, 28              | 123, 40             |
| ')'                  | {}                  | 7B, 29              | 123, 41             |
| '*'                  | {*                  | 7B, 2A              | 123, 42             |
| '{'                  | {{                  | 7B, 7B              | 123, 123            |
| FNC3                 | {3                  | 7B, 33              | 123, 51             |
| FNC4                 | {4                  | 7B, 34              | 123, 52             |
| '{'                  | {{                  | 7B, 7B              | 123, 123            |

- ・　A space character is used as the HRI character for FNC1 and FNC3 function characters.
- ・　A space character is used as the HRI control characters (00H to 1FH and 7FH).
