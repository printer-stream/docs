<!-- image -->

Details

Reference

- This command is effective for all characters (ANK and Chinese characters), excluding HRI characters.
- If the vertical and horizontal magnification ratios are outside the defined range, this command is ignored.
- In standard mode, the vertical direction is the paper feed direction; the horizontal direction traverses the paper feed direction. Therefore, when character orientation changes in 90 degree clockwise rotation mode, the relationship between vertical and horizontal directions is reversed.
- In page mode, vertical and horizontal directions are based on the character orientation.
- The base line for characters is the same when there are characters having different vertical direction ratios in the same line.
- The ESC ! (Batch specify print mode) command can also turn double-width and doubleheight modes on or off, but the setting of the last received command is effective.

ESC !
