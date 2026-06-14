Rev.2.52 

## **GS:** 

Name Start/execute macro definition Code ASCII GS : 

Code ASCII GS : Hex. 1D 3A Decimal 29 58 Function Starts and stops macro definition. Details • If this command is input during normal operation, the macro definition is started. 

   - If this command is input while defining a macro, the macro definition is stopped. 

   - If GS ^ (Execute macro definition) is input while defining a macro, the macro definition is cancelled and the contents are cleared. 

   - The initial status of the macro is undefined. 

   - The contents of the definition are not cleared by ESC @ (Initialize printer). 

   - The macro enters an undefined status if GS: is input immediately after inputting GS:. 

   - The data count that can be defined in a macro is 2048 bytes.  Data that exceeds 2048 bytes is not defined. 

- STAR • Operators should be aware that if the raster graphic command (GS v) is inserted into the data while defining a macro, the macro definition is immediately ended as being undefined and the printer enters a raster graphics process. 

Reference 

GS ^ 

ESC/POS Command Specifications 

127 
