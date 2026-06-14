## **C O N F I D E N T I A L** 

- The roll paper end sensor is enabled when either bit 2 or bit 3 is on or both are on. 

- When a paper near-end is detected, printing stops after printing the current line and feeding the paper. The printer goes offline and Paper LED comes on after printing stops. To resume printing, cancel the “roll paper near-end” status by replacing the roll paper. 

- If the roll paper near-end sensor is disabled and a paper near-end is detected, printing does not stop and the printer does not go offline, but the Paper LED does come on. 

- When a roll paper end is detected, the printer performs the same operations as when a roll paper near-end is detected. 

- The settings of this command are effective until ESC @ is executed, the printer is reset, or the power is turned off. 

[Model-dependent variations] 

TM-J2000/J2100, TM-T90, TM-T88IV, TM-T88V, TM-T70, TM-L90, TM-U230, TM-U220 

## **Program Example for all printers** 

PRINT #1, CHR$(&H1B);"c4";CHR$(1); ← Roll paper near-end sensor enabled 

## TM-J2000/J2100, TM-T90, TM-T88IV, TM-T70, TM-L90 

## **Bits 2 and 3 are undefined.** 

**The roll paper end sensor is always enabled, and when it detects a paper-end, the printer stops printing.** 

**When a roll paper near-end or a roll paper end is detected, the PAPER OUT LED comes on.** 

## TM-T88V 

## **Bits 2 and 3 are undefined.** 

**The roll paper end sensor is always enabled, and when it detects a paper-end, the printer stops printing.** 

**When a roll paper near-end or a roll paper end is detected, the Paper LED comes on.** 
