Rev.2.52 

## **GS C 2 nL nH** 

Name Set counter mode value Code ASCII GS C 2 nL nH Hex. 1D 43 32 nL nH Decimal 29 67 50 nL nH 0 ≤ nL ≤ 255 Defined Region 0 ≤ nH ≤ 255 Initial Value nL = 1, nH = 0 Function Sets the serial number counter value. Details • nL and nH set the counter value. 

- In the count up mode, if the counter value specified by this command goes out of the counter operating range, specified by GSC1 or GSC;, it is forced to convert to the minimum value by the next GSc. 

- In the count down mode, if the counter value specified by this command goes out of the counter operating range, specified by GSC1 or GSC;, it is forced to convert to the maximum value by the next GSc. 

Reference GS C 0, GS C 1, GS C ; , GS c 

ESC/POS Command Specifications 

131 
