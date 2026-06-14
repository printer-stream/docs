## **C O N F I D E N T I A L** 

## TM-T20 

**Receive buffer capacity [Msw 1-2]: Large (when** b **= 48) = 4 KB; small (when** b **= 49) = 45 bytes.** 

**The following memory switches are all reserved: [Msw 1-1], [Msw 1-6] , [Msw 1-7], and [Msw 1-8]** 

- **When** a **= 2, all bits of memory switch 2 are reserved.** 

- **When** a **= 3, all bits of memory switch 3 are reserved.** 

- **When** a **= 4, all bits of memory switch 4 are reserved.** 

- **When** a **= 5, memory switch 5 is set as follows:** 

|**Msw**|**Setting value (**b**) **|**Function**|
|---|---|---|
|**5-1**|**48**|**USBpower-saving function is enabled**|
||**49**|**USBpower-saving function is disabled**|
|**5-2**|**48**|**Recovery conditions from receive buffer BUSY: Recovers when the remaining**<br>**receive buffer capacity becomes 256 bytes.**|
||**49**|**Recovery conditions from receive buffer BUSY: Recovers when the remaining**<br>**receive buffer capacity becomes 138 bytes.**|
|**5-3 to 5-8 **|**Undefined**||



## TM-T88IV, TM-T88V, TM-T70 

**This printer does not support this function.** 

## TM-L90 

## TM-L90 **with Peeler:** 

**Receive buffer capacity [Msw 1-2]: Large (when** b **= 48) = 4 KB; small (when** b **= 49) = 45 bytes** 

**“DM-D (customer display) is connected or not” [Msw 1-6] function is not supported.** 

**The settings of [Msw 1-2]  ~ [Msw 1-4], [Msw 1-7], [Msw 1-8], and [Msw 8-4] can also be changed by the memory switch setting mode of the panel switch operation when turning on the power.** 
