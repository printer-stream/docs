Rev.2.52 

- See the printer’s product specifications manual for details on NV memory capacity. 

- One NV bit image definition data is configured by [xL xH yL yH d1…dk].  Therefore, if defining only one NV bit image data, n = 1.  The data of [xL xH yL yH d1…dk] is processed only once.  This uses ([data: (xL + xH x 256) x (yL + yH x 256) x 8] + [Data: 4]) of non-volatile memory. 

- The maximum region for NV bit image definition varies according to the printer model. Several NV bit images can be defined, but NV bit image data that exceeds the maximum definition region with a total capacity of (data bit image data + header) cannot be defined. 

- The printer is in a BUSY state just prior to writing to the non-volatile memory. The printer will be in a BUSY state prior to writing data regardless of the conditions for a BUSY state. 

- The sending of ASB status and detection of status are not possible while processing this command even when the ASB function is specified. 

- When processing this command while defining a macro, the macro definition is terminated and the command commences with processing. 

- NV bit images that have been defined are not initialized by the ESC @ (Initialize printer), a reset or by turning off the printer’s power. 

- This command only defines the NV bit image, but it does not print it.  To print an NV bit image, use FS p (Print NV bit image). 

Notes: 

- There is the potential of damaging the non-volatile memory by overusing the command, so only use this command once a day to write to the non-volatile memory. 

- The printer executes a hardware reset just after writing to the non-volatile memory. Therefore, download characters and download bit images and macros are handled as being undefined and the reception buffer and print buffer are cleared.  The printer returns all settings to their default status. 

- The printer may enter a BUSY state while writing data to the non-volatile memory when using this command.  While the printer is BUSY, the printer will stop receptions so data will not be received from the host (including real-time commands). 

## STAR 

- Dot density (when the STAR printer head = 203 DPI) on STAR printers. 

|m|Mode|Densityof Vertical Direction Dots|Densityof Horizontal Direction Dots|
|---|---|---|---|
|0,48|Normal Mode|203 DPI|203 DPI|
|1,49|Double-wide Mode|203 DPI|101 DPI|
|2,50|Double-tall Mode|101 DPI|203 DPI|
|3,51|Quadruple Mode|101 DPI|101 DPI|



Related Commands FS p 

ESC/POS Command Specifications 

84 
