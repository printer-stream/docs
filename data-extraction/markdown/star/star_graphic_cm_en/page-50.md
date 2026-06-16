Rev. 2.31

<!-- image -->

## Printer status

The printer status is the status itself that is sent for the 3rd byte onwards for the standard status.

Printer status is (the 2 sent bytes that is attached to header 1) which is returned.

The printer status will always be updated to the newest information. (History does not exist)

The configuration of the status body is shown below.

## &lt; Printer Status 1 printer state (third byte) &gt;

|   Bit |                           | Condition    | Condition        | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   |
|-------|---------------------------|--------------|------------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|       |                           | '0'          | '1'              | U        | PU       | IIU      | GT       | LAN      | IIIW     | IIILAN   | IIIBI    | IIIU     |
|     7 | Fixed at '0'              |              | -                | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     6 | -                         |              |                  | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     5 | Cover status              | CLOSE        | OPEN             | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       |
|     4 | Fixed at '0'              |              | -                | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     3 | ON-LINE ／ OFF-LINE status | ON-LINE      | OFF-LINE         | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       |
|     2 | Compulsion SW             | OPEN         | CLOSE            | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       |
|     1 | <ETB> command             | Not executed | Already executed | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       |
|     0 | Fixed at '0'              |              | -                | -        | -        | -        | -        | -        | -        | -        | -        | -        |

・ &lt;ETB&gt; command

Cleared to 0 when sent back to the host

## &lt; Printer Status 2 error information (fourth byte) &gt;

|   Bit |                                            | Condition      | Condition    | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   |
|-------|--------------------------------------------|----------------|--------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|       |                                            | '0'            | '1'          | U        | PU       | IIU      | GT       | LAN      | IIIW     | IIILAN   | IIIBI    | IIIU     |
|     7 | Fixed at '0'                               |                | -            | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     6 | Stopped due to print head high temperature | Is not stopped | Is stopped   | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       |
|     5 | Unrecoverable error                        | No error       | Error occurs | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       |
|     4 | Fixed at '0'                               |                | -            | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     3 | Auto cutter error                          | no error       | Error occurs | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       | OK       |
|     2 | -                                          |                |              | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     1 | Not used (Fixed at '0')                    |                |              | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     0 | Fixed at '0'                               |                | -            | -        | -        | -        | -        | -        | -        | -        | -        | -        |

## &lt; Printer Status 3 error information (fifth byte) &gt;

|   Bit |              | Condition   | Condition   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   | TSP100   |
|-------|--------------|-------------|-------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
|       |              | '0'         | '1'         | U        | PU       | IIU      | GT       | LAN      | IIIW     | IIILAN   | IIIBI    | IIIU     |
|     7 | Fixed at '0' |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     6 | -            |             |             | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     5 | -            |             |             | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     4 | Fixed at '0' |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     3 | -            |             |             | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     2 | -            |             |             | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     1 | -            |             |             | -        | -        | -        | -        | -        | -        | -        | -        | -        |
|     0 | Fixed at '0' |             | -           | -        | -        | -        | -        | -        | -        | -        | -        | -        |

--------------------------------------------------------------------------------------
