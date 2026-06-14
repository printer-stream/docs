corner of the first character space and the carriage-return point. After lettering a character, the pen stops at the lower-left corner of the next character space as shown below. For a further explanation of character spacing, refer to Spacing Between Characters in this chapter. 

**==> picture [201 x 186] intentionally omitted <==**

**----- Start of picture text -----**<br>
—<br>| WIDE |q—<br>a oe<br>CHARACTER —<br>STARTING ~+— SPACE _.<br>POINT<br>KA<br>**----- End of picture text -----**<br>


When the plotter receives the character, carriage return, while in label mode, it returns to a defined carriage-return point. The carriage-return point usually reflects the pen’s position when the preceding LB instruction was executed. The carriage-return point is updated to the current pen position whenever: 

- © one of the following instructions is executed: PA, PR, DI, DR, AA, AR, RO, DF, or IN. 

- ® you use the front-panel CLEAR and RESET function keys or use the pen controls to move the pen to a new point. 

## Labeling with Variables 

In some applications, it is desirable to label the plot using variables rather than literals to define the label string. Many different conventions are used in different computer languages and computers to define variable length and the character field format in which these variables will be printed. To avoid unexpected placement of the labels defined by variables, refer to your computer manual for a definition of the conventions used to define the output character field. 

Quotation marks are used by many computers to define the literal characters that are to be sent, but variables are not included within quotation marks. The comma is used by some computers as a delimiter 

5-8 LABELING 
