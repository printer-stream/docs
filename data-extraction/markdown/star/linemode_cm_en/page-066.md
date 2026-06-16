<!-- image -->

## ESC GS BEL m t1 t2

[Name] [Code]

Ring buzzer

ASCII

ESC GS  BEL m t1 t2

Hex. 1B 1D 07 m t1 t2

Decimal

27 29 7 m t1 t2

[Defined Area]

1 ≤ m ≤ 2, 49 ≤ m ≤ 50 ('1' ≤ m ≤ '2')

1 ≤ t1 ≤ 255

1 ≤ t2 ≤ 255

[Initial Value] [Function]

- - -

Rings the buzzer.

m specifies the drive terminal of the buzzer.

| m     | Buzzer Drive Terminal   |
|-------|-------------------------|
| 1, 49 | Buzzer Drive Terminal 1 |
| 2, 50 | Buzzer Drive Terminal 2 |

t1 specifies energizing time; t2 specifies the delay time.

- Energizing time = 20 msec x t1
- Delay time = 20 msec x t2

The buzzer will not ring while printing.

Use of this command other than for ringing the buzzer is prohibited.

(There is the possibility of damage if using this command for driving the drawer on models that support external device terminals.)

<!-- image -->

-----------------------------------------------------------------------------
