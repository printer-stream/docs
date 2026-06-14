## **C O N F I D E N T I A L** 

■ This command is effective until ESC @ is executed, the printer is reset, or the power is turned off. 

- All ink ASB status items represent the enabled status whenever the status changes. Therefore, the disabled status items may change, because each status transmission represents the current status. 

- The ink ASB status, corresponding to each bit for n are as follows: 

|n|n|**ASB status description**|**ASB status description**|
|---|---|---|---|
|**Bit**|**Status**|**ASB status**|**Bit**|
|0|Online/offline status of<br>ink mechanism|Detect ink end|Status A: Bit 1<br>Status B: Bit 1|
|||Detect ink cartridge|Status A: Bit 2<br>Status A: Bit 3|
|||Cleaning|Status A: Bit 5|
|1|Ink detection status|Detect ink near-end|Status A: Bit 0<br>Status B: Bit 0|
|||Detect ink end|Status A: Bit 1<br>Status B: Bit 1|
|||Detect ink cartridge|Status A: Bit 2<br>Status B: Bit 3|



- The ink ASB status is a 4-byte message, consisting of the following table. 

|**Transmitted data **|**Hexadecimal**|**Decimal**|**Data amount**|
|---|---|---|---|
|Header|35H|53|1 byte|
|Status A (*1)|40H ~ 7FH|64 ~ 127|1 byte|
|Status B (*2)|40H ~ 7FH|64 ~ 127|1 byte|
|NUL|00H|0|1 byte|
