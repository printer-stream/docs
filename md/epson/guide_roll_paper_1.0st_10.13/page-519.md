## **C O N F I D E N T I A L** 

- **Printer model (** n **= 67)** 

## **Printer model:** TM-J2000 **or** TM-J2100 

- **Model dependent printer information (** n **= 112):** 

## **Transmits 3 bytes data group composed of [header + printer information type B (1 byte) + NUL].** 

|**Bit**|**Off/On**|**Hex**|**Decimal**|**Function**|
|---|---|---|---|---|
|**0**|**Off**|**00**|**0**|**Black and white model**|
||**On**|**01**|**1**|**Two-color model**|
|**1 to 5**|**-**|**-**|**-**|**Reserved**|
|**6**|**On**|**40**|**64**|**Fixed**|
|**7**|**Off**|**00**|**0**|**Fixed**|



## TM-T90 

- **Printer model ID (** n **= 1, 49)** 

**Hex = 2EH / Decimal = 46 [When Japanese model is used or memory switch [Msw 8-7] is OFF.] Hex = 20H / Decimal = 32 [When memory switch [Msw 8-7] is ON.]** 

- **Type ID (** n **= 2, 50)** 

- **Bit 1: [Autocutter is installed/not installed] indicates the state of Memory switch 2-2.** 

- **Bit 2: The bit [DM-D (Customer display) isn’t supported.** 

- **Version ID (** n **= 3,51)** 

## **By the firmware version [When Japanese model is used or memory switch [Msw 8-7] is OFF.] Hex = 46H / Decimal = 70 [When memory switch [Msw 8-7] is ON.]** 

- **Printer model (** n **= 67)** 

**Printer model:** TM-T90 

- **Model-dependent printer information (** n **= 112):** 

**Transmits 4 byte data group composed of [header + DIP switches information (2 bytes) + NUL].** 
