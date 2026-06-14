## Summary of Output Response Types ————————— 

The following table shows the number and type of items in the re sponse to each HP-GL output command. The table includes output commands explained in Chapters 2 and 6 as well as in this chapter. This table will be helpful when programming in languages such as FORTRAN which require you to specify the type of and number of digits in a variable. 

**==> picture [331 x 219] intentionally omitted <==**

**----- Start of picture text -----**<br>
|||||||||
|---|---|---|---|---|---|---|---|
|Number|of|
|Parameters|
|Instruction|Returned*|Type|and|Range|
|OA|3|integers,|all <|5|digits|.|
|OC**|3|decimals,|all <|11|digits|
|OD|3|integers,|all <|5|digits|
|OE|1|integer,|1|digit|
|OF|2|integers,|2|digits|each|
|OI|1|5-character|string|
|OO|8|integers,|1|digit|each|
|OP|4|integers,|lst|and|3rd <|5|digits;|
|2nd|and|4th <|4|digits|
|OS|1|integer,|<|3|digits|
|OW|4|integers,|lst|and|3rd <|5|digits;|
|2nd|and|4th < 4|digits|

**----- End of picture text -----**<br>


*In addition to these parameters, the output terminator [TERM] is always sent at the end of output, and commas are sent to separate parameters. 

- **If you have an HP-IB or RS-232-C plotter that has a serial prefix number lower than 2308A, OC parameters are output as integers. For more information, refer to the explanation of the OC instruction in this chapter. 

OBTAINING INFORMATION FROM THE PLOTTER 7-9 
