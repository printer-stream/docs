Rev.2.52 

## **3. COMMAND FUNCTION LIST** 

○: Valid 

- (L): Effective only at the top of the line (S): Only setting effective 

- (D): Effective only when there is no data in print buffer 

## **Standard Commands** 

|Commands|Name|Command<br>Class|Command<br>Class|Std Mode|Page<br>Mode|GS P<br>Efect|
|---|---|---|---|---|---|---|
|||Exe.|Set||||
|HT|Horizontal tab|○||○|○||
|LF|Line feed|○||○|○||
|FF|Print and recover topage mode|○||Ignored|○||
|CR|Print and carriage return|○||○|○||
|CAN|Cancelprint data inpage mode|○||Ignored|○||
|DLE EOT|Real-time status transmission|○||○|○||
|DLE ENQ|Real-time request toprinter|○||○|○||
|DLE DC4|Real-time output of specifedpulse|○||○|○||
|ESC FF|Print data inpage mode|○||Ignored|○||
|ESC SP|Set character right space amount||○|○|○|○|
|ESC !|Batch specify print mode||○|○|○||
|ESC $|Specifyabsoluteposition|○||○|○|○|
|ESC %|Specify/cancel download character set||○|○|○||
|ESC &|Defne download characters||○|○|○||
|ESC *|Specifybit image mode|○||○|○||
|ESC -|Specify/cancels underline mode||○|○|○||
|ESC 2|Set default line spacing||○|○|○||
|ESC 3|Set line feed amount||○|○|○|○|
|ESC =|Selectperipheral device||○|○|○||
|ESC ?|Delete download characters||○|○|○||
|ESC@|Initializeprinter|○|○|○|○||
|ESC D|Set horizontal tabposition||○|○|○||
|ESC E|Specify/cancel emphasizedprinting||○|○|○||
|ESC G|Specify/cancel doubleprinting||○|○|○||
|ESC J|Print and Paper Feed|○||○|○|○|
|ESC L|Selectpage mode|○||(L)|Ignored||
|ESC M|Select character font|||○|○||
|ESC R|Select international characters||○|○|○||
|ESC S|Select standard mode|○||Ignored|○||
|ESC T|Select character print direction in page mode||○|(S)|○||
|ESC V|Specify/cancel char. 90 deg. clockwise rotation||○|○|(S)||
|ESC W|Set print region in page mode||○|(S)|○|○|
|ESC \|Specify relative position|○||○|○|○|
|ESC a|Position alignment||○|(L)|(S)||
|ESC c 3|Select paper out sensor to enable at paper out signal<br>output||○|○|○||
|ESC c 4|Select paper out sensor to enable at printing stop||○|○|○||
|ESC c 5|Enable/disable panel switches||○|○|○||
|ESC d|Print and feedpaper n lines|○||○|○||
|ESCp|Specify pulse|○||○|○||
|ESC t|Select character code table||○|○|○||
|ESC{|Specify/cancel upside-down characters||○|(L)|(S)||
|FSg1|Write data to user NV memory||○|○|Invalid||
|FS g 2|Read user NV memory data|○||○|○||



ESC/POS Command Specifications 

23 
