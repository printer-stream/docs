## **ESC GS s U z n [k1 k2 k3 d1 … dk]1 … [k1 k2 k3 d1 … dk]n** 

[Name] Register user area NV audio data [Code] ASCII ESC GS s U z n [k1 k2 k3 d1 .. dk]1 .. [k1 k2 k3 d1 .. dk]n Hexadecimal 1B 1D 73 55 z n [k1 k2 k3 d1 .. dk]1 .. [k1 k2 k3 d1 .. dk]n Decimal 27 29 115 85 z n [k1 k2 k3 d1 .. dk]1 .. [k1 k2 k3 d1 .. dk]n [Defined Area] Z = 0 0 ≤ n ≤ 255 0 ≤ [ k1 + k2x256 + k3x65536 ]1 + … +  [ k1 + k2x256 + k3x65536 ]n ≤ 1701888 0 ≤ d ≤ 255 [Initial Value] Japanese or English (See table below) n English Audio 1 Welcome ! 2 Thank you ! 3 Order coming in. 4 Drink Order coming in. 5 Food Order coming in. 6 Order has been Cancelled. 7 New order coming in. 8 Order to go coming in. 9 Print finished. 10 Please take your receipt. 11 Please come again. 12 Please give your receipt to the operator. 13 Now printing, please wait a moment. 14 Please do not pull the paper until printing finishes. 15 Thank you for visiting. 16 Please take the number ticket. 17 Please have a seat and wait a moment. 18 Thank you for your purchase. 19 Please wait here, we will guide you shortly. 

[Function] 

All data already registered in the user area is erased when starting processing of this command. Registers n audio data to the user area. (However, when n = 0, nothing is registered.) 

Audio numbers are set in ascending order in the order they are registered from user area audio number 1 to n. 

(k1 + k2 x 256 + k3 x 65536) specifies the number of bytes of the audio data. 

d is audio data in sampling frequency of 11.025 kHz, monaural ADPCM format in quantization bit rate of 4 bits. 

The size of the registration region is 1,662 KB (approx. 308 seconds). This command should be specified at the top of the line. 

When the first parameter is determined to be free of error, the printer starts processing this command. 

If the defined area specified by the parameter is not empty, or if there is an error in the parameter specification, register processing is aborted. (The pre-registered and complete data is effective.) The printer should be reset if audio data registration is completed or register processing is forcibly aborted. 

Error processing, mechanical operations and status processing and the like cannot executed while registering audio data (the time from when the first parameter is determined to be OK until printer initialization is completed after registering audio data). 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-151 
