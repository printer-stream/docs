<!-- image -->

## &lt;Example	of	Command	Transmission&gt;

- 1) Set the Auto Logo function in advance and register it to the non-volatile memory.

```
ESCGS/1n (n = 0x01): Standard Auto Logo Function ON ESCGS/2n (n = '/'): Specify Auto Logo Command Character ('/') ESCGS/3nLnHd1d2...dk: User Macro 1 Definition nL = 3n H = 0: Registered Macro Count = 3 Bytes d1 = 0x1 bd2 = 0x61 d3 = 0x01: Registered Macro <ESC a1: Center Alignment> ESCGS/4nLnHd1d2...dk: User Macro 2 Definition nL = 16 nH = 0: Registered Macro Count = 16 Bytes d1 = 0x1d d2 = 0x56 d3 = 0x42 d4 = 0x00: Registered Macro <GS V 660: Transport to Cutting Position and Perform Partial Cut> d5 = 0x1c d6 = 0x70 d7 = 0x01 d8 = 0x00: <FS p10: Logo1 Print> d9 = 0x1b d10 = 0x61 d11 = 0x00: <ESC a0: Left Alignment> d12 = 0x1b d13 = 0x70 d14 = 0x03 d15 = 0x64 d16 = 0x00: <ESC p3 100 0: Draw Drive> ESCGS/5n (n = 0x01): Auto Logo Command Character, Space Switch ESCGS/6n (n = 0x01): Partial Cut Before Auto Logo Printing Valid ESCGS/W: Register Auto Logo Definition Data to Non-volatile Memory
```

## 2)	Send	registered	command	character	embedded	in	print	data

'CHEESEBURGER/2' -&gt;  '/' is recognized as the Auto Logo command character; '/2' switch to space; '2' speci -fies Logo2.
