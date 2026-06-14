- ; 

Chapter y Obtaininge e Informatione from the Plotter 

## What You’ll Learn in This Chapter 

Up to this time we have mainly been concerned with sending information or data to the plotter. Sometimes, however, we want to know something about the plotter, its current pen position, its status, whether an error has occurred, or what capabilities the plotter has. In this chapter you will learn about most of the plotter’s output instructions. The output P1 and P2 and output window instructions are discussed in Chapter 2 and the output digitized point instruction is discussed in Chapter 6. Ali other output instructions are discussed in this chapter. The timing of output depends on your interface (HP-IB, RS-232-C, or HP-IL). Before using the output instructions, you should have read the notes below and the appropriate interfacing chapter in this manual. 

## HP-GL Instructions Covered 

- OA The Output Actual Position and Pen Status Instruction OC The Output Commanded Position and Pen Status Instruction 

- OE The Output Error Instruction OF The Output Factors Instruction OI The Output Identification Instruction OO The Output Options Instruction OS The Output Status Instruction 

## Terms You Should Understand 

Output Terminator — denoted in this manual as [TERM] — the ASCII character or characters sent by the plotter at the end of a plotter re sponse to an output command. With an HP-IB or HP-IL interface, the two characters, carriage return and line feed, are the output terminator. With an RS-232-C interface, the output terminator is a carriage return, unless modified by an ESC. M command. 
