<!-- image -->

3-1-4) Other

## ESC GS # m N n1 n2 n3 n4 LF NUL

| [Name]   | Set memory SW   | Set memory SW   | Set memory SW   | Set memory SW   | Set memory SW   | Set memory SW   | Set memory SW   | Set memory SW   | Set memory SW   | Set memory SW   | Set memory SW   | Set memory SW   |
|----------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| [Code]   | ASCII           | ESC             | GS              | #               | m               | N               | n1              | n2              | n3              | n4              | LF              | NUL             |
|          | Hex             | 1B              | 1D              | 23              | m               | N               | n1              | n2              | n3              | n4              | 0A              | 00              |
|          | Decimal         | 27              | 29              | 35              | m               | N               | n1              | n2              | n3              | n4              | 10              | 0               |

0

[Defined Area]  m = 87, 84, 44, 43, 45, 64 ( m = 'W', 'T', ',', '+', '-', '@' )

48 ≦ N ≦ 57 ('0' ≦ N ≦ '9'), 65 ≦ N ≦ 70 ('A' ≦ N ≦ 'F'), 97 ≦ N ≦ 102 ('a' ≦ N ≦ 'f')

48 ≦ n1 ≦ 57 ('0' ≦ n1 ≦ '9'), 65 ≦ n1 ≦ 70 ('A' ≦ n1 ≦ 'F'), 97 ≦ n1 ≦ 102 ('a' ≦ n1 ≦ 'f')

48 ≦ n2 ≦ 57 ('0' ≦ n2 ≦ '9'), 65 ≦ n2 ≦ 70 ('A' ≦ n2 ≦ 'F'), 97 ≦ n2 ≦ 102 ('a' ≦ n2 ≦ 'f')

48 ≦ n3 ≦ 57 ('0' ≦ n3 ≦ '9'), 65 ≦ n3 ≦ 70 ('A' ≦ n3 ≦ 'F'), 97 ≦ n3 ≦ 102 ('a' ≦ n3 ≦ 'f')

48 ≦ n4 ≦ 57 ('0' ≦ n4 ≦ '9'), 65 ≦ n4 ≦ 70 ('A' ≦ n4 ≦ 'F'), 97 ≦ n4 ≦ 102 ('a' ≦ n4 ≦ 'f')

---

Sends command to write after defining memory switch using the definition command specified by the following classes.

Memory switch information defined by the command to write is written to the volatile memory. When writing to the volatile memory by the command to write, the printer executes a reset. For information on the memory switch, see the product specifications document for each model.

| Function                                       | Class      | m    | N            | n1 n2 n3 n4     |
|------------------------------------------------|------------|------|--------------|-----------------|
| Definition data write and reset                | Write      | 'W'  | Fixed at '0' | Fixed at '0000' |
| Definition data write and reset and self print | Write      | 'T'  | Fixed at '0' | Fixed at '0000' |
| Data definition (data specification)           | Definition | ', ' | N            | n1 n2 n3 n4     |
| Data definition (specify bit and set)          | Definition | '+'  | N            | n1 n2 n3 n4     |
| Data definition (specify bit and clear)        | Definition | '-'  | N            | n1 n2 n3 n4     |
| Definition data (all data initialized)         | Definition | '@'  | Fixed at '0' | Fixed at '0000' |
| Data definition (load factory setting )        | Definition | '*'  | Fixed at '0' | Fixed at '0000' |

- ・ m

: Mode selection

- ・ N

: Memory switch number to specify

- ・ n1 n2 n3 n4  : Specified data

m=',' -&gt; Specified data

m='+' -&gt; Bit number to set

m='-' -&gt; Bit number cleared

--------------------------------------------------------------------------------------

## [Initial Value] [Function]

Rev. 2.31
