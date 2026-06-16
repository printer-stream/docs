## C O N F I D E N T I A L

Bit 1: [Autocutter is installed/not installed] indicates the state of DIP switch 2-2.

- Type ID ( n = 2, 50) Bit 2: The bit [DM-D (Customer display) isn't supported.
- Printer model ( n = 67)

Printer model: TM-U220

- Model dependent printer information ( n = 112) send status of DIP switch as follows.

Send data is 4 bytes data group composed of [header + printer information (2 bytes) + NUL].

- Type information ( n = 33)

Type information consists of 1 byte of [First byte].

Bit 1: [Autocutter is installed/not installed] indicates the state of DIP switch 2-2.

Bit 2: The bit [DM-D (Customer display) isn't supported.

- Font of Language for each country ( n = 69)

Simplified Chinese model send the state of Memory switch [MSW 2-3].
