## **C O N F I D E N T I A L DLE DC4 (** _**fn**_ **= 3)** 

EXECUTING COMMAND 

- [Name] Sound buzzer in real-time 

- [Format] ASCII DLE DC4 fn a n r t1 t2 Hex 10 14 03 a n r t1 t2 Decimal 16 20 3 a n r t1 t2 

- [Printers not featuring this command] TM-J2000/J2100, TM-L90, TM-T88IV, TM-T70, TM-P60, TM-U230, TM-U220 

- [Range] a = 0 

   - n = 0 

   - r = 0 

   - fn = 3 

   - t1 = 1 t2 = 0 

- [Description] Sounds the buzzer with a sound pattern specified by a the number of times specified by r. 

      - When a = 0, does not sound the buzzer. 

      - When r = 0, repeats a sound pattern specified by a infinitely. 

- [Notes] 

- This command can be used after enabling real time command processing with GS ( D. 

- This is a real-time command that the printer executes upon receiving it. Note the following when using this command. 

   - If this command is embedded within the code string of another command, it is processed as a parameter of the other command, and the print result is not correct. 

   - If another command (such as graphics data or defined data) has a code string in a parameter that is the same as this command, the printer starts processing this command. 

- This command cannot be used when sending the block data (Header ~ NUL). 

- This command is effective when the printer is disabled by ESC = (select peripheral device). 

- With a serial interface, the printer executes this command even when it is in offline, receive buffer full, or error status. 
