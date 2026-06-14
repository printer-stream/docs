## **C O N F I D E N T I A L** 

|**Bit**|**Off/On**|**Hex**|**Decimal**|**Function**|
|---|---|---|---|---|
|**4, 5 **|**-**|**-**|**-**|**Reserved**|
|**6**|**On**|**40**|**64**|**Fixed**|
|**7**|**Off**|**00**|**0**|**Fixed**|



## TM-L90 

## TM-L90 **with Peeler:** 

- **Printer model ID (** n **= 1, 49)** 

## **Hex = 4DH / Decimal = 77** 

- **Type ID (** n **= 2, 50)** 

## **Bit 1: Autocutter is not installed.** 

## **Bit 2: The bit DM-D (Customer display) isn’t supported.** 

- **Type information (** n **= 33)** 

**Printer type information consists of 3 bytes of [First byte] to [Third byte].** 

**Bit 1 of [First byte]: [Autocutter is installed/not installed] is not supported.** 

**Bit 2 of [First byte]: DM-D (Customer display) isn’t supported.** 

**Bit 0 of [Third byte]: When the peeling issuing mode is selected, it is 1, when the continuous issuing mode is selected, it is 0.** 

**The peeling issuing mode and the continuous issuing mode can be selected by a switch on the printer. This is a slide switch that can be used when the roll paper cover is opened.** 

**Printer model (** n **= 67): [** TM-L90 **]** 

- **Model dependent printer information (** n **= 112):** 

## **Sends 4 byte data group composed of [header + DIP switch information (2 bytes) + NUL].** 
