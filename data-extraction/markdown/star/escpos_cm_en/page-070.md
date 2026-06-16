<!-- image -->

## ESC a n

Name

Position alignment

Code

ASCII ESC a n

Hex. 1B 61 n

Decimal 27 97 n

Defined Region

0 ≤ n ≤ 2, 48 ≤ n ≤ 50

Initial Value

n = 0

Function

Aligns all print data in one line to a specified position.

| n     | Position        |
|-------|-----------------|
| 0, 48 | Left alignment  |
| 1, 49 | Center          |
| 2, 50 | Right alignment |

## Details

[Ex.]

- This command is effective only when input at the top of the line when standard mode is being used.
- This command does has no affect in page mode.  In page mode, this command is only effective for the setting.
- Specifies the alignment position in the printing region that has been set.
- Portions skipped using the following commands are also targeted for position alignment.

- a. HT

: Horizontal tab

b. ESC $

: Specify absolute position

- c. ESC \

: Specify relative position

| Left alignment   | Center   | Right alignment   |
|------------------|----------|-------------------|
| ABC              | ABC      | ABC               |
| ABCD             | ABCD     | ABCD              |
| ABCDE            | ABCDE    | ABCDE             |
