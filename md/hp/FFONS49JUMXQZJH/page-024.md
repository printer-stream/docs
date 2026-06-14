## Ce EMULE §=No parameters are used; a numeric parameter will cause error 2 and the instruction will not execute. 

An IN command is the equivalent of switching the plotter off and then on again (except that conditions set by escape code sequences are not changed in an RS-232-C environment). The initialize command sets the plotter to the same conditions as the default command and sets these additional conditions. 

## e The pen is raised. 

- e The scaling points Pl and P2 are set to the points Pl = 250, 279 and P2 = 10 250, 7479. . 

- e All HP-GL errors are cleared. Bit position 3 of the output status byte is set to true(1) indicating the plotter has been initialized. (This bit is cleared by OS.) 

- e The setting of the us/a4 switch (for paper size) is read, thus establishing the limits within which the pen can move (mechanical hard clip limits). 

| The Input Mask Instruction, IM SHEE =The input mask instruction, IM, controls the conditions under which HP-GL error status is reported, the conditions that can cause an HP-IB service request message, and the conditions that can cause a positive response to an HP-IB parallel poll. USSF With all three interface configurations (HP-IB, HP-IL, and RS232-C), this instruction can be used to change the conditions under which HP-GL error status is reported. In an HP-IB system only, the instruction is used to enable the plotter to send a service request message when specified bits of the status byte are set, and/or enable a positive response to a parallel poll under the conditions specified. SQUENS 2) E-mask value (,S-mask value (,P-mask value)) (terminator) or IM (terminator) SELON «tn both the RS-232-C and HP-IL configurations, the S- and P-masks are of no use and are ignored if present. The E-mask is used by all three configurations. 

The E-mask value specified is the sum of any combination-of the bit values shown in the following table. When an HP-GL error occurs, the bit in the E-mask corresponding to the error number as shown below is tested to determine if the error bit (bit 5) of the status byte is to be set and the front panel ERROR LED is to be turned on. If a bit is not set, | there is no way to ever determine if that error occurred. 
