Rev.2.52 

## **DLE DC4 n m t** 

Name Real-time output of specified pulse Code ASCII DLE DC4 n m t Hex. 10 14 n m t Decimal 16 20 n m t n = 1 Defined Region m = 0,1 1 ≤ t ≤ 8 Function This outputs a signal specified by t to the connector pin specified by m. m = 0: #2 Pin of the drawer kick connector m = 1: #5 Pin of the drawer kick connector On time is set to t x 100 msec; Off time is set to t x 100 msec. 

- Details • This command is ignored if the printer experiences an error while processing this command. 

   - This command is ignored while outputting the pulse (while executing either ESC p or DEL DC4) to the connector pin while processing this command. 

   - This command is processed upon reception. 

   - This command is executed even when the printer is offline, the reception buffer is full, or there is an error status on serial interface models. 

   - This command cannot be executed when the printer is busy on parallel interface models. The printer will not enter a BUSY status when offline or when there is an error when BUSY condition of reception buffer full, offline/reception buffer full is handled as a reception buffer full in the DIP switch settings. 

   - This command is enabled even when the printer specification is disabled by ESC  =  (select peripheral devices). 

- Notes: • Operators must use caution for other commands when a data string that is the same as this command is received because it operates in the same manner as this command. 

   - Do not use this command to interrupt code strings of other commands that consist of 2 or more codes. 

STAR Printing and drawer drive cannot be performed simultaneously.  Therefore, this command is processed when data has been read out from the reception buffer.  If the printer is printing, this waits for the printing to end to drive the drawer, so real-time operation is not possible using the reception buffer status. 

Reference 

ESC p 

ESC/POS Command Specifications 

40 
