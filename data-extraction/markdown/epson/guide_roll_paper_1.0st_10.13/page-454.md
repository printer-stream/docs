## C O N F I D E N T I A L

## ESC ( A pL pH fn a b n c t1 t2 &lt; Function 99 &gt; (TM-U230)

[Name]

Set integrated beeper except when offline factors occur in TM-U230 models

[Format]

[Range]

## [Default] [Description]

[Notes]

ASCII ESC ( A pL pH fn a b n c t1 t2 Hex 1B 28 41 07 00 63 30 01 64 c t1 t2 Decimal 27 40 65 7 0 99 48 1 100 c t1 t2

( pL + pH × 256) = 7 ( pL = 7, pH = 0)

fn = 99

a = 48

b = 1

n = 100

c = 0, 255

1 ≤ t2 ≤ 50

1 ≤ t1 ≤ 50, t1 = 255

Beeps the integrated beeper (select sound variation by DIP switch [SW2-5]).

Sets the integrated beeper control when roll paper near end detector detects [No roll paper].

- When roll paper near end detector detects [No roll paper], 1 ≤ t1 ≤ 50 specifies beeping time ( t1 × 100ms).

t1 = 255 specifies beeping time (infinity).

- t2 specifies time for stop beeping ( t2 × 100ms).
- ■ This function repeats integrated beeper control of [( t1 × 100 ms) beep/ ( t2 × 100 ms) stop] when the roll paper near end detector detects a paper-end. However, when ( t1 = 255) continuous beeping occurs.
- ■ If roll paper detector is selected to stop printing when there is no paper, when the detector detects no roll paper and goes offline, the setting of this function is disabled.
- ■ When there is no roll paper, the integrated beeper can be stopped by any of the following:
- Clear the factor.
- Press FEED switch.
- Offline factor specified by Function 98 occurs.
