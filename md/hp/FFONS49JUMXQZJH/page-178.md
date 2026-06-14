A description of the instruction’s parameters follows: 

- <DEC> The first parameter is optional. If present, it is the intercharacter delay. The delay implemented is (parame ter X 1.1875)mod 65 536)/1.2 milliseconds. The parameter range is 0 to 54 612. If parameters follow, the semicolon must be included, even if this decimal parameter is omitted. 

- <ASC>...<ASC> This parameter is optional. If present, it is a list of the decimal equivalents of 1 to 10 ASCII characters in the range 0 to 127. For Xon-Xoff handshake mode, it specifies the Xoff trigger character(s). For enquire/ acknowledge handshake mode, it specifies the immediate response string. Semicolons must separate each parameter in the list. 

## EXAMPLES 

## For Xon-Xoff Handshake 

.N;19: Sets the Xoff trigger character to DC3. There will be no intercharacter delay, since the first parameter is defaulted to zero by the semicolon. 

## For Enquire/Acknowledge Handshake 

The examples given here include ail handshaking instructions. In addition to illustrating the use of intercharacter delays and immediate response strings set by ESC.N, they are designed to clarify the difference between handshake mode 1 and‘ mode 2 and give some insight into why certain values are logical choices for some parameters. Note the CHR$ function is used to send the escape character. 

10 DIM OUT$(8O) 

40 PRINT CHR$(27)5" .MO;63;0;13:"; CHRS(27)5".N5:" SO PRINT CHR$(27);".H80;18;49:" 60 OUT$="IN;SP1;PAS00,500;":GOSUB 100 

100 PRINT CHR$(18): INPUT 2: PRINT OUT$: RETURN 

The following parameters are set in lines 40 and 50: 

turnaround delay = 0, 

output trigger character = ? (decimal equivalent 63), 

no echo terminate character, 

10-36 RS-232-C/CCITT V.24 INTERFACING 
