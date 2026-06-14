## **ESC GS s T a t1 t2** 

|[Name]|Batch playback of NV audio|Batch playback of NV audio|Batch playback of NV audio||||
|---|---|---|---|---|---|---|
|[Code]|ASCII|ESC<br>GS|s<br>T|t1|t2||
||Hexadecimal<br>1B<br>1D||73<br>54|t1|t2||
||Decimal|27<br>29|115<br>84|t1|t2||
|[Defined Area]||a = 1, 49|||||
|||0≤<br> t1 + t2 x 256≤<br>|65535||||
|[Initial Value]||---|||||
|[Function]||Lump-playback of NV audio registered in the non-volatile memory from #1 in ascending order.|Lump-playback of NV audio registered in the non-volatile memory from #1 in ascending order.|||Lump-playback of NV audio registered in the non-volatile memory from #1 in ascending order.|
|||a specifies the audio data registration area.|||||
||a|Audio data storage area|||||
||1,49|User area|||||
|||(t1 + t2 x 256) specifies how many seconds from the top to playback each audio data.||(t1 + t2 x 256) specifies how many seconds from the top to playback each audio data.|(t1 + t2 x 256) specifies how many seconds from the top to playback each audio data.||
|||However, when () = 0, plays back each audio data completely without specifying the number of|However, when () = 0, plays back each audio data completely without specifying the number of||However, when () = 0, plays back each audio data completely without specifying the number of||
|||seconds.|||||
|||Insert 1 second of interval time between the previous audio and the next audio.|Insert 1 second of interval time between the previous audio and the next audio.||||
|||Audio will stop by inputting the FEED switch while this command is running.|||||
|||Audio will stop using the NV audio stop command (ESC GS s P) while running this command.||Audio will stop using the NV audio stop command (ESC GS s P) while running this command.|Audio will stop using the NV audio stop command (ESC GS s P) while running this command.||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-152 
