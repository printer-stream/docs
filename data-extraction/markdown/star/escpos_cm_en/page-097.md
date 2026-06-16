<!-- image -->

## &lt;Function	51&gt;	GS	(	L	pL	pH	m	fn		(fn=51) &lt;Function	51&gt;	GS	8	L	p1	p2	p3	p4	m	fn		(fn=51)

Name

Send NV graphics memory capacity

Code

ASCII GS ( L  pL  pH m fn

Hex. 1D   28  4C  pL  pH

m fn

Decimal     29   40  76  pL  pH m fn

ASCII GS   8    L p1  p2 p3 p4  m  fn

Hex. 1D   38  4C p1  p2 p3 p4  m  fn

Decimal 29   56  76 p1  p2 p3 p4  m  fn

Defined Region

- Parameter for GS ( L

(pL+pH×256)=2  (pL=2, pH=0)

- Parameter for GS 8 L

(p1+p2×256+p3x65536+p4x16777216)=2  (p1=2, p2=0, p3=0, p4=0)

- Parameter are shared by for GS ( L and GS 8 L.

m = 48,

fn = 3, 51

Function

Sends the remaining capacity (or unused area) of NV graphics area in bytes.

Details

- Sends the number of bytes in the following format.:

| Transmission data   | Hex        | Decimal   | Data length   |
|---------------------|------------|-----------|---------------|
| Header              | 37H        | 55        | 1 Byte        |
| Identifier          | 30H        | 48        | 1 Byte        |
| Unused capacity *1  | 30H to 39H | 48 to 57  | 1 to 8 Byte   |
| NUL                 | 00H        | 0         | 1 Byte        |

The decimal value indicating the unused capacity is converted to text data and sent in order from the MSB.

Ex.: When the unused capacity is 120 bytes:

'120' (Hex:31H, 32H, 30H, Decimal:49, 50, 48) is converted to 3-bytes of data.

- Information region is also included in the use capacity.
- Do not use this function at the same time as the NV bit image (FS q) command.
- See the Note for &lt;Function 48&gt; for a detailed explanation of the sending process.

Reference

FS q, GS ( L/GS 8 L &lt;Function 48&gt;
