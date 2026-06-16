<!-- image -->

## ESC GS EM DC2 m n1 n2

| [Name]   | External buzzer drive execution   | External buzzer drive execution   | External buzzer drive execution   | External buzzer drive execution   | External buzzer drive execution   | External buzzer drive execution   | External buzzer drive execution   | External buzzer drive execution   |
|----------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|
| [Code]   | ASCII                             | ESC                               | GS                                | EM                                | DC2                               | m                                 | n1                                | n2                                |
|          | Hex.                              | 1B                                | 1D                                | 19                                | 12                                | m                                 | n1                                | n2                                |
|          | Decimal                           | 27                                | 29                                | 25                                | 18                                | m                                 | n1                                | n2                                |

[Defined Area]

[Initial Value] [Function]

1 ≤ m ≤ 2 1 ≤ n1 ≤ 20 n2=0

---

Repeatedly drives the buzzer according to the ON/OFF conditions set by the external buzzer drive pulse conditions command &lt;ESC&gt; &lt;GS&gt; &lt;EM&gt; &lt;DC1&gt; m t1 t2.

m specifies the buzzer drive terminal to drive.

| m     | Buzzer Drive Terminal   |
|-------|-------------------------|
| 1, 49 | Buzzer Drive Terminal 1 |
| 2, 50 | Buzzer Drive Terminal 2 |

Specifies the number of repetitions of the buzzer drive with (n2 x 256 + n1).

The buzzer will not ring while printing.

This command is prohibited for uses other than to ring the buzzer.

(If this command is used to drive the cash drawer on models that have an external device terminal, the system will be damaged. Absolutely never use it for other purposes.)

The buzzer can be stopped by pressing the paper feed switch or opening the cover when it is ringing.

## Example:

<!-- image -->

(Note) If the off time is set to 0 (zero), it is possible to ring the buzzer continuously for the amount of n1. For example, if on = 5 seconds, off = 0, and n1 = 20 times, the buzzer will ring for 100 seconds.

-----------------------------------------------------------------------------

49 ≤ m ≤ 50
