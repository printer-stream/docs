Rev.2.52 

## **<Function 065> GS ( k pL pH m cn n  (cn=48, fn=65)** 

Name Set PDF417 position count (level length) Code ASCII GS ( k pL pH m cn fn n Hex. 1D   28  6B  pL  pH  m  cn fn n Decimal   29   40  107  pL  pH m cn fn n Defined Region pL = 3, pH = 0 cn = 48, fn = 65 0 ≤ n ≤ 30 Initial Value n = 0 Function Sets PDF417 symbol position count (level length). • When n = 0, sets the automatic process. • When n≠0, sets the number of positions of the symbol data region to n code words. Details The setting of this function affects processes of Functions 081 and 082. When automatic processing is specified (n = 0), the maximum row number in the data region is 30. The following data is not included in the number of positions. • Start patterns and stop patterns • Indicator code words of the right and left levels. The number of positions when automatic processing is specified (n = 0), calculates the number of code words based on the current print region, when processing Functions 081, and 082, module width (Function 067), and the option settings (Function 070). This setting is valid until ESC @ is executed, the printer is reset or the power is turned off. Reference GS ( k Function 081, 082, 067, 070, ESC @ 

ESC/POS Command Specifications 

108 
