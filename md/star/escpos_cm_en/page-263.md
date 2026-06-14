Rev.2.52 

## **ESC GS s T a t1 t2** 

|Name|Batch Playback|Batch Playback|NV Audio|NV Audio||||
|---|---|---|---|---|---|---|---|
|Code|ASCII|ESC|GS|s|T|t1|t2|
||Hex.|1B|1D|73|54|t1|t2|
||Decimal|27|29|115|84|t1|t2|



Defined Region a =  1,  49 0 ≤ t1 + t2 x 256 ≤ 65535 Initial Value --Function Lump-playback of NV audio registered in the non-volatile memory from #1 in ascending order. a specifies the audio data registration area. 

a Audio data storage area 1, 49 User area (t1 + t2 x 256) specifies how many seconds from the top to playback each audio data. 

However, when (t1 + t2 x 256) = 0, plays back each audio data completely without specifying the number of seconds. 

Insert 1 second of interval time between the previous audio and the next audio. 

Audio will stop by inputting the FEED switch while this command is running. 

Audio will stop using the NV audio stop command (ESC GS s P) while running this command. 

ESC/POS Command Specifications 

263 
