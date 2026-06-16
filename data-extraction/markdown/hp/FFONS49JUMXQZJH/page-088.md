## The Character Slant Instruction, SL

UESCWPTIUNThe character slant instruction, SL, specifies the slant with which characters are lettered.

M Theinstructionmay beusedto createslantedtext,particularly for emphasis, or to reestablish upright labeling after an SL command with parameters has been in effect. |

## SYNTAX SL

tan0(terminator)

or

SL (terminator)

EXPLANATIONThe instruction may be used with or without param­ eters. When parameters are included, the first parameter is interpreted as the tangent of the angle from vertical as shown below. Parameters following the first parameter are ignored. An SL command without parameters defaults to the same value as SLO and labels are not slanted.

<!-- image -->

The useful parameter range is i0.05 to i2 when using default-size characters and up to i3.5 for large letters.

An SL command remains in effect until an IN, DF or new SL command is received or the plotter is initialized from the front panel.

The following example letters HP at a slant of +45 degrees and -45 degrees.

```
'DF;SP1;SI1.3,1.B;PH3000,BOOO;' 'SL1;LBHP&' 'SL-1;PR1300,0;LBHP&'
```

<!-- image -->
