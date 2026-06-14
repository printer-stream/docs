Rev.2.52 

## **GS E n** 

Name Set printing speed Code ASCII GS E n Hex. 1D 45 n Decimal 29 69 n 

0 ≤ n ≤ 255 Defined Region Initial Value n = 0 Function Sets print speed. 

|Bit|Function<br>|“0”|“1”|
|---|---|---|---|
|7|Undefned<br>|--|--|
|6|<br>Undefned|--|--|
|5|<br>Print Speed<br>|(See table below)||
|4||||
|3|Undefned<br>|--|--|
|2|<br>Undefned<br>|--|--|
|1|<br>Undefned<br>|--|--|
|0|<br>Undefned|--|--|



## Spec. A Print Speed 

|Bit-5|Bit-4|Print Speed|
|---|---|---|
|0|0|High speed|
|0|1|Mid-speed|
|1|0|Slow speed<br>|
|1|1|Undefned|



Spec. B 

## Print Speed 

|Bit-5|Bit-4|Print Speed|
|---|---|---|
|0|0|High speed<br>|
|0|1|Undefned|
|1|0|Slow speed<br>|
|1|1|Undefned|



## Details 

- This command is effective in standard mode. 

- This command is enabled only when at the top of the line. 

- The speed setting is disabled during reduced printing in the vertical direction. However, this command setting is enabled when reduced printing in the vertical direction is released. 

STAR 

- This command changes the print speed after the test print is stopped. 

ESC/POS Command Specifications 

133 
