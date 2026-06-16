<!-- image -->

## &lt;Function	64&gt;	GS	(	L	pL	pH	m	fn	d1	d2			(fn=64) &lt;Function	64&gt;	GS	8	L	p1	p2	p3	p4	m	fn	d1	d2		(fn=64)

(p1+p2×256+p3x65536+p4x16777216)=4  (p1=4, p2=0, p3=0, p4=0)

Name

Send a key code list of predefined NV graphics

Code

ASCII GS ( L  pL  pH m    fn  d1  d2

Hex.

1D   28  4C  pL  pH m    fn  d1  d2

Decimal     29   40  76  pL   pH m    fn  d1  d2

ASCII GS   8    L p1  p2 p3 p4  m  fn  d1  d2

Hex. 1D   38  4C

p1  p2 p3 p4  m  fn  d1  d2

Decimal 29   56  76

p1  p2 p3 p4  m  fn  d1  d2

Defined Region

- Parameter for GS ( L (pL+pH×256)=4  (pL=4, pH=0)

- Parameter for GS 8 L

- Parameter are shared by for GS ( L and GS 8 L.

m = 48,

fn = 64

d1 = 75, d2 = 67

Function

Sends the defined NV graphics key code list.

Details

- Sends the key code in the following format:

| Transmission data      | Hex        | Decimal   | Data length   |
|------------------------|------------|-----------|---------------|
| Header                 | 37H        | 55        | 1 Byte        |
| Identifier             | 72H        | 114       | 1 Byte        |
| Identifier information | 40H/41H    | 64/65     | 1 Byte        |
| *1, 2                  |            |           |               |
| Data                   | 20H to 7EH | 32 to 126 | 2 to 80 Byte  |
| NUL                    | 00H        | 0         | 1 Byte        |

- If there is no defined NV graphics key code list, it sends the following format.
- See the Note for &lt;Function 48&gt; for a detailed explanation of the sending process.

| Transmission data      | Hex   |   Decimal | Data length   |
|------------------------|-------|-----------|---------------|
| Header                 | 37H   |        55 | 1 Byte        |
| Identifier             | 72H   |       114 | 1 Byte        |
| Identifier information | 40H   |        64 | 1 Byte        |
| NUL                    | 00H   |         0 | 1 Byte        |

Reference

FS q, GS ( L/GS 8 L &lt;Function 48&gt;
