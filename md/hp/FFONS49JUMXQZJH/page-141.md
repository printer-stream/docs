; 

Displayed current pen position and identification. 1000 1000 0 7470a 

## Apple II Applesoft BASIC Example: 

10 PR 3: IN# 3 20 Z2$= "WTs" + CHRE (26) 30 ¥¢= "RDE" + CHR$ (26) 40 PRINT 2$; "PA1000,1000;0C;" 50 PRINT Y$; 560 INPUT A,B,C 70 PRINT ‘Y$; 80 INFUT D$ 90 PRINT Z$; "OI" 100 PRINT Y$; 110 INPUT A$ 120 PRINT Y$ 130 INPUT D$ 140 PR O: IN# O 150 PRINT A,B,C,A$ 160 END 

## Displayed current pen position and identification, 

1000 1000 0) T470A 

For an explanation of PR# 3, Z$ and PR# 0, refer to the Apple II example in the prior section. The string Y$ instructs the plotter at address 5 to talk. The Apple II sends an untalk command after it receives a carriage return character. The plotter with an HP-IB interface terminates all output with a carriage return followed by a line feed. Therefore, in order to clear the plotter’s buffer for future output, another talk instruction and another input statement containing a dummy variable (D$ in this program) must follow the input statement which reads parameters of the plotter output statement. The additional talk and input instructions will read the line feed character, thus clearing the plotter’s buffer. 

HP-IBINTERFACING 9-13 
