Page 7-7 

## OO The Output Options Instruction 

OO () Purpose: Used to output features implemented on the plotter. Response: 0,1,0,0,1,0,0,0[TERM] only with RS-232-C plotters that have the Serial Prefix number 2308A or higher). | IndicatesCopenIndicatesselect arcscapability and circleis instructions areincluded (available includedon all (availableplotters). 

## OP The Output P1 and P2 Instruction 

   - Page 2-5 

- OP (;) Purpose: Used to output the plotter unit coordinates of the scaling points Pl and P2. 

Response: Plx, Ply, P2x, P2y [TERM] — four integers in ASCII. Range — dependent on settings of paper switch. 

US A4 

- 0 < X-coordinate < 10 300 0 < X-coordinate < 10 900 0 < Y-coordinate < 7650 0 < Y-coordinate < 7650 

OS The Output Status Instruction Page 7-8 OS () Purpose: Used to output the plotter’s status. Response: status [TERM] — integer in ASCII in the range 0 to 255. Power-on status, 24. 

## Page 7-8 

## OW The Output Window Instruction 

Page 2-10 

- OW (;) Purpose: Used to output the plotter unit coordinates of the lowerleft and upper-right corners of the current window. 

- Response: Xlower left, Ylower left, Xupper right, Yupper right [TERM] — integers in ASCII. Range same as OP. 

INSTRUCTION SYNTAX B-7 
