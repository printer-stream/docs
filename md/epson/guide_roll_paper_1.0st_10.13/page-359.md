## **C O N F I D E N T I A L** 

## **• Selecting the continuous issuing mode** 

|**Step**|**Operation**|
|---|---|
|**1**|**Press the cover open button, and open the peeler cover.**|
|**2**|**If the paper roll cover was open in Step 1, close the paper roll cover.**|
|**3**|**Fold up the peeler holder.**|
|**4**|**Close the peeler cover.**|



## TM-P60 **Models without Peeler** 

**The function of Bit 0 of parameter (n) is not supported. Specify 1 to bit 0 of** _**n**_ **or bits of “Reserved.”** 

## ■ **First byte (printer information)** 

## **• Bit 2 status is as follows:** 

|**n:**<br>**Bit**|**Binary**|**Hex**|**Decimal**|**Function**|
|---|---|---|---|---|
|**2**|**0**|**00**|**0**|**Does not go to offline by low battery.**|
||**1**|**04**|**4**|**Offline by low battery.**|



## ■ **Basic second byte (printer information)** 

- **Bits 0 and 2 of the second byte are not supported.** 

- **Basic third byte (paper sensor information)** 

- **Bits 0 and 1 of the third byte are not supported.** 

- **When the cover is open, the status of the roll paper end sensor (bit 2, 3) retains the value when the cover was closed immediately before.** 

## TM-U230 

**The default value is set by DIP switch 1-8.** 

## ■ **Second byte (printer information)** 
