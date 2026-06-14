The timing of output depends on the plotter’s interface (HP-IB, HP-IL, or RS-282-C). Refer to A Brief Word about Plotter Output in Chapter 7 for more information. 

The pen position and status are output to the computer as integers in ASCII in the form: 

## X,Y,P [TERM] 

- where X is the X-coordinate of the digitized point in plotter units, Y is the Y-coordinate of the digitized point in plotter units, Pis the pen status when the point was entered (0 = pen up, 1 = pen down), and 

- [TERM] is the output terminator for your system (refer to Chapter 7). 

The ranges of the X- and Y-coordinates are the mechanical limits of the plotter as determined by the setting of the paper switch. 

Upon receipt of the OD command by the plotter, bit position 2 of the output status byte is cleared. 

## Digitizing with the 7470 

When using the plotter as a digitizer, it is important to ascertain that a point has been entered before an attempt is made to retrieve that point using the OD command. There are three methods for doing this. 

## Manual Method 

The first method, which might be called the manual method, is easiest to understand. It is not efficient in applications where many points will be entered, or in an RS-232-C environment where the mainframe is not adjacent to the plotter or where human intervention in program execution is not possible. The steps in this method are as follows: 

1. In a program, send a DP command to the plotter. Follow the DP command immediately with a statement that will cause the program to display or print a message prompting you to enter a point. Follow the prompt with a statement that will cause the program to pause until instructed to continue. The BASIC statement PAUSE will accomplish this. 

2. Move the digitizing sight (pen) to the point to be entered, using frontpanel buttons. Final positioning should be done with the sight (pen) down. 

3. Press ENTER on the plotter’s front panel. Now resume running of the program. This is done on HP desktop computers by pressing the key marked CONTINUE or CONT. 

6-4 DIGITIZING 
