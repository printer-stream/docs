Rev.2.52 

## **<Function 472> GS ( k pL pH cn fn n (cn=52, fn=72)** 

Name e 

Name e Compound symbol: Store data in symbol saving region Code ASCII GS ( k pL pH cn fn n Hex. 1D   28  6B  pL  pH cn fn n Decimal   29   40  107  pL  pH cn fn n Defined Region pL = 3, pH = 0 cn = 52 fn = 72 0 ≤ n ≤ 2 , 48 ≤ n ≤ 50 Initial Value n = 0 

Function Select the font for HRI characters when printing combined symbols. 

|n|HRI font|
|---|---|
|0,48|notprinted|
|1,49|printed(Select font A(12x24))|
|2,50|printed (Select font B(9x17))|



Note Data stored in the symbol saving region by this function is processed using function 481. 

When “Print” HRI is selected, HRI is printed under 1D bar codes. 

When the combined symbol uses a 2D code (GS1 DataBar Stacked, GS1 DataBar Stacked Omnidirectional, GS1 DataBar Expanded Stacked), this setting is not affected and HRI is not printed. 

This setting is valid until this function is reset, ESC@ is executed, the printer is reset, or the power is off. 

Reference GS ( k Function 481, ESC @ 

ESC/POS Command Specifications 

122 
