Rev.2.52 

## **ESC GS # m N n1 n2 n3 n4 LF NUL** 

|Name|Memory Switch Settings|
|---|---|
|Code|ASCII<br>ESC<br>GS<br>#<br>m<br>N<br>n1<br>n2<br>n3<br>n4<br>LF NUL|
||Hex.<br>1B<br>1D<br>23<br>m<br>N<br>n1<br>n2<br>n3<br>n4<br>0A<br>00|
||Decimal<br>27<br>29<br>35<br>m<br>N<br>n1<br>n2<br>n3<br>n4<br>10<br>0|
|Defned Region|48≤ n1≤57 (”0” ≤n1 ≤ “9”), 65 ≤n1 ≤70 (”A” ≤n1 ≤ “F”), 97 ≤n1 ≤102 (“a”≤n1 ≤“f”)|
||48≤n2 ≤57 (”0” ≤n2 ≤ “9”), 65 ≤n2 ≤70 (”A” ≤n2 ≤ “F”), 97 ≤n2 ≤102 (“a”≤n1 ≤“f”)|
||48≤ n3 ≤57 (”0” ≤n3 ≤ “9”), 65 ≤n3 ≤70 (”A” ≤n3 ≤ “F”), 97 ≤n3 ≤102 (“a”≤n3 ≤“f”)|
||48 ≤ n4 ≤ 57 (”0” ≤n4 ≤ “9”), 65 ≤n4 ≤70 (”A” ≤n4 ≤ “F”), 97 ≤n4 ≤102 (“a”≤n4 ≤“f”)|
||Spec. A|
||m = 87, 84, 44, 43, 45, 64 (m = “W”, “T”,  “,”, “+”, “-”, “@”)|
||48≤N≤57 (”0”≤N≤“9”), 65≤N≤(*)70 (”A”≤N≤(*)“F”), 97≤N≤(*) 102, (“a”≤N≤(*) (*) “f”)|
||Spec. B|
||m = 87, 84, 44, 43, 45, 64 (m = “W”, “T”,  “,”, “+”, “-”, “@”)|
||48≤N≤57 (”0”≤N≤“9”), 65≤N≤(*)70 (”A”≤N≤(*)“F”), 97≤N≤(*) 102, (“a”≤N≤(*) (*) “f”)|
||N = 85 (N = “U”) User defned area|
||Spec. C|
||m = 87, 84, 44, 43, 45, 64, 42 (m = “W”, “T”, “,”, “+”, “-”, “@”, “*”)|
||48≤N≤57 (”0”≤N≤“9”), 65≤N≤(*)70 (”A”≤N≤(*)“F”), 97≤N≤(*) 102, (“a”≤N≤(*) (*)“f”)|
||N = 85 (N = “U”) User defned area|
||(*) The memory switch defned area difers according to the model.|
|Initial Value|---|
|Function|Sends command to write after defning memory switch using the defnition command|
||specifed by the following classes.|
||Memory switch information defned by the command to write is written to the volatile memory.|
||When writing to the volatile memory by the command to write, the printer executes a reset.|
||This command exists in models that have the specifcations of A, B, and C as indicated in the|
||above defned areas.|
||Models having B and C specifcations can register any 16 bit data by specifying N = 85 (U).|
||Models with Spec. C can load the factory default settings by specifying m=42 (“*”).|
||(See the “Special Appendix, Command Table per Model” for details per model.)|
||Consider the life of the non-volatile memory and avoid over-use of this command.|



|Function<br>|Class|m|N|n1 n2 n3 n4|
|---|---|---|---|---|
|Defnition data write and reset<br>|Write|“W”|Fixed at “0”|Fixed at “0000”|
|<br>Defnition data write and reset and testprint<br>|Write<br>|“T”|Fixed at “0”|Fixed at “0000”|
|<br>Data Defnition(Data Specifcation)<br>|Defnition<br>|“,”|N|n1 n2 n3 n4|
|<br>Data defnition(Set specifed bit)<br>|Defnition<br>|“+”|N|n1 n2 n3 n4|
|<br>Data defnition(Clear specifed bit)<br>|Defnition<br>|“-”|N|n1 n2 n3 n4|
|<br>Data Defnition(Initialize all data)<br>|Defnition<br>|“@”|Fixed at “0”|Fixed at “0000”|
|<br>Data Defnition(Load FactoryDefault Setting)|Deftion|“*”|Fixed at “0”|Fixed at “0000”|



ESC/POS Command Specifications 

184 
