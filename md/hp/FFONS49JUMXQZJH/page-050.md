Error 3 will be set (parameter out of range). A PR command with out of range parameters will still establish relative plotting mode for future occurrences of PD or PU with parameters. 

When scaling is off, in-range parameters are between —32 768 and 32 767. When scaling is on, in-range parameters and their plotter unit equivalent must be between —32 768 and 32 767. To find plotter unit equivalents, refer to the section Converting from User Units to Plotter Units in Appendix C. 

The following strings of HP-GL instructions, when sent to the plotter using your computer’s output statements, cause triangles to be drawn that are identical to the ones previously drawn using only the PA instruction. The numbers in parentheses on the plot are the X.Y increments of the PR commands. The numbers without parentheses are the plotter unit coordinates of the vertices. 

- "TH; SP1;" 

- "PAZ000, 1500,PD,PR-Z000,0, 2000, 2000,0, -Z000,PU,500, 03" "PDZ000,0, -2000, 2000,0, -2000, PU;" 

**==> picture [323 x 204] intentionally omitted <==**

**----- Start of picture text -----**<br>
2000 , 3500 2500 , 3500<br>(2000 , 2000) {-2000 , 2000)<br>vA NN<br>a Fz KN ”<br>0, 1500 START 2500 , 1500 4500 , 1500<br>(-2000 , 0) 2000 , 1500 (500 , 0) (2000, 0)<br>{0 , -2000) (0 , -2000) END<br>**----- End of picture text -----**<br>


3-10 CONTROLLING THE PEN AND PLOTTING 
