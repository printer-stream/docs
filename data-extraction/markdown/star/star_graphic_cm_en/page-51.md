<!-- image -->

Rev. 2.31

## &lt; Printer Status 4 error information (sixth byte) &gt;

|   Bit |                         | Condition   | Condition   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   |
|-------|-------------------------|-------------|-------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|       |                         | '0'         | '1'         | U        | PU       | IIU      | GT       | LAN      | IIIW     | IIILAN   | IIIBI    | IIIU     |
|     7 | Fixed at '0'            |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     6 | Not used (Fixed at '0') |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     5 | Not used (Fixed at '0') |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     4 | Fixed at '0'            |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     3 | Paper end               | Has paper   | No paper    | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       |
|     2 | -                       |             |             | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     1 | -                       |             |             | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     0 | Fixed at '0'            |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |

## &lt; Printer Status 5 error information (seventh byte) &gt;

|   Bit |                         | Condition   | Condition   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   |
|-------|-------------------------|-------------|-------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|       |                         | '0'         | '1'         | U        | PU       | IIU      | GT       | LAN      | IIIW     | IIILAN   | IIIBI    | IIIU     |
|     7 | Fixed at '0'            |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     6 | Not used (Fixed at '0') |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     5 | Not used (Fixed at '0') |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     4 | Fixed at '0'            |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     3 | -                       |             |             | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     2 | -                       |             |             | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     1 | -                       |             |             | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     0 | Fixed at '0'            |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |

## &lt; Printer Status 6 ETB counter (eighth) &gt;

| Bit   |                   | Condition   | Condition   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   |
|-------|-------------------|-------------|-------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| Bit   |                   | '0'         | '1'         | U        | PU       | IIU      | GT       | LAN      | IIIW     | IIILAN   | IIIBI    | IIIU     |
| 7     | Fixed at '0'      |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |
| 6     | ETB counter Bit-4 |             |             | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       |
| 5     | ETB counter Bit-3 |             |             | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       |
| 4     | Fixed at '0'      |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |
| 3     | ETB counter Bit-2 |             |             | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       |
| 2     | ETB counter Bit-1 |             |             | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       |
| 1     | ETB counter Bit-0 |             |             | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       |
| 0     | Fixed at '0'      |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |

## (*) ETB counter

This counter is the ETB counter of 5 bits.

(0-31 count possible. If the counter overflows, it counts up to 31 -&gt; 0.)

This counter is incremented by one by the &lt;ETB&gt; command.

The ETB counter is initialized with the following command. In this case, ETB status for standard status is also cleared.

## &lt;ETB counter initialization command &gt;

- ・ &lt;ESC&gt;&lt;RS&gt; e n

: ETB counter initialization

--------------------------------------------------------------------------------------
