—_— 

**==> picture [153 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
{f«*ss CIRCLE<br>CHORD ANGLE<br>**----- End of picture text -----**<br>


The most useful chord angle values range from 0 to 180; where 0 produces the smoothest circle and larger numbers progressively reduce the number of chords used. Values from 180 to 360 work just the opposite; i.e., larger numbers progressively increase the number of chords used and 360 produces the smoothest circle. This pattern follows modulo 360 through the permitted range of —32 768 to —32 767. Specifying out-of-range parameters sets error 3 and the command is ignored. 

The following strings of HP-GL instructions, when sent to the plotter using your computer’s output statements, show the effect of different chord angles. 

"IN; SP1;IPZ650,1325, 7650,6325;" "SC-100, 100, -100, 100;" 

"PA-50,40;CI30,45;" 

“PASO, 40;CI30, 303" 

- "PA-S0, -40;C1I30,15;" 

"PASO, -40;C130,5;" 

CONTROLLING THE PEN AND PLOTTING 3-13 
