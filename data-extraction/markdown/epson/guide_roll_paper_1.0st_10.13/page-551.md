## C O N F I D E N T I A L

## FS ( E pL pH fn [parameter]

[Name]

Group of commands for receipt enhancement control

[Printers not featuring this command] TM-J2000/J2100 , TM-L90 , TM-T88IV , TM-T70 , TM-P60 , TM-U230 , TM-U220 [Description] Controls the receipt enhancement functions

- pL , pH specify ( pL + pH × 256) as the number of bytes after pH ( fn and [parameter] ).
- fn specifies the function.
- [parameters] specify the process of each function.
- Frequent write command executions by an NV memory write command may damage the NV memory. Therefore, it is recommended to limit using the commands to no more than 10 times a day.
- If the power is turned off or the printer is reset via an interface while this command is being executed, the printer may go into an abnormal condition.  Be careful not to turn the power off or let the printer be reset via an interface while this command is being executed.

|   fn | Code                                 | Function no.   | Function name                                       |
|------|--------------------------------------|----------------|-----------------------------------------------------|
|   60 | FS ( E p L p H fn mc d1 d2 d3        | Function 60    | Cancel set values for top/ bottom logo printing     |
|   61 | FS ( E p L p H fn mc                 | Function 61    | Transmit set values for top/ bottom logo printing   |
|   62 | FS ( E p L p H fn mkc1 kc2 a n       | Function 62    | Set top logo printing                               |
|   63 | FS ( E p L p H fn mkc1 kc2 a         | Function 63    | Set bottom logo printing                            |
|   64 | FS ( E p L p H fnm a1 n1 ... [ak nk] | Function 64    | Make extended settings for top/bottom logo printing |
|   65 | FS ( E p L p H fnman                 | Function 65    | Enable/disable top/bottom logo printing             |

[Notes]
