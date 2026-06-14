Perform lump registration until 0xFF which is the end code. 

When the parameter is determined to be free of error, the printer starts processing this command. When the parameter has an invalid value, there is no setting. (Sets already determined to be free of problems are valid.) 

This command should be specified at the top of the line. After registering automatic audio setting information, reset the printer. 

Error processing mechanical operations or status processing and the like are not possible while registering automatic audio setting information (the time from receiving 0xFF which is the end code until printer reset is completed after automatic audio registration ends). 

Audio will stop by inputting the FEED switch while there is audio playback using this setting. 

Command Transmission Example Cutter error: User area 12[th] /3 times/delay 2 seconds/interval 1 second, Flash ROM error: User area 13[th] /4 times/delay 5 seconds/interval 6 seconds ESC GS s  I  z e  a  n  c1 c2 d1 d2 t1 t2 1B  1D 73 49 00 00 01 0C 03 00 02 00 01 00 01 01 0D 04 00 05 00 06 00 FF 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-150 
