## **ESC * r S** 

[Name] Raster mode NV audio playback [Code] ASCII ESC * r S Hexadecim 1B 2A 72 53 al Decimal 27 42 114 83 

[Defined Area] --[Initial Value] --[Function] Plays back the specified NV audio. 

You must set the operating conditions using the audio playback setting command before sending this command. 

(1) ESC * r s 0 a n NUL Number 

(2) ESC * r s 1 n NUL Number of times 

(3) ESC * r s 2 n NUL Delay time 

(4) ESC * r s 3 n NUL Interval time 

(5) ESC * r S Playback 

((1) to (4) can be in any order.) 

Delay time is the time from processing this command to the start of audio playback. Interval time is the time from the end of audio to the start of the next audio. 

If audio is already being played back, run after waiting for the end of the audio. If the printer is printing, run after printing is ended. 

If the audio data of the specified audio number has not been registered, there will be no playback. Audio will stop by inputting the FEED switch while this command is running. Invalid in page mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-84 
