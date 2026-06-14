## **C O N F I D E N T I A L** 

|n:<br>**Bit**|**Binary**|**Hex**|**Decimal**|**Function**|
|---|---|---|---|---|
|6|0|00|0|Panel switch status disabled.|
||1|40|64|Panel switch status enabled.|
|7|0|00|0|Undefined.|



## [Notes] 

- ASB is the function that transmit the status of [cover open/close], [Online/Offline] from the printer automatically. It is called [ASB function] and the status is [ASB status]. If you use ASB, application can acquire the printer change in a real-time and passively. 

- Select any status enabled (except n = 0) and basic ASB starts. Then transmit the current basic ASB status. After that, while ASB is active the selected enabled basic ASB status is transmitted whenever the status changes. 

- When n = 0, basic ASB is disabled. When ASB is disabled, basic ASB status is not transmitted. 

- Multiple status items can be selected. 

- When ASB is active, ASB status is transmitted whenever the status changes even if the printer is disabled by ESC =. 

- This command setting is effective until ESC @ is executed, the printer is reset or power is turned off. 

- Any basic ASB status represents the enabled status whenever the status changes. Therefore the disabled status items may change, because each status transmission represents the current status. 
