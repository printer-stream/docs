<!-- image -->

## 4-3-17 Star	Original		Audio	Commands

## ESC	GS	s	O	z	a	n	c1	c2	d1	d2	t1	t2

Name

Playback NV Audio

Code

ASCII ESC GS s O z a n c1 c2 d1 d2 t1 t2

Hex. 1B 1D 73 4F z a n c1 c2 d1 d2 t1 t2

Decimal 27 29 115 79 z a n c1 c2 d1 d2 t1 t2

Defined Region

Z = 0

a = 0, 1, 48, 49

1 ≤ n ≤ 255

1 ≤ c1 + c2 x 256 ≤ 65535

0 ≤ d1 + d2 x 256 ≤ 65535

0 ≤ t1 + t2 x 256 ≤ 65535

Initial Value

---

Function

Plays back the specified NV audio.

a specifies the area where the audio data to playback is stored.

| a     | Audio data storage area   |
|-------|---------------------------|
| 1, 49 | User area                 |

n specifies the audio number to playback.

(c1 + c2 x 256) specifies the number of times.

(d1 + d2 x 256) specifies the delay time.

Delay time is the time from starting to process this command to the start of audio playback (in seconds).

(t1 + t2 x 256) specifies the interval time.

Interval time is the time from the end of the previous audio to the start of the next audio (in seconds).

<!-- image -->

If audio is already being played back, playback after waiting for the end of the audio.

If the printer is printing, playback after printing is ended.

When the parameter has an invalid value, there is no audio playback.

If the audio data of the specified audio number has not been registered, there will be no playback.

Audio will stop by inputting the FEED switch while there is audio playback using this command.

Audio will stop using the NV audio stop command (ESC GS s P) while there is audio playback using this command.
