## **C O N F I D E N T I A L** 

## **DLE DC4 (** _**fn**_ **= 1)** 

## EXECUTING COMMAND 

- [Name] Generate pulse in real-time 

[Format] ASCII DLE DC4 n m t Hex 10 14 n m t Decimal 16 20 n m t 

- [Printers not featuring this command] TM-P60,  TM-U230 

- [Range] n = 1 

   - m = 0, 1 

   - 1 ≤ t ≤ 8 

- [Description] Outputs the pulse specified by t to connector pin m as follows in real time: 

   - m **Connector pin** 

   - 0 Drawer kick-out connector pin 2 1 Drawer kick-out connector pin 5 

The pulse ON time is [t × 100 ms] and the OFF time is [t × 100 ms] 

- [Notes] ■ This is a real-time command that the printer executes upon receiving it. Note the following when using this command. 

      - If this command is embedded within the code string of another command, it is processed as a parameter of the other command, and the print result is not correct. 

      - If another command (such as graphics data or defined data) has a code string in a parameter that is the same as this command, the printer starts processing this command. 

   - This command is ignored in the following states: 

      - In error status 

      - When the pulse is being output to the connector pin (during processing of ESC p and during execution of this command) 

      - During transmission of block data (Header ~ NUL) 
