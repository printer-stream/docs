<Example of Command Transmission> 

1) Set the Auto Logo function in advance and register it to the non-volatile memory. ESC GS / 1 n (n=0x01) Auto Logo Function ON ESC GS / 2 n ( n=“/” ) Specify Auto Logo Command Character (“/”) ESC GS / 3 nL nH d1 d2... dk User Macro 1 Definition nL=4  nH=0 Registered Macro Count = 4 Bytes d1=0x1b  d2=0x1d  d2=0x61  d3=0x01 Registered Macro <ESC GS a 1: Center Alignment> ESC GS / 4 nL nH d1 d2... dk User Macro 2 Definition nL=12  nH=0 Registered Macro Count = 12 Bytes d1=0x1b  d2=0x64  d3=0x03 Registered Macro <ESC d 3: Cutting position partial cut> d4=0x1b  d5=0x1c  d6=0x70  d7=0x01  d8=0x00 <ESC FS p 1 0: Print Logo 1 d9=0x1b  d10=0x1d  d11=0x61  d12=0x00 <ESC GS a 0: Left Alignment> ESC GS / 5 n (n=0x01) Auto Logo Command Character, Space Switch ESC GS / 6 n ( n=0x01) Partial Cut Before Auto Logo Printing Valid ESC GS / W Register Auto Logo Definition Data to Non-volatile Memory 

2) Send registered command character embedded in print data “CHEESE BURGER /2” → “/” is recognized as a command character. Command characters are replaced by spaces. “2” specifies Logo 2. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-113 
