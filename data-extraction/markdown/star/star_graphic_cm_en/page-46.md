<!-- image -->

Rev. 2.31

## 3-6) Customer display Commands

Applicable Customer display

Refer to the printer's specification manuals.

## ESC GS B @

[Name] Send data to a customer display

[Code]

ASCII

ESC GS B @ n1 n2 d1 ・・・ dk

Hex.

1B 1D 42 40 n1 n2 d1 ・・・ dk

Decimal

27 29 66 64 n1 n2 d1 ・・・ dk

[Defined Area]

n1+n2x256  : BYTE count (1 ≤ d ≤ 65535)

k

: n1+ n2x256

[Initial Value]

- - -

[Function]

The customer display command is sent to a customer display.

## ESC RS B A

[Name]

Status request

[Code]

ASCII

ESC RS B A

Hex.

1B 1E 42 41

Decimal

27 30 66 65

[Defined Area]

- - -

[Initial Value]

- - -

[Function]

Receives the printer status

The customer display status transmission format from the printer &lt;ESC&gt; &lt;RS&gt; B A n

| Bit (n)   | Status                                       |
|-----------|----------------------------------------------|
| 0         | No data in customer display buffer           |
|           | Data exists in customer display buffer       |
| 1         | No connection of customer display            |
|           | Customer display is connected to the printer |
| 2 - 7     | Reserved                                     |

--------------------------------------------------------------------------------------
