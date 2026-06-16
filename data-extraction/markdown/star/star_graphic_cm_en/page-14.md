<!-- image -->

Rev. 2.31

## ESC GS EM DC2 m n1 n2

[Name]

Output External buzzer drive pulse

[Code]

ASCII

ESC GS EM DC2 m n1 n2

Hex

1B 1D 19 12 m n1 n2

Decimal

27 29 25 18 m n1 n2

[Defined Area]  1

≦ m ≦ 2, 49 ≦ m ≦ 50

1 ≦ n1 ≦ 20

n2 = 0

[Initial Value] [Function]

---

Repeatedly drives the buzzer according to the ON/OFF conditions set by the external buzzer drivepulse conditions command &lt;ESC&gt; &lt;GS&gt; &lt;EM&gt; &lt;DC1&gt; m t1 t2.

m specifies the buzzer drive terminal to drive.

m specifies the buzzer drive terminal to drive.

| m     | Buzzer Drive Terminal   |
|-------|-------------------------|
| 1, 49 | Buzzer Drive Terminal 1 |
| 2, 50 | Buzzer Drive Terminal 2 |

Specifies the number of repetitions of the buzzer drive with (n2 x 256 + n1).

The buzzer will not ring while printing.

Use of this command other than for ringing the buzzer is prohibited.

(If this command is used to drive the cash drawer on models that have an external device terminal, the system will be damaged. Absolutely never use it for other purposes.)

The buzzer can be stopped by pressing the paper feed switch when it is ringing.

## &lt;Example&gt;

<!-- image -->

(Special Note)   If off time=0, it is only possible to continuously sound it n1 times. For example, if on=5 seconds, off=0 and n1=20 times, it will sound for 100 seconds.

--------------------------------------------------------------------------------------
