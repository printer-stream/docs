Rev.2.52 

## **GS C 0 n m** 

|Name|Name|Set counter print mode||
|---|---|---|---|
|Code||ASCII<br>GS<br>C<br>0<br>n<br>m||
|||Hex.<br>1D<br>43<br>30<br>n<br>m||
|||Decimal<br>29<br>67<br>48<br>n<br>m||
|Defned Region<br>0≤n≤5||||
|||0≤m≤2, 48≤m≤50||
|Initial Value||<br>n = 0||
|||m = 0||
|Function||Sets the serial number counter print mode.||
||m|PrintingPosition<br>Processingof Counter Value Less than Set Digit Count||
||0,48|Align Right<br>Applies a space to the left side||
||1,49|Align Right<br>Applies a 0 to the left side||
||2,50|Align Left<br>Applies a space to the right side||
|Details||• n specifes the digits to print.||
|||• When n = 0, the printer prints only the actual number of digits of the counter value.||
|||• Sets the print digit count when n ≠ 0.||
|||• m sets the serial number counter printing position in the set digit count.||



- If the counter value is larger than the n set digit count, the printer prints n digits below the counter value. 

**==> picture [405 x 140] intentionally omitted <==**

**----- Start of picture text -----**<br>
<n = 3, m = 0>   <n = 3, m = 1>   <n = 3, m = 2><br>ΔΔ1  001  1ΔΔ<br>Δ=Space<br>**----- End of picture text -----**<br>


Reference GS C 1, GS C 2, GSC ;, GS c 

ESC/POS Command Specifications 

129 
