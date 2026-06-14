Page 5-3 

## CS. The Designate Standard Character Set Instruction 

CS m 

(;) 

Purpose: Designates the standard character set. 

Parameter: integer, 0 through 4; default set 0. 

## DC The Digitize Clear Instruction 

## Page 6-3 

DC () 

Purpose: Clears digitize mode without entering a point from the front panel. 

## DF The Default Instruction 

Page 1-10 

DF ; 

Purpose: Returns plotter to default conditions. See the table in Appendix C. 

## DI The Absolute Direction Instruction 

## Page 5-10 

DI run, rise ; 

Purpose: Sets the direction of labels. 

- Parameters: run, rise — decimal values, unitless. At least one must be nonzero, i.e., | parameter| > 0.0004 . 

Omitting parameters causes horizontal labels and is the same as DI1,0. 

## DP The Digitize Point Instruction 

## Page 6-2 

- DP (;) 

Purpose: Places plotter in digitize mode waiting for point to be entered from front panel. 

## DR The Relative Direction Instruction 

Page 5-11 

- DR run, rise ; 

Purpose: Sets the direction of labels. 

Parameters: decimals, —128 to +127.9999. 

run is % of (P2x — P1x), rise is % of (P2y — Ply). 

Omitting parameters causes horizontal labels as does DR1,0. 

INSTRUCTION SYNTAX B-3 
