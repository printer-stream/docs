4. The program step following the pause will now be executed. The next steps of the program, in order, should be an OD command to the plotter, a read statement by the computer to read the X- and Y-coordinates and the pen status, a statement to remove the prompt (requesting you to enter a point) from the screen, and then steps to process the digitized data in the appropriate manner. 

Using this method, there is no need to monitor the status byte because the program does not proceed to the OD command until the user enters a point and causes the program to resume. 

A simpler procedure, using OA or OC instead of OD, can also be used. It omits the DP in step 1 and pressing ENTER in step 3. Using the shorter procedure with OC makes it possible to obtain coordinate values in user units. Refer to Chapter 7. 

A short program to digitize a single point and display the coordinates and pen status is given below. The program is in BASIC for an HP-85 with an HP-IB interface. An I/O ROM is required in order to execute the ENTER statement to obtain the digitized point. 

- 10 PRINTER IS 705,80 20 PRINT "DP;" 30 DISP "ENTER A POINT" 40 PAUSE SO PRINT "OD;" 60 ENTER 705 ; X,Y,P 70 DISP X;Y;P 80 END 

## Monitoring the Status Byte 

The second method can be used with any interface and is the only method of checking based on software that can be done in an RS-232-C environment. This method monitors bit position 2, the third least significant bit, of the plotter’s status byte which is set when a digitized point is available. Refer to The Output Status Instruction, OS, Chapter 7 for more information. 

Monitoring bit position 2 can be done in a variety of ways depending on the commands available on the computer being used. If there are instructions to check bits directly, the third least significant bit (Isb) should be checked for the occurrence of a 1. If no bit operations are available, the status byte can be operated on arithmetically to check for the availability of a digitized point. Executing successive divisions of a number by two and checking for an odd or even integer answer is a common way of monitoring bits without converting the number to binary form. Either of the following sequences of BASIC instructions 

DIGITIZING 6-5 
