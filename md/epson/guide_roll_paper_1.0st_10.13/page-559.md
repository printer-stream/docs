EXECUTING COMMAND 

## **C O N F I D E N T I A L** 

## <Function 64> **FS ( E** _**pL pH fn m a1 n1…[ak nk]**_ ( _fn_ =64) 

- [Name] Make extended settings for top/bottom logo printing 

[Format] ASCII FS ( E pL pH fn m a1 n1 ... [aknk] Hex 1C 28 45 pL pH fn m a1 n1 ... [aknk] Decimal 28 40 69 pL pH fn m a1 n1 ... [aknk] [Range] 4 ≤ (pL + pH × 256) ≤ 12  (However, (pL+ pH × _256_ ) = 2 × K + 2: 4 ≤ pL ≤ 12, pH = 0) fn = 64 

- m = 2 

TM-T20 **:** a **= 64 to 67** TM-T88V: a **= 48, 64 to 67** n = 48, 49 

1 ≤ _k_ ≤ 5 

- [Default] n _=_ 49 [when a = 48] (TM-T88V only) 

   - n _=_ 48 [when a = 64] 

   - n _=_ 49 [when a = 65] n _=_ 49 [when a = 66] n _=_ 48 [when a = 67] 

- [Description] Makes extended settings for top/bottom logo printing. 

|**a**|**Function**|
|---|---|
|48|Prints the top logo while paper feeding to the<br>cutting position.|
|64|Prints the top logo at power-on.|
|65|Prints the top logo when the roll paper cover is<br>closed.|
|66|Prints the top logo while clearing the buffer to<br>recover from a recoverable error.|
|67|Prints the top logo after paper feeding with the<br>paper Feed button has finished.|
