<!-- image -->

## ESC s n1 n2

[Name]

Set 2 byte Kanji character left/right spaces

[Code]

ASCII

ESC s n1 n2

Hex.

1B 73 n1 n2

Decimal

27 115 n1 n2

[Defined Area]

0 ≤ n1 ≤ 7

48 ≤ n1 ≤ 55 ('0' ≤ n1 ≤ '7')

0 ≤ n2 ≤ 15

48 ≤ n2 ≤ 57 ('0' ≤ n2 ≤ '9')

65 ≤ n2 ≤ 70 ('A' ≤ n2 ≤ 'F')

[Initial Value] [Function]

Memory switch setting

Adds n1 dots left space amount and n2 dots right space amount to Kanji characters.

The Kanji character width is "left space amount' + "Kanji font dot count' + "right space amount.' (See the information on character specifications in the appropriate printer specifications manual for details on the Kanji font dot count.)

This command is ignored for models not equipped with Chinese fonts (for overseas) and when the specification for the location of use is specified as SBCS (single byte countries) by the memory switch.

Standard mode and page mode can be set independently of each other.

## ESC t n1 n2

[Name]

Set 1 byte Kanji character left/right spaces

[Code]

ASCII

ESC t n1 n2

Hex.

1B 74 n1 n2

Decimal

27 116 n1 n2

[Defined Area]

0 ≤ n1 ≤ 7

48 ≤ n1 ≤ 55 ('0' ≤ n1 ≤ '7')

0 ≤ n2 ≤ 15

48 ≤ n2 ≤ 57 ('0' ≤ n2 ≤ '9')

65 ≤ n2 ≤ 70 ('A' ≤ n2 ≤ 'F')

[Initial Value] [Function]

Memory switch setting

Adds n1 dots left space amount and n2 dots right space amount to single-byte Kanji characters. The single-byte Kanji character width is "left space amount' + "single-byte Kanji font dot count' + "right space amount.'

(See the information on character specifications in the appropriate printer specifications manual for details on the single-byte Kanji font dot count.)

This command is ignored for models not equipped with Chinese fonts (for overseas) and when the specification for the location of use is specified as SBCS (single byte countries) by the memory switch.

Standard mode and page mode can be set independently of each other.

-----------------------------------------------------------------------------
