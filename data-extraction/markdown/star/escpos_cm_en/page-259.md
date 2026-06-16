<!-- image -->

## ESC	GS	s	I	z	e	a	n	c1	c2	d1	d2	t1	t2	…	0xFF

Name

Register automatic audio setting information

Code

ASCII ESC GS s I z e a n c1 c2 d1 d2 t1 t2  … 0xFF Hex. 1B 1D 73 49 z e a n c1 c2 d1 d2 t1 t2  … FF Decimal 27 29  115 73 z e a n c1 c2 d1 d2 t1 t2  … 255

Defined Region

z = 0, 1

0 ≤ e ≤ 63 (0x3F)

a = 1,  49

0 ≤ n ≤ 255

0 ≤ c1 + c2 x 256 ≤ 65535

0 ≤ d1 + d2 x 256 ≤ 65535

0 ≤ t1 + t2 x 256 ≤ 65535

Initial Value

At the time of shipment: Set to automatic audio

| e            | Printer Internal Status          |   a |   n |   c1+ c2 x 256 |   d1 + d2 x 256 |   t1 + t2 x 256 |
|--------------|----------------------------------|-----|-----|----------------|-----------------|-----------------|
| 0x00         | Cutter error                     |   0 |   1 |              1 |               0 |               0 |
| 0x01         | Flash ROM error                  |   0 |   2 |              1 |               0 |               0 |
| 0x02         | EE-PROM error                    |   0 |   3 |              1 |               0 |               0 |
| 0x03         | SRAM error                       |   0 |   4 |              1 |               0 |               0 |
| 0x04         | Head temperature detection error |   0 |   5 |              1 |               0 |               0 |
| 0x05         | Power voltage error              |   0 |   6 |              1 |               0 |               0 |
| 0x06 to 0x0F | (Reserved)                       |   0 |   0 |              0 |               0 |               0 |
| 0x10         | BM Error                         |   0 |   7 |              1 |               0 |               0 |
| 0x11         | PE error                         |   0 |   8 |              1 |               0 |               0 |
| 0x12         | Cover open                       |   0 |   9 |              1 |               5 |               0 |
| 0x13         | NE error                         |   0 |  10 |              1 |               0 |               0 |
| 0x14 to 0x1F | (Reserved)                       |   0 |   0 |              0 |               0 |               0 |
| 0x20         | Head high temperature stop error |   0 |  11 |              1 |               0 |               0 |
| 0x21 to 0x2F | (Reserved)                       |   0 |   0 |              0 |               0 |               0 |
| 0x30         | Idling                           |   0 |   0 |              0 |               0 |               0 |
| 0x31 to 0x3F | (Reserved)                       |   0 |   0 |              0 |               0 |               0 |

When z = 1, the automatica audio setting information returns to the default factory setting. (At this time, do not send parameters after e.)

When z = 0, register the automatic audio setting information to playback when the printer's internal status occurs.

e specifies the printer's internal status assigned to audio.

a specifies the area where the audio data to set is stored.

| a     | Audio data storage area   |
|-------|---------------------------|
| 1, 49 | User area                 |

n specifies the audio number to playback.

However, when n = 0, or audio data of a specified number is not registered, automatic audio is invalid.

(c1 + c2 x 256) specifies the number of times.

## Function
