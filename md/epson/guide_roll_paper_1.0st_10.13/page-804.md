## **C O N F I D E N T I A L** 

■ The counter print mode is set by GS C 0. 

■ The counter mode (count-up, count-down, count-stop) and details of counter (maximum value, minimum value, stepping amount of incrementing or decrementing of a counter value, the repetition number of printing) are set by GS C 1 or GS C ;. 

■ The counter value is set by GS C 2 or GS C ;. 

[Model-dependent variations] None 

**Program Example Print Sample** PRINT #1, "AAAAA";CHR$(&H1D);"c";CHR$(&HA); AAAAA 1 PRINT #1, "BBBBB";CHR$(&H1D);"c";CHR$(&HA); BBBBB 2 
