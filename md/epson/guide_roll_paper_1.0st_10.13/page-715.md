## **C O N F I D E N T I A L** 

|**8-7**|**50**|**Reserved**|
|---|---|---|
|**8-8**|**48**|**Rollpaper cover open during printing: automatic recoverable error**|
||**49**|**Rollpaper cover open during printing: recoverable error**|



**The setting of [Msw8-2] affects the recovery operation from the paper layout error. Memory switch [Msw8-2] is supported differently, depending on the firmware version.** 

|**[Msw8-2]**|**Recovery operation from error**|
|---|---|
|**OFF**|**Can recover from the error by opening/closing the printer cover or by executing DLE ENQ.**<br>**While the printer recovers from the error, paper layout is measured automatically and paper**<br>**is fed to the label print starting position. If the paper layout is stored in the non-volatile**<br>**memory, it will be rewritten. Afterwards, the printer operates following the paper layout**<br>**previously measured.**|
|**ON**|**Can recover by executing DLE ENQ. While the printer recovers from the error, paper is fed to**<br>**the label print starting position. The paper layout stored in the non-volatile memory will not**<br>**be changed. Change the setting of the paper layout stored in the non-volatile memory so**<br>**that it matches the currently used paper layout. See function 49 of this command for setting**<br>**thepaper layout.**|



- **Setting of [Msw 8-3] is supported differently, depending on the firmware version.** 

- **Setting of [Msw 8-4] affects the performance as follows:** 

   - **Executing “Automatic paper layout setting mode function (** m **= 64)” of** GS ( A 

   - **Executing “Automatic paper layout setting mode function” by panel operation when turning on the power** 

   - **Executing “Automatic Paper Recognition Function.” (The function is automatically executed when the printer has no setting of paper layout setting.)** 

- **Setting of [Msw 8-5] affects the performing of command** GS k **.** 

- **Settings of [Msw 8-6] affect the initializing operation when the power is turned on, when the paper layout (origin of layout) is “bottom of a label” or “top of a black mark“. Paper layout can be set by this function (Function 49) or “automatic setting of paper layout” function (by** GS ( A (m **= 64) or panel operation).** 

- **When [Msw 8-6] is set to** b **= 49 (does not perform paper feed to the print starting position, when power is turned on), printer performs assuming that paper is set to the print starting position. Therefore, user should note the following.** 
