## C O N F I D E N T I A L

## ESC ( A pL pH fn n c t &lt; Function 48 &gt;

[Name] Beep integrated beeper [Format] ASCII ESC ( A pL pH fn n c t Hex 1B 28 41 04 00 30 n c t Decimal 27 40 65 4 0 48 n c t [Range] ( pL + pH × 256) = 4 ( pL = 4, pH = 0) fn = 48 TM-P60 : 48 ≤ n ≤ 58 1 ≤ c ≤ 63 10 ≤ n ≤ 255

[Description]

[Notes]

Beeps the integrated beeper.

- n specifies the tone that is beeped. The tones depend on the printer model. When n specifies 'doesn't beep,' the parameters c and t are still required for this function.
- c specifies the number of beeps.
- t specifies the beeping cycle time ( t × 100 ms).
- ■ This function beeps the beeper '( t × 100 ms) × c .' Example: When tone ( n ) specifies '500ms beeps' and c = 3 and t = 10

<!-- image -->
