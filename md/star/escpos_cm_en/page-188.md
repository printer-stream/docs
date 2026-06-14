Rev.2.52 

## **ESC RS L m** 

Name Batch Control Logo Code ASCII ESC RS L m Hex. 1B 1E 4C m Decimal 27 30 76 m Defined Region Spec. A  m = 255 Spec. B   0 ≤ m ≤ 3,   48 ≤ m ≤ 51 (“0” ≤ m ≤ “3”), m = 255) Initial Value --Function Spec. A: Batch deletes all registered logos. After printing is completed, the printer is reset. Spec. B: Performs a control specified by parameter m for the logo. After execution, the printer is reset 

|After execution,|the printer is reset|
|---|---|
|m|Logo Control Mode|
|0,48|Normal mode,batchprinting|
|1,49|Double-wide mode,batchprinting|
|2,50|Double-tall mode,batchprinting|
|3,51|Double-wide,double tall mode,batchprinting|
|255|Batch delete logos|



This command is ignored in page mode. 

ESC/POS Command Specifications 

188 
