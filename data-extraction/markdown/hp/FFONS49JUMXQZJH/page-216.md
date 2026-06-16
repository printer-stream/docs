## HP-GLError Messages

- error 0 No error.
- error 1 Instruction not recognized. The plotter has received an illegal character sequence.
- error 2 Wrong number of parameters. Too many or too few param­ eters have been sent with an instruction.
- error 3 Bad parameter. The parameters sent to the plotter with an instruction are out of range for that instruction.
- error 4 Not used.
- error 5 Unknown character set. A character set out of the range 0 through 4 has been designated as either the standard or alternate character set.
- error 6 Position overflow. An attempt to draw a character (LB or UC) or perform a CP that is located outside the plotter's numeric limit of -32 768 to +82 767.
- error 7 Not used.
- error 8 Vector received while pinch wheels raised.

## RS-232-CError Messages

- 0 No I/O error has occurred.
- 10 Output instruction received while another output instruction is ex­ ecuting. The original instruction will continue normally; the one in error will be ignored.
- 11 Invalid byte received after first two characters, . , in a device control instruction.
- 12 Invalid byte received while parsing a device control instruction. The parameter containing the invalid byte and all following parameters are defaulted.
- 13 Parameter out ofrange.
- 14 Toomany parameters received. Additional parameters beyond the proper number are ignored; parsing of the instruction ends when a colon (normal exit) or the first byte of another instruction is received (abnormal exit).
- 15 A framing error, parity error, or overrun error has been detected.
- 16 The input buffer has overflowed. As a result, one or more bytes of data have been lost, 'and therefore, an HP-GL error will probably occur.
