## **ESC GS s P** 

[Name] Stop NV audio [Code] ASCII ESC GS s P Hexadecimal 1B 1D 73 50 Decimal 27 29 115 80 --[Defined Area] --[Initial Value] [Function] Stops audio playback for the following reasons. O NV audio playback command ESC GS s O 0 NV audio lump playback command ESC GS s T When run in real-time when this command is received This command is ignored with there is no audio playback. 

## **ESC GS s R z n1 n2 n3 d1 … dn** 

|[Name]|Playback received audio|Playback received audio|Playback received audio|||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|
|[Code]|ASCII|ESC|GS<br>s|R|z|n1|n2|n3|d1|…|dn|
||Hexadecimal<br>1B||1D 73|52|z|n1|n2|n3|d1|…|dn|
||Decimal|27|29 115|82|z|n1|n2|n3|d1|…|dn|
|[Defined Area]||Z = 0||||||||||
|||1≤<br> (n = n1 + n2 x 256 + n3 * 65536)||(n = n1 + n2 x 256 + n3 * 65536)≤<br>|||16777215|||||
|||0≤<br> d≤<br> 255||||||||||
|[Initial Value]||---||||||||||
|[Function]|[Function]|Does not register audio data in the non-volatile memory and plays back one time while receiving||||Does not register audio data in the non-volatile memory and plays back one time while receiving|||||Does not register audio data in the non-volatile memory and plays back one time while receiving|
|||data.||||||||||
|||(n1 + n2 x 256 + n3 x 65536) specifies the number of bytes of the audio data.|||||(n1 + n2 x 256 + n3 x 65536) specifies the number of bytes of the audio data.||(n1 + n2 x 256 + n3 x 65536) specifies the number of bytes of the audio data.|||
|||d is audio data in sampling frequency of 11.025 kHz, ADPCM format in quantization bit rate of 4|||||d is audio data in sampling frequency of 11.025 kHz, ADPCM format in quantization bit rate of 4|||||
|||bits.||||||||||
|||When data transfer from the host is slow (theoretical value: 44,100 bps or lower), playback is||||When data transfer from the host is slow (theoretical value: 44,100 bps or lower), playback is||||||
|||intermittent.||||||||||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-148 
