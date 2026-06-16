## C O N F I D E N T I A L

## (a) Basic structure

| Start character     | FNC 1               | AI          | Data part   | Checkdigit A   | Checkdigit B        | Stop character      |
|---------------------|---------------------|-------------|-------------|----------------|---------------------|---------------------|
| Automatically added | Automatically added | ( d1...dn ) | ( d1...dn ) | ( d1...dn )    | Automatically added | Automatically added |

## (b) Concatenated code structure

| Start character   | FNC 1         | AI          | Data part   | Check digit A   | FNC 1       | AI          | Data part   | Check digit A   | Check digit B       | Stop character      |
|-------------------|---------------|-------------|-------------|-----------------|-------------|-------------|-------------|-----------------|---------------------|---------------------|
| Automatically     | Automatically | ( d1...dn ) | ( d1...dn ) | ( d1...dn )     | ( d1...dn ) | ( d1...dn ) | ( d1...dn ) | ( d1...dn )     | Automatically added | Automatically added |

- ■ Transmit the data relevant to check digit A along with the application identifier (AI), from the host.
- ■ The start character number system character (CODE A, CODE B, CODE C), FNC1, check digit B (1 character), and stop character are added automatically.
- ■ The 4 special characters (SP, "(," ")," "*") are processed as shown in the table below.

| Special characters   | Special characters   | Special characters   | Special characters                                                                                                                                                                                                                      |
|----------------------|----------------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Character            | Hex                  | Decimal              | Processing                                                                                                                                                                                                                              |
| SP                   | 20                   | 32                   | After d1 , the first SP is processed as AI and the data part delimiter, and a space is inserted for the HRI characters. Spaces are inserted for the HRI characters for subsequent SP. In any case, SP does not constitute encoded data. |
