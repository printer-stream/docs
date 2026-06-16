<!-- image -->

## ESC r c1 c2 d1...dk

[Name]

Register Chinese download characters

[Code]

ASCII

ESC

r

c1

c2

d1

...

dk

Hex.

1B 72 c1 c2 d1 ... dk

Decimal

27 114 c1 c2 d1 ... dk

[Defined Area]

[Initial Value] [Function]

0 ≤ d ≤ 255 k=72

c1 and c2 differ according to specifications and code type (see table below).

All spaces

Registers Chinese download characters to c1 and c2 addresses.

Those already registered to these addresses are overwritten.  If c1 and c2 are outside of the defined are or the printer is model not equipped with Chinese fonts (for overseas) and when the specification for the location of use is specified as SBCS (single byte countries) by the memory switch, the printer discards up to d1 and dk.

This command exists in models that have the specifications of A and B below.  (See the 'Special Appendix, Command Table per Model' for details.)

## Specification A

| Specification                 | c1     | c2                            | Registration count   |
|-------------------------------|--------|-------------------------------|----------------------|
| Japanese char./JIS type       | c1=77h | 30h ≤ c2 ≤ 4Fh                | 32 characters        |
| Specification B               |        |                               |                      |
| Specification                 | c1     | c2                            | Registration count   |
| Japanese char./JIS type       | c1=77h | 21h ≤ c2 ≤ 7Eh                | 94 characters        |
| Japanese char./Shift JIS type | c1=ECh | 40h ≤ c2 ≤ 7Eh 80h ≤ c2 ≤ 9Eh | 94 characters        |
| Kanji characters              | c1=FEh | A1h ≤ c2 ≤ FEh                | 94 characters        |

<!-- image -->

Vertical 24 Dots

<!-- image -->

-----------------------------------------------------------------------------
