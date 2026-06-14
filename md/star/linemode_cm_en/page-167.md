## **ESC GS s I z e a n c1 c2 d1 d2 t1 t2 … 0xFF** 

[Name] Register automatic audio setting information [Code] ASCII ESC GS s I z e a n c1 c2 d1 d2 t1 t2 … 0xFF Hexadecimal 1B 1D 73 49 z e a n c1 c2 d1 d2 t1 t2 … FF Decimal 27 29 115 73 z e a n c1 c2 d1 d2 t1 t2 … 255 

[Defined Area] z = 0, 1 0 ≤ e ≤ 63(0x3F) a = 1, 49 0 ≤ n ≤ 255 0 ≤ c1 + c2 x 256 ≤ 65535 0 ≤ d1 + d2 x 256 ≤ 65535 0 ≤ t1 + t2 x 256 ≤ 65535 

|e<br>Printer Internal Status<br>~~a~~<br>~~aa~~|a<br>~~OC~~<br>~~OO~~|n<br>~~OC~~<br>~~OO~~|c1 + c2x256<br>~~OC~~<br>~~OO~~|d1 + d2x256<br>~~OO~~|t1 + t2x256<br>~~OO~~|
|---|---|---|---|---|---|
|0x00<br>Cutter error<br>~~aa~~|0<br>~~OO~~|1<br>~~OO~~|1<br>~~OO~~|0<br>~~OO~~|0<br>~~OO~~|
|0x01<br>Flash ROM error<br>~~a a ~~<br>~~SC~~<br>~~**a**~~<br>~~a~~|0<br> ~~OO~~<br>~~SC~~<br>~~a~~|2<br>~~OO~~<br>~~SC~~<br>|1<br>~~OO~~<br>~~SC~~<br>|0<br>~~OO~~<br>~~SC~~|0<br>~~OO~~<br>~~SC~~|
|0x02<br>EE-PROM error<br>~~SC~~<br>~~**a**~~<br>~~a~~<br>~~—~~|0<br>~~SC~~<br>~~a~~<br>|3<br>~~SC~~<br>~~SC~~<br>|1<br>~~SC~~<br>~~SC~~<br>|0<br>~~SC~~<br>|0<br>~~SC~~<br>|
|0x03<br>SRAM error<br>~~**a**~~<br>~~a~~<br>~~—~~|0<br>~~a ~~<br>|4<br> ~~SC~~<br>|1<br>~~SC~~<br>|0<br>|0<br>|
|0x04<br>Head<br>temperature<br>detection error<br><br>~~— |~~<br>~~a~~|0<br> <br>~~|~~|5<br> ~~SC~~<br>~~|~~<br>~~CO~~|1<br>~~SC~~<br>~~|~~<br>~~CO~~|0<br>~~|~~|0<br>~~|~~|
|0x05<br>Power voltage error<br><br>~~— |~~<br>~~a~~<br>~~a~~|0<br> <br>~~|~~<br>~~a~~|6<br> ~~SC~~<br>~~|~~<br>~~a~~<br>~~CO~~|1<br>~~SC~~<br>~~|~~<br>~~a~~<br>~~CO~~|0<br>~~|~~<br>~~a~~|0<br>~~|~~<br>~~a~~|
|0x06 to 0x0F<br>(Reserved)<br>~~a~~|0<br>~~CC~~|0<br>~~CO~~<br>~~CC~~|0<br>~~CO~~<br>~~CC~~|0<br>~~CC~~|0<br>~~CC~~|
|0x10<br>BM Error<br>~~CC~~|0<br>~~CC~~|7<br>~~CC~~|1<br>~~CC~~|0<br>~~CC~~|0<br>~~CC~~|
|0x11<br>PE error<br>~~a~~|0<br>~~OC~~|8<br>~~OC~~|1<br>~~OC~~|0<br>~~OC~~|0<br>~~OC~~|
|0x12<br>Cover open<br>~~SC~~|0<br>~~SC~~|9<br>~~SC~~|1<br>~~SC~~|5<br>~~SC~~|0<br>~~SC~~|
|0x13<br>NE error<br>~~SC~~|0<br>~~SC~~|10<br>~~SC~~|1<br>~~SC~~|0<br>~~SC~~|0<br>~~SC~~|
|0x14 to 0x1F<br>(Reserved)<br>~~a~~<br>~~a~~<br>~~ee ee~~|0<br>~~ee~~|0<br>~~C~~<br>~~ee~~|0<br>~~C~~<br>~~ee~~|0|0|
|0x20<br>Head<br>high<br>temperature stoperror<br>~~a~~<br>~~ee ee~~|0<br>~~ee~~|11<br>~~ee~~|1<br>~~ee~~|0|0|
|0x21 to 0x2F<br>(Reserved)<br>~~a~~<br>~~ee ee~~<br>~~CC~~|0<br>~~ee~~<br>~~CC~~|0<br>~~ee~~<br>~~CC~~|0<br>~~ee~~<br>~~CC~~|0<br>~~CC~~|0<br>~~CC~~|
|0x30<br>Idling<br>~~A~~|0<br>~~OC~~|0<br>~~OC~~<br>~~SC~~|0<br>~~OC~~<br>~~SC~~|0|0|
|0x31 to 0x3F<br>(Reserved)<br>~~a~~|0<br>~~a~~|0<br>~~a~~<br>~~SC~~|0<br>~~a~~<br>~~SC~~|0<br>~~a~~|0<br>~~a~~|



[Function] When z = 1, the automatic audio setting information returns to the default factory setting. (At this time, do not send parameters after e.) 

When z = 0, register the automatic audio setting information to playback when the printer’s internal status occurs. e specifies the printer’s internal status assigned to audio. a specifies the area where the audio data to set is stored. a Audio data storage area 1, 49 User area n specifies the audio number to playback. However, when n = 0, or audio data of a specified number is not registered, automatic audio is invalid. (c1 + c2 x 256) specifies the number of times. (d1 + d2 x 256) specifies the delay time. Delay time is the time from the occurrence of the printer’s internal status to the start of audio playback (in seconds). (t1 + t2 x 256) specifies the interval time. Interval time is the time from the end of the previous audio to the start of the next audio (in seconds). You can register multiple times by repeating parameters e to t2. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-149 
