## C O N F I D E N T I A L

[Model-dependent variations]

## TM-J2000/J2100 , TM-T90 , TM-L90 , TM-T20 , TM-T88IV , TM-T88V , TM-T70 , TM-P60

## Program Example

PRINT #1, CHR$(&amp;H10);CHR$(&amp;H14);CHR$(2);CHR$(1);CHR$(8);

GOSUB *RECEIVE

← Confirmation Ò power off notice Ò

## TM-J2000/J2100 , TM-T90 , TM-L90

The BUSY condition is selected by memory switch 1-3.

While processing a set up of power-off, the POWER LED blinks fast and changes to slow blinking after the printer transmits a power-off notice. Be sure that the POWER LED is blinking slowly; then turn off the power switch.

When DIP switch [SW1-1] is ON, the power will not be turned off by this command. Be sure that the power is turned off by an operator.

## TM-T20

The BUSY condition is selected by memory switch 1-3. The power will not be turned off by this command. Be sure that the power is turned off by an operator.

## TM-T88IV , TM-T88V , TM-T70

The BUSY condition is selected by DIP switch 2-1.

The power will not be turned off by this command. Be sure that the power is turned off by an operator.

## TM-P60

When memory switch [Msw8-1] is OFF, the power-off notice is not transmitted.

This command processes power-off disconnection.
