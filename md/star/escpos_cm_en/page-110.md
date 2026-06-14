Rev.2.52 

## **<Function 067> GS ( k pL pH cn fn n  (cn=48, fn=67)** 

## Name e 

Name e Set PDF417 module width Code ASCII GS ( k pL pH cn fn n Hex. 1D   28  6B  pL  pH cn fn n Decimal   29   40  107  pL  pH cn fn n Defined Region pL = 3, pH = 0 cn = 48, fn = 67 2 ≤ n ≤ 8 Initial Value n = 3 Function Sets one PDF417 module width to n dots. Details The setting of this function affects processes of Functions 081 and 082. This setting is valid until ESC @ is executed, the printer is reset or the power is turned off. Set in units of 1 dot. The width is set in 0.125 mm (1/203 inches) units. Reference GS ( k Function 081, 082, ESC @ 

## **<Function 068> GS ( k pL pH cn fn n  (cn=48, fn=68)** 

Name Set the PDF417 symbol level height Code ASCII GS ( k pL pH cn fn n Hex. 1D   28  6B  pL  pH cn fn n Decimal   29   40  107  pL  pH cn fn n Defined Region pL = 3, pH = 0 cn = 48, fn = 68 2 ≤ n ≤ 8 Initial Value n = 3 Function Sets one PDF417 symbol module height to [module width x n]. Details The setting of this function affects processes of Functions 081 and 082. This setting is valid until ESC @ is executed, the printer is reset or the power is turned off. The height of one level affects the reading rate of symbols. The height of one level is recommended to be set to 3 to 5 times the module width. When the symbol vertical size is less than 5 mm (0.2 inches), there is the possibility that the reading rate will drop. It is possible to check the vertical size of the symbol using the size information status of Function 082. Reference GS ( k Function 081, 082, ESC @ 

ESC/POS Command Specifications 

110 
