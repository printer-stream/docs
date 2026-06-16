<!-- image -->

Rev. 2.31

## 3. COMMAND DETAILS

## 3-1) Standard Command Details

## 3-1-1) External Device Drive

## ESC BEL n1 n2

[Name]

Set external drive device 1 pulse width

[Code]

ASCII

ESC  BEL n1 n2

Hex

1B 07 n1 n2

Decimal

27 7 n1 n2

[Defined Area]  1

≦ n1 ≦ 127

1 ≦ n2 ≦ 127

[Initial Value]

n1 = 20 (Energizing time: 200 msec)

n2 = 20 (Delay time: 200 msec)

[Function]

Sets the energizing and delay times for driving the external device.

- ・ Energizing time = 10 x n1 (ms)

- ・ Delay time = 10 x n2 (ms)

This setting value is not initialized with a soft reset.

<!-- image -->

--------------------------------------------------------------------------------------
