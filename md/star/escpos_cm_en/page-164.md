Rev.2.52 

## **FS – n** 

Name Specify/cancel Chinese character underline Code ASCII FS - n Hex. 1C 2D n Decimal 28 45 n Defined Region 0 ≤ n ≤ 2, 48 ≤ n ≤ 50 Initial Value n = 0 Function Specifies or cancels Chinese character underlines. 

|||n|Function||
|---|---|---|---|---|
||0,|48|Cancels Chinese character underline||
||1,|49|Sets to one-dot width Chinese character underline and specifes Chinese<br>character underlines.||
||2,|50|Sets to two-dot width Chinese character underline and cancels Chinese<br>character underlines.||
|Details|||• An underline is applied to Chinese characters for the entire character width, including the left||
||||and right character space amount.||
||||However, underlines are not applied to portions that have been skipped using HT (horizontal||
||||tab) or rotated 90 degrees to the right.||
||||• When Chinese character underline mode is cancelled by setting the value of n to 0,||
||||subsequent Chinese character data is not underlined, and the underline thickness set before<br>the mode is turned of is maintained.||
||||In default, the underline width for Chinese characters is set to 1 dot.||
||||• The set Chinese character underline width is the constant specifed thickness regardless of||
||||the size of the character.||
||||• The FS ! (Batch specify Chinese character print mode) command can also turn Chinese<br>character underline mode on or of, but the setting of the last received command is efective.||
|STAR|||• This command is ignored when the memory switch location of use is specifed as SBCS||
||||(single byte countries).||
||||• The underline for Chinese characters is applied in the following positions.||
||||• 1-dot width underline → 24thdot||
||||• 2-dot thickness underline → 23rdand 24thdot||
|Reference|||FS !||



ESC/POS Command Specifications 

164 
