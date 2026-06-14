Rev.2.52 

## **ESC GS s U z n [k1 k2 k3 d1 … dk]1 … [k1 k2 k3 d1 … dk]n** 

Name Register user area NV audio data 

Code 

ASCII ESC GS s U z n [k1 k2 k3 d1 ... dk]1 ... [k1 k2 k3 d1 ... dk]n Hex. 1B 1D 73 55 z n [k1 k2 k3 d1 ... dk]1 ... [k1 k2 k3 d1 ... dk]n Decimal 27 29 115 85 z n [k1 k2 k3 d1 ... dk]1 ... [k1 k2 k3 d1 ... dk]n 

Z = 0 Defined Region 

0 ≤ n ≤ 255 

0 ≤ [ k1 + k2 x 256 + k3 x 65536 ] 1 + … + [ k1 + k2 x 256 + k3 x 65536 ] n ≤ 1701888 

0 ≤ d ≤ 255 

Initial Value English (See table below) 

|n|English Audio|
|---|---|
|1|Welcome !|
|2|Thankyou !|
|3|Order comingin.|
|4|Drink Order comingin.|
|5|Food Order comingin.|
|6|Order has been Cancelled.|
|7|New order comingin.|
|8|Order togo comingin.|
|9|Print fnished.|
|10|Please takeyour receipt.|
|11|Please come again.|
|12|Pleasegiveyour receipt to the operator.|
|13|Nowprinting, please wait a moment.|
|14|Please do notpull thepaper untilprintingfnishes.|
|15|Thankyou for visiting.|
|16|Please take the number ticket.|
|17|Please have a seat and wait a moment.|
|18|Thankyou foryourpurchase.|
|19|Please wait here,we willguideyou shortly.|



Function All data already registered in the user area is erased when starting processing of this command. 

Registers n audio data to the user area. (However, when n = 0, nothing is registered.) 

Audio numbers are set in ascending order in the order they are registered from user area audio number 1 to n. 

(k1 + k2 x 256 + k3 x 65536) specifies the number of bytes of the audio data. 

d is audio data in sampling frequency of 11.025 kHz, monoaural ADPCM format in quantization bit rate of 4 bits. 

The size of the registration region is 1,662 KB (approx. 308 seconds). 

This command should be specified a the top of the line. However, if there is unprinted data in the line buffer, this command is executed after printing that data. 

When the first parameter is determined to be free of error, the printer starts processing this command. 

If the defined area specified by the parameter is not empty, or if there is an error in the parameter specification, register processing is aborted. 

ESC/POS Command Specifications 

261 
