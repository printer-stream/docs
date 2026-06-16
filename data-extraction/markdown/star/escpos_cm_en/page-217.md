<!-- image -->

## ESC	GS	EM	DC1	m	n1	n2

Name

External buzzer drive pulse condition settings

Code

ASCII

ESC

GS

EM  DC1

m

n1

n2

Hex.

1B 1D 19 11 m n1 n2

Decimal

27

29

25

17

m

n1

n2

Defined Area

1 ≤ m ≤ 2 49 ≤ m ≤ 50

0 ≤ n1 ≤ 255

1 ≤ n2 ≤ 255

Initial Value

n1=0,n2=0

Function

Sets external buzzer derive pulse condition.

m specifies the buzzer drive terminal to perform the condition settings.

| m     | Buzzer Drive Terminal   |
|-------|-------------------------|
| 1, 49 | Buzzer Drive Terminal 1 |
| 2, 50 | Buzzer Drive Terminal 2 |

n1 specifies the energizing time; n2 specifies the delay time.

- Energizing time:  =20msec x n1
- Delay time:  =20msec x n2

<!-- image -->

Drives for external buzzers set using this command is performed by &lt;ESC&gt; &lt;GS&gt; &lt;EM&gt; &lt;DC2&gt; m n1 n2.

The setting value is not initialized by &lt;ESC&gt; '@' and &lt;CAN&gt;.
