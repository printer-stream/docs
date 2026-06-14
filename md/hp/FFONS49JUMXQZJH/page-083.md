Specifying both parameters as zero will set error 3, and having only one or more than two parameters will set error 2. The plotter will ignore such instructions. 

## Spacing Between Characters 

Character spacing and line spacing are functions of character size. In the diagram below, you can see the relative position of a character, in this case M, within the character space. The character-space field is set indirectly by the SI command, since the character space height is twice the character’s height and the character-space width is 1% times the character’s width. The space above and beside a drawn character becomes the spacing between lines and characters. The character space is illustrated below. 

**==> picture [237 x 190] intentionally omitted <==**

**----- Start of picture text -----**<br>
SPACECHARACTER WIDTH = W | —<br>re ne oe<br>l|<br>||<br>|<br>| | CHARACTER<br>| HEIGHTSPACE=H<br>CHARACTER |<br>HEIGHT =O5H |<br>|<br>en Se ee<br>CHARACTER CHARACTER STARTING POINT<br>STARTING WIDTH OF NEXT<br>POINT =0.67W CHARACTER<br>**----- End of picture text -----**<br>


When you specify the height of a character in an SI or SR command, however, you should specify the character height, not the height of a character space. 

## The Character Plot Instruction, CP 

WHA =The character plot instruction, CP, moves the pen the specified number of character-space fields. WISE The instruction can be used to move the pen any number of character spaces or lines from a point on the plotting surface, to align with a left-hand margin, or to center or right-justify a label. Thus, the 

LABELING 5-13 
