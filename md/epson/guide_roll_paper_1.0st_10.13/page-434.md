## **C O N F I D E N T I A L** 

- With a parallel interface, if the printer is BUSY, this command cannot be used in the following states. 

   - When DIP switch or memory switch (BUSY condition) is on: receive buffer full 

   - When DIP switch or memory switch (BUSY condition) is off: offline, receive buffer full, or error status 

- The function of not sounding the buzzer affects autonomous buzzer sound (errors, paper-end) and buzzer sound with ESC ( A <Function 97>, buzzer sound during cutting, buzzer sound by generating the specified pulse. 

- When the buzzer has stopped sounding, the printer transmits the buzzer sound end response as shown below to the host. 

|**Buzzer sound end**<br>**response**|**Hex**|**Decimal**|**Data quantity**|
|---|---|---|---|
|Header|37H|55|1 byte|
|Identifier|54H|84|1 byte|
|NUL|00H|0|1 byte|



[Model-dependent variations] 

## TM-T20, TM-T88V 

## TM-T20, TM-T88V 

**This command can be used when “Enabling/disabling optional external buzzer” is set to “Enabled “ with** GS ( E **<Function 5>, Set the customized setting values.** 

**When “Enabling/disabling optional external buzzer” is set to “Disabled”, the printer transmits “Buzzer sound end response” only.** 
