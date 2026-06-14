**ESC GS # m N n1 n2 n3 n4 LF NUL** 

|[Name]|Set memory switch|Set memory switch||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|[Code]|ASCII|ESC GS<br>#|m<br>N<br>n1||n2|n3<br>n4<br>LF NUL||||||||||
||Hex.|1B<br>1D<br>23|m<br>N<br>n1||n2|n3<br>n4<br>0A||00||||||||
||Decimal|27<br>29<br>35|m<br>N<br>n1||n2|n3<br>n4<br>10||0||||||||
|[Defined Area]|[Defined Area]|48≤<br> n1≤<br> 57 (”0”≤<br>|n1≤<br> “9”), 65≤|≤<br> n1≤<br>||70 (”A”≤<br>|n1≤<br> “F”), 97|“F”), 97≤<br>|n1≤<br>||102 (“a”≤<br>|n1≤<br>||“f”)|“f”)|
|||48≤<br> n2≤<br> 57 (”0”≤<br>|n2≤<br> “9”), 65≤|≤<br> n2≤<br>||70 (”A”≤<br>|n2≤<br> “F”), 97|“F”), 97≤<br>|n2≤<br>||102 (“a”≤<br>|n2≤<br>||“f”)||
|||48≤<br> n3≤<br> 57 (”0”≤<br>|n3≤<br> “9”), 65≤|≤<br> n3≤<br>||70 (”A”≤<br>|n3≤<br> “F”), 97|“F”), 97≤<br>|n3≤<br>||102 (“a”≤<br>|n3≤<br>||“f”)||
|||48≤<br> n4≤<br> 57 (”0”≤<br>|n4≤<br> “9”), 65≤|≤<br> n4≤<br>||70 (”A”≤<br>|n4≤<br> “F”), 97|“F”), 97≤<br>|n4≤<br>||102 (“a”≤<br>|n4≤<br>||“f”)||
|||Spec. A||||||||||||||
|||m = 87, 84, 44, 43, 45, 64|m = 87, 84, 44, 43, 45, 64（m = “W”, “T”,  “,”, “+”, “-”, “@”|m = “W”, “T”,  “,”, “+”, “-”, “@”）||||）||||||||
|||48≤<br> N≤<br> 57 (”0”≤<br> N≤<br> “9”), 65≤<br>||N≤<br>|(*)70 (”A”≤<br>||N≤<br> (*)“F”), 97≤||≤<br>|N≤<br>|(*) 102, (“a”≤<br>||N≤<br>(*) (*) “f”)||(*) (*) “f”)|
|||Spec. B||||||||||||||
|||m = 87, 84, 44, 43, 45, 64|m = 87, 84, 44, 43, 45, 64（m = “W”, “T”,  “,”, “+”, “-”, “@”|m = “W”, “T”,  “,”, “+”, “-”, “@”）||||）||||||||
|||48≤<br> N≤<br> 57 (”0”≤<br> N≤<br> “9”), 65≤<br>||N≤<br>|(*)70 (”A”≤<br>||N≤<br> (*)“F”), 97≤||≤<br>|N≤<br>|(*) 102, (“a”≤<br>||N≤<br>(*) (*) “f”)||(*) (*) “f”)|
|||N = 85 (N = “U”) User defined area||||||||||||||
|||Spec. C||||||||||||||
|||m = 87, 84, 44, 43, 45, 64, 42 (m = “W”, “T”, “,”, “+”, “-”, “@”, “*”|m = 87, 84, 44, 43, 45, 64, 42 (m = “W”, “T”, “,”, “+”, “-”, “@”, “*”||||m = 87, 84, 44, 43, 45, 64, 42 (m = “W”, “T”, “,”, “+”, “-”, “@”, “*”）|||）||||||
|||48≤<br> N≤<br> 57 (”0”≤<br> N≤<br> “9”), 65≤<br>||N≤<br>|(*)70 (”A”≤<br>||N≤<br> (*)“F”), 97≤||≤<br>|N≤<br>|(*) 102, (“a”≤<br>||N≤<br>(*) (*) “f”)||(*) (*) “f”)|
|||N = 85 (N = “U”) User defined area||||||||||||||
|||(*) The memory switch defined area differs according to the model.|||(*) The memory switch defined area differs according to the model.|||||||||||



[Initial Value] - - - [Function] Sends command to write after defining memory switch using the definition command specified by the following classes. 

Memory switch information defined by the command to write is written to the volatile memory. When writing to the volatile memory by the command to write, the printer executes a reset. This command exists in models that have the specifications of A, B and C indicated in the above defined areas. 

On models that have specification C, you can load the default settings by specifying m = 42 (*). Models having specifications B can register any 16 bit data by specifying N = 85 (”U”).   (See the “Special Appendix, Command Table per Model” for details per model.) 

|Functions|Class|m|N|n1 n2 n3n4|
|---|---|---|---|---|
|Definition data write and reset|Write|“W”|Fixed at“0”|Fixed at“0000”|
|Definition data write and reset and|Write|“T”|Fixed at “0”|Fixed at “0000”|
|selfprint|||||
|Data definition (data specification)|Definition|“,”|N|n1 n2 n3 n4|
|Data definition(specify bit and set)|Definition|“+”|N|n1 n2 n3n4|
|Data definition(specify bit and clear)D|Definition|“-”|N|n1 n2 n3n4|
|Definitiondata (alldatainitialized)|Definition|“@”|Fixed at“0”|Fixed at“0000”|
|Definitiondata (load default settings)D|Definition|“*”|Fixed at“0”|Fixed at“0000”|
|• m:<br>Mode selection|||||
|• N:<br>Memory switch number to specify|||Memory switch number to specify||
|• n1 n2 n3 n4:<br>Specify data||Specify data<br>m = (“,”) Specify data|||
|||m = (“+”) Bit number to set|||
|||m = (“-“) Bit number to clear|||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-65 
