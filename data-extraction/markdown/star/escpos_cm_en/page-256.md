<!-- image -->

## &lt;Function	50&gt;	E	S	C	G	S	)	L	p	L	p	H	f	n	d	1	d	2

Name

Send all key code of the registered NV graphics

Code

ASCII

ESC GS ) L pL pH fn d1 d2

Hex.

1B 1D 29 4C pL pH fn d1 d2

Decimal         27 29 41 76 pL pH fn d1 d2

Defined Region

pL = 3, pH = 0

fn = 50

d1 = 0, d2 = 0

Function

Send all key code of NV graphics already stored in the printer.

Details

Specification A

- All key code of only NV graphics, stored by the  'GS ( L' or 'GS 8 L' command, cannot be sent.

- All key code of NV graphics, stored by the 'FS q' command, cannot be sent.

Sends  all key code in the following format:

ESC GS ) L pL pH fn kc1 kc2  [ key code key code .... ] LF NUL

Where, k1 and k2 indicate the number of data bytes (k1 + k2 * 256) transmitted after the key codes.

Ex.: When a NV graphics with key codes 01 and 02 is registered,

a  nd k1 = 6, k2 = 0, ['key code' key code' ...] is '0102' (Hex: 30h, 31h, 30h, 32h; Decimal: 48, 49, 48, 50)

When no NV graphics is registered, the following is transmitted.

ESC GS ) L pL pH fn k1 k2 LF NUL (Where, k1 = 2, k2 = 0)

## Specification B

- If NV graphics are registered with 'GS ( L' or 'GS 8 L' command, all of their key codes can be sent.
- If NV graphics are registered with 'FS q' command, none of their key codes can be sent.

All key codes are sent in the following format.

ESC GS) L pL pH fn k1 k2 [key-code key-code ...] LF NUL

Up to 512 key codes can be sent, but logo key codes exceeding this limit are not sent.

k1 and k2 represent the number of transmission data bytes (k1+k2*256) after the key codes.

Example: If NV graphics of key codes 01 and 02 are registered, k1=6 and k2=0. [key-code key-code...] is '0102' (30h, 31h, 30h, 32h in Hex; and 48, 49, 48, 50 in Decimal).

If NV graphics are not registered, the following data is sent.

ESC GS ) L pL pH fn k1 k2 LF NUL (where, k1=2 and k2=0)

If the USB interface is used, the NSB must be made invalid.

GS ( L, GS 8 L

Reference
