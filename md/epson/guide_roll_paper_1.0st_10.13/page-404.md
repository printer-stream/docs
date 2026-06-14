## **C O N F I D E N T I A L** 

## **GS ^** 

EXECUTING COMMAND 

[Name] Execute macro [Format] ASCII GS ^ r    t    m Hex 1D 5E r    t    m Decimal 29 94 r    t    m [Range] 1 ≤ r ≤ 255 0 ≤ t ≤ 255 m = 0, 1 [Default] None 

[Printers not featuring this command] TM-P60, TM-U230, TM-U220 

- [Description] Executes a macro r times while waiting t × 100 msec for each macro execution, using the mode specified by m as follows: 

   - When m = 0, the macro executes r times continuously at the interval specified by t. 

   - When m = 1, the printer waits for the period specified by t, flashes the LED, and then waits for the paper feed button to be pressed. After this button is pressed, the printer executes the macro once. The printer repeats this operation r times. 

## [Notes] 

- If a macro is not defined or if r is 0, this command is ignored. 

- Even if the panel buttons are disabled by ESC C 5, the paper feed button will be enabled temporarily while the printer is waiting for the buttons to be pressed when execution mode by button (m = 1) is specified. 

   - However, paper cannot be fed if the paper feed button is pressed. When the paper feed button is pressed, if DLE ENQ (n = 0) is processed, the printer performs in the same way as if the button were pressed once. 

- The waiting status for the paper feed to be pressed can be checked by DLE EOT (n = 1: Printer status) or basic ASB status. 

- If this command is processed while a macro is being defined, the printer cancels macro definition and clears the definition. 

- This command cannot be contained in the macro. Do not use this command when the macro is defined. 

- The LED and the paper feed button are different, depending on the printer model. 
