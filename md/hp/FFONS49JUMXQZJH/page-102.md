| 

will check the proper bit of the status byte. Insert as line 110 or line 1010 a suitable BASIC read statement to read the status byte into a variable called Status. 

400 PRINT "05S;" 110 | STORE STATUS BYTE IN Status 120 Status*®INT(Status/’2) !SHIFTS BITS RIGHT ONE POSITION 130 Status*INT(Status’2) !SHIFTS BITS RIGHT AGAIN 140 Status=Status MOD 2 !THIS RESULT IS O IF LSB NOT 1 150 IF Status*0 THEN 100 160 PRINT "OD;" !ISEND OD SINCE POINT AVAILABLE 1000 PRINT "Q5S;" 1010 | STORE STATUS BYTE IN Status 1020 StatussINT(Status/’4) !SHIFTS BITS RIGHT 2 POSITIONS 1030 IF Status#INT(Status’zZ)*Z THEN 1000 !1sb NOT 1 1040 PRINT "0O0;" 

On some HP computers with an I/O ROM, the following three lines are equivalent to lines 100 to 150 of the first program segment shown. 

ZOO0O0 PRINT "05;" 2010 [THIS IS THE STATEMENT TO READ THE STATUS 2050 IF BIT(Status,2)20 THEN 2000 

In many applications, a large number of points need to be digitized. When the computer is used to monitor bit position 2, the points may or may not be processed immediately. In most applications, memory would be allocated for the total number of points to be digitized. A loop would be established to process the total number of points, calling the subroutine each time to check that a point had been entered. A complete BASIC program for an HP-85 with an HP-IB interface follows. This program prints out the 500 points after they all have been entered. 

6-6 DIGITIZING 
