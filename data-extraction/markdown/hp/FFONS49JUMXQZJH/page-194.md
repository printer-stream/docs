messages, are sent over the eight data lines and the three handshake lines. Uni-line messages are transferred over the five individual lines of the management bus.

The commands serve several different purposes:

- 0 Addresses or talk and listen commands select the instruments that will transmit and accept data. They are all multi-line messages.
- 0 Unviersal commands cause every instrument equipped to do so to perform a specific interface operation. They include multi-linemes­ sages and three uni-line commands: interface clear (IFC), remote enable (REN), and attention (ATN).
- 0 Addressed commands (also referred to as primary commands) are similar to universal commands, except that they affect only those devices that are addressed and are all multi-line commands. An in­ strument responds to an addressed command, however, only after an address has already told it to be talker or listener.
- 0 Secondary commands are multi-line messages that are always used in series with an address, universal command, or addressed com­ mand to form a longer version of each. Thus they extend the code space when necessary.

To address an instrument, the controller uses seven of the eight data­ bus lines. This allows instruments using the ASCII 7-bit code to act as controllers. As shown in the following table, five bits are available for addresses, and a total of 31 allowable addresses are available in one byte. If all secondary commands are used to extend this into a two-byte addressing capability, 961 addresses become available (31 allowable addresses in the second byte for each of the 31 allowable in the first byte.)

## Command and Address Codes

| Code Form   | Code Form   | Code Form   | Code Form   | Code Form   | Code Form   | Code Form   | Meaning            |
|-------------|-------------|-------------|-------------|-------------|-------------|-------------|--------------------|
| X           | 0           | 0 A5        | A4          | A3          | A2          | A1          | Universal Commands |
| X           | 0           | 1           | A5          | A4          | A3 A2       | A1          | Listen Addresses   |
| X           | 0           | 1 1         | except      | 1 1         | 1           | 1           | Unlisten Command   |
| X           | 1           | 0 A5        | A4          | A3          | A2          | A1          | Talk Address       |
| X           | 1           | 0 1         | except 1    | 1           | 1           | 1           | Untalk Command     |
| X           | 1           | 1 A5        | A4          | A3          | A2          | A1          | Secondary Commands |
| X           | 1 1         | 1           | except 1    | 1           | 1           | 1           | Ignored            |

Code used when attention (ATN) is true (low).

X= don't care.
