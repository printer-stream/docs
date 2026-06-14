## The No Operation Instructions, NOP 

In order to maintain software compatibility with the 9872 plotter, the 7470 recognizes six 9872-related instructions as no operation NOP instructions. These six NOP instructions are: 

Automatic Pen Pickup AP Advance Full Page AF Adaptive Velocity VA Advance Half Page AH Normal Velocity VN Enable Cutter EC 

If these instructions are included in a program, they are recognized by the 7470 and implemented as a NOP ({i.e., they are ignored). 

On a 7470 plotter with an HP-IL interface, UC is also a NOP instruction. 

## ASCIT Character Codes 

Binary is often used as a code to represent not only numbers, but also alphanumeric characters such as “A” or “,” or “x” or “2”. One of the most common binary codes used is ASCII. ASCII is an eight-bit code, containing seven data bits and one parity bit. The plotter uses ASCII for most I/O operations. No parity bit is used. For example: 

||ASCII|ASCII|
|---|---|---|
|Character|Binary Code|Decimal Code|
|A|01000001|65|
|B|01000010|66|
|?|00111111|63|



A complete list of ASCII characters and their decimal representation and the characters drawn by the plotter in each of the five character sets are shown on the following pages. The five character sets are: 

|Set No.|Description|
|---|---|
|Set 0|ANSI<br>ASCII|
|Set 1|9825 Character Set|
|Set 2|French/German|
|Set 3|Scandinavian|
|Set4|Spanish/LatinAmerican|



‘American Standard Code for Information Interchange. 

REFERENCE MATERIAL C-7 
