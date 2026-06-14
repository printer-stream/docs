## **C O N F I D E N T I A L** 

|(nL+nH ×256)|**Type**|**Maintenance counter**|
|---|---|---|
|148~157|Accumulation|Thermal head|
|158~167|Accumulation|Ink jet head|
|168~177|Accumulation|Shuttle head|
|178~187|Accumulation|Devices that conform to the normal specification|
|188~197|Accumulation|Option devices|
|198~207|Accumulation|Time|



## [Notes] 

- There are two types of maintenance counters: resettable counters and accumulation counters. A resettable counter is a maintenance counter that can be initialized by GS g 0, and an accumulation counter indicates the counter value from when the printer starts operation. 

- When a counter reaches its maximum value, its value is reset to 0 in the next updating process. Units and maximum values of counters differ, depending on the printer model and function. See the modeldependent variations for details. 

- Unsupported counter numbers cannot be specified. 

- This command transmits  [Header ~  NUL], as shown below: 

|**Transmitted data**|**Hex**|**Decimal**|**Amount of data**|
|---|---|---|---|
|Header|5FH|95|1 byte|
|Counter value (*1)|30H ~ 39H|48 ~ 57|1 ~ 10 byte|
|NUL|00H|0|1 byte|



- (*1) When the counter values are transmitted, the printer converts them to character codes corresponding to the decimal value and transmits from the most significant bit. 

Example: When the counter value is 120, the “120” (expressed hexadecimally as 31H, 32H, 30H. Decimally as 49, 50, and 48) is converted to 3 bytes of data. 

- The resettable maintenance counter can be initialized by GS g 0. 

- The maintenance counters built in the printer are standard; therefore, their values will be different, depending on the timing of occurring errors or turning off the power. 
