between variables to cause the label string to be right-justified in a specific character-field width. The unused character positions in this field are normally sent as leading blank spaces to establish fixed spac­ ing between label strings. For close spacing of label strings, the blank spaces can normally be suppressed by substituting a semicolon as a delimiter between variables.

The following example illustrates use of the comma to establish fixed spacing when using variables for labeling. When the value of X is 50, the labels shown are produced by the given HP-GL instructions. The first statement causes the plotter to label the value of X, X+1, and X+2. Blank spaces between the printed integers normally include space for the sign which may or may not be printed depending on your computer. The number of blank character-field spaces may vary with different computers.

<!-- image -->

The following example illustrates the closer spacing achieved in BASIC when semicolons separate variables in labeling commands. The semi­ colons between the variables cause suppression of blank spaces. The space between the printed integers varies with different computers, but normally includes the sign space.

ll ;X+2;|lE|| Xp X+1

## 50 51 52

Any spaces required to fit into the context of the item being labeled must normally be sent enclosed in quotes. The following example labels the same variables as above, but with four extra spaces between each of the integers. Note that four spaces enclosed in quotes are sent be­ tween each variable, but the semicolon suppresses unwanted blank spaces.

<!-- image -->

*
