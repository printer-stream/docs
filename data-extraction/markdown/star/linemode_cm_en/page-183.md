<!-- image -->

## &lt;Printer status 6  ETB Counter (Eighth Byte)&gt;

| Bit   | Contents          | Status   | Status   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   | Model Compatability   |
|-------|-------------------|----------|----------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| Bit   | Contents          | '0'      | '1'      | TSP800                | TSP700                | TSP600                | TUP900                | TSP1000               | TSP828L               | TSP700II              | TSP650                | TUP500                | TSP800II              | FVP10                 |
| 7     | Fixed at 0        |          | -        | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     |
| 6     | ETB Counter Bit-4 |          |          | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    |
| 5     | ETB Counter Bit-3 |          |          | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    |
| 4     | Fixed at 0        |          | -        | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     |
| 3     | ETB Counter Bit-2 |          |          | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    |
| 2     | ETB Counter Bit-1 |          |          | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    |
| 1     | ETB Counter Bit-0 |          |          | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    | OK                    |
| 0     | Fixed at 0        |          | -        | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     | -                     |

## (*) ETB Counter

This counter is the 5 bit ETB counter.

(It counts from 0 to 31.  When the counter overflows, it counts up from 31 to 0.)

This counter is incremented by 1 using the &lt;ETB&gt; command.

The ETB counter is initialized by the following commands.   When doing so, ASB ETB status is cleared.

However, when initializing the ETB counter, ASB is not transmitted.

## &lt;ETB Counter Initialization Commands&gt;

- &lt;ESC&gt; &lt;RS&gt; E n

: ETB Counter Initialization

- &lt;CAN&gt;

: Cancel print data and initialize commands

-----------------------------------------------------------------------------
