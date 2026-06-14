|n|Printing<br>Direction|Starting Point|
|---|---|---|
|0, 48|Left to<br>Right|Upper Left<br>(Drawing at<br>Right A)|
|1, 49|Bottom to<br>Top|Bottom Left<br>(Drawing at<br>Right B)|
|2, 50|Right to<br>Left|Bottom Right<br>(Drawing at<br>Right C)|
|3, 51|Top to<br>Bottom|Top Right<br>(Drawing at<br>Right D)|



• When standard mode is selected, only internal printer flag operations are executed when this command is entered. 

In that case, printing in standard mode is unaffected. 

- The starting point in the print region specified by ESC GS P 3 (Set print region in page mode) is used for the start of character expansion. 

## **ESC GS P 3 xL xH yL yH dxL dxH dyL dyH** 

[Name] Select character print direction in page mode 

[Code] ASCII ESC GS P 3 Hexadecimal 1B 1D 50 33 Decimal 27 29 80 51 [Defined Area] 0 ≤ xL, xH, yL, yH, dxL, dxH, dyL, dyH ≤ 255 However, this excludes dxL = dxH = 0 or dyL = dyH = 0. [Initial Value] xL = xH = yL = yH = 0 See the table below for dxL, dxH, dyL, and dyH. [Function] Set print region in page mode Sets the position and size of the print region. • Horizontal starting point = [(xL + xH x 256) x 1/8] mm • Vertical starting point = [(yL + yH x 256) x 1/8] mm • Horizontal direction length = [(dxL + dxH x 256) x 1/8] mm • Vertical direction length = [(dyL + dyH x 256) x 1/8] mm 

• When standard mode is selected, only internal printer flag operations are executed when this command is entered. Has no affect on printing. • If the horizontal or vertical starting point is outside of the print region, invalidate all settings. • If the horizontal or vertical length direction is 0, invalidate all settings. 

- The character expansion stating point is the one specified by the selection of the character printing direction (ESC GS P 2) in page mode in the print region. 

• If the (horizontal direction starting point + horizontal direction length) exceeds the horizontal direction printable region, the (horizontal direction printable region – horizontal direction starting point) becomes the horizontal direction length. 

• If the (vertical direction starting point + vertical direction length) exceeds the vertical direction printable region, the (vertical direction printable region – vertical direction starting point) becomes the vertical direction length. 

• If the calculated results is a fraction, that is corrected to the minimum mechanical pitch and excess is discarded. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-137 
