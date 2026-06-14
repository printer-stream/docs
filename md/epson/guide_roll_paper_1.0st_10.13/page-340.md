## **C O N F I D E N T I A L** 

■ **Roll paper sensor status (** n **= 4)** 

**When the cover is open, the states of the roll paper near end sensor (bit 2, 3) and the roll paper end sensor (bit 5, 6) retain the values when the cover was closed immediately before.** 

## TM-P60 

TM-P60 **with Peeler** 

**Use this command according to the following rule; otherwise, the status might not be transmitted.** 

**The next data is not transmitted until the status is received when this command is transmitted.** 

**Only when it is necessary to acquire plural real-time status items continuously, this command can be transmitted continuously up to 5 times. However, the next data is not transmitted until all status items are received in this case.** 

■ **Printer status (** n **= 1)** 

## **Bit 2 status is as follows:** 

|n**: Bit**|**Binary**|**Hex**|**Decimal**|**Function**|**_... how to use_**<br>**_this table_**|
|---|---|---|---|---|---|
|**2**|**0**|**00**|**0**|**Does not go offline by low battery.**||
||**1**|**04**|**4**|**Offline by low battery.**||



## **Bit 5 of the printer status is not supported.** 

■ **Offline cause status (when** n **= 2 is specified)** 

## **Bit 2 indicates the open/closed status of the peeler cover.** 

■ **Error cause status (** n **= 3)** 

**Bit 3 of the error cause status is not supported.** 

**If the cause of an automatically recoverable error (bit 6) is a "paper error," recovery from the error is possible by opening and closing the peeler cover.** 

■ **Roll paper sensor status (** n **= 4)** 
