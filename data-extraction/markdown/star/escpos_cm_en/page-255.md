<!-- image -->

## &lt;Function	49&gt;	ESC	GS	)	L	pL	pH	fn	kc1	kc2

Name

Send the registered individual logo CRC

Code

ASCII

ESC  GS  ) L pL  pH

fn  kc1  kc2

Hex.

1B  1D   29  4C  pL    pH

fn  kc1  kc2

Decimal     27   29   41  76  pL   pH fn  kc1  kc2

Defined Region

pL = 3, pH = 0 fn = 49

32 ≤ kc1 ≤ 126,  32 ≤ kc2 ≤ 126

Function

Send the individual used capacity of NV graphics already stored in the printer.

Details

- The used capacity is the total number of bytes of the used region.

- The management data (14 bytes) are also included in the use capacity.

- The only NV graphics memory capacity, stored by the  'GS ( L' or 'GS 8 L' command, cannot be sent.

- The NV graphics memory capacity, stored by the 'FS q' command, cannot be sent.

Sends the used capacity in the following format:

ESC GS ) L pL pH fn kc1 kc2  [ used capacity ] LF NUL

Ex.: When the used capacity is 1200 bytes:

'120' (Hex:31H, 32H, 30H, 30H, Decimal:49, 50, 48, 48) is converted to 4-bytes of data. If a unregistered key code is specified, the following data is sent instead:

ESC GS ) L pL pH fn kc1 kc2 LF NUL

Reference

GS ( L, GS 8 L
