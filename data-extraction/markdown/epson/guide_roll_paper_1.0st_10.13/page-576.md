## C O N F I D E N T I A L

TM-T70 : k = 72 [Kanji Font A (24 × 24) k = 32 [Kanji Font B (16 × 16) TM-P60 : k = 72 [Kanji Font A (24 × 24) k = 60 [Kanji Font B (20 × 24) k = 32 [Kanji Font C (16 × 16) TM-U230 , TM-U220 :

k = 32

Defines the user-defined Kanji character pattern specified by the character codes ( c1 and c2 ) of the currently selected Kanji font.

- c1 specifies the first byte of a character code for a user-defined Kanji character.
- c2 specifies the second byte of a character code for a user-defined Kanji character.
- d specifies the defined data (column format).
- k indicates the number of defined data. k is an explanation parameter; therefore, it does not need to be transmitted.
- ■ This command is effective only for the Japanese, Simplified Chinese, Traditional Chinese, and Korean models.
- ■ The printer processes k byte data of d1 ... dk as defined data. The defined data ( d ) sets a corresponding bit to 1 to print a dot or to 0 not to print a dot.
- ■ The number of characters to be defined differ, depending on the printer models.
- ■ Different user-defined characters can be defined for each Kanji character. Kanji fonts can be specified by function 48 of FS ( A .
- ■ Defined data is effective until it is redefined, ESC @ is executed, the printer is reset, or the power is turned off.
- ■ User-defined characters are not defined and space is printed at the default.

## [Description]

## [Notes]
