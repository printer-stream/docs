<!-- image -->

Rev. 2.31

## 3-5) Printer Information Related Commands Details

## ESC GS ( S n m [d1...dm]

[Name]

Register/Clear printer information

[Code]

ASCII

ESC  GS

(

S

n

m

[d1

．．

dm]

Hex

1B 1D 28 53 n m [d1 ．． dm]

Decimal

27 29 40 83 n m [d1 ．． dm]

## [Defined Area]  n = 5

When registering information:

Defined region of m is as in the following table

48 ≦ d ≦ 57 ('0' ≦ d ≦ '9'), 65 ≦ d ≦ 90 ('A' ≦ d ≦ 'Z'), 97 ≦ d ≦ 122 ('a' ≦ d ≦ 'z')

When clearing information:

m = 0

## [Initial Value] [Function]

---

Parameter details

- ・ n : Register information

・ m

: Registered number of data against information

- ・ d : Registration data

This command is, in addition to the printer information that is set at the factory, is a command for the user to arbitrarily register and clear the printer information.

This command can be specified at the beginning of a line.

However, if there is unprinted data in the line buffer, print the data in the line buffer and execute this command.

If it is determined that there are no problems with the parameter n and m, start processing this command.

If n or m was outside the definition, abort the command analysis.

After the registration is finished or the enforced termination of registration process, execute the printer set.

During the registration process (between the first parameter which is judged OK to when the initialization of the printer is completed after registration), error processing, mechanical operation, status processing and such are not executed.

When clearing registration information, specify m = 0.

|   n | m          | Register information   |    Usage example |
|-----|------------|------------------------|------------------|
|   0 |            | Reserved               |                  |
|   1 |            | Reserved               |                  |
|   2 |            | Reserved               |                  |
|   3 |            | Reserved               |                  |
|   4 |            | Reserved               |                  |
|   5 | 1 ≦ m ≦ 16 | Product serial number  | 2284210080600197 |
|   6 |            | Reserved               |                  |
|   7 |            | Reserved               |                  |

--------------------------------------------------------------------------------------
