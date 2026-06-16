<!-- image -->

Spec. B.

[Defined Area]

n1 = 0

n2 = 48

1 ≤ (n1 + n2 x 256)

0 ≤ da ≤ 255 (Font-A data)

0 ≤ db ≤ 255 (Font-B data)

k = (n1 + n2 x 256) ÷ 2

[Initial Value] [Function]

---

A  blank  code  page  indicates  a  character  code  table  where  character  codes  from  80h  to  FFh are all blank.

A blank code page can be selected using the ESC GS t n command n = 255.

The following is the data written to the blank code page.

Font-A: 1 character = 48 bytes   6144 bytes = 48 bytes x 128 characters

Font-B: 1 character = 48 bytes   6144 bytes = 48 bytes x 128 characters

Send Font-A and Font-B data continuously.

The printer is reset when writing with this command is completed.

[Font-A Data Format  Vertical 24 dots x Horizontal 12 dots]

<!-- image -->

[Font-B Data Format  Vertical 24 dots x Horizontal 9 dots]

<!-- image -->

-----------------------------------------------------------------------------
