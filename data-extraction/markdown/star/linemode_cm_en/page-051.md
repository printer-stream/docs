<!-- image -->

## ESC &amp; c1 c2 n

[Name]

Delete 12 x 24 dot font download characters

[Code]

ASCII

ESC &amp; c1 c2 n

Hex.

1B 26 c1 c2 n

Decimal

27 38 c1 c2 n

[Defined Area]

c1 = 1, 49

c2 = 0, 48

32 ≤ n ≤ 127

[Initial Value]

- - -

[Function]

Deletes 12 x 24 dot font download characters registered to the nth address.

## ESC % n

[Name]

Specifies/cancels ANK download characters

[Code]

ASCII

ESC % n

Hex.

1B 25 n

Decimal

27 37 n

[Defined Area]

n=0, 1, 48, 49

[Initial Value]

ANK download characters cancelled

[Function]

Specifies/cancels ANK download characters

| n     | Download characters              |
|-------|----------------------------------|
| 0, 48 | Cancels ANK download characters  |
| 1, 49 | SpecifiesANK download characters |

&lt;Print example of ANK download characters&gt;

1. ANK download character register (ESC &amp; c1 c2 n d1…d48)
2. Specify ANK download characters (ESC % n (n = 1))
3. Prints ANK download characters

-----------------------------------------------------------------------------
