## **C O N F I D E N T I A L** 

Msw 1-4, 1-6, 1-7, 1-8: Activated only with the serial interface printers. Msw 1-5: Not activated with the serial interface printers. 

- When a = 2, memory switch 2 is set as follows: 

|**Msw**|**Setting value (**b**)**|**Function**|
|---|---|---|
|2-1|49|Reserved|
|2-2|48|Autocutter is provided|
||49|Autocutter is not provided|
|2-3|48|Character code system for the simplified Chinese model: GB18030|
||49|Character code system for the simplified Chinese model: GB2312|
|2-4 to 2-8|50|Reserved|



- Specifications when memory switches 7 (a = 7) and 8 (a = 8) are different, depending on the printer models. 

## [Notes] 

- This function works only in the user setting mode. 

- The value of the memory switch is specified from bit 8 to bit 1 by b18...b11. When b = 50, the status of the bit applied is not changed. 

Example: 

Transmission data that specifies memory switch 1, “Transmits the power ON notice” and does not change other settings. 

- [Format] ASCII GS ( E pL pH fn a b8 b7 b6 b5 b4 b3 b2 b1 Hex 1DH 28H 45H 0AH 00H 03H 01H 32H 32H 32H 32H 32H 32H 32H 31H Decimal 29 40 69 10 0 3 1 50 50 50 50 50 50 50 49 

- Specifies b = 50 or depends on each model for a reserved bit. 

- Memory switches set are valid until the following operations are executed. They are not initialized by power off or ESC @. 

   - Execution of this function. 

   - Execution of memory switch setting mode by panel operation when the power is turned on (supported by some printer models.) 
