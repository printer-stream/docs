Rev.2.52 

## **4. COMMAND DETAILS 4-1 Explanation of Terms** 

## **• Reception buffer** 

The buffer for storing data (reception data) received from the host, as it is called the reception buffer. Reception data is temporarily stored in the reception buffer, then processed sequentially. 

## **• Print buffer** 

The buffer for storing image data for printing is called the print buffer. 

## **• Print buffer full** 

The state in which the buffer has no more space available is called print buffer full.  When the print buffer is full in standard mode, data in the print buffer is printed and a line feed is performed when new print data is processed. This is the same as a LF.  When the print buffer is full in the page mode, the printer move the print position to the head of the next line then starts with the new print data. 

## **• Top of line** 

The top of line is a state that satisfies the following conditions. 

1. There is currently no print data in the print buffer. 

2. There is no skipped portion using HT 3. A print position has not been specified using ESC$, and ESC \ 

## **• Printable region** 

This is the maximum printable area with the printer’s specifications. 

## **• Print region** 

This is the printing area specified by a command. (Print region **≤** printable region) 

- ANK character base line 

**==> picture [387 x 184] intentionally omitted <==**

**----- Start of picture text -----**<br>
1.  Normal direction characters FONT-A/FONT-B (Standard Mode/Page Mode)<br>20 Dots<br>24 Dots<br>Ay ���� ���������<br>2.  Rotated characters FONT-A (Standard Mode)<br>10 Dots (11 dots when using<br>enhanced printing)<br>< Base Line<br>A y<br>�<br>**----- End of picture text -----**<br>


**3. Rotated characters FONT-B (Standard Mod** 

**==> picture [240 x 56] intentionally omitted <==**

**----- Start of picture text -----**<br>
7 Dots (8 dots when using<br>enhanced printing)<br>< [----] Base Line<br>A y<br>�<br>**----- End of picture text -----**<br>


ESC/POS Command Specifications 

30 
