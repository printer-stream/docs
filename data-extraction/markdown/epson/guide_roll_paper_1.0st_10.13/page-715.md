## C O N F I D E N T I A L

| 8-7   |   50 | Reserved                                                           |
|-------|------|--------------------------------------------------------------------|
| 8-8   |   48 | Roll paper cover open during printing: automatic recoverable error |
| 8-8   |   49 | Roll paper cover open during printing: recoverable error           |

| [Msw8-2]   | Recovery operation from error                                                                                                                                                                                                                                                                                                                                                                      |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OFF        | Can recover from the error by opening/closing the printer cover or by executing DLE ENQ. While the printer recovers from the error, paper layout is measured automatically and paper is fed to the label print starting position. If the paper layout is stored in the non-volatile memory, it will be rewritten. Afterwards, the printer operates following the paper layout previously measured. |
| ON         | Can recover by executing DLE ENQ. While the printer recovers from the error, paper is fed to the label print starting position. The paper layout stored in the non-volatile memory will not be changed. Change the setting of the paper layout stored in the non-volatile memory so that it matches the currently used paper layout. See function 49 of this command for setting the paper layout. |

<!-- image -->
