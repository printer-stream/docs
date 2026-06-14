## **C O N F I D E N T I A L** 

## **Sends 3 byte data group composed of [header + Paper width and resolution (1 byte) + NUL].** 

|**Bit**|**Function**|**Binary**|**Hex**|**Decimal**|
|---|---|---|---|---|
|**0**|**Paper width 80 mm**|**0**|**00**|**0**|
||**Paper width 58 mm**|**1**|**01**|**1**|
|**1**|**Resolution : 180dpi**|**0**|**00**|**0**|
||**Resolution : 203dpi**|**1**|**02**|**2**|
|**2 ~  5 **|**Reserved**|**-**|**-**|**-**|
|**6**|**Fixed**|**1**|**40**|**64**|
|**7**|**Fixed**|**0**|**00**|**0**|



## TM-P60 

## **Peeler models** 

**Model ID (when** n **= 1, 49 is specified)** 

- **Hexadecimal = 69H / Decimal = 105** 

**Type ID (when** n **= 2, 50 is specified)** 

- **Bit 1: Always transmits [No autocutter].** 

- **Bit 2: Always transmits [No DM-D (customer display) connection].** 

**Type information (when** n **= 33 is specified) The type information of this printer consists of the first to third 3 bytes.** 

- **First byte - bit 1: Always transmits [No autocutter].** 

- **First byte - bit 2: Always transmits [No DM-D (customer display) connection].** 

- **Second byte: Always transmits [Hexadecimal = 40H / Decimal = 64].** 

- **Third byte - bit 0: Always transmits [Peeler mechanism].** 

**Model name (when** n **= 67 is specified)** 

- **The model name is [** TM-P60 **].** 
