## **C O N F I D E N T I A L** 

|**D E N T I A L**||
|---|---|
|**Cause**|**Solution**|
|(Number of columns×number of<br>rows) < number of codeword|Increase the number of columns by Function 065.<br>Increase the number of rows by Function 066.|
|Number of the codeword in the<br>data area is more than 928.|Reduce the data by Function 080.<br>Lower the error correction level by Function 069.|
|There is no data in the symbol<br>storage area.|Sends data to the symbol storage area by Function<br>080.|



■ See previous [Notes for transmission process] for process sending data group. [Model-dependent variations] TM-T90, TM-L90, TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-P60 

## TM-T90, TM-L90 

**When the vertical size exceeds 831 dots in standard mode, “other information” is “Printing is impossible“(in decimal: 49).** 

## TM-T88IV, TM-T70 

**This function is not supported in the Japanese specification.** 

**When the vertical size exceeds 831 dots in standard mode, "other information" is "Printing is impossible"(in decimal: 49).** 

## TM-T20, TM-T88V 

**When the vertical size exceeds 831 dots in standard mode, "other information" is "Printing is impossible"(in decimal: 49).** 

## TM-P60 

TM-P60 **with peeler supports this function.** 

**When the vertical size exceeds 1200 dots in standard mode, “other information” is “Printing is impossible“(in hexadecimal: 31H / in decimal: 49).** 
