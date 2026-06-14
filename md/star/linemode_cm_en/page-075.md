(Reference Information) Differences between the ETB command and this command 

|Item|ESC GS ETX s n1 n2|ETB|
|---|---|---|
|Affect on ASB (ETB Status)|None|Yes|
|ASB occurrence|None|Yes|
|Affect of ASB valid/invalid setting|None|Yes|
|Affect of the ESC RS E n command|None|Yes|
|Status<br>transmission<br>destination<br>in<br>Ethernet<br>(When multi-sessionsisvalid)|Send only when in the print<br>session<br>(host)<br>that<br>is<br>connected|Send ASB to all sessions<br>(hosts) that are connected|



* This print end counter and the ETB counter sent by the ETB command are separate. They have no affect on each other. 

The following shows a communication example of this command. 

|Communication Example 1|Communication Example 1||||
|---|---|---|---|---|
||Host Transmission Data||Printer return data||
||ESC GS ETX**0x00**0x00 0x00|→||(Reference|
|||←|ESC GS ETX**0x00**0x00 0x00 0x00 0x00|Counter)|
||Print Data + ESC GS ETX**0x01**0x00 0x00|→||(Reference|
|||←|ESC GS ETX**0x01**0x00 0x00 0x01 0x00|Update)|
||Print Data + ESC GS ETX**0x01**0x00 0x00|→||(Reference|
|||←|ESC GSETX**0x01** 0x00 0x00 0x020x00|Update)|
|Communication Example 2|||||
||Host Transmission Data||Printer return data||
||ESC GS ETX**0x02**0x02 0x00|||(Clear|
||ESC GS ETX**0x00**0x02 0x00|→||Counter)|
|||←|ESC GS ETX**0x00**0x02 0x00 0x00 0x00|(Reference|
|||||Counter)|
||Print Data + ESC GS ETX**0x01**0x02 0x11|→||(Reference|
|||←|ESC GS ETX**0x01**0x02 0x11 0x01 0x00|Update)|
||Print Data + ESC GS ETX**0x01**0x02 0x12|→||(Reference|
|||←|ESC GS ETX**0x01**0x02 0x12 0x02 0x00|Update)|
||Print Data + ESC GS ETX**0x01**0x02 0x13|→||(Reference|
|||←|ESC GS ETX**0x01**0x02 0x13 0x03 0x00|Update)|
||Print Data + ESC GS ETX**0x01**0x02 0x14|→||(Reference|
|||←|ESC GSETX**0x01** 0x020x140x040x00|Update)|



## <Example using n1, n2> 

- For Ethernet:  Specify as n1 = host ID, n2 = document number, and check the compatibility of source information and returned information for the host ID and document ID along with getting the returned print end counter. 

- For cases other than Ethernet:  Specify n1+n2 x 256 as the document ID and check the compatibility with the document ID in the same way. 

- When it is not possible to check compatibility of the source and returned data, fix at n1 = 0, n2 = 0. 

When s = 3, and s = 4, printer operates as though in data cancel mode. 

(1)  Receive and discard all data being received. (Document start command) 

- (2) Receive and discard only the current page. 

(Document start command + document end command) 

If there is an error after receiving the document start command, reception data is received and discarded until the document end command is received when the printer is recovered from the error. If the document end command cannot be recognized, all reception data is destroyed. Timeouts are two seconds. Automatically cancels the data intake mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-57 
