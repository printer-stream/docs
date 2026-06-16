## C O N F I D E N T I A L

## GS ( A

```
[Name] Execute test print [Format] ASCII GS ( A pL pH n m Hex 1D 28 41 02 00 n m
```

Decimal 29 40 65 2 0 n m [Printers not featuring this command] TM-P60 [Range] ( pL + ( pH × 256)) = 2   ( pL = 2, pH = 0) 0 ≤ n ≤ 2, 48 ≤ n ≤ 50 TM-J2000/J2100 , TM-T90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-U230 , TM-U220 : 1 ≤ m ≤ 3, 49 ≤ m ≤ 51 TM-L90 : 1 ≤ m ≤ 3, 49 ≤ m ≤ 51, m = 64

[Description]

Executes a specified test print.

- pL , pH specifies ( pL + pH × 256) as the number of bytes after pH ( n and m ).
- n specifies the paper used for the test print as follows:
- m specifies a test pattern as follows:

| n           | Paper                    |
|-------------|--------------------------|
| 0, 48       | Basic sheet (roll paper) |
| 1, 49 2, 50 | Roll paper               |

| m     | Test pattern                      |
|-------|-----------------------------------|
| 1, 49 | Hexadecimal dump                  |
| 2, 50 | Printer status printing           |
| 3, 51 | Rolling pattern                   |
| 64    | Automatic setting of paper layout |

EXECUTING COMMAND
