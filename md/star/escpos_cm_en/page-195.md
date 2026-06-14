Rev.2.52 

## **ESC SYN 3 n** 

|Name|Name|Name||Get presenter paper counter||
|---|---|---|---|---|---|
|Code||||ASCII<br>ESC SYN<br>3<br>n||
|||||Hex.<br>1B<br>16<br>33<br>n||
|||||Decimal<br>27<br>22<br>51<br>n||
|Defned Region||||n = 0, 1, 48, 49||
|Function||||Acquires presenter paper counter.||
|||||This command is ignored when a presenter is not connected.||
|||||Counter can count to 0xFFFFFFFF sheets.||
|||||Counter is cleared to zero when the following conditions are met.||
|||||• At a printer reset||
|||||• At <ESC> <SYN> 4 n command||
|||||The paper counter sends the counter value at the time this command is processed.||
|||||The counter is counted up when paper is completely recovered or when pulled out.||
|||||The counter counts from when the power is turned ON, excluding the following.||
|||||• When paper is discharged because of an error||
|||||• When printing using self-print||
|||||• When paper in the presenter is discharged when the power is turned ON||
|||n|Counter|||
||n =|0,48|Acquirespaper reel counter|||
||n =|1,49|Acquirespaper recoverycounter|||
|||||<Counter transmission format from printer: When using the paper reel counter>||
|||||Printer Transmission: ESC SYN 3 n c1 c2 c3 c4||
|||||Reel counter: c4 + (c3 x 256) + (c2 x 256 x 256) + (c1 x 256 x 256 x 256)||
|Reference||||ESC SYN 0, ESC SYN 1, ESC SYN 2, ESC SYN 4||



ESC/POS Command Specifications 

195 
