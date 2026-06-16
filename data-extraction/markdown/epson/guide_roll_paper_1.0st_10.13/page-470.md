## C O N F I D E N T I A L

- ■ For the label paper or black paper control, it calculates the effect value used for the actual print operation based on the paper layout set value, the paper width set value, or the limitation value of the mechanical structure (mechanical pitch or position of the print head, and so on). The set value and effect value can be acquired by Function 50 of GS ( E .

[Model-dependent variations]

TM-L90

## TM-L90

When processing for automatic setting of paper layout ( m = 64), the printer recognizes origin of layout on current paper as the setting value, and other setting values are read from measuring or fixed values. After executing this command, the setting values of paper layout can be confirmed by GS ( E &lt;Function 50&gt;.

- The letters in parentheses () indicate the parameter of GS ( E &lt;Function 49&gt;.

When origin of layout ( sa ) is 'None (paper layout is not used)':

| Parameter of Paper layout                             | Setting value   |
|-------------------------------------------------------|-----------------|
| The layout of the vertical direction ( sb ) ~ ( sf )  | None            |
| The layout of the horizontal direction ( sg ), ( sh ) | None            |

When origin of layout ( sa ) is 'Top of a black mark' (BM = black mark):

| Parameter of Paper layout                                       | Setting value   |
|-----------------------------------------------------------------|-----------------|
| Top of a BM ~ top of next BM ( sb )                             | Measured value  |
| Top of a BM ~ bottom of BM ( sc )                               | Measured value  |
| Other than the layout of the vertical direction ( sd ) ~ ( sf ) | Fixed value     |
| The layout of the horizontal direction ( sg ), ( sh )           | Fixed value     |

## Program Example

PRINT #1, CHR$(&amp;H1D); Ó (A Ó ;CHR$(1);CHR$(2);
