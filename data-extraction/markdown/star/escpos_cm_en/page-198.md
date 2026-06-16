<!-- image -->

## ESC	GS	SUB	DC2	m	t1	t2

Name

Specify Snout LED ON/OFF time

Code

ASCII

ESC GS SUB DC2 m t1 t2

Hex.

1B   1D  1A   12   m  t1  t2 27   29  26   18   m  t1  t2

Decimal

Defined Region

1 ≤ m ≤ 2, 49 ≤ m ≤ 50 0 ≤ t1 ≤ 255, 0 ≤ t2 ≤ 255

Initial Value

t1 = 2, t2 = 2

Function

Specify Snout LED ON/OFF times. m specifies the snout operation mode.

| m     | Snout Operating Mode                                                                                                                |
|-------|-------------------------------------------------------------------------------------------------------------------------------------|
| 1, 49 | This command specifies the LED ON/OFF times while the presenter is operating. (LED lights in orange while the printer is printing.) |
| 2, 50 | This command specifies the LED ON/OFF times for recoverable and non-recover - able errors.                                          |

t1 specifies the snout LED ON time. When 1 ≤ t1 ≤ 255:  ON time = t1 x 50 msec When t1 =:   When ON time is default value (t1=2) t2 specifies the snout LED OFF time. When 1 ≤ t2 ≤ 255:  OFF time = t2 x 50 msec When t2 = 0:   When OFF time is default value (t2=2) This command is valid when a presenter is connected.

When the snout is not connected, this command is prohibited from use.

Reference

ESC GS SUB DC1, ESC GS SUB DC3
