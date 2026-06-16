<!-- image -->

## 6-2 Appendix	2	Status	Specifications

## 6-2-1 Identifying	Transmission	Status

The status of commands is identifiable because those transmitted by this printer use a dedicated but value.  However, if using ASB, the three bytes after confirming the first ASB byte, excluding XOFF, are processed as ASB data.  Without this, it is not possible to identify statuses such as GS r (Send status) and statuses after the second byte of an ASB.

## Identification of Transmission Status

| Command/Functions     | Status   | Status   | Status   | Status   | Status   | Status   | Status   | Status   |
|-----------------------|----------|----------|----------|----------|----------|----------|----------|----------|
|                       | Bit7     | Bit6     | Bit5     | Bit4     | Bit3     | Bit2     | Bit1     | Bit0     |
| GS I                  | 0        | *        | *        | 0        | *        | *        | *        | *        |
| GS r                  | 0        | *        | *        | 0        | *        | *        | *        | *        |
| X ON                  | 0        | 0        | 0        | 1        | 0        | 0        | 0        | 1        |
| X OFF                 | 0        | 0        | 0        | 1        | 0        | 0        | 1        | 1        |
| DLE EOT               | 0        | *        | *        | 1        | *        | *        | 1        | 0        |
| ASB (1th Byte)        | 0        | *        | *        | 1        | *        | *        | 0        | 0        |
| ASB (2th to 4th Byte) | 0        | *        | *        | 0        | *        | *        | *        | *        |

## 6-2-2 Error	Details	Per	Model

| Error                  | Error                       | TSP600   | TSP700   | TSP800   | TSP900   | TUP1000   | TSP700II   | TSP650   | TSP500   | TSP800II   | FVP10   | BSC10   | TSP043   | TSP650II   | TSP650IISK   |
|------------------------|-----------------------------|----------|----------|----------|----------|-----------|------------|----------|----------|------------|---------|---------|----------|------------|--------------|
| Recoverable Error      | Cover Open Error            | ○        | ○        | ○        | ○        | ○         | ○          | ○        | ○        | ○          | ○       | ○       | ○        | ○          | ○            |
| Recoverable Error      | Paper out error             | ○        | ○        | ○        | ○        | ○         | ○          | ○        | ○        | ○          | ○       | ○       | ○        | ○          | ○            |
| Recoverable Error      | Near-end error              | ○        | ○        | ○        | ○        | ○         | ○          | ○        | ○        | ○          | ○       | ○       | ○        | ○          | x            |
| Auto- recovery Error   | Heat high temperature error | ○        | ○        | ○        | ○        | ○         | ○          | ○        | ○        | ○          | ○       | ○       | ○        | ○          | ○            |
| Auto- recovery Error   | Auto-cutter error           | ○        | x        | x        | x        | x         | x          | x        | x        | x          | x       | x       | x        | x          | x            |
| Non- recoverable Error | Power voltage error         | ○        | ○        | ○        | ○        | ○         | ○          | ○        | ○        | ○          | ○       | ○       | ○        | ○          | ○            |
| Non- recoverable Error | Thermistor error            | ○        | ○        | ○        | ○        | ○         | ○          | ○        | ○        | ○          | ○       | ○       | ○        | ○          | ○            |
| Non- recoverable Error | SRAM error                  | ○        | ○        | ○        | ○        | ○         | ○          | ○        | ○        | ○          | ○       | ○       | ○        | ○          | ○            |
| Non- recoverable Error | FLASH error                 | ○        | ○        | ○        | ○        | ○         | ○          | ○        | ○        | ○          | ○       | ○       | ○        | ○          | ○            |
| Non- recoverable Error | EEPROM error                | x        | x        | ○        | ○        | ○         | ○          | ○        | ○        | ○          | ○       | x       | ○        | x          | x            |
| Non- recoverable Error | Auto-cutter error           | x        | ○        | ○        | ○        | ○         | ○          | ○        | ○        | ○          | ○       | ○       | ○        | ○          | ○            |
| Non- recoverable Error | Paper jam at presenter      | x        | x        | x        | ○        | x         | x          | x        | ○        | x          | x       | x       | x        | x          | x            |
