|Bit||Logic|Logic|||
|---|---|---|---|---|
|No.|||State|Description||
|0||0|Set and hold line high (disable hard-||
||||wire handshake).||
|||1|Enable hardwire handshake mode.*||
|1||xX|Ignored.||
|2||0|Establish monitor mode0|(all bytes|
||||displayed on terminal as they are||
||||parsed from the buffer).||
|||1|Establish monitor mode1|(all bytes|
||||displayed as they are received).||
|3||0|Disable monitor mode. *||
|||1|Enable the monitor mode established||
||||bybit2.||



*When hardwire handshake is enabled, the DTR line becomes a “buffer space available” flag. The line is high when available buffer space is greater than or equal to the current block size, and is held low when available buffer space is less than the current block size. This size defaults to 80 bytes unless a different value is specified by the ESC . H or ESC . I command. 

EXAMPLE . @:13: will establish monitor mode 1 where all bytes are displayed on the terminal as they are received by the plotter. 

## The Output Buffer Space Instruction, 

- DESCRIPTION Biwi output buffer space instruction, ESC. B, outputs 

- the plotter’s available buffer space. 

- | USES | This command is used in a software checking handshake to interrogate the plotter regarding available buffer space. SYNTAX -B Ag UEU §=No parameters are used. 

   - <DEC> The plotter’s response is a decimal number in the range 0 to 255, and represents the number of bytes of buffer space currently available for storing graphic instructions sent from the computer. 

   - [TERM] This decimal number is followed by the output terminator which defaults to carriage return, CR, or is as set by ESC. M. 

10-26 RS-232-C/CCITT V.24 INTERFACING 
