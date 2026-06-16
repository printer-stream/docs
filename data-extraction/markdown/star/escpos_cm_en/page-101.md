<!-- image -->

## &lt;Function	67&gt;	GS	(	L	pL	pH	m	fn	a	kc1	kc2	b	xL	xH	y	L	yH	[c	d1	...	dk]	1	...	[c	d1	...	dk]	b			(fn=67) &lt;Function	67&gt;	GS	8	L	p1	p2	p3	p4	m	fn	a	kc1	kc2	b	xL	xH	y	L	yH	[c	d1	...	dk]	1	...	[c	d1	...	dk]	b			(fn=67)

Name

Define NV graphics data (in raster format)

Code

ASCII GS ( L  pL  pH m    fn  a  kc1 kc2  b xL xH y L yH [c  d1 ... dk] 1 ... [c  d1 ... dk] b

Hex. 1D   28  4C  pL  pH m    fn  a  kc1 kc2  b xL xH y L yH [c  d1 ... dk] 1 ... [c  d1 ... dk] b

Decimal     29   40  76  pL   pH m    fn  a  kc1 kc2  b xL xH y L yH [c  d1 ... dk] 1 ... [c  d1 ... dk] b

ASCII GS   8    L p1  p2 p3 p4  m  fn  a  kc1 kc2  b xL xH y L yH [c  d1 ... dk] 1 ... [c  d1 ... dk] b

Hex. 1D   38  4C p1  p2 p3 p4  m  fn  a  kc1 kc2  b xL xH y L yH [c  d1 ... dk] 1 ... [c  d1 ... dk] b

Decimal 29   56  76 p1  p2 p3 p4  m  fn  a  kc1 kc2  b xL xH y L yH [c  d1 ... dk] 1 ... [c  d1 ... dk] b

## Defined Region

## Function

- Parameter for GS ( L

12 ≤ (pL+pH×256) ≤ 65535 (0 ≤ pL ≤ 255, 0 ≤ pH ≤ 255)

- Parameter for GS 8 L

12 ≤ (p1+p2×256+p3x65536+p4x16777216) ≤ 4294967295

(0 ≤ p1 ≤ 255, 0 ≤ p2 ≤ 255, 0 ≤ p3 ≤ 255, 0 ≤ p4 ≤ 255)

- Parameter are shared by for GS ( L and GS 8 L.

m = 48, fn = 67, a = 48

32 ≤ kc1 ≤ 126

32 ≤ kc2 ≤ 126

b = 1, 2

1 ≤ (xL+xH×256) ≤ 8192,  (0 ≤ xL ≤ 255, 0 ≤ xH ≤ 32)

1 ≤ (yL+yH×256) ≤ 2304,  (0 ≤ yL ≤ 255, 0 ≤ yH ≤ 9)

c = 49  (Single-color), c = 49,50  (2-color)

0 ≤ d ≤ 255

k = int (((xL + xH×256) + 7)÷8)×(yL + yH×256)

Defines the NV graphics data (in raster format) as the record specified by key codes kc1 and kc2.

- 'b' specifies a number of colors of the definition data.
- 'xL' and 'xH' specify the horizontal size of definition data to 'xL + xH x 256' dots.
- 'yL' and 'yH' specify the vertical size of definition data to 'yL + yH x 256' dots.
- 'c' specifies the definition data color as follows.

c=49: Black

c=50: Red

- 'd' specifies the definition data (in raster format).
- If the specified key code already exists in memory, it is overwritten by the specified one.
