## The Character Slant Instruction, SL 

Ha )©=6The character slant instruction, SL, specifies the slant with which characters are lettered. 

| USES | The instruction may be used to create slanted text, particularly for emphasis, or to reestablish upright labeling after an SL command with parameters has been in effect. 

## SME =SL tan é (terminator) or 

## SL (terminator) 

AMGEN) =The instruction may be used with or without parameters. When parameters are included, the first parameter is interpreted as the tangent of the angle from vertical as shown below. Parameters following the first parameter are ignored. An SL command without parameters defaults to the same value as SLO and labels are not slanted. 

**==> picture [167 x 32] intentionally omitted <==**

**----- Start of picture text -----**<br>
i] 8<br>”<br>/\<br>**----- End of picture text -----**<br>


The useful parameter range is +0.05 to +2 when using default-size characters and up to +3.5 for large letters. 

An SL command remains in effect until an IN, DF or new SL command is received or the plotter is initialized from the front panel. 

The following example letters HP at a slant of +45 degrees and —45 degrees. 

"DEsSP1;SI1.3,1.8;PAI000, 6000;" "SL1;LBHP%" "SL-1;PR1300,0;LBHP&" 

5-18 LABELING 
