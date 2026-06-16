<!-- image -->

## ESC	SYN	DC4	n

Name

Hold print status control settings

Code

ASCII ESC  SYN  DC4

Hex. 1B 16 14 n

Decimal 27 22 20 n

n

Defined Region

n = 0, 1, 48, 49, 255

Initial Value

Memory S/W setting

Function

Hold print status control settings

| n     | Hold print status control   |
|-------|-----------------------------|
| 0, 48 | Invalid                     |
| 1, 49 | Valid                       |
| 255   | Memory switch setting       |

When this is set to enabled, it is possible to use the hold print status.

If paper is in the hold print sensor, the hold print status is "paper present'.

The hold time can be set with the memory switches, and it is possible to select automatic cancel of the 'paper present' status when timeout occurs.

When this is set to disabled, the hold print status is fixed at 'no paper'.

For information about the hold print status, refer to Appendix 2 'Status Specifications'.

In line mode, if unprinted data exists in the image buffer, the data is printed out first and then this command is executed.

However printing is not executed in page mode.

If printing is in progress at the time this command is processed, the printer waits for printing to stop, and then executes this command.

This command setting will not be initialized by the ESC @, CAN commands.

The setting by this command will be initialized by a printer reset.
