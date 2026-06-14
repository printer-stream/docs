Negative parameters greater than or equal to —32 768 will be set to zero. Parameters outside the maximum plotting area (determined by the setting of the paper switch) but less than 32 767 will be set to the limits of the plotting area. Parameters less than —32 768 or greater than 32 767 will cause error 3 and the coordinates of P1 and P2 will not change. 

An IP command without parameters will default Pl and P2 to the values 250 , 279, 10 250, 7479 regardless of the paper switch setting. 

Upon receipt of a valid IP command, bit position 1 of the output status word is set true (1). oe 

Upon power on, front-panel reset, or execution of an IN or DF command, the character size is set relative (SR) to the locations of P1 and P2. Unless an SI command has been entered as part of the program, the character size will be directly affected by the IP command. 

The following HP-GL command relocates the scaling points P1 and P2 to the positions shown in the figure. 

"IP 3000,2000,5000,5000;" 

**==> picture [96 x 85] intentionally omitted <==**

**----- Start of picture text -----**<br>
© P2<br>(5000,5000)<br>@Pi<br>{3000,2000)<br>**----- End of picture text -----**<br>


The Output P1 and P2 Instruction, OP SHEE §=The output Pl and P2 instruction, OP, provides the means to make the current coordinates of Pl and P2 available for output. 

ESTABLISHING BOUNDARIES AND UNITS 2-5 
