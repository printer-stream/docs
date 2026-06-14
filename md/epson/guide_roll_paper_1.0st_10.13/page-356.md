## **C O N F I D E N T I A L** 

■ **Basic second byte (printer information)** 

- **If the cause of the recoverable error (bit 2) is the paper layout error, the printer can recover from the error by opening/closing the roll paper cover or by the** DLE ENQ **command or pressing the paper feed button only when memory switch Msw8-2 is OFF. See Function 3 of** GS E **.** 

- **Basic third byte (paper sensor information)** 

- **When the cover is open, the status of the roll paper end sensor (bit 2, 3) retains the value when the cover was closed immediately before.** 

## TM-T20 

**The default value is set by Msw 1-3.** 

- n **= 0 when Msw 1-3 is off.** 

- n **= 2 when Msw 1-3 is on.** 

- **Second byte (printer information)** 

- **Bits 0, 1, and 2 of the second byte are undefined.** 

- **Third byte (paper sensor information)** 

- **When the cover is open, the status of the roll paper end sensor (bit 2, 3) retains the value when the cover was closed immediately before.** 

- **Bits 0 and 1 of the third byte are always OFF, “Paper adequate.”** 

## TM-T88IV, TM-T88V 

**The default value is set by DIP switch 2-1.** 

- **Second byte (printer information)** 

- **Bits 0, 1, and 2 of the second byte are undefined.** 

- **Third byte (paper sensor information)** 

- **When the cover is open, the status of the roll paper end sensor (bit 2, 3) retains the value when the cover was closed immediately before.** 

## TM-T70 

**The default value is set by DIP switch 2-1.** 
