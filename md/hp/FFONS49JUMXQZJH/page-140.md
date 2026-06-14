## TEK 4051 Example: 

100 DIM A$[S] 110 PRINT @5:"PA1000, 1000;a0C;" 120 INPUT @5:F,8B,C 130 PRINT @5:"01;" 140 INPUT @5:A$ 150 PRINT A,B,C,A$ 160 END 

Displayed current pen position and identification. 1000 1000 0 

TAT0A 

## Commodore PET 2001 Example: 

~ 

10 OPEN 5,5 20 PRINT#S, 'PA1000, 1000;0C" 30 INPUT#5,A,B,C 90 PRINT#S,"OI" SO INPUT#S,AS$ 60 PRINT A,B,C,AS 70 END 

Displayed current pen position and identification. 1000 1000 0 7T470A 

## Commodore PET 8032 Example: 

On the PET 80382, all alphabetic characters are displayed as lowercase. This is true for both BASIC program statements and for the plotter’s response. 

A dummy string variable should be included at the end of every input command which reads data from the plotter because the PET 8032 sends an untalk command after it receives a carriage return character. Since the plotter with an HP-IB interface terminates all output with a carriage return followed by a line feed, the line feed must be read into this dummy string variable in order to clear the plotter’s output buffer for future output. 

10 OPEN 5,5 ZO PRINT#S," PA1000, 1000; 0C" 30 INPUT#5,A,B,C,BS 40 PRINT#5, "OI" 50 INPUT#5,A$,BS 60 PRINT A,B,C,AS 70 END 

9-12 HP-IB INTERFACING 
