## C O N F I D E N T I A L

[Notes]

- ■ The serial number counter is stored in the print buffer by GS c .
- ■ Settings of this command are effective until ESC @ is executed, the printer is reset, or the power is turned off.

## Program Example

PRINT #1, CHR$(&amp;H1D);"C0";CHR$(3);CHR$(0);

PRINT #1, "AAAAA";CHR$(&amp;H1D);"c";CHR$(&amp;HA);

PRINT #1, CHR$(&amp;H1D);"C0";CHR$(4);CHR$(1);

PRINT #1, "BBBBB";CHR$(&amp;H1D);"c";CHR$(&amp;HA);

## Print Sample

AAAAA 3 digits + right alignment + adding spaces to the left BBBBB0002 ← 4 digits + right alignment + adding "0"  to the left

1  ←
