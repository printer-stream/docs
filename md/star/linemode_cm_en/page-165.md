## **3.18. Audio Command Details** 

**ESC GS s O z a n c1 c2 d1 d2 t1 t2** 

|[Name]|Playback NV audio|Playback NV audio|||||||
|---|---|---|---|---|---|---|---|---|
|[Code]|ASCII<br>ESC<br>GS<br>s<br>O<br>z<br>a<br>n||c1|c2|d1|d2|t1|t2|
||Hexadecimal<br>1B<br>1D<br>73<br>4F<br>z<br>a<br>n||c1|c2|d1|d2|t1|t2|
||Decimal<br>27<br>29<br>115<br>79<br>z<br>a<br>n||c1|c2|d1|d2|t1|t2|
|[Defined Area]<br>Z = 0|||||||||
|||a = 0, 1, 48, 49|||||||
|||1≤<br> n≤<br> 255|||||||
|||1≤<br> c1 + c2x256≤<br> 65535|||||||
|||0≤<br> d1 + d2x256≤<br> 65535|||||||
|||0≤<br> t1 + t2x256≤<br> 65535|||||||
|[Initial Value]||---|||||||
|[Function]||Plays back the specified NV audio.|||||||
|||a specifies the area where the audio data toplayback is stored.|||||back is stored.||
|||a<br>Audio data storage area|||||||
||1,49|49<br>User area|||||||
|||n specifies the audio number to playback.|||||||
|||(c1 + c2 x 256) specifies the number of times.|||||||
|||(d1 + d2 x 256) specifies the delay time.|||||||
|||Delay time is the time from starting to process this command to the start of audio playback|||||Delay time is the time from starting to process this command to the start of audio playback|Delay time is the time from starting to process this command to the start of audio playback|
|||(in seconds).|||||||
|||(t1 + t2 x 256) specifies the interval time.|||||||
|||Interval time is the time from the end of the previous audio to the start of the next audio|Interval time is the time from the end of the previous audio to the start of the next audio|Interval time is the time from the end of the previous audio to the start of the next audio|||Interval time is the time from the end of the previous audio to the start of the next audio|Interval time is the time from the end of the previous audio to the start of the next audio|
|||(in seconds).|||||||
|||If audio is already being played back, playback after waiting for the end of the audio.|||||||
|||If the printer is printing, playback after printing is ended.|||||||
|||When the parameter has an invalid value, there is no audio playback.||When the parameter has an invalid value, there is no audio playback.|||||
|||If the audio data of the specified audio number has not been registered, there will be no|||If the audio data of the specified audio number has not been registered, there will be no||||
|||playback.|||||||
|||Audio will stop by inputting the FEED switch while there is audio playback using this command.|||||||
|||Audio will stop using the NV audio stop command (ESC GS s P) while there is audio playback||||||Audio will stop using the NV audio stop command (ESC GS s P) while there is audio playback|
|||using this command.|||||||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-147 
