## **C O N F I D E N T I A L** 

|n|**Function**|**Number of error correction codeword**|
|---|---|---|
|51|Error correction level 3|16|
|52|Error correction level 4|32|
|53|Error correction level 5|64|
|54|Error correction level 6|128|
|55|Error correction level 7|256|
|56|Error correction level 8|512|



■ Error correction level specified by “ratio” (m = 49) is as follows. The error correction level is defined by the calculated value [number of data codeword × n × 0.1 = (A)]. The number of the error correction codeword is changeable in proportion to the number of the codeword in the data area. 

|**Calculated value (A)**|**Correction level**|**Number of error correction codeword**|
|---|---|---|
|0 – 3|Error correction level 1|4|
|4 – 10|Error correction level 2|8|
|11 – 20|Error correction level 3|16|
|21 – 45|Error correction level 4|32|
|46 – 100|Error correction level 5|64|
|101 – 200|Error correction level 6|128|
|201 – 400|Error correction level 7|256|
|401 or more|Error correction level 8|512|



■ The error correction codeword calculated by modulus 929. 

■ Settings of this function are effective until ESC @ is executed, the printer is reset, or the power is turned off. [Model-dependent variations] TM-T20, TM-T88IV, TM-T88V, TM-T70, TM-P60 
