Rev.2.52 

## (Reference Information) Differences between the ETB command and this command 

|Item|ESC GS ETX s n1 n2|ETB|
|---|---|---|
|Afect on ASB(ETB Status)|No|○|
|ASB Occurrence|No|○|
|Afect on ASB valid/invalid setting|No|○|
|Afect of the ESC RS E n command|No|○|
|Status transmission destination in Ethernet<br>(When multi-sessions is valid)|Send only when in the<br>print session (host) that is<br>connected|Send ASB to all sessions<br>(hosts) that are connected|



* This print end counter and the ETB counter sent by the ETB command are separate. They have no affect on each other. 

## (Cautions on Ethernet interfacing) 

When using the Ethernet interface, be sure to use the same communication socket for transmission of this command by the host device and for reception of print end counter data (between #9100 port connection and disconnection). After the command has been transmitted, if the socket is disconnected before the print end counter data is received (#9100 port is disconnected), the print end counter data is returned to the next connected socket (#9100 port). 

The following shows a communication example of this command. 

## Communication Example 1 

Host Transmission Data Printer return data ESC GS ETX 0x00 0x00 0x00 → (Reference Counter) ← ESC GS ETX 0x00 0x00 0x00 0x00 0x00 Print Data + ESC GS ETX 0x01 0x00 0x00 → (Reference Update) ← ESC GS ETX 0x01 0x00 0x00 0x01 0x00 Print Data + ESC GS ETX 0x01 0x00 0x00 → (Reference Update) ← ESC GS ETX 0x01 0x00 0x00 0x02 0x00 Communication Example 2 Host Transmission Data Printer return data ESC GS ETX 0x02 0x02 0x00 (Clear Counter) ESC GS ETX 0x00 0x02 0x00 → (Reference Counter) ← ESC GS ETX 0x00 0x02 0x00 0x00 0x00 Print Data + ESC GS ETX 0x01 0x02 0x11 → (Reference Update) ← ESC GS ETX 0x01 0x02 0x11 0x01 0x00 Print Data + ESC GS ETX 0x01 0x02 0x12 → (Reference Update) ← ESC GS ETX 0x01 0x02 0x12 0x02 0x00 Print Data + ESC GS ETX 0x01 0x02 0x13 → (Reference Update) ← ESC GS ETX 0x01 0x02 0x13 0x03 0x00 Print Data + ESC GS ETX 0x01 0x02 0x14 → (Reference Update) ← ESC GS ETX 0x01 0x02 0x14 0x04 0x00 

## Communication Example 2 

## <Example using n1, n2> 

- For Ethernet: Specify as n1 = host ID, n2 = document number, and check the compatibility of source information and returned information for the host ID and document ID along with getting the returned print end counter. 

- For cases other than Ethernet: 

Specify n1+n2 x 256 as the document ID and check the compatibility with the document ID in the same way. 

- When it is not possible to check compatibility of the source and returned data, fix at n1 = 0, n2 = 0. 

ESC/POS Command Specifications 

190 
