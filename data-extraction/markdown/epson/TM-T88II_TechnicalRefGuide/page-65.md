## A.1.4  Code

The hexadecimal numbers corresponding to the XON/XOFF codes are shown below.

- ❏ XON code:

11H

- ❏ XOFF code:

13H

<!-- image -->

Note:

When the printer goes from offline to online and the receive buffer is full, XON is not transmitted.

When the printer goes from online to offline and the receive buffer is full, XOFF is not transmitted.

When memory switch MSW 1-3 is off, XON is not transmitted as long as the printer is offline, even if a receive buffer full state has been cleared.

## A.2  IEEE 1284 Parallel Interface

## A.2.1  Modes

The IEEE 1284 parallel interface supports the following two modes.

Table A-4  Parallel modes

| Mode               | Communication direction      | Other information                                    |
|--------------------|------------------------------|------------------------------------------------------|
| Compatibility mode | Host → Printer communication | Centronics-compliant                                 |
| Reverse mode       | Printer → Host communication | Assumes a data transfer from an asynchronous printer |

## Compatibility mode

Compatibility mode allows data transmission from host to printer only: Centronics-compatible.

## Specifications

- Data transmission:

8-bit parallel

- Synchronization:

Externally supplied STROBE* signals

- Handshaking:

ACK* and BUSY signals

- Signal levels:

TTL-compatible connector

- Connector:

ADS-B36BLFDR176 (HONDA) or equivalent product (IEEE 1284 Type B)

- Reverse communication:

Nibble or byte mode

*A rule above a signal name indicates an ' L ' active signal.
