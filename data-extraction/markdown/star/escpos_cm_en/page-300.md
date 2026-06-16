<!-- image -->

## 6-6-2 General Description of GS-1	Bar	Codes

## Basic structure of data

| Start character     | FNC1                | AI        | Data      | check digit A   | check digit B       | Stop character      |
|---------------------|---------------------|-----------|-----------|-----------------|---------------------|---------------------|
| Added automatically | Added automatically | (d1...dn) | (d1...dn) | (d1...dn)       | Added automatically | Added automatically |

## Connection structure of data

| Start character     | FNC1                | AI        | Data      | check digit A   | FNC1      | AI        | Data      | check digit A   | check digit B       | Stop character      |
|---------------------|---------------------|-----------|-----------|-----------------|-----------|-----------|-----------|-----------------|---------------------|---------------------|
| Added automatically | Added automatically | (d1...dn) | (d1...dn) | (d1...dn)       | (d1...dn) | (d1...dn) | (d1...dn) | (d1...dn)       | Added automatically | Added automatically |

The following four special characters (SP, '(', ')', '*') operate as shown below.

| Special Characters   | Special Characters   | Special Characters   | Special Characters                                                                                                                                               |
|----------------------|----------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Characters           | Hex.                 | Decimal              |                                                                                                                                                                  |
| SP                   | 20                   | 32                   | The first SP after d1 is the data division identifier for identifying (AI). The SP is reflected by the HRI but is not included in the encoding data.             |
| (                    | 28                   | 40                   | '(' is reflected by the HRI. This is useful when using '(',')' to highlight the AI. It is not included in encoding data.                                         |
| )                    | 29                   | 41                   | The first ' ) ' after d1 is the data division identifier for identifying (AI). The ' ) ' is reflected by the HRI but is not included in the encoding data.       |
| *                    | 2A                   | 42                   | The check digit calculated by modulus 10 is inserted automatically at the position specified in '*'. The check digit is reflected in the HRI instead of the '*'. |

Data added automatically is not entered in the HRI characters.

Special HRI characters are processed as shown below.

- Start characters (CODE A, CODE B, CODE C) are not printed in HRI characters.
- SP is used for HRI characters for function characters (FNC1 and FNC3) and control characters (00H to 1FH and 7FH).
- HRI characters for SP and '(',')' are printed as they are.
- The check digit is printed in the '*' position.

The available data ranges for each code set (CODE A, CODE B, CODE C) are shown in the following table. Bar code data for special characters (FNC1, FNC3) or '(',')', '*', '{' sends double-byte characters as shown in the following table.
