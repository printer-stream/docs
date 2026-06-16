<!-- image -->

Name

Code

Defined Region

Function

Details Real-time status transmission ASCII DLE  EOT n Hex. 10 04 n Decimal 16 4 n Spec. A:    1 ≤ n ≤ 4

Spec. B:   1 ≤ n ≤ 5

Transmits the status specified by n in real-time.

n = 1: Transmit printer status

n = 2: Transmit offline cause status

n = 3: Transmit error cause status

n = 4: Transmit continuous paper detector status

n = 5: Transmit presenter paper detector status

- The printer transmits the present status.
- Each status is represented by one-byte of data.
- The printer transmits statuses without confirming whether the host computer can receive data.
- This command is executed even when the printer is offline, the reception buffer is full, or there is an error status.
- The printer executes this command upon reception.
- This command is executed even when the printer is offline, the reception buffer is full, or there is an error status on serial interface models.
- This command cannot be executed when the printer is busy on parallel interface models. The printer will not enter a BUSY status when offline or when there is an error when BUSY condition of reception buffer full, offline/reception buffer full is handled as a reception buffer full in the DIP switch settings.
- When ASB is enabled , the status transmitted by this command and the ASB status must be differentiated. See Appendix-2 for details on how to identify.
- This command is enabled even when the printer specification is disabled by ESC  =  (select peripheral devices).
- See Appendix-2 for details on statuses.

Spec. B-1:

Transmit printer status within 2msec.

Spec. B-2:

Transmit printer status within 10msec.

Notes:

- Operators must use caution for other commands when the data string of &lt;10&gt;H&lt;04&gt;H&lt; n &gt; (Spec. A:    1 ≤ n ≤ 4, Spec. B:   1 ≤ n ≤ 5) is received because it operates in the same manner as this command.  Example: In   ESC * m n L n H [d1...dk], d1=&lt;10&gt;H, d2=&lt;04&gt;H, d3=&lt;01&gt;H

- Do not use this command to interrupt code strings of other commands that consist of 2 or more codes.

Example: If you attempt to transmit DLE EOT 3 up to transmitting ESC3 by trying to transmit ESC 3 n from the host, it is processed as ESC 3 &lt;10&gt;H. Operators must use caution.

Reference

DLE ENQ,  GS r, Appendix-2
