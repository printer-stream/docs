messages, are sent over the eight data lines and the three handshake lines. Uni-line messages are transferred over the five individual lines of the management bus. 

The commands serve several different purposes: 

- e Addresses or talk and listen commands select the instruments that will transmit and accept data. They are all multi-line messages. 

- e Unviersal commands cause every instrument equipped to do so to perform a specific interface operation. They include multi-line messages and three uni-line commands: interface clear (IFC), remote enable (REN), and attention (ATN). 

- e Addressed commands (also referred to as primary commands) are similar to universal commands, except that they affect only those devices that are addressed and are all multi-line commands. An instrument responds to an addressed command, however, only after an address has already told it to be talker or listener. 

- e Secondary commands are multi-line messages that are always used in series with an address, universal command, or addressed command to form a longer version of each. Thus they extend the code space when necessary. 

To address an instrument, the controller uses seven of the eight databus lines. This allows instruments using the ASCII 7-bit code to act as controllers. As shown in the following table, five bits are available for addresses, and a total of 31 allowable addresses are available in one byte. If all secondary commands are used to extend this into a two-byte addressing capability, 961 addresses become available (31 allowable addresses in the second byte for each of the 31 allowable in the first byte.) 

## Command and Address Codes 

|X|0|0<br>As|Ag|Ag|Az|Al|Universal Commands|
|---|---|---|---|---|---|---|---|
|X|O|1<br>As|Ag|Ag|Ag|AX|Listen Addresses|
|||except||||||
|xX|011||1|1|1|1|Unlisten Command|
|X|1|0A5|Ag|Az|Ad|Ai|Talk Address|
|||except||||||
|xX|101||1|1|1|1|UntalkCommand|
|X|1|LAs|Aa|Ag|Ad|Ai|Secondary Commands|
|||except||||||
|X|111||1|1|1|1|Ignored|



Code used when attention (ATN) is true (low). X = don’t care. 

A-6 

AN HP-IB OVERVIEW 
