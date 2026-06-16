<!-- image -->

## ESC GS s P

[Name]

Stop NV audio

[Code]

ASCII

ESC GS s P

Hexadecimal

1B 1D 73 50

Decimal

27 29  115 80

[Defined Area]

---

[Initial Value]

---

[Function]

Stops audio playback for the following reasons.

- [ ] NV audio playback command ESC GS s O

- [ ] NV audio lump playback command ESC GS s T

When run in real-time when this command is received

This command is ignored with there is no audio playback.

## ESC GS s R z n1 n2 n3 d1 … dn

[Name] Playback received audio

[Code]

ASCII

ESC GS s R z n1 n2 n3 d1 … dn

Hexadecimal

1B 1D 73 52 z n1 n2 n3 d1 … dn

Decimal

27 29  115 82 z n1 n2 n3 d1 … dn

[Defined Area]

Z = 0

1 ≤ (n = n1 + n2 x 256 + n3 * 65536) ≤ 16777215 0 ≤ d ≤ 255

[Initial Value] [Function]

---

Does not register audio data in the non-volatile memory and plays back one time while receiving data.

(n1 + n2 x 256 + n3 x 65536) specifies the number of bytes of the audio data.

d is audio data in sampling frequency of 11.025 kHz, ADPCM format in quantization bit rate of 4 bits.

When data transfer from the host is slow (theoretical value: 44,100 bps or lower), playback is intermittent.

-----------------------------------------------------------------------------
