## **C O N F I D E N T I A L** 

Printer status ➁: Not printing because of a paper-end 

When the sensor detects that a roll paper is inserted, the printer starts loading. 

- Printer status ➂: Waiting for a roll paper to be inserted (waiting for online recovery) 

The printer is in the paper wait status after loading and the paper out LED is off. 

- Printer status ➃: Recovery confirmation status (online recovery wait status) 

After waiting for a roll paper to be inserted, the paper out LED blinks, and the printer is in the recovery confirmation status. 

- Printer status ➄: Normal operation 

When the online recovery wait time (the printer status ➂ + ➃) has elapsed, when the paper feed button is pressed during the recovery confirmation time, or when DLE ENQ (n = 0) is executed, the paper out LED is off, the printer recovers online, and the printer executes normal processing. 

- During printer status ➂ and ➃, ASB status and DLE EOT (n = 1: Printer status) are “online recovery wait status.” 

User Operation 

- Operation ➀: When the printer stops printing because of a paper-end, open the printer cover, remove the old roll paper, and insert a new roll paper. 

- Operation ➁: When paper position adjustment is needed, close the printer cover after the adjustment. If the paper out LED is off, the paper can be fed by the paper feed button. After completing paper insertion, be sure to close the printer cover. 

Operation ➂: Make sure that the paper out LED is blinking. If the paper out LED is off, wait until it blinks. After confirming that the paper out LED is blinking, press the paper feed button. 

[Model-dependent variations] TM-U230 

## **Program Example for all printers** 

PRINT #1, CHR$(&h1D);"z0";CHR$(10);CHR$(60) ← Transmits Waiting for a roll paper to be inserted in 5 sec, Recovery confirmation status in 30 sec. 
