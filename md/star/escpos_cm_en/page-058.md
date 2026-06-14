Rev.2.52 

## **ESC E n** 

|**ESC E n**||
|---|---|
|Name|Specify/cancel emphasized characters|
|Code|ASCII<br>ESC<br>E<br>n|
||Hex.<br>1B<br>45<br>n|
||Decimal<br>27<br>69<br>n|
|Defned Region|0≤n≤255|
|Initial Value|n = 0|
|Function|Specifes or cancels emphasized characters.|
||• Cancels emphasized characters when n = <*******0>B.|
||• Specifes emphasized characters when n = <*******1>B.|
|Details|• n is efective only when it is the lowest bit.|
||• The setting of the last received command is efective even when emphasized printing is|
||executed by the ESC! (Batch specify print mode) command.|
||• This command is enabled for ANK characters and Chinese characters.|
|Reference|ESC !|



ESC/POS Command Specifications 

58 
