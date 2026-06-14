SETTING COMMAND 

## **C O N F I D E N T I A L** 

## **ESC c 4** 

[Name] Select paper sensor(s) to stop printing [Format] ASCII ESC c 4 n Hex 1B 63 34 n Decimal 27 99 52 n [Range] 0 ≤ n ≤ 255 

[Default] n = 0 

[Printers not featuring this command] TM-P60, TM-T20 

[Description] Selects the paper sensor(s) to use to stop printing when a paper end is detected using n as follows: 

|n:**Bit**|**Off/On**|**Hex**|**Decimal**|**Function**|**_... how to use_**<br>**_this table_**|
|---|---|---|---|---|---|
|0|Off|00|0|Roll paper near-end sensor disabled.||
||On|01|1|Roll paper near-end sensor enabled.||
|1|Off|00|0|Roll paper near-end sensor disabled.||
||On|02|2|Roll paper near-end sensor enabled.||
|2|Off|00|0|Roll paper end sensor disabled.||
||On|02|4|Roll paper end sensor enabled.||
|3|Off|00|0|Roll paper end sensor disabled.||
||On|08|8|Roll paper end sensor enabled.||
|4-7|—|—|—|Undefined.||



[Notes] 

■ It is possible to select multiple sensors to stop printing. When any sensor detects a paper-end, printing stops. 

- Some sensors are not present, depending on the printer model. 

- The names of some sensors differ, depending on the printer model. 

■ The roll paper near-end sensor is enabled when either bit 0 or bit 1 is on or both are on. 
