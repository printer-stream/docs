**==> picture [340 x 381] intentionally omitted <==**

**----- Start of picture text -----**<br>
The following example labels the years 1978 through 1985, in a circular<br>pattern starting with vertical labeling. The direction in which each<br>year is labeled is changed by 45 degrees. Then the labels in the center<br>are drawn to illustrate the use of cosine and sine values as parameters.<br>The label _*_2000 contains both a carriage return and a line feed<br>character before the label terminator, ETX, so the pen position at the<br>end of that label is one line below the beginning of that label. The fact<br>that DI commands update the carriage return point can be clearly seen<br>by observing the pen’s position at the end of the program. The final<br>character in the last label is a carriage return and the pen returns to .<br>the carriage return point, the position of the pen at the last DI<br>command.<br>“IN; SPZ;PA1050, 4450;"<br>"DIO, 1;LB_*_1978% DI1,1;LB_¥_197958"<br>“DI1,0;LB_*_19¢0% DI1,-1;LB_*_1981&"<br>"DIO, -1;LB_*_1982% DI-1,-1;LB_*_19834"<br>"DI-1,0;LB_¥_1984& DI-1,1;LB_*_1985%"<br>"PA1I509,5350;DI" ,COS(O), SINCOI;"LB_*_ 200084 &"<br>"DI" ,COS(-45);S1 NC-45)5"LB RETURN POINTS&!<br>a?_*_1980aa \%<br>FINAL PEN POSITION = Y “9.<br>CARRIAGE RETURN vont @2 2000 o|<br>nNa ‘, L*<br>"7 GW wo<br>* Y @<br>|<br>%<br>“~N Vp x<br>*\ K<br>veer —«¢<br>**----- End of picture text -----**<br>


NOTE: Check the format of the COS and SIN functions on your computer, and change these accordingly. Also, check your computer documentation to see how your computer interprets angles. If angles are interpreted as radians, you need to change to degrees before using the COS and SIN functions. On the HP Series 80 computers, execute the BASIC statement DEG. m 

The Relative Direction Instruction, DR SHUM §=6The relative direction instruction, DR, specifies the direction in which characters are lettered. 

LABELING 5-11 
