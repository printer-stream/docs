|Function|SW 2-3|SW 2-4|
|---|---|---|
|Do not set|ON|ON|
|Print density (standard)|OFF|OFF|
|Print density (darker than standard)|ON|OFF|
|Print density (dark)|OFF|ON|



- If the print density is set to “Darker than standard” or “Dark” level, print speed may be reduced. 

- The print density can be set with DIP switches (2-3/2-4) or the customized value. (See "Setting the Memory Switches (Customized Value)" on page 63.) The default setting of the customized value is “Depends on the DIP switch settings.” If the customized value is changed, the value set with the customized value is enabled. 

With DIP switch 2-1, you can select conditions for invoking a BUSY state as either of the following: 

- When the receive buffer is full 

- When the receive buffer is full or the printer is offline 

In either case above, the printer enters the BUSY state after power is turned on (including resetting with the interface) and when a self-test is being run. 

## Printer BUSY Condition and Status of DIP Switch 2-1 

||Printer status|DIP SW 2-1|DIP SW 2-1|
|---|---|---|---|
|||ON|OFF|
|Offline|During the period after power is turned on<br>(including resetting with the interface) to when the<br>printer is ready to receive data.|BUSY|BUSY|
||During the self-test.|BUSY|BUSY|
||When the cover is open.|—|BUSY|
||During paper feed with the Feed button.|—|BUSY|
||When the printer stops printing due to a paper-end<br>(when printer has run out of roll paper).|—|BUSY|
||When waiting for the paper Feed button to be<br>pressed before macro execution.|—|BUSY|
||When an error has occurred.|—|BUSY|
|When the receive buffer becomes full.||BUSY|BUSY|



**62** 
