<!-- image -->

Name

Real-time request to printer

Code

ASCII DLE  ENQ n

Hex. 10 05 n

Decimal

16 5 n

Defined Region

1 ≤ n ≤ 2

Function

Responds to requests n specifications from the host in real-time.  n specifications are below.

n = 1: Recover from the error and start printing from the line where the error occurred.

n = 2: Recover from error after clearing the reception buffer and print buffer.

Details

- This command is enabled even when the printer specification is disabled by ESC  =  (select peripheral devices).

- This command is enabled only when an auto-cutter error occurs.

- This command is processed upon reception.

- This command is executed even when the printer is offline, the reception buffer is full, or there is an error status on serial interface models.

- This command cannot be executed when the printer is busy on parallel interface models. The printer will not enter a BUSY status when offline or when there is an error when BUSY condition of reception buffer full, offline/reception buffer full is handled as a reception buffer full.

- The printer retains the settings by ESC !, ESC 3, that were in effect when an error occurred even when DLE ENQ 2 is executed. The printer is initialized completely using this command and ESC @.

Notes:

- Operators must use caution for other commands when the data string of &lt;10&gt;H&lt;05&gt;H&lt; n &gt; (1 ≤ n ≤ 2) is received because it operates in the same manner as this command.

Example: In ESC * m n L n H [d]k; d1 = &lt;10&gt;H; d2 = &lt;05&gt;H; d3 = &lt;01&gt;H

- Do not use this command to interrupt code strings of other commands that consist of 2 or more codes.

Example: If you attempt to transmit DLE EBQ 2 up to transmitting ESC3 by trying to transmit ESC 3 n from the host, it is processed as ESC 3 10H. Operators must use caution.

STAR

- Auto-cutter error specifications vary according to model, so for models for which there are non-recoverable auto-cutter errors, three byes of this command are ignored. See Appendix-2 for details on auto-cutter error specifications for model types.

- Models connected to a presenter ignore this command.

- When this command is set to n = 2, the printer is reset.

Reference

DLE EOT, Appendix-2
