## **C O N F I D E N T I A L** 

## TM-J2000/J2100 

## **The following print control modes are available.** 

|m|**Print control mode**|**Specification**|
|---|---|---|
|**1, 49 **|**Normal**|**Enables printing in high density**|
|**2, 50 **|**High speed**|**Enables printing in high speed and saving ink**|
|**3, 51 **|**Economy**|**Prints saving more ink than “High speed”**|



**Bar code mode is in addition to the modes mentioned above. Bar code mode prints the bar code or the 360 dpi graphics and is automatically selected when printing that data. When printing data other than the bar code or the 360 dpi graphics, the printing mode automatically returns to the mode specified by this function.** 

**Even when “high speed” or “economy” is selected, the spool slot might not be improved because of the data communication speed between the printer and the host.** 

## TM-T90 

## **The following print control modes are available.** 

|m|**Print control mode**|
|---|---|
|**1, 49**|**Standard print control mode**|
|**2, 50**|**Suitable print control mode for printing a fence bar code**|
|**3, 51**|**Suitable print control mode for printing a ladder bar code**|
|**4, 52**|**Suitable print control mode for printing a two dimension code**|



**In printing when (** m **= 3, 4, 51, 52), the printer starts actual printing after it reaches control speed. The paper must be fed 10 dots or less in this operation. Therefore, when the printer starts printing, paper feeding for 10 dots or less without printing might occur.** 

## TM-T20, TM-T88IV, TM-T88V, TM-T70 

**The printer does not support this function.** 
