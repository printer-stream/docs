Rev.2.52 

## **<Function 70> GS ( k pL pH cn fn m  (cn=48, fn=70)** 

Name Set PDF417 options Code ASCII GS ( k pL pH cn fn m Hex. 1D   28  6B  pL  pH cn fn m Decimal   29   40  107  pL  pH cn fn m Defined Region pL = 3, pH = 0 cn = 48, fn = 70 m = 0, 1 Initial Value m = 0 Function Set PDF417 options m Function 0 Selects the standard PDF417 options. 1 Selects the simple PDF417 options. 

. 

Details The setting of this function affects processes of Functions 081 and 082. 

This setting is valid until ESC @ is executed, the printer is reset or the power is turned off. Reference GS ( k Function 081, 082, ESC @ 

## **<Function 080> GS ( k pL pH cn fn m d1...dk (cn=48, fn=80)** 

## Name e 

Name e Set the PDF417 symbol level height Code ASCII GS ( k pL pH cn fn m   d1...dk Hex. 1D   28  6B  pL  pH cn fn m   d1...dk Decimal   29   40  107  pL  pH cn fn m   d1...dk Defined Region 4 ≤  (pL + pH×256) ≤ 65535 (0 ≤ pL ≤ 255, 0 ≤ pH ≤ 255) cn = 48, fn = 80, m = 48 2 ≤ d ≤ 255, k = (pL + pH×256) - 3 Function Stores the symbol data (d1 … dk) of PDF417 in the symbol saving region. Details Data stored in the symbol saving region using this function is processed using Function 081 and 082. After processing Functions 081 and 082, data of the saving region is maintained. k bytes of d1 … dk are processed as symbol data. This function specifies only the data word count of the symbol. The printer automatically applies this so the following data is not included in the d1 … dk data. 

- Start patterns and stop patterns 

- Indicator code words of the right and left levels. 

- Descriptor related to symbol length (initial code word of the data region) 

This setting is valid until this function is reset, ESC @ is executed, the printer is reset or the power is off. 

Reference GS ( k Function 081, 082, ESC @ 

ESC/POS Command Specifications 

112 
