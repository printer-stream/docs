<!-- image -->

## ESC * r s 0 a n NUL

[Name] Set raster mode NV audio playback number

[Code] ASCII ESC * r s 0 a n NUL Hexadecim al 1B 2A 72 73 30 a n 00 Decimal 27 42 114 115 48 a n 0

[Defined Area]

a = 48, 49

'1' ≤ n ≤ '255'

[Initial Value] [Function]

No audio playback number setting.

Set the audio playback number to play in the raster mode audio playback command (ESC * r S). a specifies the area where the audio data to playback is stored.

a

49

Audio data storage area

User area

n is a decimal description (max. 5 digits) using ASCII characters.

No setting when the parameter is not defined. Invalid in Page Mode.

-----------------------------------------------------------------------------
