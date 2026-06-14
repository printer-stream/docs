Page 10-33 

## Set Output Mode 

-M [(<DEC>); (<ASC>) ; (KASC>) ; (KASC>(;(<ASC>)) ; (<ASC>) ]: 

Purpose: Sets parameters for output. 

Parameters: <DEC> — Turnaround delay, 0-54 612. 

<ASC> — Output trigger character, ASCII 0-127. 

<ASC> — Echo terminator character, ASCII 0-127. 

<ASC> ...<ASC> — 1 or 2 output terminators, ASCII 0-127, 0 terminates string. 

<ASC> — Output initiator character, ASCII 0-127. 

## Set Extended Output and Handshake Mode 

## Page 10-34 

-N [(<DEC>);(<ASC>(; ... <ASC>))]: 

Purpose: Establishes extended parameters for any output command. Parameters: <DEC> — Delay between output characters, 0-54 612. 

<ASC> ... <ASC>— Immediate response string of 1 to 10 characters. ASCII 0-127, 0 terminates string; or Xoff trigger characters. 

## Output Extended Status 

## Page 10-38 

## .O 

Purpose: Outputs the decimal equivalent value of a 16-bit immediate status word. Responses <DEC> [TERM] —a value 40 or less. 

## Reset Handshake 

## Page 10-40 

## .R 

Purpose: Resets the handshake to its default value. It is the same as sending the commands ESC.@, ESC.H, ESC.I, ESC .M,and ESC .N without parameters. 

B-14 INSTRUCTION SYNTAX 
