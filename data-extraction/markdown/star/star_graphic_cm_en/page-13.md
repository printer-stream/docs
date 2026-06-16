<!-- image -->

Rev. 2.31

## ESC GS EM DC1 m n1 n2

[Name]

Set external buzzer drive pulse condition

[Code]

ASCII

ESC GS EM DC1 m n1 n2

Hex

1B 1D 19 11 m n1 n2

Decimal

27 29 25 17 m n1 n2

[Defined Area]  1

≦ m ≦ 2, 49 ≦ m ≦ 50

0 ≦ n1 ≦ 255

0 ≦ n2 ≦ 255

[Initial Value]

n1 = 0, n2 = 0

[Function]

Set external buzzer drive pulse condition

m specifies the buzzer drive terminal to perform the condition settings.

m

Buzzer Drive Terminal

1, 49

Buzzer Drive Terminal 1

2, 50

Buzzer Drive Terminal 2

| m     | Buzzer Drive Terminal   |
|-------|-------------------------|
| 1, 49 | Buzzer Drive Terminal 1 |
| 2, 50 | Buzzer Drive Terminal 2 |

n1 specifies energizing time; n2 specifies the delay time.

- ・ Energizing time = 20 x n1 (ms)
- ・ Delay time = 20 x n2 (ms)

Drives for external buzzers set using this command is performed by &lt;ESC&gt; &lt;GS&gt; &lt;EM&gt; &lt;DC2&gt; m n1 n2. When n1 = 0, regardless of the value of n2, the external buzzer drive command &lt;ESC&gt;&lt;GS&gt;&lt;EM&gt;&lt;DC2&gt; is ignored.

This setting value is not initialized with a soft reset.

<!-- image -->

--------------------------------------------------------------------------------------
