Rev.2.52 

## **ESC % n** 

Name Specify/cancel download character set Code ASCII ESC % n Hex. 1B 25 n Decimal 27 37 n 0 ≤ n ≤ 255 Defined Region Initial Value n = 0 Function Specifies or cancels the download character set. • When n  =  <*******0>B, the download character set is cancelled. • When n  =  <*******1>B, the download character set is specified. Details • n is effective only when it is the least significant bit. • When the download character set is cancelled, the internal character set is automatically specified. STAR Because ESC& (define download characters) and GS* (define download bit images) are used in the same region, they cannot both be defined simultaneously. a. When download characters are defined, previously defined download bit images are cleared. b. Conversely, when download bit images are defined, previously defined download characters are cleared and the definition returns to same the internal character set. Reference ESC &, ESC ? 

ESC/POS Command Specifications 

45 
