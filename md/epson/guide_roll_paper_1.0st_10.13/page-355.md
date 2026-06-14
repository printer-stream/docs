## **C O N F I D E N T I A L** 

- **When the cover is open, the status of the roll paper end sensor (bit 2, 3) retains the value when the cover was closed immediately before.** 

- **Basic fourth byte (paper sensor information)** 

- **Bits 0 and 2 indicate the following status:** 

   - **Fourth byte (paper sensor information)** 

|**Bit**|**Binary**|**Hex**|**Decimal**|**Status for ASB**|**_... how to use_**<br>**_this table_**|
|---|---|---|---|---|---|
|**0**|**0**|**00**|**0**|**Not waiting for a label to be**<br>**removed**||
||**1**|**01**|**1**|**Waiting for a label to be**<br>**removed**||
|**1**|**—**|**—**|**—**|**Reserved**||
|**2**|**0**|**00**|**0**|**Paper present in label peeling**<br>**detector**||
||**1**|**04**|**4**|**No paper present in label**<br>**peeling detector**||
|**3**|**—**|**—**|**—**|**Reserved**||
|**4**|**0**|**00**|**0**|**Not used. Fixed to Off.**||
|**5,6**|**—**|**—**|**—**|**Reserved**||
|**7**|**0**|**00**|**0**|**Not used. Fixed to Off.**||



## ■ **Bit 0: When the continuous issuing is selected, this bit is always 0.** 

- **Bit 2: When the peeling issuing mode is selected, this bit is changed during paper feeding or when a label is in the peeling position. When a label removal is checked by pressing the paper feed button, this bit may be incorrect.  When the continuous issuing mode is selected, this bit is always 1.** 

TM-L90 **Models without Peeler** 

**The default value is set by Msw 1-3.** 
