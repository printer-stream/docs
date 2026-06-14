## **C O N F I D E N T I A L** 

## **FS ( L** 

## EXECUTING COMMAND 

[Name] Select label and black mark control function(s) 

[Printers not featuring this command] TM-J2000/J2100, TM-T90, TM-T20, TM-T88IV **,** TM-T88V **,** TM-T70, TM-U230, TM-U220 

- [Description] Various processes are performed on label or black mark paper. 

   - Function code (fn) specifies the function. 

|fn|**Function No.**|**Function name**|
|---|---|---|
|33|**Function 33**|Paper layout setting|
|34|**Function 34**|Paper layout information transmission|
|48|**Function 48**|Transmit the positioning information|
|65|**Function 65**|Feed paper to the label peeling position|
|66|**Function 66**|Feed paper to the cutting position|
|67|**Function 67**|Feed paper to the print starting position|
|80|**Function 80**|Paper layout error special margin setting|



- pL, pH specifies (pL + pH × 256) as the number of bytes after pH (fn and [parameters]). Description of the [parameters] is described in each function. 

## [Notes] 

- The functions of this command are determined by the (fn) setting. The actual command operation varies according to function. 

- When using label paper (die-cut label), use Functions 65 and 67. 

- When using black mark paper, use Functions 66 and 67. 

- When origin of layout is set to “paper layout is not used,“ Functions 65, 66, and 67 do not operate. 

- The position information of Function 48 is useful information when the origin of layout is set to “bottom of a label” or “top of a black mark.“ 

- The paper layout (layout reference) is set with <Function 33> of this command or GS ( E <Function 49>. 
