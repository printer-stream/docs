## **3.3.7. Do wnload** 

## **ESC & c1 c2 n d1…d48** 

[Name] Register 12 x 24 dot font download characters [Code] ASCII ESC & c1 c2 n d1 ... d48 Hex. 1B 26 c1 c2 n d1 ... d48 Decimal 27 38 c1 c2 n d1 ... d48 [Defined Area] c1 = 1, 49 c2 = 1, 49 32≤n≤127 0≤d≤255 [Initial Value] - - - [Function] Registers 12 x 24 dot font download characters to the nth address. Download characters can be registered to <20>H to <7F>H. If one has been already registered to an address, it is overwritten. When parameters c1 and c2 and n are outside of the defined area, subsequent data is handled as normal data. Horizontal 12 Dots 

||d1<br>d3|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~PPrPrprppyy])~~<br>~~OO ~~|d2<br>d4<br>|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br>●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br>~~PPppypyy~~<br>~~yy~~<br> ~~OO~~|
|---|---|---|---|---|
||d5|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~OO ~~|d6<br>|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br> ~~OO~~|
||d7|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~OO~~|d8|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d9|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>d10<br>●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br>~~OC~~|||
||d11|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d12|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d13|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>d14<br>●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br>~~OC~~|||
||d15|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d16|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d17|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d18|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d19|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d20|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d21|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d22|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
|Vertical<br>24 Dots|d23<br>d25<br>d27|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~<br>~~Pee ~~<br>~~OO ~~|d24<br>d26<br>d28<br> <br>|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br>●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br>●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br> ~~eee~~<br> ~~OO~~|
||d29|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~OO ~~|d30<br>|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br> ~~OO~~|
||d31|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~OO~~|d32|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d33|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~OO~~|d34|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d35|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~OO~~|d36|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d37|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>d38<br>●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br>~~OC~~|||
||d39|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d40|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d41|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d42|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d43|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d44|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d45|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d46|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d47|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~|d48|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
|||bit7 bit6 bit5 bit4 bit3<br>bit2<br>bit1<br>Bit0||bit7<br>bit6<br>bit5 bit4 bit3 bit2<br>bit1<br>bit0|
||●: Font data<br>○: Invalid data||||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-32 
