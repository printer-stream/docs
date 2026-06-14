Rev.2.52 

## **ESC SYN 1 n** 

|**ESC SYN 1 n**|**ESC SYN 1 n**|
|---|---|
|Name<br>Set presenter paper recovery function and automatic recovery time<br>Code<br>ASCII<br>ESC SYN<br>1<br>n<br>Hex.<br>1B<br>16<br>31<br>n<br>Decimal<br>27<br>22<br>49<br>n<br>Defned Region<br>0≤n≤255<br>Initial Value<br>Memory Switch Setting<br>Function<br>Sets presenter paper automatic recovery function and automatic recovery time.<br>This command is ignored when a presenter is not connected.<br>Settings using this command are efective from the next sheet when the printer processes<br>this command and paper has already been supplied to the presenter.<br>n<br>Function<br>n = 0<br>Paper automatic recoveryfunction invalid.<br>1≤n≤255<br>Paper automatic recovery function valid.<br>Automatic recoverytime: n x 0.5 sec(0.5 sec to 127.5 sec)||
|n|Function|
|n = 0|Paper automatic recoveryfunction invalid.|
|1≤n≤255|Paper automatic recovery function valid.<br>Automatic recoverytime: n x 0.5 sec(0.5 sec to 127.5 sec)|



Reference ESC SYN 0, ESC SYN 2, ESC SYN 3, ESC SYN 4 

ESC/POS Command Specifications 

194 
