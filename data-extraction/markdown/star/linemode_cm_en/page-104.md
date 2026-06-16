<!-- image -->

## ESC * r s 1 n NUL

[Name]

Set raster mode NV audio playback count

[Code]

ASCII ESC * r s 1 n NUL

Hexadecim 1B 2A 72 73 31 n 00

al

Decimal

27 42 114 115 49 n 0

[Defined Area]

'1' ≤ n ≤ '65535'

[Initial Value]

No audio playback count setting.

[Function]

Set the audio playback count to n times in the raster mode audio playback command (ESC * r S).

n is a decimal description (max. 5 digits) using ASCII characters.

No setting when the parameter is not defined.

Invalid in page mode.

## ESC * r s 2 n NUL

[Name] Set raster mode NV audio playback delay time

[Code] ASCII

* r s 2 n NUL ESC

Hexadecimal

1B 2A 72 73 32 n 00

Decimal

27 42 114 115 50 n 0

[Defined Area]

'0' ≤ n ≤ '65535'

[Initial Value]

n = '0'

[Function]

Set  the  audio  playback  delay  time  to  n  second  in  the  raster  mode  audio  playback  command (ESC * r S).

Delay time  is  the  time  from  starting  processing  of  the  raster  mode  audio  playback  command (ESC * r S) to the start of audio playback.

n is a decimal description (max. 5 digits) using ASCII characters.

No setting when the parameter is not defined.

Invalid in page mode.

## ESC * r s 3 n NUL

[Name] Set raster mode NV audio playback interval time

[Code] ASCII

ESC * r s 3 n NUL

Hexadecimal

1B 2A 72 73 33 n 00

Decimal

27 42 114 115 51 n 0

[Defined Area]

'0' ≤ n ≤ '65535'

[Initial Value]

n = '0'

[Function]

Set the audio playback interval time to n second in the raster mode audio playback command (ESC * r S).

Interval time is the time from the end of audio to the start of the next audio.

n is a decimal description (max. 5 digits) using ASCII characters.

No setting when the parameter is not defined.

Invalid in page mode.

-----------------------------------------------------------------------------
