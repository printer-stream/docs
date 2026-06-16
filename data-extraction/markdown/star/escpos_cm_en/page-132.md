<!-- image -->

## GS	C	;	sa;	sb;	sn;	sr;	sc;

Name

Set Counter Mode (B)

Code

ASCII

GS

C

;

sa

;

sb

;

sn

;

sr

;

sc

;

Hex.

1D

43

3B

sa

3B

sb

3B

sn

3B

sr

3B

sc

3B

Decimal

29

67

59

sa

59

sb

59

sn

59

sr

59

sc

59

Defined Region

'0' ≤ sa ≤ '65535'

'0' ≤ sb ≤ '65535'

'0' ≤ sn ≤ '255'

'0' ≤ sr ≤ '255'

'0' ≤ sc ≤ '65535'

Initial Value

sa = '1'

sb = '65535'

sn = '0'

sr = '1'

sc = '1'

Function

Sets the serial number counter counting mode and counter value.

Details

- sa, sb, sn, sr and sc are all ASCII character strings represent setting values using decimals. They are composed of character strings of 0 to 9.

- sa, and sb specify the counter range.
- sn specifies the number of steps to count up or down.
- sr specifies the number of times to repeat printing with the counter value fixed.
- sc specifies the counter value.
- If {sa &lt; sb and sn ≠ 0 and sr ≠ 0} this command sets the count up mode.
- If {sa &gt; sb and sn ≠ 0 and sr ≠ 0} this command sets the counter down mode.
- If {sa = sb or n = 0 and sr = 0} this command stops counting.
- When the count up mode is set, sa is the counter minimum value and sb is the counter maximum value.

Also, if the counter exceeds the maximum value, it starts counting again from the minimum value.

- When the count down mode is set, sa is the counter maximum value and sb is the counter minimum value.

Also, if the counter is smaller than the minimum value, it starts counting down again from the maximum value.

- Each argument from sa to sc can be omitted.  The setting just prior is maintained without change to the setting value that corresponds to the omitted argument.
- Executing this command clears the internal counter that shows the number of times printing was repeated.
- If an argument outside of the definition region is input, the command is stopped and processing is handled normally from subsequent data.

GS C 0, GS C 1, GS C 2, GS c

Reference
