<!-- image -->

## &lt;Function	48&gt;	ESC	GS	)	L	pL	pH	fn	kc1	kc2

Name

Send the registered individual logo CRC

Code

ASCII

ESC  GS  ) L pL  pH

fn  kc1  kc2

Hex.

1B  1D   29  4C  pL    pH fn  kc1  kc2

Decimal     27   29   41  76  pL   pH fn  kc1  kc2

Defined Region

pL = 3, pH = 0

fn = 48

32 ≤ kc1 ≤ 126,  32 ≤ kc2 ≤ 126

Function

Sends a CRC of the logo already stored in the printer.

Details

- The CRC operation is used only for the logo graphics data currently stored in the printer.
- The key codes, size and color information are excluded from the CRC operation.
- When the printer receives the command, it calculates the CRC and sends it.
- If a logo containing multiple colors is stored, the logo data of the 'n+1' color is added after the logo data of the 'n-th' color and calculated.  ·
- The CRC operation is as follows.
* See the sample codes for concrete implementation examples.
- The CRC of only the stored logo can be sent by the 'GS ( L' or 'GS 8 L' command.
- When logo data is stored, the CRC of the received data is operated.
- If the logo data exceeds the horizontal print area, the CRC is operated based on the data that is received when logo data is stored.
- A CRC of the logo, stored by the 'FS q' command, cannot be sent.

CRC16:           P  olynomial = x 16 +x 15 +x 2 +x 0

Initial value:

FFFF (Hex)

Shift direction:           Right

Output XOR:

FFFF (Hex)

The CRC is sent in the following format:

ESC GS ) L pL pH fn kc1 kc2 CRC-data LF NUL

* The CRC data is converted into a character string and sent.

If a unregistered key code is specified, the following data is sent instead:

ESC GS ) L pL pH fn kc1 kc2 LF NUL

## &lt;Command	processing	flow&gt;

<!-- image -->
