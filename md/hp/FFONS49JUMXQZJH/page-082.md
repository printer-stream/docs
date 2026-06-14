UNS9 = The instruction can be used to change the direction of lettering from its default direction, horizontal, to a direction which is relative to P1,P2 settings. It is useful when creating graphs which will be plotted in several sizes and you want labels to have the same relationship to the data on all plots. 

## SYNTAX 

Baye run, rise terminator or DR terminator 

Ae §=Run and rise are in decimal format, 0 to +127.9999, and specify the label direction according to the same relationship specified in The Absolute Direction Instruction, DI. 

Run and rise specify a percentage of the algebraic distance between P1 and P2 where run is the desired percentage (—128 to 127.9999) of P2x — P1x , rise is the desired percentage (—128 to 127.9999) of P2y — Ply, and P1 and P2 are the scaling points. 

If you imagine the current pen position to be the origin, the sign of the parameters determines in which quadrant the lettering will be. In the example below, rise and run assume all combinations of +1 with default P1 and P2. 

**==> picture [335 x 187] intentionally omitted <==**

**----- Start of picture text -----**<br>
No<br>>> ae<br>+RISE-RUN “23y/p ©& +RUN<br>04 +RISE<br>-RUN-RISE «© OL +RUN-RISE<br>P Op,<br>“y YW<br>Re<br>A change in P1 or P2 will affect the direction of lettering. Refer to the<br>section Parameter Interaction in Labeling Commands.<br>**----- End of picture text -----**<br>


A DR command remains in effect until another DR or DI command or an IN or DF command or front-panel initialization is executed. A DR command with no parameters will default to the values DR 1,0 (horizontal). 

5-12 LABELING 
