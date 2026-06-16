## CS The Designate Standard Character Set Instruction

C8 In (;)

Purpose:

Designates the standard character set.

Parameter:

integer, 0 through 4; default set 0.

## DC The Digitize Clear Instruction

DC ( ;)

Purpose:

## Page 5-3

## Page6-3

Clears digitize mode without entering a point from the front panel.

## DF The Default Instruction

DF ;

Purpose:

Page1-10

Returns plotter to default conditions. See the table in Appendix C.

## DI The Absolute Direction Instruction Page5-10

DI run, rise ;

Purpose:

Sets the direction of labels.

Parameters:

run, rise -decimal values, unitless. At least one must be nonzero, i.e., |parameter| 2 0.0004. |

Omitting parameters causes horizontal labels and is the sameas Dl1,0.

## DP The Digitize Point Instruction Page6-2

DP (;)

Purpose:

Places plotter in digitize mode waiting for point to be entered from front panel.

## DR The Relative Direction Instruction Page5-11

DR run, rise ;

Sets the direction of labels.

decimals, -128 to +127.9999.

run is %of (P2,; / Plx), rise is %of (P2y -Ply).

Purpose:

Parameters:

Omitting parameters causes horizontal labels as does DR1,0.
