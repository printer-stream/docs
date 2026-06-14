Page 10-28 

## Set Handshake Mode 1 

~H [(KDEC>) ; (KASC>) ; (KASC>(;...<ASC>)) ]: Purpose: Establishes parameters for handshake mode 1, used when response to enquiry character requires ESC . M parameters. Parameters: <DEC> — Block size or Xoff threshold level. 

<ASC> — Enquiry character or not used. 

<ASC> ...<ASC> — Acknowledgment string of 1 to 10 characters or Xon trigger characters. 

## Set Handshake Mode 2 

## Page 10-29 

. 1 [(KDEC>) ; (KASC>) ; (KASC>(;...<ASC>))]: Purpose: Establishes parameters for handshake mode 2, used when response to enquiry character does not require ESC. M parameters. 

Parameters: <DEC> — Block size or Xoff threshold level. 

- <ASC> — Enquiry character or omitted. 

<ASC> ...<ASC> — Acknowledgment string of 1 to 10 characters or Xon trigger characters. 

## Abort Device Control 

Page 10-31 

## J 

Purpose: Aborts any partially decoded or executed device control instructions including outputs. 

## Abort Graphic Instruction 

## Page 10-32 

.K 

Purpose: Aborts any partially decoded HP-GL instruction and discards instructions in buffer. - 

## Output Buffer Size 

Page 10-32 

## .L 

Purpose: Outputs the buffer size. 

Response: 255. Not output until the buffer is empty. 

INSTRUCTION SYNTAX B-13 
