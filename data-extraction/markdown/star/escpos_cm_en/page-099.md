<!-- image -->

## &lt;Function	65&gt;	GS	(	L	pL	pH	m	fn	d1	d2	d3			(fn=65) &lt;Function	65&gt;	GS	8	L	p1	p2	p3	p4	m	fn	d1	d2	d3			(fn=65)

Name

Erase entire NV graphics data

Code

ASCII GS ( L  pL  pH m    fn  d1  d2  d3

Hex. 1D   28  4C  pL  pH m    fn  d1  d2  d3

Decimal     29   40  76  pL   pH m    fn  d1  d2  d3

ASCII GS   8    L

p1  p2 p3 p4  m  fn  d1  d2  d3

Hex. 1D   38  4C

p1  p2 p3 p4  m  fn  d1  d2  d3

Decimal 29   56  76

p1  p2 p3 p4  m  fn  d1  d2  d3

Defined Region

- Parameter for GS ( L (pL+pH×256)=5  (pL=5, pH=0)

- Parameter for GS 8 L

(p1+p2×256+p3x65536+p4x16777216)=5  (p1=5, p2=0, p3=0, p4=0)

- Parameter are shared by for GS ( L and GS 8 L.

m = 48,

fn = 65

d1 = 67, d2 = 76, d3 = 82

Function

Erases all NV graphics data defined by Function 67.

- The erased area is set to be an 'unused area.'

- All key codes become undefined.

Details

- Effective only at the top of the line in standard mode.

- Data for this parameter is discarded in page mode.

- Do not use this function for macro definition because this function is not compatible with the macros.

- If you use this function, all NV graphics data is erased. Take special care if NV graphics data is used in multiple applications.

- This function also erases the NV graphics data defined by the 'FS q' command.

Reference

FS q, GS ( L/GS 8 L &lt;Function 67&gt;
