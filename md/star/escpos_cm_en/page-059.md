Rev.2.52 

## **ESC G n** 

Name Specify/cancel double printing Code ASCII ESC G n Hex. 1B 47 n Decimal 27 71 n 0 ≤ n ≤ 255 Defined Region Initial Value n = 0 Function Specifies or cancels double printing. • Cancels double printing when n = <*******0>B. • Specifies double printing when n = <*******1>B. Details • n is effective only when it is the lowest bit. • This printer is not capable of double printing, so the print is the same as when using emphasized printing. 

• This command is enabled for ANK characters and Chinese characters. Reference ESC E 

ESC/POS Command Specifications 

59 
