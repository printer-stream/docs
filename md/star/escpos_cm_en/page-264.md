Rev.2.52 

## **4-3-17 Star Original Hold print control Commands** 

## **ESC SYN DC3 n** 

|Name|Hold print|control settings|control settings||
|---|---|---|---|---|
|Code|ASCII|ESC SYN|DC3|n|
||Hex.|1B<br>16|13|n|
||Decimal|27<br>22|19|n|



Defined Region n = 0, 1, 48, 49, 255 Initial Value Memory S/W setting Function Hold print control settings 

|Hold print|control settings|
|---|---|
|n|Holdprint control|
|0,48|Invalid|
|1,49|Valid|
|255|Memoryswitch setting|



When this is set to enabled, check that there is no paper in the hold print sensor, and then execute printing. 

If there is paper in the hold print sensor, the next printing is put on hold until the paper is removed. 

The hold time can be set with the memory switches, and it is possible to select automatic cancel when 

timeout occurs. 

When this is set to disabled and printing is performed regardless of the paper hold sensor status. 

Set to disabled when performing continuous printing. 

If unprinted data exists in the image buffer at the time this command is processed, the data is printed out first 

and then the command is executed. 

However when in page mode, printing is not executed even if unprinted data exists in the image buffer. 

If printing is in progress at the time this command is processed, the printer waits for printing to stop, and then 

executes this command. 

This command setting will not be initialized by the ESC @, CAN commands. 

The setting by this command will be initialized by a printer reset. 

ESC/POS Command Specifications 

264 
