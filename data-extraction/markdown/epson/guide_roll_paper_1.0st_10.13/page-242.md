## C O N F I D E N T I A L

## GS ( L pL pH m fn &lt; Function 52 &gt;

[Name]

Transmit the remaining capacity of the download graphics memory.

[Format]

[Range]

[Description]

[Notes]

<!-- formula-not-decoded -->

(

pL

+

pH

×

pL

m = 48

fn = 4, 52

Transmits the number of bytes of remaining memory (unused area) in the downloaded graphics area.

- This function does not require ESC/POS Handshaking Protocol.
- ■ This function is used to send the following data groups, beginning with the Header and ending with NUL.
- (*1) The unused capacity is the total byte count for the unused area. The decimal value for the unused capacity is converted to text data and sent starting from the high order end.

| Send data            | Hexadecimal   | Decimal   | Data length   |
|----------------------|---------------|-----------|---------------|
| Header               | 37H           | 55        | 1 byte        |
| Identifier           | 32H           | 50        | 1 byte        |
| Unused capacity (*1) | 30H to 39H    | 48 to 57  | 1 to 8 bytes  |
| NUL                  | 00H           | 0         | 1 byte        |

## Example:

If the available capacity is 120 bytes, the '120' (expressed hexadecimally as 31H, 32H, and 30H, decimally as 49, 50, and 48) is converted to 3-byte data.

- ■ The control information for download graphics data is included in the capacity in use.
- ■ Do not use this function in conjunction with download bit images ( GS ✻ ) and download characters ( ESC &amp; ).
- ■ See previous [Notes for transmission process] for process sending data group.

256) = 2 (

= 2, pH

= 0)
