## Line Thermal Printer 

## STAR Line Mode **Command Specifications** 

**Rev 1.12** 

Star Micronics Co., Ltd. Special Products Division 

## **Table of Contents** 

||**Table of Contents**|**Table of Contents**|
|---|---|---|
|1.|INTERFACE CONFIGURATION.........................................................................................................................1-1||
||1.1.|RS-232 Serial Interface..............................................................................................................................1-1|
||1.1.1.|Specifications (Conforming to RS-232)..............................................................................................1-1|
||1.1.2.|1.1.2.<br>Signal array and explanations according to interface connector pin ..................................................1-1|
||1.1.3.|Communication Protocol....................................................................................................................1-2|
||1.2.|Parallel Interfaces (Amphenol 36 pins).......................................................................................................1-4|
||1.2.1.|1.2.1.<br>Specifications (Conforming to IEEE1284)..........................................................................................1-4|
||1.2.2.|Signal array and explanations according to interface connector pin ..................................................1-4|
||1.2.3.|Signal Output Timing..........................................................................................................................1-5|
||1.2.4.|Status Specification............................................................................................................................1-5|
||1.3.|USB Interface.............................................................................................................................................1-6|
||1.4.|Ethernet Interface.......................................................................................................................................1-6|
||1.5.|Wireless LAN Interface...............................................................................................................................1-6|
||1.6.|Powered USB Interface..............................................................................................................................1-6|
|2.|COMMAND FUNCTION LIST.............................................................................................................................2-1||
|3.|COMMAND DETAILS.........................................................................................................................................3-1||
||3.1.|Explanation of Terms..................................................................................................................................3-1|
||3.2.|Exception Processing.................................................................................................................................3-2|
||3.3.|Standard Command Details .......................................................................................................................3-3|
||3.3.1.|Font style and Character Set .............................................................................................................3-3|
||3.3.2.|Character Expansion Settings..........................................................................................................3-12|
||3.3.3.|Print Mode .......................................................................................................................................3-16|
||3.3.4.|Line Spacing ....................................................................................................................................3-20|
||3.3.5.|Page Control Commands.................................................................................................................3-23|
||3.3.6.|Horizontal Direction Printing Position...............................................................................................3-27|
||3.3.7.|Download.........................................................................................................................................3-32|
||3.3.8.|Bit Image Graphics ..........................................................................................................................3-34|
||3.3.9.|Logo.................................................................................................................................................3-38|
||3.3.10.<br>Bar Code..........................................................................................................................................3-42||
||3.3.11.<br>Cutter Control...................................................................................................................................3-44||
||3.3.12.<br>External Device Drive ......................................................................................................................3-45||
||3.3.13.<br>Print Settings....................................................................................................................................3-51||
||3.3.14.<br>Status...............................................................................................................................................3-53||
||3.3.15.<br>Kanji characters ...............................................................................................................................3-59||
||3.3.16.<br>Others..............................................................................................................................................3-63||
||3.4.|Raster Graphics Command Details..........................................................................................................3-68|
||3.5.|Black Mark Related Command Details.....................................................................................................3-87|
||3.6.|USB Related Command Details ...............................................................................................................3-91|
||3.7.|2 Color Printing Command Details ...........................................................................................................3-92|
||3.8.|Presenter Related Command Details.....................................................................................................3-101|
||3.9.|Mark Command Details..........................................................................................................................3-106|
||3.10.|AUTO LOGO Function Command Details.............................................................................................. 3-111|
||3.11.|Two-dimensional Bar Code PDF417 Command Details.........................................................................3-120|
||3.12.|Details of the Print Starting Trigger Control Command...........................................................................3-125|
||3.13.|Two-Dimensional Bar Code QR Code Command Details ......................................................................3-126|
||3.14.|Page Function Command Details...........................................................................................................3-133|
||3.15.|Reduced Printing Function Command Details........................................................................................3-134|
||3.16.|Page Mode Command Details................................................................................................................3-135|
||3.17.|Text Search Command Details...............................................................................................................3-142|
||3.18.|Audio Command Details.........................................................................................................................3-147|
|4.|CHARACTER CODE TABLES............................................................................................................................4-1||
|5.|APPENDIX .........................................................................................................................................................5-1||
||5.1.|Appendix 1: Bar Code Specification Details ...............................................................................................5-1|
||5.1.1.|Code 39 .............................................................................................................................................5-1|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 1 

||5.1.2.|5.1.2.<br>Interleaved 2 of 5 ...............................................................................................................................5-1|
|---|---|---|
||5.1.3.|JAN/EAN/UPC ...................................................................................................................................5-2|
||5.1.4.|Code 128 ...........................................................................................................................................5-3|
||5.1.5.|Code 93 .............................................................................................................................................5-5|
||5.1.6.|NW7 (CODERBAR) ...........................................................................................................................5-5|
||5.2.|Appendix 2: Status Specifications ..............................................................................................................5-6|
||5.2.1.|ENQ Command Status.......................................................................................................................5-6|
||5.2.2.|EOT Command Status .......................................................................................................................5-6|
||5.2.3.|Automatic Status................................................................................................................................5-7|
||5.2.4|Printer status transmission specification when using Ethernet I/F and Wireless LAN I/F.....................5-14|
||5.3.|Appendix 3: Blank Code Page Configuration ...........................................................................................5-16|
||5.4.|Appendix 7 Maximum Number of Input Characters for Each Version of QR Code...................................5-19|
||5.5.|Appendix 8 TSP828L Cut Command Specifications.................................................................................5-23|
||5.6.|Appendix 6 Explanation of Page Mode ....................................................................................................5-24|
||5-6-1.|Overview..........................................................................................................................................5-24|
||5-6-2.|Setting Values Using Each Command in Standard Mode and Page Mode ......................................5-24|
||5-6-3.|Print Data Expansion to the Print Region.........................................................................................5-25|
||5.7.|5-7) Appendix 7 Explanation of Print Startup Control Starting Printing When Set to Page Units ..............5-27|
|6.|SPECIAL APPENDIX COMMAND LIST FOR EACH MODEL IN EACH I/F........................................................6-1||
||6.1.|RS-232C I/F ...............................................................................................................................................6-1|
||6.2.|Parallel I/F • USB I/F (Ver2.0)  • Powered USB I/F.....................................................................................6-6|
||6.3.|USB I/F (Ver1.0)  • Ethernet I/F (Silex Ver1.0)..........................................................................................6-12|
||6.4.|Ethernet I/F / Wireless LAN I/F.................................................................................................................6-18|
||6.5.|Wireless LAN I/F ......................................................................................................................................6-24|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 2 

This specifications document describes the command specifications for the STAR LINE MODE on line thermal printers. Information contained herein applies to models with the following conditions. 

- Line thermal printers 

- Interfaces: 

- Parallel - RS-232C - USB - Ethernet - Wireless LAN - Powered USB 

< Applicable Models:> TSP700 TSP600 TSP800 TUP900 TSP1000 TSP828L TSP700II TSP650 TUP500 TSP800II FVP10 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3 

## **1. INTERF ACE CONFIGURATION** 

## **1.1. RS-232 Serial Interface** 

**1.1.1. Sp ecifications (Conforming to RS-232)** Rating: RS-232C Synch method: Start-Stop synchronization method Handshake: DTR mode Baud rates: 4800, 9600, 19200, 38400 bps (Set by DIP switches) Bit length: 7, 8 bits (Set by DIP switches) Parity: Yes/No (Set by DIP switches) Parity bit: Odd/even (Set by DIP switches) Stop bit: 1 bit (Fixed) Signal polarity: Mark    = logic 1 (-3 to -15 V) Space = logic 0  (+3 to +15 V) 

## **1.1.2. Signal array and explanations according to interface connector pin** 

<Signal Array and Functions> 

|Pin<br>No.<br>~~a~~|Signal Name<br>~~A~~|Signal<br>Direction<br>~~Cn~~|Remarks|
|---|---|---|---|
|1<br>~~a~~|FG<br>~~A~~|-<br>~~Cn~~|Frame ground|
|2<br>~~a ~~<br>~~a~~|TXD<br> ~~A~~|OUT<br>~~Cn~~|Transmissiondata|
|3<br>~~a ~~|RXD<br> ~~A~~|IN|Reception data|
|4<br>~~aA~~|RTS<br>~~aA~~|OUT<br>~~aA~~|Same as DTR|
|5<br>~~a~~|N.C<br>~~aSC~~|-<br>~~SC~~|Not used|
|6<br>~~a~~|DSR<br>~~SC~~|IN<br>~~SC~~|Not used|
|7<br>~~a~~|SG<br>~~SC~~|-<br>~~SC~~|Signal ground|
|8-19<br>~~aA~~|N.C<br>~~aA~~|-<br>~~aA~~|Not used|
|20|DTR|OUT|Data terminal ready signal  (SPACE: printer is ready to receive.)<br>1)  When in DTR mode:<br>When printer is ready to receive data: SPACE<br>2)  When in XON/XOFF mode:<br>Always SPACE except in the following conditions.<br>1. Until communication is possible after a reset.<br>2. When test printing|
|21-24|N.C||Signal ground|
|25<br>~~a~~|/INIT<br>~~a~~<br>~~A~~|IN|Signalground|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

1-1 

## **1.1.3. Communic ation Protocol** 

## 1)  General description of operations in the DTR mode 

This mode abides by the DIP switch settings.  (Ex-factory settings) 

This mode performs communication while handshaking with the DTR signals.  In the operations to receive printer data, this mode controls the DTR signals by confirming the BUSY signal.  A SPACE indicates that the printer is ready to receive data; conversely, a “mark” indicates that the printer cannot receive data. 

**==> picture [383 x 239] intentionally omitted <==**

**----- Start of picture text -----**<br>
<When ON-LINE><br>    RXD     DATA                             DATA                          DATA<br>    DTR<br>Printing<br>Power ON     Buffer full               Buffer empty<br><When out of paper><br>    RXD                                  OFF-LINE                                                          ON-LINE<br>    DTR                                                                                                             ON-LINE Recovery<br>Printing                  Out of paper<br>No paper signal<br>                      Power ON<br>**----- End of picture text -----**<br>


If there is no printer error after turning ON the power, the DTR signal line is set to a SPACE.  When the host computer confirms that the DTR signal line is a SPACE, it sends the data text to the RXD signal line.  The printer sets the DTR signal line to a “Mark” after the empty area of the data buffer reaches a maximum of 256 bytes.  When the host computer confirms that the DTR signal line is a Mark, it stops the transmission of data text to the printer buffer, but at this point as well, the printer is still capable of receiving data, up to the amount of empty space in the data buffer.  If the host computer ignores the DTR signal and transmits data, all data exceeding the amount of space in the data buffer is simply discarded.  The printer sets the DTR signal line to SPACE again when the amount of empty space in the data buffer increased because of the printing and the data in the buffer is a maximum of 256 bytes.  As the empty area in the data buffer increases because of printing, the printer sets the DTR signal line to “SPACE.” 

## 2)  Buffer full/Buffer full cancel in the DTR mode 

|Empty area: 256 bytes|Empty area: 512 bytes||
|---|---|---|
|DTR "Mark"                                                                           DTR "SPACE"|DTR "Mark"                                                                           DTR "SPACE"|DTR "Mark"                                                                           DTR "SPACE"|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 1-2 

## 3)  General description of operations in the XON/XOFF mode 

This mode is set when DIPSW #1 to #3 are turned OFF.  This mode notifies the host of the XON (DC1) data when the printer can receive data and the XOFF (DC3) data when the printer cannot receive data, using the TXD signals. This functions so that XON outputs only 1 byte when the printer shifts from OFFLINE (printer busy) to ONLINE (printer ready) and; XOFF outputs 1 byte when the printer shifts from ONLINE (printer ready) to OFFLINE (printer busy) . 

**==> picture [411 x 134] intentionally omitted <==**

**----- Start of picture text -----**<br>
                                XON                        XOFF                       XON                          XOFF                      XON<br>TXD<br>RXD                                            DATA                                                       DATA                                                  DATA<br>Printing<br>Out of<br>paper<br>signal<br>Power ON                                                                         No paper                     ON-LINE Recovery<br>**----- End of picture text -----**<br>


If there is no error after turning the power ON, XON (control code name: DC1; Hexadecimal name: 11H) is output by the TXD signal line.  After the host computer receives the XON, it sends the data text to the RXD signal line.  XOFF (DC 3; 13H) is output when the empty space in the data buffer is a maximum of 256 bytes.  The host computer stops sending data text when it receives the XOFF, however, the printer is capable of receiving data at that time for the amount of empty space in the data buffer.  Data exceeding the amount of empty space is discarded.  As the empty space in the data buffer increases through printing, XON is output when the data in the buffer is a maximum of 256 bytes.  When the empty area of the data buffer increases because of printing, the printer outputs XON. 

## 4)  Buffer full/Buffer full cancel in the XON/XOFF mode 

|Buffer<br>Empty area: 256 bytes|Empty area: 512 bytes||
|---|---|---|
|XOFF Output|XON Output|XON Output|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 1-3 

## **1.2. Parallel Interfaces (Amphenol 36 pins)** 

## **1.2.1. Specifications (Conforming to IEEE1284)** 

Rating: Conforms to IEEE 1284 Mode: Compatibility Mode/Nibble Mode/Byte Mode Data transfer speed: 1000 to 6000 CPS Synch method: According to externally supplied strobe pulse Handshake: According to ACK and BUSY signals Logic level: Compatible to TTL 

## **1.2.2. Signal array and explanations according to interface connector pin** 

<Signal Array and Functions> 

|Pin No.|Compatibility Mode Signal Name|Nibble Mode Signal Name|Byte Mode Signal Name|
|---|---|---|---|
|1<br>2 to 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19 to 30<br>31<br>32<br>33<br>34<br>35<br>36|nStrobe<br>Data0 to 7<br>nAck<br>Busy<br>PError<br>Select<br>N/C<br>N/C<br>Signal GND<br>Frame GND<br>+5V<br>Twisted Pair Return<br>nInit<br>nFault<br>External GND<br>N/C<br>N/C<br>nSelectIn|HostClk<br>Data0 to 7<br>PtrClk<br>PtrBusy/Data3,7<br>AckDataReq/Data2,6<br>Xflag/Data1,5<br>HostBusy<br>-<br>Signal GND<br>Frame GND<br>+5V<br>Twisted Pair Return<br>nInit<br>nDataAvail/Data0,4<br>-<br>-<br>-<br>1284Active|HostClk<br>Data0 to 7<br>PtrClk<br>PtrBusy<br>AckDataReq<br>Xflag<br>HostBusy<br>-<br>Signal GND<br>Frame GND<br>+5V<br>Twisted Pair Return<br>nInit<br>nDataAvail<br>-<br>-<br>-<br>1284Active|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 1-4 

## **1.2.3. Signal Output Timing** 

## 1) Compatibility mode 

**==> picture [307 x 95] intentionally omitted <==**

**----- Start of picture text -----**<br>
T  T  T  T= Min. 0.5 μs<br>nStrobe<br>Data 0 to 7<br>——— . .<br>nAck<br>Busy<br>**----- End of picture text -----**<br>


- 2)  Nibble Mode/Byte Mode Conforms to IEEE 1284 standard 

## **1.2.4. Status Specification** See Appendix 2 for details. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

1-5 

## **1.3. USB Interface** 

Specifications: Conforms to USB 2.0 Full Speed. Supports printer class and vendor class (Refer to each printer specifications manual for selections.) Connector: Type B 

## **1.4. Eth ernet Interface** 

Specifications: Conforms to IEEE 802.3. Cable: 10BASE-T/10BASE-TX Connector: RJ45 

## **1.5. W ireless LAN Interface** 

Specifications: Conforms to IEEE 802.11b. 

## **1.6. Powered USB Interface** 

Specifications See the IFBD-BPU03 Specifications Manual Cable See the IFBD-BPU03 Specifications Manual Connector See the IFBD-BPU03 Specifications Manual 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 1-6 

## **2. COMMAND FUNCTION LIST** 

## **• Standard Commands** 

|**Class**|**Commands**|**Name**|
|---|---|---|
|Font style<br>And character set<br>~~Pp~~|ESCRSF<br>~~a~~|Selectfont|
||ESC GS t<br>~~a~~<br>~~a~~|Specify code page|
||ESC GS=<br>~~a~~<br>~~a~~|Write blank code page data|
||ESCR<br>~~a~~<br>~~a~~|Specifyinternationalcharacterset|
||ESC /<br>~~a ~~<br>~~Pp~~|Specify/cancel slash zero<br> ~~pT~~<br>|
||ESC SP<br> <br>~~Pp~~|Set ANK right space<br> ~~pT~~<br>|
||ESCM<br> <br>~~PpI~~|SpecifyANK 12dot pitch<br> ~~pT~~<br>~~I~~|
||ESC P<br>~~Re~~|Specify ANK 15 dot pitch<br>~~Re~~|
||ESC :<br>~~Re~~|Specify ANK 16 dot pitch<br>~~Re~~|
||ESC g<br>~~a~~|SpecifyANK 14dot pitch|
|Character<br>expansion settings<br>~~Pp~~|ESC i<br>~~a~~|Set/cancel the double wide/high printing|
||ESC W<br>~~a~~|Set/cancel the double wide printing|
||ESCh<br>~~a~~|Set/cancelthe doublehighprinting|
||SO<br>~~a~~<br>~~a~~|Set double wide printing|
||DC4<br>~~a~~<br>~~a~~|Cancel double wide printing<br>|
||ESC SO<br>~~a ~~<br>~~Pp~~|Set printingmagnified double character height<br> ~~pe~~<br>|
||ESC DC4<br> <br>~~Pp~~|Cancel printing magnified character height<br> ~~pe~~<br>|
|Print modes<br>~~Pp~~<br>~~Pp~~|ESC E<br> <br>~~Ppa~~|Select emphasized printing<br> ~~pe~~<br>~~a~~|
||ESCF<br>~~I~~|Cancelemphasized printing<br>~~I~~|
||ESC-<br>~~Re~~|Select/cancels underling mode<br>~~Re~~|
||ESC _<br>~~Re~~|Select/cancels upperline mode<br>~~Re~~|
||ESC4|Selectwhite/black inverted printing|
||ESC 5<br>~~a ~~<br>~~Pp~~|Cancel white/black inverted printing<br> ~~pe~~<br>|
||SI<br> <br>~~Pp~~|Select upside-down printing<br> ~~pe~~<br>|
||DC2<br> <br>~~Ppa~~|Cancelupside-downprinting<br> ~~pe~~<br>~~a~~|
|Line spacing<br>~~Pp~~|LF|Line feed|
||CR<br>~~a~~|Carriage return  (same as line feed)<br>~~a~~|
||ESC a<br>~~a~~|Feed paper n lines<br>~~a~~|
||ESC z<br>~~a~~|Select line feed amount<br>~~a~~|
||ESC 0<br>~~a~~|Specify line spacing to 3 mm<br>~~a~~|
||ESC J<br>~~I~~<br>~~Pp~~|n/4 mm linefeed<br>~~I~~<br>~~pT~~|
||ESC I<br>~~Pp~~|n/8 mm line feed<br>~~pT~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 2-1 

|**Class**|**Commands**|**Name**|
|---|---|---|
|Page control<br>commands<br>~~Pp~~|FF<br>~~a~~|Form feed|
||ESC C<br>~~a~~|Set pagelengthton lines|
||ESC C 0<br>~~a~~<br>~~a~~|Set page length in 24 mm units|
||VT<br>~~a~~<br>~~a~~<br>~~Pp~~|Feed paper to vertical tab position<br>~~pe~~<br>|
||ESCB<br>~~a ~~<br>~~Pp~~|Setverticaltab position<br> ~~pe~~<br>|
||ESC N<br> <br>~~Ppa~~|Set bottom margin to n lines<br> ~~pe~~<br>~~a~~|
||ESC O<br>~~I~~|Cancel bottom margin<br>~~I~~|
|Horizontal<br>direction<br>position<br>~~ee ee~~|ESCl<br>~~a~~|Setleftmargin<br>~~a~~|
||ESC Q<br>~~Re~~|Set right margin<br>~~Re~~|
||HT<br>~~Re~~|Move print position to horizontal tab position<br>~~Re~~|
||ESCD<br>~~a~~|Set/cancel horizontaltab position|
||ESC GS A<br>~~a~~|Move absolute position|
||ESC GS R<br>~~a~~|Move relative position|
||ESC GS a<br>~~a~~<br>~~ee eee~~|Specify positionalignment<br>~~eee~~|
|Download<br>~~ee ee~~|ESC &<br>~~a~~<br>~~a~~<br>~~ee eee~~|Register/delete 12 x 24 dot font download characters<br>~~eee~~|
||ESC %<br>~~a~~<br>~~ee eee~~|Set/cancel download characters<br>~~eee~~|
|Bit image<br>graphics<br>~~ee ee~~|ESCK<br>~~ee eee~~<br>~~a~~|Standard density bitimage<br>~~eee~~|
||ESC L<br>~~a~~|High density bit image|
||ESC k<br>~~a~~|Fine bit image|
||ESCX<br>~~a~~|Fine bitimage|
|Logos<br>~~Ge~~|ESC FS q<br>~~a~~|Register logo data|
||ESC FS p|Print logo data|
||ESCRSL<br>~~a~~<br>~~Ge~~|Printregisteredlogoinbatch/Batchcontrolof registeredlogos<br>~~Ge~~|
|Bar code<br>~~Ge~~<br>~~|~~<br>~~|~~|ESC b<br>~~Ge~~<br>~~|~~|Print bar code<br>~~Ge~~<br>~~pe~~|
|Cutter control<br>~~Ge~~<br>~~|~~<br>~~|~~|ESC d<br>~~Ge ~~<br>~~|~~|Paper cutter instruction<br> ~~Ge~~<br>~~pe~~|
|External device<br>Drive<br>~~|~~<br>~~|~~<br>~~————————~~|ESCBEL<br>~~|~~|Set pulsewidth forexternaldevice drive<br>~~pe~~|
||BEL<br>~~a~~|External device 1 drive instruction<br>~~a~~|
||FS<br>~~a~~|External device 1 drive instruction<br>~~a~~|
||SUB<br>~~a~~|Externaldevice2driveinstruction<br>~~a~~|
||EM<br>~~a~~|External device 2 drive instruction<br>~~a~~|
||ESC GS BEL<br>~~a~~|Ring buzzer<br>~~a~~|
||ESC GSEM DC1<br>~~I~~|Externalbuzzerdrive pulse conditionsettings<br>~~I~~|
||ESC GS EM DC2<br>~~a~~<br>~~————————~~|External buzzer drive execution<br>~~a~~<br>~~————————~~|
|Print settings<br>~~————————~~|ESC RS d<br>~~————————~~|Set print density<br>~~————————~~|
||ESCRSr<br>~~————————~~<br>~~a~~|Set printing speed<br>~~————————~~|
|Status<br>~~————————~~|ESC RS a<br>~~————————~~<br>~~a~~|Set status transmission conditions<br>~~————————~~|
||ESC ACK SOH<br>~~a~~|Real-time printer status  (ASB Status)|
||ENQ<br>~~a~~|Real-time printerstatus (1)|
||EOT<br>~~a~~|Real-time printer status  (2)|
||ESC ACK CAN<br>~~a~~|Real-time printer reset|
||ETB<br>~~a~~|UpdateETBstatus|
||ESC RS E<br>~~a ~~<br>~~ee een~~|Clear ETB counter, ETB status<br> ~~pT~~<br>~~een~~|
||ESC GS ETX<br> <br>~~ee een~~|Send print end counter and initialize<br> ~~pT~~<br>~~een~~|
|||Print data cancel function<br> ~~pT~~<br>~~een~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 2-2 

|**Class**|**Commands**|**Name**|
|---|---|---|
|Chinese<br>characters|ESCp|Set to JIS Kanji character mode|
||ESCq|Cancel JIS Kanji character mode|
||ESC$|Set/cancel JIS Kanji character mode|
||ESC s|Set two byte Kanji characters left/right spaces|
||ESC t|Set 1 byte Kanji characters left/right spaces|
||ESC r|Register Chinese download characters|
|Others|CAN|Cancel print data and initialize commands|
||ESC @|Commandinitialization|
||ESC GS #|Set memory switch|
||ESC ?|Reset printer|
||ESC GSr|Get CRC code|
|Macro|ESC GS+|Register macro|



- (*)  Kanji character commands 

   - Kanji character control commands are ignored on printers not installed with Kanji character fonts (those intended for overseas). 

   - All Kanji character control commands are ignored if the specification for the location of use is specified as SBCS (single byte countries) by the memory switch. 

• Raster related commands 

|**Class**<br>~~re~~|**Commands**<br>~~re~~|**Name**<br>~~re~~|
|---|---|---|
|Raster commands<br>~~re~~|ESC*r R<br>~~re~~<br>~~——~~|Initialize raster mode<br>~~re~~<br>~~——~~|
||ESC* r A<br>~~——~~<br>~~__~~|Enter raster mode<br>~~——~~|
||ESC*r B<br>~~——~~<br>~~es~~|Quit raster mode<br>~~——~~<br>~~es~~|
||ESC*r C<br>~~es~~|Clear raster data<br>~~es~~|
||ESC* r D<br>~~_—_~~|Drive drawer<br>~~OT~~|
||ESC*r E<br>~~a~~|Set EOT mode|
||ESC*r F<br>~~a~~|Set FF mode|
||ESC* r P<br>~~a~~|Set pagelength|
||ESC*r Q<br>~~a~~|Set print quality|
||ESC*r m l<br>~~a~~|Set left margin|
||ESC* r m r<br>~~a~~|Setrightmargin|
||ESC*r T<br>~~a~~|Set top margin|
||ESC*r K<br>~~a~~ ~~——~~|Set print color<br>~~——~~|
||bn1 n2d1...dk<br> ~~——~~<br>~~__~~|Transfer rasterdata (autolinefeed)<br>~~——~~|
||k n1 n2 d1...dk<br> ~~——~~<br>~~a~~|Transfer raster data<br>~~——~~|
||ESC * r Y<br>~~a~~|Position movementin verticaldirection(Line breakat specified dot)|
||ESCFF NUL<br>~~_—_~~|Executeform feedmode|
||ESC FF EOT<br>~~a~~|Execute EOT mode|
||ESC*r N<br>~~a~~|Discard data for specified byte count|
||ESC* r V<br>~~a~~|Execute external buzzer drive|
||ESC * r e s NUL<br>~~a~~|Set print data cancel function|
||ESC*r S<br>~~a~~|Playback NV audio|
||ESC* rs 0<br>~~a~~|SetNVaudio playback number|
||ESC*r s 1<br>~~a~~|Set NV audio playback count|
||ESC*r s 2<br>~~a TT~~|Set NV audio playback delay time<br>~~TT~~|
||ESC* rs 3<br>~~TT~~<br>~~__~~|SetNVaudio playback interval<br>~~TT~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 2-3 

|•Black mark related commands|
|---|
|**Commands**<br>**Name**<br>**Class**<br>Black mark<br>ESC d<br>Paper cut instruction<br>Related<br>FF<br>Form feed<br>Commands<br>ESC C<br>Set page length to n lines<br>ESC C 0<br>Set page length in 24 mm units<br>VT<br>Feed papertoverticaltab position<br>ESC B<br>Set vertical tab position<br>ESC N<br>Set n line bottom margin<br>ESC O<br>Cancelbottom margin<br>~~_~~|
|•2-Color Printing Related Commands|
|**Commands**<br>**Name**<br>**Class**<br>2-Color Printing<br>ESCRS c<br>Specify printing color in 2-colorprintingmode<br>Related<br>commands<br>ESC RS C<br>Select/cancel 2-color printing mode<br>ESC 4<br>Specify white/black inversion and printing color red<br>ESC 5<br>Cancel white/black inversionand specify printing colorblack<br>ESC FS q<br>Register logo<br>ESCFS p<br>Printlogo<br>~~==~~|
|•2 color printing related commands|
|**Commands**<br>**Name**<br>**Class**<br>2 color printing<br>ESC RS c<br>Specify printing color in 2 color printing mode<br>Related<br>ESCRS C<br>Select/cancel 2colorprintingmode<br>Commands<br>ESC 4<br>Specify white/black inversion and printing color red<br>ESC 5<br>Cancel white/black inversion and specify printing color black<br>ESCFS q<br>Register logo<br>ESC FS p<br>Print logo<br>~~__—_—~~|
|•Presenter related commands|
|**Commands**<br>**Name**<br>**Class**<br>Presenter<br>ESC SYN 0<br>Execute presenter paper recovery<br>related<br>ESC SYN 1<br>Set presenter automatic recovery function and recovery time<br>commands<br>ESC SYN3<br>Acquire presenterpapercounter<br>ESC SYN 4<br>Initialize presenter paper counter<br>ESC GS SUB DC1<br>Specify snout operation mode<br>ESC GS SUB DC2<br>Specify snoutLEDON/OFFtime<br>ESC GS SUB DC3<br>Snout LED output<br>~~——~~|
|―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――|
|STAR Line Mode Command Specifications<br>2-4|

## • Mark commands 

|•Mark commands|Mark commands||
|---|---|---|
|**Class**|**Commands**|**Name**|
|Mark<br>commands|ESC GS*0|Print mark|
||ESC GS* 1|Specifymark height andlinefeed amount|
||ESC GS*2|Specify mark color and horizontal width in each mark number|
||ESC GS*W|Register mark format in non-volatile memory|
||ESC GS*C|Initializemark formatin non-volatilememory|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

2-5 

- Auto Logo commands 

|**Class**|**Commands**|**Name**|
|---|---|---|
|Auto Logo<br>commands|ESC GS / W|Register Auto Logo setting in non-volatile memory|
||ESC GS / C|InitializeAutoLogo settingin non-volatilememory|
||ESC GS / 1|ON/OFF setting of Auto Logo function|
||ESC GS / 2|Command character setting|
||ESC GS / 3|User macro1setting|
||ESC GS / 4|User macro 2 setting|
||ESC GS / 5|Command character rewriting method setting|
||ESC GS / 6|Setting ofpartialcut just priortoAutoLogo printing|



## • PDF417 commands 

|**Class**|**Commands**|**Name**|
|---|---|---|
|PDF417<br>commands|ESC GS x S0|Set PDF417 bar code size|
||ESC GS x S1|Set PDF417 ECC (security level)|
||ESC GSxS2|SetPDF417 moduleXdirectionsize|
||ESC GS x S3|Set PDF417 module aspect ratio|
||ESC GS x D|Set PDF417 bar code data|
||ESC GSx P|PrintPDF417barcode|
||ESC GS x I|Get PDF 417 bar code expansion information|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

2-6 

- Print Starting Trigger Control commands 

|**Class**|**Commands**|**Name**|
|---|---|---|
|Print starting|ESC GS g0|Print starting trigger|
|trigger|ESC GS g1|Print starting timersetting|



- QR Code commands 

|**Class**|**Commands**|**Name**|
|---|---|---|
|QR code|ESC GS y S0|Set QRcodemodel|
||ESC GS y S1|Set QR code mistake correction level|
||ESC GS y S2|Set QR code cell size|
||ESC GS yD1|Set QRcode data|
||ESC GS y D2|Set QR code data (Manual)|
||ESC GS y P|Print QR code|
||ESC GS yI|Get QRcode expansion information|



- •Page function commands 

|**Class**|**Commands**|**Name**|
|---|---|---|
|Page function|ESC GS h 0|180 degree turnover|
||ESC GSh 1|Water mark|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

2-7 

- Reduced Printing Function Commands 

||**Class**|**Commands**|**Name**|
|---|---|---|---|
||Reduced Printing<br>Function|ESC GS c h v|Reduced Printing|
||•Page Mode Commands|||
|**Class**<br>**Commands**<br>**Name**<br>Page Mode<br>ESC GS P 0<br>Selects page mode<br>ESC GS P 1<br>Cancels page mode<br>ESC GSP 2<br>Select printing direction<br>ESC GS P 3<br>Set print region<br>ESC GS P 4<br>Specify character vertical direction absolute position<br>ESC GSP5<br>Specify character verticaldirection relative position<br>ESC GS P 6<br>Prints<br>ESC GS P 7<br>Cancel printing and page mode<br>ESC GSP8<br>Cancelprint data<br>~~—~~||||
||•Text Search Commands|||
||**Class**|**Commands**|**Name**|
||Text Search|ESC GS)B(fn = 48)|Enable and disables text search|
|||ESC GS)B(fn = 49)|Set the number of times to run the text search macro|
|||ESC GS)B(fn = 50)|Set toprint the stringthat matches in the text search|
|||ESC GS)B(fn = 64)|Define the text search string|
|||ESC GS)B(fn = 65)|Define the text search macro|
|||ESC GS ) B  (fn = 80)|Register text search settings and definitions in the non-volatile|
||||memory|
|||ESC GS)B(fn = 81)|Initialize text search settings and definitions|
|||ESC GS)B(fn = 96)|Print the text search settings and definitions|



|ESC GS)B(fn = 65)<br>Define the text search macro<br>ESC GS ) B  (fn = 80)<br>Register text search settings and definitions in the non-volatile<br>memory<br>ESC GS)B(fn = 81)<br>Initialize text search settings and definitions<br>ESC GS)B(fn = 96)<br>Print the text search settings and definitions||
|---|---|
|ESC GS)B(fn = 97)<br>Run the text search macro||
|•Audio Commands||
|**Class**<br>**Commands**<br>**Name**<br>Audio<br>ESC GS s O<br>Playback NV audio<br>ESC GS s P<br>Stop NV audio<br>ESC GS sR<br>Playback received audio<br>ESC GS s I<br>Register automatic audio setting information<br>ESC GS s U<br>Register user area NV audio data<br>ESC GS sT<br>Batchplaybackof NVaudio<br>~~——~~||
|―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――||
|STAR Line Mode Command Specifications<br>2-8||

## **3. COMMAND DETAILS** 

## **3.1. Exp lanation of Terms** 

## • Reception buffer 

The buffer for storing data (reception data) received from the host, as it is called the reception buffer. Reception data is temporarily stored in the reception buffer, then processed sequentially. 

## • Line buffer 

The buffer for storing image data for printing is called the line buffer. 

## • Line buffer full 

The state in which the buffer has no more space available is called line buffer full.  When the buffer is full in standard mode, data in the line buffer is printed and a line feed is performed when new print data is processed.  This is the same as a Line Feed.  When the line buffer is full in the page mode, the printer move the print position to the head of the next line then starts with the new print data. 

## • Top of line 

The top of line is a state that satisfies the following conditions. 

   - There is currently no print data in the line buffer. 

   - The position is not specified with the horizontal direction position command. 

- Printable region 

This is the maximum printable area with the printer’s specifications. 

## • Print region 

This is the printing area specified by a command. (Print region ≤ printable region) 

- ANK character base line 

**==> picture [311 x 62] intentionally omitted <==**

**----- Start of picture text -----**<br>
20 dots<br>24 dots<br>      Base Line<br>Ay<br>f f <_——<br>**----- End of picture text -----**<br>


- ASB Function 

Sends the automatic status to the host each time the printer’s status changes. 

## • NSB Function 

When the printer uses a parallel I/F or USB I/F, sends the automatic status each time the reverse transfer mode is entered. When the printer uses Ethernet I/F or wireless I/F, sends the automatic status when the printer is connected to the print port (TCP#9100). The ASB and NSB status formats are the same. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-1 

## **3.2. Excep tion Processing** 

## 1)  Undefined codes 

- Codes from <00>H to <1F>H are targeted.  When codes not defined as commands in this region are received, they are discarded. 

- (Ex.)  If processing the data string of <30>H<31>H<03>H<32>H<0A>H<33>H, the printer will discard <03>H as an undefined code. 

## 2)  Undefined commands 

When data continuing the codes of ESC, FS, GS, DLE are codes not defined as commands, ESC, FS,GS and subsequent codes are discarded. 

- (Ex.)  If processing the data string of <30>H<1B>H<22>H<31>H<32>H, the printer will read and discard <1B>H<22>H as an undefined command. 

## 3)  Settings outside of the defined area 

Processing values outside of the defined area in commands accompanying arguments, those commands are ignored and the preset values are unchanged.  The processing of commands is terminated at the point values outside of the defined region are processed in arguments having a plurality of commands.  Data after that is processed as normal data. 

- (Ex.)  If processing the data string of <1B>H<52>H<15>H, the printer will discard the data string of <1B>H<52>H<15>H because although <1B>H<52>H is defined as a commands (ESC R), the argument <15>H is outside of the definition.  Therefore, the international character set that is already set experiences no change. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-2 

## **3.3. Standard Command Details** 

## **3.3.1. Font style and Character Set** 

## **ESC RS F n** 

|**ESC RS F n**|**ESC RS F n**|**ESC RS F n**|**ESC RS F n**|||
|---|---|---|---|---|---|
|[Name]|Select font|||||
|[Code]|ASCII||ESC RS|F|n|
||Hex.||1B<br>1E|46|n|
||Decimal||27<br>30|70|n|
|[Defined Region]||0≤<br>n≤<br>1, n = 16||, n = 16||
|[Initial Value]||n = 0||||
|[Function]||Selects a font||Selects a font||
||n||Font|||
||0||Font-A(12 x 24|12 x 24dots)||
||1||Font-B (9 x 24 dots)||B (9 x 24 dots)|
||16||OCR-B(16x 24|x 24dots)||



The following functions are disabled when OCR-B font is selected. 

• Code page 

- Blank code page 

• International characters 

- Slash zero 

When using OCR-B font to read characters via a scanning operation, adornment, expansion and external characters are canceled. 

OCR-B font should be checked by actually trying it first before use. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-3 

## **ESC GS t n** 

[Name] Select code page [Code] ASCII ESC GS t n Hex. 1B 1D 74 n Decimal 27 29 116 n 

[Defined Region] 0≤n≤21 32≤n≤34 64≤n≤79 [Initial Value] Memory switch setting When installed with Japanese language characters and DBCS setting: Fixed at n=2 

[Function] Specifies code page 

When installed with Japanese and Chinese language characters and DBCS setting, this command is ignored. 

|n<br>CodePage<br>~~a ee~~||n|CodePage|
|---|---|---|---|
|0<br>Normal*<br>1<br>CodePage437(USA, Std. Europe)<br>2<br>Katakana<br>3<br>CodePage437(USA, Std. Europe)<br>4<br>Codepage 858 (Multilingual)<br>5<br>Codepage 852(Latin-2)<br>6<br>Codepage 860 (Portuguese)<br>7<br>Codepage 861(Icelandic)<br>8<br>Codepage 863 (Canadian French)<br>9<br>Codepage 865 (Nordic)<br>10<br>Codepage 866 (Cyrillic Russian)<br>11<br>Codepage 855 (CyrillicBulgarian)<br>12<br>Codepage 857(Turkey)<br>13<br>Codepage 862(Israel(Hebrew) )<br>14<br>Codepage 864(Arabic)<br>15<br>Codepage737(Greek)<br>16<br>Codepage 851 (Greek)<br>17<br>Codepage 869 (Greek)<br>18<br>Codepage 928 (Greek)<br>19<br>Codepage772(Lithuanian)<br>20<br>Codepage774(Lithuanian)<br>21<br>Codepage 874(Thai)<br>~~a~~<br>~~ee~~<br>~~ee~~<br>~~a~~<br>~~ee~~<br>~~eeee~~<br>~~ee~~<br>~~ee~~<br>~~a~~<br>~~eeee~~<br>~~ee~~<br>~~ee~~<br>~~ee~~<br>~~a~~<br>~~ee~~<br>~~ee~~<br>~~ee~~<br>~~ee~~<br>~~a~~<br>~~ee~~<br>~~ee~~<br>~~ee~~||32<br>33<br>34<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>74<br>75<br>76<br>77<br>78<br>79<br>255|Codepage 1252 (Windows Latin-1)<br>Codepage1250 (WindowsLatin-2)<br>Codepage1251(Windows Cyrillic)<br>Codepage 3840 (IBM-Russian)<br>Codepage 3841 (Gost)<br>Codepage 3843 (Polish)<br>Codepage 3844(CS2)<br>Codepage 3845 (Hungarian)<br>Codepage 3846 (Turkish)<br>Codepage 3847(Brazil-ABNT)<br>Codepage 3848 (Brazil-ABICOMP)<br>Codepage1001(Arabic)<br>Codepage2001(Lithuanian-KBL)<br>Codepage 3001(Estonian-1)<br>Codepage 3002(Estonian-2)<br>Codepage 3011(Latvian-1)<br>Codepage 3012 (Latvian-2)<br>Codepage 3021(Bulgarian)<br>Codepage 3041(Maltese)<br>UserSettingBlankCodePage|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-4 

**ESC GS = n1 n2 da1 da2...dak db1 db2...dbk** 

[Name] Write blank code page data [Code] ASCII ESC GS = n1 n2 da1 da2 ... dak db1 db2 … dbk Hex. 1B 1D 3D n1 n2 da1 da2 ... dak db1 db2 … dbk Decimal 27 29 61 n1 n2 da1 da2 ... dak db1 db2 … dbk 

Spec. Aification [Defined Area] n1= 0 n2 = 48 1≤(n1 + n2 x 256) 0≤da≤255      (Font-A data) db = 0            (STAR mode is not installed with Font-B.) k = (n1 + n2 x 256) ÷ 2 [Initial Value] - - - [Function] A blank code page indicates a character code table where character codes from 80h to FFh are all blank. 

A blank code page can be selected using the ESC GS t n command n = 255. The printer is reset when writing with this command is completed. 

Font-A Data Format  Vertical 24 dots x Horizontal 12 dots] 

|~~po~~||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Da1<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da2|●|●|●|●|○|○|○|○|
|Da3<br>~~po~~<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da4|●|●|●|●|○|○|○|○|
|Da5<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da6|●|●|●|●|○|○|○|○|
|Da7<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da8<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da9<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da10|●|●|●|●|○|○|○|○|
|Da11<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da12|●|●|●|●|○|○|○|○|
|Da13<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da14<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da15<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da16|●|●|●|●|○|○|○|○|
|Da17<br>~~po~~<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da18|●|●|●|●|○|○|○|○|
|Da19<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da20|●|●|●|●|○|○|○|○|
|Da21<br>~~**p**o~~|●|●|●|●|●|●|●|●<br>~~o~~|Da22<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da23<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da24<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da25<br>~~po~~<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da26<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da27<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da28|●|●|●|●|○|○|○|○|
|Da29<br>~~po~~<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da30|●|●|●|●|○|○|○|○|
|Da31<br>~~po~~<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da32|●|●|●|●|○|○|○|○|
|Da33<br>~~po~~<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da34|●|●|●|●|○|○|○|○|
|Da35<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da36|●|●|●|●|○|○|○|○|
|Da37<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da38<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da39<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da40|●|●|●|●|○|○|○|○|
|Da41<br>~~po~~<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da42|●|●|●|●|○|○|○|○|
|Da43<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da44|●|●|●|●|○|○|○|○|
|Da45<br>~~**p**o~~<br>~~Po TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~o~~<br>~~TT~~|Da46<br>~~o~~<br>~~TT~~|●<br>~~o~~<br>~~TT~~|●<br>~~o~~<br>~~TT~~|●<br>~~o~~<br>~~TT~~|●<br>~~o~~<br>~~TT~~|○<br>~~o~~<br>~~TT~~|○<br>~~o~~<br>~~TT~~|○<br>~~o~~<br>~~TT~~|○<br>~~o~~<br>~~TT~~|
|Da47<br>~~Po TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|Da48<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|●<br>~~TT~~|○<br>~~TT~~|○<br>~~TT~~|○<br>~~TT~~|○<br>~~TT~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-5 

Spec. B. 

[Defined Area] n1 = 0 n2 = 48 1 ≤ (n1 + n2 x 256) 0 ≤ da ≤ 255 (Font-A data) 0 ≤ db ≤ 255 (Font-B data) k = (n1 + n2 x 256) ÷ 2 --- 

[Initial Value] --[Function] A blank code page indicates a character code table where character codes from 80h to FFh are all blank. 

A blank code page can be selected using the ESC GS t n command n = 255. The following is the data written to the blank code page. Font-A: 1 character = 48 bytes   6144 bytes = 48 bytes x 128 characters Font-B: 1 character = 48 bytes   6144 bytes = 48 bytes x 128 characters Send Font-A and Font-B data continuously. 

The printer is reset when writing with this command is completed. 

## [Font-A Data Format  Vertical 24 dots x Horizontal 12 dots] 

|~~po~~||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Da1<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da2|●|●|●|●|○|○|○|○|
|Da3<br>~~po~~<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da4|●|●|●|●|○|○|○|○|
|Da5<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da6|●|●|●|●|○|○|○|○|
|Da7<br>~~**p**o~~|●|●|●|●|●|●|●|●<br>~~o~~|Da8<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da9<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da10<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da11<br>~~po~~<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da12<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da13<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da14|●|●|●|●|○|○|○|○|
|Da15<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da16|●|●|●|●|○|○|○|○|
|Da17<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da18<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da19<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da20|●|●|●|●|○|○|○|○|
|Da21<br>~~po~~<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da22|●|●|●|●|○|○|○|○|
|Da23<br>~~po~~<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da24|●|●|●|●|○|○|○|○|
|Da25<br>~~po~~<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da26|●|●|●|●|○|○|○|○|
|Da27<br>~~po~~<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da28|●|●|●|●|○|○|○|○|
|Da29<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da30|●|●|●|●|○|○|○|○|
|Da31<br>~~**p**o~~|●|●|●|●|●|●|●|●<br>~~o~~|Da32<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da33<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da34<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da35<br>~~po~~<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da36<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da37<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da38|●|●|●|●|○|○|○|○|
|Da39<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da40|●|●|●|●|○|○|○|○|
|Da41<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da42<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da43<br>~~po~~<br>~~po~~|●<br>|●<br>|●<br>|●<br>|●<br>|●<br>|●<br>|●<br>|Da44<br>|●<br>|●<br>|●<br>|●<br>|○<br>|○<br>|○<br>|○<br>|
|Da45<br>~~po~~<br>~~po~~|●<br>|●<br>|●<br>|●<br>|●<br>|●<br>|●<br>|●<br>|Da46<br>|●<br>|●<br>|●<br>|●<br>|○<br>|○<br>|○<br>|○<br>|
|Da47<br>~~poPo~~|●<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|Da48<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|●<br>~~Po~~|○<br>~~Po~~|○<br>~~Po~~|○<br>~~Po~~|○<br>~~Po~~|



• = Data region/ ○ =Zero data 

## [Font-B Data Format  Vertical 24 dots x Horizontal 9 dots] 

|~~**p**o~~||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Da1<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da2|●|○|○|○|○|○|○|○|
|Da3<br>~~**p**o~~|●|●|●|●|●|●|●|●<br>~~o~~|Da4<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da5<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da6<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da7<br>~~po~~<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da8<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da9<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da10|●|○|○|○|○|○|○|○|
|Da11<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da12|●|○|○|○|○|○|○|○|
|Da13<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da14<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da15<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da16|●|○|○|○|○|○|○|○|
|Da17<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da18|●|○|○|○|○|○|○|○|
|Da19<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da20<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da21<br>~~po~~<br>~~po~~|●|●|●|●|●|●|●|●|Da22|●|○|○|○|○|○|○|○|
|Da23<br>~~po~~<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da24|●|○|○|○|○|○|○|○|
|Da25<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da26|●|○|○|○|○|○|○|○|
|Da27<br>~~**p**o~~|●|●|●|●|●|●|●|●<br>~~o~~|Da28<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da29<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da30<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da31<br>~~po~~<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|●<br>~~po~~|Da32<br>~~po~~|●<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|○<br>~~po~~|
|Da33<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da34|●|○|○|○|○|○|○|○|
|Da35<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da36|●|○|○|○|○|○|○|○|
|Da37<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da38<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da39<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da40|●|○|○|○|○|○|○|○|
|Da41<br>~~po~~<br>~~**p**o~~|●|●|●|●|●|●|●|●|Da42|●|○|○|○|○|○|○|○|
|Da43<br>~~**p**o~~<br>~~po~~|●|●|●|●|●|●|●|●<br>~~o~~|Da44<br>~~o~~|●<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|○<br>~~o~~|
|Da45<br>~~po~~<br>~~GO~~|●<br>~~GO~~|●<br>~~GO~~|●<br>~~GO~~|●<br>~~GO~~|●<br>~~GO~~|●<br>~~SG~~|●<br>~~SG~~|●<br>~~NGG~~|Da46<br>~~NGG~~|●<br>~~NGG~~|○<br>~~GO~~|○<br>~~GO~~|○<br>~~GO~~|○<br>~~GO~~|○<br>~~NG~~|○<br>~~NG~~|○<br>~~GO~~|
|Da47<br>~~po~~<br>~~GO~~|●<br>~~GO~~|●<br>~~GO~~|●<br>~~GO~~|●<br>~~GO~~|●<br>~~GO~~|●<br>~~SG~~|●<br>~~SG~~|●<br>~~NGG~~|Da48<br>~~NGG~~|●<br>~~NGG~~|○<br>~~GO~~|○<br>~~GO~~|○<br>~~GO~~|○<br>~~GO~~|○<br>~~NG~~|○<br>~~NG~~|○<br>~~GO~~|



• = Data region/ ○ =Zero data 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-6 

## **ESC R n** 

[Name] Specify international character set [Code] ASCII ESC R n Hex. 1B 52 n Decimal 27 82 n [Defined Area] 0≤n≤14 n = 64 48≤n≤57 (”0”≤n≤”9”) 65≤n≤69 (”A”≤n≤”E”) [Initial Value] Memory switch setting When installed with Japanese language characters and DBCS setting: Fixed at n=8 [Function] Specifies international characters 

|n|International Characters|
|---|---|
|0,48|USA|
|1,49|France|
|2, 50|Germany|
|3, 51|UK|
|4, 52|Denmark|
|5, 53|Sweden|
|6, 54|Italy|
|7, 55|Spain|
|8, 56|Japan|
|9, 57|Norway|
|10, 65|Denmark II|
|11, 66|Spain II|
|12, 67|Latin America|
|13, 68|Korea|
|14, 69|Ireland|
|64|Legal|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-7 

## **ESC / n** 

[Name] Specify/cancel slash zero [Code] ASCII ESC / n Hex. 1B 2F n Decimal 27 47 n 

[Defined Area] n = 0, 1, 48, 49 [Initial Value] Memory switch setting [Function] Specifies and cancels slash zeros. 

|n|InternationalCharacters|
|---|---|
|0, 48|Cancels slash zero|
|1,49|Specifies slash zero|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-8 

**ESC SP n** [Name] Set ANK right space [Code] ASCII ESC SP n Hex. 1B 20 n Decimal 27 32 n 

[Defined Area] 0≤n≤15 48≤n≤57 (”0”≤n≤”9”) 65≤n≤70 (”A”≤n≤”F”) [Initial Value] Memory switch setting [Function] Specify the right space amount of ANK characters in n dots. 

The ANK character width is "left space amount” + "ANK font dot count” + right space amount.” (See the information on character specifications in the appropriate printer specifications manual for details on the ANK font dot count.) 

Character spacing can be specified also with the following commands. 

- Specify 12 dot pitch (ESC M) • Specify 14 dot pitch (ESC g) • Specify 15 dot pitch (ESC P) • Specify 16 dot pitch (ESC :) 

Standard mode and page mode can be set independently of each other. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-9 

|**ESC M**|**ESC M**||
|---|---|---|
|[Name]|Specify 12 dot pitch||
|[Code]|ASCII|ESC<br>M|
||Hex.|1B<br>4D|
||Decimal|27<br>77|
|[Defined Area]||- - -|
|[Initial Value]||Memory switch setting|
|[Function]|[Function]|Specify the right space amount of ANK characters in 0 dots.|
|||The ANK character width is "left space amount” + "ANK font dot count” + right space amount.”|
|||(See the information on character specifications in the appropriate printer specifications manual|
|||for details on the ANK font dot count.)|
|||Standard mode and page mode can be set independently of each other.|



|**ESC P**|**ESC P**||
|---|---|---|
|[Name]|Specify 15 dot pitch||
|[Code]|ASCII|ESC<br>P|
||Hex.|1B<br>50|
||Decimal|27<br>80|
|[Defined Area]||- - -|
|[Initial Value]||Memory switch setting|
|[Function]|[Function]|Specify the right space amount of ANK characters in 3 dots.|
|||The ANK character width is "left space amount” + "ANK font dot count” + right space amount.”|
|||(See the information on character specifications in the appropriate printer specifications manual|
|||for details on the ANK font dot count.)|
|||Standard mode and page mode can be set independently of each other.|



|**ESC :**|**ESC :**||
|---|---|---|
|[Name]|Specify 16 dot pitch||
|[Code]|ASCII|ESC<br>:|
||Hex.|1B<br>3A|
||Decimal|27<br>58|
|[Defined Area]||- - -|
|[Initial Value]||Memory switch setting|
|[Function]|[Function]|Specify the right space amount of ANK characters in 4 dots.|
|||The ANK character width is "left space amount” + "ANK font dot count” + right space amount.”|
|||(See the information on character specifications in the appropriate printer specifications manual|
|||for details on the ANK font dot count.)|
|||Standard mode and page mode can be set independently of each other.|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-10 

**ESC g** [Name] Specify 14 dot pitch [Code] ASCII ESC g Hex. 1B 67 Decimal 27 103 [Defined Area] - - - [Initial Value] Memory switch setting [Function] Specify the right space amount of ANK characters in 2 dots. The ANK character width is "left space amount” + "ANK font dot count” + right space amount.” (See the information on character specifications in the appropriate printer specifications manual for details on the ANK font dot count.) 

Standard mode and page mode can be set independently of each other. 

Specification A 

This command is enabled only when the memory switch setting is set for DBCS (2 byte countries). It is ignored when the memory switch setting is set for SBCS (1 byte countries). Specification B 

This command is enabled for both when the memory switch setting is set for either DBCS (2 byte countries) or SBCS (1 byte countries). 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-11 

## **3.3.2. Character Expansion Settings** 

**ESC i n1 n2** [Name] Set/cancel the double wide/high [Code] ASCII ESC i n1 n2 Hex. 1B 69 n1 n2 Decimal 27 105 n1 n2 [Defined Area] 0≤n1≤5 48≤n1≤53 (”0”≤n1≤”5”) 0≤n2≤5 48≤n2≤53 (”0”≤n2≤”5”) [Initial Value] n1 = 0 (Double high cancelled) n2 = 0 (Double wide cancelled) [Function] Specifies/cancels double high/wide for ANK characters and Kanji characters. This command is ignored if either n1 or n2 is outside of the defined area. 

|n1|Expandedhigh|
|---|---|
|0,48|Cancels expandedhigh|
|1, 49|Specifies 2x high expansion|
|2, 50|Specifies 3x highexpansion|
|3, 51|Specifies4x highexpansion|
|4, 52|Specifies 5x highexpansion|
|5, 53|Specifies 6x highexpansion|
|||
|n2|Expandedwide|
|0,48|Cancels expandedwide|
|1, 49|Specifies 2x wide expansion|
|2, 50|Specifies 3x wide expansion|
|3, 51|Specifies4x wide expansion|
|4, 52|Specifies 5x wide expansion|
|5, 53|Specifies 6x wide expansion|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-12 

## **ESC W n** 

[Name] Specify/cancel expanded wide [Code] ASCII ESC W n Hex. 1B 57 n Decimal 27 87 n [Defined Area] 0≤n≤5 48≤n≤53 (”0”≤n≤”5”) [Initial Value] n = 0 (Double wide cancelled) [Function] Specifies/cancels double wide for ANK characters and Kanji characters. 

||n|Expandedwide|
|---|---|---|
|0, 48|0, 48|Cancels expanded wide|
|1,4|49|Specifies2x wide expansion|
|2,|50|Specifies 3x wide expansion|
|3,|51|Specifies4x wide expansion|
|4,|52|Specifies 5x wide expansion|
|5,|53|Specifies 6x wide expansion|



## **ESC h n** 

[Name] Specify/cancel expanded high [Code] ASCII ESC h n Hex. 1B 68 n Decimal 27 104 n 

[Defined Area] 0≤n≤5 48≤n≤53 (”0”≤n≤”5”) [Initial Value] n = 0 (Double high cancelled) [Function] Specifies/cancels double high for ANK characters and Kanji characters. 

|n|Expandedhigh|
|---|---|
|0,48|Cancels expandedhigh|
|1, 49|Specifies 2x expansion|
|2, 50|Specifies 3xexpansion|
|3, 51|Specifies4xexpansion|
|4, 52|Specifies 5xexpansion|
|5, 53|Specifies 6xexpansion|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-13 

|**SO**|||
|---|---|---|
|[Name]|Set double wide||
|[Code]|ASCII|SO|
||Hex.|0E|
||Decimal|14|
|[Defined Area]||- - -|
|[Initial Value]||Cancels 2x wide expansion|
|[Function]|[Function]|Specifies double wide for ANK characters and Kanji characters.|
|||This command is equivalent to ESC W  n (n = 1).|
|**DC4**|||
|[Name]|Cancel expanded wide||
|[Code]|ASCII|DC4|
||Hex.|14|
||Decimal|20|
|[Defined Area]||- - -|
|[Initial Value]||- - -|
|[Function]|[Function]|Cancels expanded wide if the following commands specify expanded wide.|
|||• Double wide specifying command (SO)|
|||• Set/cancel double wide (ESC W)|
|||• Set/cancel double wide/high (ESC i)|
|||This command is equivalent to ESC W  n (n = 0).|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-14 

**ESC SO** [Name] Set double high [Code] ASCII ESC SO Hex. 1B 0E Decimal 27 14 [Defined Area] - - - [Initial Value] Double high expansion cancelled. [Function] Specifies double high for ANK characters and Kanji characters. This command is equivalent to ESC h  n (n = 1). 

|**ESC DC4**|**ESC DC4**||
|---|---|---|
|[Name]|Cancel expanded high||
|[Code]|ASCII|ESC DC4|
||Hex.|1B<br>14|
||Decimal|27<br>20|
|[Defined Area]||- - -|
|[Initial Value]||- - -|
|[Function]|[Function]|Cancels expanded high if the following commands specify expanded high.|
|||• Double high specifying command (ESC SO)|
|||• Set/cancel the double high (ESC h)|
|||• Set/cancel double wide/high (ESC i)|
|||This command is equivalent to ESC h  n (n = 0).|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-15 

## **3.3.3. Prin t Mode** 

## **ESC E** 

[Name] Select emphasized printing [Code] ASCII ESC E Hex. 1B 45 Decimal 27 69 [Defined Area] - - - [Initial Value] Emphasized printing selected [Function] Specifies emphasized printing for ANK characters. IBM block ignores emphasized printing. 

## **ESC F** 

[Name] Cancel emphasized printing [Code] ASCII ESC F Hex. 1B 46 Decimal 27 70 [Defined Area] - - - [Initial Value] Emphasized printing cancelled. [Function] 

Specification A Cancels emphasized printing for ANK characters. 

Specification B Cancels emphasized printing for ANK and Kanji characters. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-16 

## **ESC – n** 

[Name] Select/cancels underling mode [Code] ASCII ESC - n Hex. 1B 2D n Decimal 27 45 n 

[Defined Area] n = 0, 1, 48, 49 [Initial Value] n = 0 (Underline cancelled) [Function] Specifies underlining (2 dots). Underlines are composed of 2 dot lines. Underlines are not applied to horizontal tabs and to specified horizontal direction positions. Underlines are expanded if the character expansion is specified. (When double high expansion is used, underlines are composed of 4 dots.) Underlines are enabled for white/black inversion. This command is enabled for ANK characters and Kanji characters. IBM block ignores underlines. 

||n|Underline|
|---|---|---|
|0, 48|0, 48|Cancels underline|
|1,4|49|Specifies underline|



## **ESC _ n** 

|[Name]|Specify/cancelupperline|Specify/cancelupperline|
|---|---|---|
|[Code]|ASCII|ESC<br>_<br>n|
||Hex.|1B<br>5F<br>n|
||Decimal|27<br>95<br>n|
|[Defined Area]||n = 0, 1, 48, 49|
|[Initial Value]||n = 0 (Upperline cancelled)|
|[Function]|[Function]|Specifies upperlining (2 dots).|
|||Upperlines are composed of 2 dot lines.|
|||Upperlines are not applied to horizontal tabs and to specified horizontal direction positions.|
|||Upperlines are expanded if the character expansion is specified. (When double high expansion is|
|||used, upperlines are composed of 4 dots.)|
|||Upperlines are enabled for white/black inversion.|
|||This command is enabled for ANK characters and Kanji characters.|
|||IBM block ignores upperlines.|



||n|Upperline|
|---|---|---|
|0, 48|0, 48|Cancels upperline|
|1,4|49|Specifies upperline|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-17 

## **ESC 4** 

[Name] Select white/black inverted printing [Code] ASCII ESC 4 Hex. 1B 34 Decimal 27 52 [Defined Area] - - - [Initial Value] White/black inversion cancelled [Function] Specifies white/black inversion for ANK characters and Kanji characters. IBM block ignores white/black inversion. 

## **ESC 5** 

[Name] Cancel white/black inversion [Code] ASCII ESC 5 Hex. 1B 35 Decimal 27 53 [Defined Area] - - - [Initial Value] White/black inversion cancelled [Function] Cancels white/black inversion for ANK characters and Kanji characters. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-18 

**SI** [Name] Select upside-down printing [Code] ASCII SI Hex. 0F Decimal 15 [Defined Area] - - - [Initial Value] Upside-down cancelled [Function] Specifies upside-down printing This command is enabled only when at the top of the line. Upside down and right-side up characters cannot both exist in the same line. This command is enabled for following. • ANK characters • Kanji characters • Bit images • Logos • Bar codes 

## **DC2** 

[Name] Cancel upside-down printing [Code] ASCII DC2 Hex. 12 Decimal 18 [Defined Area] - - - [Initial Value] Upside-down printing cancelled [Function] Cancels upside-down printing This command is enabled only when at the top of the line. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-19 

## **3.3.4. L ine Spacing** 

**LF** [Name] Line feed [Code] ASCII LF Hex. 0A Decimal 10 [Defined Area] - - - [Initial Value] - - - [Function] Feeds the currently specified amount of paper. If print data exists in the line buffer, it prints that data. The initial value for the amount of paper is set according to the memory switch settings. 

|**CR**|||
|---|---|---|
|[Name]|Carriage return (line feed)|Carriage return (line feed)|
|[Code]|ASCII|CR|
||Hex.|0D|
||Decimal|13|
|[Defined Area]||- - -|
|[Initial Value]||- - -|
|[Function]|[Function]|When the CR code is enabled, the CR code functions in the same way as the LF code.|
|||If the CR code is disabled, it ignores 1 byte.|
|||Enabling and disabling the CR code is done using the memory switch settings.|



**ESC a n** [Name] Feed paper n lines [Code] ASCII ESC a n Hex. 1B 61 n Decimal 27 97 n [Defined Area] 1≤n≤127 [Initial Value] - - - [Function] Executes a paper feed for (the currently specified line feed amount x n). If print data exists in the line buffer, it prints that data. The initial value for the amount of paper is set according to the memory switch settings. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-20 

## **ESC z n** 

[Name] Select line feed amount [Code] ASCII ESC z n Hex. 1B 7A n Decimal 27 122 n [Defined Area] n = 1, 49 [Initial Value] Memory switch setting [Function] Specifies the line feed amount. 

Standard mode and page mode can be set independently of each other. 

n Line feed amount 1, 49 Specifies 4 mm line feed amount 

## **ESC 0** 

[Name] Specify line spacing to 3 mm [Code] ASCII ESC 0 Hex. 1B 30 Decimal 27 48 [Defined Area] - - - [Initial Value] Memory switch setting [Function] Specifies the line feed amount to 3 mm. 

Standard mode and page mode can be set independently of each other. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-21 

## **ESC J n** 

[Name] n/4 mm line feed [Code] ASCII ESC J n Hex. 1B 4A n Decimal 27 74 n [Defined Area] 1≤n≤255 [Initial Value] - - - [Function] Executes a n/4mm paper feed. If print data exists in the line buffer, it prints that data. Using this command will intermittently feed paper, therefore, it is normally recommended that this command not be used. 

## **ESC I n** 

[Name] n/8mm line feed [Code] ASCII ESC I n Hex. 1B 49 n Decimal 27 73 n [Defined Area] 1≤n≤255 [Initial Value] - - - [Function] Executes a n/8mm paper feed. If print data exists in the line buffer, it prints that data. Using this command will intermittently feed paper, therefore, it is normally recommended that this command not be used. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-22 

## **3.3.5. Pa ge Control Commands** 

## **FF** 

[Name] Form feed [Code] ASCII FF Hex. 0C Decimal 12 [Defined Area] - - - [Initial Value] - - - [Function] Executes a form feed. If the current position is at the top of the page, it form feeds to the top of the next page. If there is data existing in the line buffer when executing a form feed, it prints that data, then executes the form feed. 

However, by printing data remaining in the buffer, and moving to the top of the next page, a form feed is considered to have been executed, so form feed is not performed. Invalid in page mode. 

## **ESC C n** 

[Name] Set page length to n lines [Code] ASCII ESC C n Hex. 1B 43 n Decimal 27 67 n [Defined Area] 1≤n≤127 [Initial Value] (Form feed amount initial value x 42) [Function] The position whereat this command is processed is considered the top of the page and sets the page length to (current form feed amount x n). 

This command cancels the bottom margin setting when setting page length. The page length set using this command is unaffected by changing the form feed amount later. Moving to the top of the page is performed using the following commands. 

- Form feed command (FF): Executes a form feed. • Cutter command (ESC d n): Sets cutter position at top of page. • Raster command (ESC * r B): Sets top of page when quitting raster mode. 

• Error cancel operations: Sets position when quitting error cancellation operations at top of page. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-23 

**ESC C 0 n** [Name] Set page length to n x 24 mm units [Code] ASCII ESC C 0 n Hex. 1B 43 00 n Decimal 27 67 0 n [Defined Area] 1≤n≤22 [Initial Value] (Form feed amount initial value x 42) [Function] The position whereat this command is processed is considered the top of the page and sets the page length to (n x 24 mm). 

This command cancels the bottom margin setting when setting page length. 

The page length set using this command is unaffected by changing the form feed amount later. Moving to the top of the page is performed using the following commands. 

• Form feed command (FF): Executes a form feed. • Cutter command (ESC d n): 

• Cutter command (ESC d n): Sets cutter position at top of page. • Raster command (ESC * r B): Sets top of page when quitting raster mode. • Error cancel operations: Sets position when quitting error cancellation operations at top of page. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-24 

|**VT**|||
|---|---|---|
|[Name]|Feed paper to vertical tab position||
|[Code]|ASCII|VT|
||Hex.|0B|
||Decimal|11|
|[Defined Area]||- - -|
|[Initial Value]||- - -|
|[Function]|[Function]|Feeds paper to the next vertical tab position.|
|||This command is ignored if there are no tabs set.|
|||If a vertical tab is set, and the current position is the same as the vertical tab position, or if it is|
|||below that position, it feeds paper to the top of the next page.|
|||If data exists in the line buffer when feeing paper to the vertical tab position, it executes the paper|
|||feed to the vertical tab position after printing that data.  However, if moved to the vertical tab|
|||position by printing data remaining in the buffer, the move to the vertical tab position is considered|
|||to have been executed, so a move to the next vertical tab position is not performed.|
|||There is no initial value for the vertical tab.|
|||Invalid in page mode.|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-25 

## **ESC B n1 n2…nk NUL** 

[Name] Set vertical tab position [Code] ASCII ESC B n1 n2 ... nk NUL Hex. 1B 42 n1 n2 ... nk 00 Decimal 27 66 n1 n2 ... nk 0 [Defined Area] 1≤n≤255 0≤k≤16 [Initial Value] - - - [Function] Sets the vertical tab to the (current form feed amount x n) position. All other vertical tabs set before setting the vertical tab using this command are cancelled A maximum of 16 vertical tabs can be set. However, the tab position must satisfy the condition of 1≤n1≤n2...≤nk. When receiving such illegal codes, tabs up to the illegal code are set, but those after the illegal code are discarded up to the NUL code so illegal code tab are not set. The vertical tab set using this command is unaffected by changing the form feed amount later. Vertical tabs set using the ESC B NUL command are cleared. There is no initial value for the vertical tab. 

## **ESC B NUL** 

[Name] Clear vertical tab position [Code] ASCII ESC B NUL Hex. 1B 42 00 Decimal 27 66 0 

[Defined Area] - - - [Initial Value] - - - [Function] Clears the currently set vertical tab. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-26 

## **3.3.6. Ho rizontal Direction Printing Position** 

**ESC l n** [Name] Set left margin [Code] ASCII ESC l n Hex. 1B 6C n Decimal 27 108 n [Defined Area] 0≤n≤255 [Initial Value] n = 0 [Function] Uses the left edge as a standard to set the left margin as (current ANK character pitch x n). Character pitch includes the space between characters and expansion settings are enabled. The left margin set using this command is unaffected by changing the character pitch. This command is ignored if settings are for a printing region less than 36 mm. Specification A Setting this command partway will take affect from the next line. Specification B This command is enabled only when at the top of the line. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-27 

## **ESC Q n** 

[Name] Set right margin [Code] ASCII ESC Q n Hex. 1B 51 n Decimal 27 81 n 

[Defined Area] 0≤n≤255 [Initial Value] - - - [Function] Uses the left edge as a standard to set the print region as (current ANK character pitch x n). Character pitch includes the space between characters and expansion settings are enabled. The right margin set using this command is unaffected by changing the character pitch. This command is ignored if settings are for a printing region less than 36 mm. 

Specification A Setting this command partway will take affect from the next line. Specification B This command is enabled only when at the top of the line. 

Printable Region Left Margin                       Print Region Right Margin 

## **HT** 

[Name] Move horizontal tab [Code] ASCII HT Hex. 09 Decimal 9 

[Defined Area] - - - [Initial Value] - - - [Function] Move print position to next horizontal tab position. 

This command is ignored with under the following conditions. 

• When there is no horizontal tab set. 

• When the current position is the same as the furthest right horizontal tab position or to the right of it. 

There is no initial value for the horizontal tab. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-28 

## **ESC D n1 n2…nk NUL** 

|[Name]|Set horizontal tab|Set horizontal tab|
|---|---|---|
|[Code]|ASCII|ESC<br>D<br>n1<br>n2<br>...<br>nk NUL|
||Hex.|1B<br>44<br>n1<br>n2<br>...<br>nk<br>00|
||Decimal|27<br>68<br>n1<br>n2<br>...<br>nk<br>0|
|[Defined Area]||1≤<br>n≤<br>255|
|||0≤<br>k≤<br>16|
|[Initial Value]||- - -|
|[Function]|[Function]|Uses the left edge as a standard to set the horizontal tab to the position of (current ANK character|
|||pitch x n).|
|||The horizontal tab reference point is the right edge of the paper, regardless of the left margin.|
|||ANK character pitch includes the right space and expansion settings are enabled.|
|||All other horizontal tabs set before setting the horizontal tab using this command are cancelled|
|||A maximum of 16 horizontal tabs can be set.|
|||However, the tab position must satisfy the following conditions.|
|||If the following conditions are not met, data up to the NUL code is discarded.|
|||Normal tabs that meet the conditions below are set and tabs after errors occur are not set.|
|||• 1<n1 < n2... < nk|
|||• nk≤<br> Printable region|
|||The horizontal tab set using this command is unaffected by changing the character pitch.|
|||Horizontal tabs set using the ESC D NUL command are cleared.|
|||There is no initial value for the horizontal tab.|



Standard mode and page mode can be set independently of each other. 

## **ESC D NUL** 

[Name] Clear horizontal tab [Code] ASCII ESC D NUL Hex. 1B 44 00 Decimal 27 68 0 

[Defined Area] - - - [Initial Value] - - - [Function] Clears the currently set horizontal tab. 

Standard mode and page mode can be set independently of each other. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-29 

## **ESC GS A n1 n2** 

|[Name]|Move absolute position|Move absolute position||||
|---|---|---|---|---|---|
|[Code]|ASCII|ESC GS|A|n1|n2|
||Hex.|1B<br>1D|41|n1|n2|
||Decimal|27<br>29|65|n1|n2|
|[Defined Area]||0≤<br>n1≤<br>255||||
|||0≤<br>n2≤<br>255||||
|[Initial Value]||- - -||||
|[Function]|[Function]|Moves the printing position from the left margin to the (n1 + n2 x 256) position.||||
|||This command is ignored if the print region is exceeded.|This command is ignored if the print region is exceeded.||This command is ignored if the print region is exceeded.|



## **ESC GS R n1 n2** 

[Name] Move relative position [Code] ASCII ESC GS R n1 n2 Hex. 1B 1D 52 n1 n2 Decimal 27 29 82 n1 n2 [Defined Area] 0≤n1≤255 0≤n2≤255 [Initial Value] - - - [Function] Moves the printing position from the current position to the (n1 + n2 x 256) position. This command is ignored if the print region is exceeded. When (n1 + n2 x 256) ≥ 32768, it moves {65536 – (n1 + n2 x 256)} dots in the left direction. When (n1 + n2 x 256) < 32768, it moves (n1 + n2 x 256)} dots in the right direction. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-30 

## **ESC GS a n** 

[Name] Specify position alignment [Code] ASCII ESC GS a n Hex. 1B 1D 61 n Decimal 27 29 97 n 

[Defined Area] 0≤n≤2 48≤n≤50 (”0”≤n≤”2”) [Initial Value] n = 0 [Function] Specifies the alignment position in the printing region that has been set. 

|n|Positionalignment|
|---|---|
|0, 48|Left alignment|
|1,49|Centeralignment|
|2, 50|Right alignment|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-31 

## **3.3.7. Do wnload** 

## **ESC & c1 c2 n d1…d48** 

[Name] Register 12 x 24 dot font download characters [Code] ASCII ESC & c1 c2 n d1 ... d48 Hex. 1B 26 c1 c2 n d1 ... d48 Decimal 27 38 c1 c2 n d1 ... d48 [Defined Area] c1 = 1, 49 c2 = 1, 49 32≤n≤127 0≤d≤255 [Initial Value] - - - [Function] Registers 12 x 24 dot font download characters to the nth address. Download characters can be registered to <20>H to <7F>H. If one has been already registered to an address, it is overwritten. When parameters c1 and c2 and n are outside of the defined area, subsequent data is handled as normal data. Horizontal 12 Dots 

||d1<br>d3|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~PPrPrprppyy])~~<br>~~OO ~~|d2<br>d4<br>|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br>●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br>~~PPppypyy~~<br>~~yy~~<br> ~~OO~~|
|---|---|---|---|---|
||d5|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~OO ~~|d6<br>|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br> ~~OO~~|
||d7|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~OO~~|d8|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d9|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>d10<br>●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br>~~OC~~|||
||d11|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d12|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d13|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>d14<br>●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br>~~OC~~|||
||d15|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d16|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d17|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d18|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d19|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d20|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d21|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d22|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
|Vertical<br>24 Dots|d23<br>d25<br>d27|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~<br>~~Pee ~~<br>~~OO ~~|d24<br>d26<br>d28<br> <br>|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br>●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br>●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br> ~~eee~~<br> ~~OO~~|
||d29|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~OO ~~|d30<br>|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br> ~~OO~~|
||d31|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~OO~~|d32|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d33|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~OO~~|d34|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d35|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~OO~~|d36|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d37|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>d38<br>●<br>●<br>●<br>●<br>○<br>○<br>○<br>○<br>~~OC~~|||
||d39|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d40|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d41|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d42|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d43|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d44|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d45|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~<br>~~OO~~|d46|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
||d47|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>~~A~~|d48|●<br>●<br>●<br>●<br>○<br>○<br>○<br>○|
|||bit7 bit6 bit5 bit4 bit3<br>bit2<br>bit1<br>Bit0||bit7<br>bit6<br>bit5 bit4 bit3 bit2<br>bit1<br>bit0|
||●: Font data<br>○: Invalid data||||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-32 

## **ESC & c1 c2 n** 

[Name] Delete 12 x 24 dot font download characters [Code] ASCII ESC & c1 c2 n Hex. 1B 26 c1 c2 n Decimal 27 38 c1 c2 n [Defined Area] c1 = 1, 49 c2 = 0, 48 32≤n≤127 [Initial Value] - - - [Function] Deletes 12 x 24 dot font download characters registered to the nth address. 

## **ESC % n** 

[Name] Specifies/cancels ANK download characters [Code] ASCII ESC % n Hex. 1B 25 n Decimal 27 37 n 

[Defined Area] n=0, 1, 48, 49 [Initial Value] ANK download characters cancelled [Function] Specifies/cancels ANK download characters 

|n|Download characters|
|---|---|
|0, 48|Cancels ANK download characters|
|1,49|SpecifiesANKdownload characters|



<Print example of ANK download characters> 

1. ANK download character register (ESC & c1 c2 n d1…d48) 

2. Specify ANK download characters (ESC % n (n = 1)) 

3. Prints ANK download characters 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-33 

## **3.3.8. Bit Image Graphics** 

**ESC K n1 n2 d1...dk** [Name] Standard density bit image [Code] ASCII ESC K n1 n2 d1 ... dk Hex. 1B 4B n1 n2 d1 ... dk Decimal 27 75 n1 n2 d1 ... dk [Defined Area] 1 ≤ {(n1 + n2 x 256) x 3} ≤ printable region k = (n1 + n2 x 256) 0≤d≤255 [Initial Value] - - - [Function] Prints bit images using 3 dots wide and 3 dots high per 1 dot of input data. The following shows the data processing in this command. • When {(n1 + n2 x 256) x 3} exceeds the printable region, data after d1 is handled as normal data. • When {(n1 + n2 x 256) x 3} exceeds the printable region that is currently set, only the data in the printing region is printed. At this time, all data for the print region is discarded. 

- If the current position already exceeds the print region, this command discards all data. 

|b7<br> b6<br> b5<br> b4<br> b3<br> b2<br> b1<br> b0<br> • • •<br>• • •<br>• • •<br> • • •<br>• • •<br>• • •<br> • • •<br>• • •<br>• • •<br> • • •<br>• • •<br>• • •<br> • • •<br>• • •<br>• • •<br> • • •<br>• • •<br>• • •<br> • • •<br>• • •<br>• • •<br> • • •<br>• • •<br>• • •|b7<br>|b6<br>|b5<br>|b4<br>|b3<br>|b2<br>|b1<br>|b0|
|---|---|---|---|---|---|---|---|---|
|• • •<br>• • •<br>• • •|||||||||
|• • •<br>• • •<br>• • •|||||||||
|• • •<br>• • •<br>• • •|||||||||
|• • •<br>• • •<br>• • •|||||||||
|• • •<br>• • •<br>• • •|||||||||
|• • •<br>• • •<br>• • •|||||||||
|• • •<br>• • •<br>• • •|||||||||
|• • •<br>• • •<br>• • •|||||||||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-34 

**ESC L n1 n2 d1...dk** [Name] Standard density bit image [Code] ASCII ESC L n1 n2 d1 ... dk Hex. 1B 4C n1 n2 d1 ... dk Decimal 27 76 n1 n2 d1 ... dk 

[Defined Area] 1 ≤ (n1 + n2 x 256) ≤ printable region k = (n1 + n2 x 256) 0≤d≤255 [Initial Value] - - - [Function] Prints bit images using 1 dot wide and 3 dots high per 1 dot of input data. The following shows the data processing in this command. • When (n1 + n2 x 256) exceeds the printable region, data after d1 is handled as normal data. • When (n1 + n2 x 256) exceeds the printable region that is currently set, only the data in the printing region is printed. At this time, all data for the print region is discarded. 

• If the current position already exceeds the print region, this command discards all data. 

**==> picture [255 x 230] intentionally omitted <==**

**----- Start of picture text -----**<br>
b7 b6 b5 b4 b3 b2 b1 b0<br>•<br>  •<br>  •<br>•<br>  •<br>  •<br>•<br>  •<br>  •<br>•<br>•<br>  •<br>  •<br>•<br>  •<br>  •<br>•<br>  •<br>  •<br>•<br>  •<br>  •<br>•<br>  •<br>  •<br>**----- End of picture text -----**<br>


――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-35 

**ESC k n1 n2 d1...dk** 

[Name] Fine density bit image [Code] ASCII ESC k n1 n2 d1 ... dk Hex. 1B 6B n1 n2 d1 ... dk Decimal 27 107 n1 n2 d1 ... dk 

[Defined Area] n2 = 0 1 ≤ {(n1 + n2 x 256) x 8} ≤ printable region k = {(n1 + n2 x 256) x 24} 0≤d≤255 

[Initial Value] - - - [Function] Prints bit images using 1 dot wide and 1 dots high per 1 dot of input data. The following shows the data processing in this command. 

• When {(n1 + n2 x 256) x 8} exceeds the printable region, data after d1 is handled as normal data. • When {(n1 + n2 x 256) x 8} exceeds the printable region that is currently set, only the data in the printing region is printed. 

At this time, all data for the print region is discarded. 

- If the current position already exceeds the print region, this command discards all data. 

|**24 Dots**|**X Bytes =(n1 + n2 x 256)**|**X Bytes =(n1 + n2 x 256)**|**X Bytes =(n1 + n2 x 256)**|**X Bytes =(n1 + n2 x 256)**|
|---|---|---|---|---|
||||||
||d1|d2|• • • • • • •|dX|
||dX x 1+1|dX x 1+2|• • • • • • •|dX x 2|
||dX x 2+1|dX x 2+2|• • • • • • •|dX x 3|
||•<br>•<br>•<br>•<br>•<br>•<br>•<br>•||•<br>•<br>•<br>•||
||dX x 23+ 1|dX x 23+ 2|• • • • • • •|dX x 24|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-36 

## **ESC X n1 n2 d1...dk** 

[Name] Fine density bit image (Compatible with 24 bit wire dots) [Code] ASCII ESC X n1 n2 d1 ... dk Hex. 1B 58 n1 n2 d1 ... dk Decimal 27 88 n1 n2 d1 ... dk 

[Defined Area] 1 ≤ (n1 + n2 x 256) ≤ printable region k = {(n1 + n2 x 256) x 3} 0≤d≤255 

[Initial Value] - - - [Function] Prints input bit images with 8 dots/mm resolution for both horizontal and vertical. The following shows the data processing in this command. 

- When {(n1 + n2 x 256) x 3} exceeds the printable region, data after d1 is handled as normal data. 

- When {(n1 + n2 x 256) x 3} exceeds the printable region that is currently set, only the data in the printing region is printed. 

At this time, all data for the print region is discarded. 

• If the current position already exceeds the print region, this command discards all data. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-37 

## **3.3.9. Logo** 

|**ESC FS q n**|**ESC FS q n**|**ESC FS q n [x11 x12 y11 y12 d1...dk]1...[xn1 xn2 yn1 yn2 d1...dk]n**|||
|---|---|---|---|---|
|[Name]|Register logo|Register logo|||
|[Code]|ASCII|ESC<br>FS<br>q<br>n [x11 x12 y11 y12<br>d1<br>... dk]1<br>... [xn1 xn2 yn1 yn2|d1|... dk]n|
||Hex.|1B<br>1C<br>71<br>n [x11 x12 y11 y12<br>d1<br>... dk]1<br>... [xn1 xn2 yn1 yn2|d1|... dk]n|
||Decimal|Decimal<br>27<br>28 113<br>n [x11 x12 y11 y12<br>d1<br>... dk]1<br>... [xn1 xn2 yn1 yn2|d1|... dk]n|
|[Defined Area]||1≤<br>n≤<br>255|||
|||0≤<br>xn1≤<br>255,0≤<br>xn2≤<br>3|||
|||1≤<br>(xn1 + xn2 x 256)≤<br>1023|||
|||0≤<br>yn1≤<br>255,0≤<br>yn2≤<br>1|||
|||1≤<br>yn1 + yn2 x 256)≤<br>288|||
|||0≤<br>d≤<br>255|||
|||k = {(xn1 + xn2 x 256) x (yn1 + yn2 x 256) x 8}|||
|[Initial Value]||- - -|||
|[Function]|[Function]|Parameter details|||
|||• n:<br>Specifies registered logo count|||
|||• xn1, xn2: Horizontal size of registered logo {(xn1 + xn2 x 256) x 8} dots|||
|||• yn1, yn2: Vertical size of registered logo {(yn1 + yn2 x 256) x 8} dots|||
|||• d:<br>Registered logo data|||
|||• k:<br>Logo data count|||
|||This command should be specified at the top of the line.|||
|||When the first parameter is determined to be free of error, the printer starts processing this||When the first parameter is determined to be free of error, the printer starts processing this|
|||command.|||
|||When logo register processing starts, all previously defined data is deleted.|||
|||(It is not possible to reregister a portion of a plurality of defined logo data.)|||
|||Logo registration numbers are defined in rising order from 1.|||
|||If the defined area specified by the parameter is not empty, or if there is an error in the parameter||If the defined area specified by the parameter is not empty, or if there is an error in the parameter|
|||specification, register processing is aborted.  (The pre-registered and complete data is effective.)||specification, register processing is aborted.  (The pre-registered and complete data is effective.)|
|||The printer should be initialized if logo registration is completed or register processing is aborted.|||
|||If an error occurs while performing register processing (the time from when the first parameter is|||
|||OK until the printer initialization is completed after registering a logo), error processing, mechanical|||
|||operation and status processing cannot be performed.|||
|||The relationships between input data and the actual print are shown on the next page.||The relationships between input data and the actual print are shown on the next page.|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-38 

**==> picture [464 x 688] intentionally omitted <==**

**----- Start of picture text -----**<br>
Relationships of logo and registered data<br>xn = xn1 + xn2 x 256,   yn = yn1 + yn2 x 256<br>{(xn1 + xn2 x 256) x 8} dots<br>Data<br>MSB<br>d[11]  d[21]  d[n1]<br>(yn1 + yn2 x 256) bytes<br>(yn1 + yn2 x 256) x 8 d[12]  d[22]  d[n2]<br>dots<br>LSB<br>ITE<br>d[x1]  d[x2]  d[xn]<br>ee<br>―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――<br>STAR Line Mode Command Specifications  3-39<br>**----- End of picture text -----**<br>

**ESC FS p n m** 

[Name] Print logo [Code] ASCII ESC FS p n m Hex. 1B 1C 70 n m Decimal 27 28 112 n m [Defined Area] 1≤n≤255 0≤m≤3 48≤m≤51 (”0”≤m≤”3”) [Initial Value] - - - [Function] Prints the logo of registration number n registered using the logo registration command (ESC FS q) according to the print mode m. 

|m|Logo printmode|
|---|---|
|0,48|Normal mode|
|1, 49|Double wide mode|
|2, 50|Doublehigh mode|
|3, 51|Doublehigh/widemode|



If there is unprinted data in the line buffer, this command is executed after printing that data. Therefore, it is not possible to print with other data in the same line (characters, bit images, bar codes). 

Form feed obeys the vertical print size of the logo. 

If the logo horizontal print size exceeds the horizontal print region, the portion exceeding the area is not printed. Logos are printed according to the following command settings. 

• Left margin (ESC I n) 

- Right margin (ESC Q n) 

- Position alignment (ESC GS a n) 

- Absolute position movement (ESC GS A n1 n2) 

- Relative position movement (ESC GS R n1 n2) 

- Upside-down printing (SI) Invalid in page mode. 

## **ESC RS L m** 

[Name] Spec. A Print logo in batch Spec. B Batch control of registered logos [Code] ASCII ESC RS L m Hex. 1B 1E 4C m Decimal 27 30 76 m 

[Defined Area] Spec. A 0 ≤ m ≤ 3 48 ≤ m ≤ 51 (“0” ≤ m ≤ “3”) Spec. B 0 ≤ m ≤ 3 48 ≤ m ≤ 51 (“0” ≤ m ≤ “3”),m=255 [Initial Value] - - - [Function] Spec. A Prints all registered logos according to a print mode specified by m. Executes a printer reset after printing. Spec. B Controls logos as specified by the parameter m. After execution, this resets the printer. Invalid in page mode. 

Spec. A 

|Spec. Apec. Aec. A|Spec. B<br>Controls logos as specified by the parameter m.<br>After execution, this resets the printer.<br>Invalid in page mode.|
|---|---|
|m|Logo printmode|
|0,48|Normal mode|
|1,49|Doublewidemode|
|2, 50|Double high mode|
|3, 51|Doublehigh/widemode|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-40 

|Spec. B||
|---|---|
|m|Logo Control Mode|
|0, 48|Normal mode Batch printing|
|1,49|DoublewidemodeBatchprinting|
|2, 50|Doublehigh modeBatchprinting|
|3, 51|Doublehigh/widemodeBatchprinting|
|255|Batchdeletelogos|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-41 

## **3.3.10. Bar Code** 

## **ESC b n1 n2 n3 n4 d1...dk RS** 

[Name] [Code] ASCII ESC b n1 n2 n3 n4 d1 ... dk RS Hex. 1B 62 n1 n2 n3 n4 d1 ... dk 1E Decimal 27 98 n1 n2 n3 n4 d1 ... dk 30 [Defined Area] 0≤n1≤8,  48≤n1≤56 (”0≤n1≤”8”) 1≤n2≤4,  49≤n2≤52 (”1”≤n2≤”4”) 1≤n4≤255 n3 (bar code mode), d (bar code data), k (bar code data count) definitions differ according to the type of bar code. [Initial Value] - - - [Function] Bar code printing is executed according to the following parameters. 

If n1, n2, n3 and n4 are acquired and detected to be out of the defined area, data up to RS is discarded. 

• n1 bar code type selection 

|n1|Barcode type|
|---|---|
|0,48|UPC-E|
|1,49|UPC-A|
|2, 50|JAN/EAN8|
|3, 51|JAN/EAN13|
|4, 52|Code39|
|5, 53|ITF|
|6, 54|Code128|
|7, 55|Code93|
|8, 56|NW-7|



• n2 Under-bar character selection and added line feed selection 

|n2|Under-barcharacterselectionand addedlinefeed selection|
|---|---|
|1, 49|No added under-bar characters Executes line feed after printing a bar code|
|2, 50|Adds under-barcharacters<br>Executeslinefeed afterprinting a barcode|
|3, 51|No added under-barcharactersDoesnot executelinefeed afterprinting a barcode|
|4, 52|Adds under-barcharacters<br>Doesnot executelinefeed afterprinting a barcode|



• n3 bar code mode selection 

|~~a~~|~~**e**ee~~|~~**e**ee~~|~~**e**ee~~|
|---|---|---|---|
|n3<br>~~a~~|Bar code type<br>~~**e**ee~~<br>~~e~~|||
||UPC-E, UPC-A, JAN/EAN8<br>JAN/EAN13, Code128, Code93<br>~~**e**ee~~|Code39, NW-7<br>~~e~~|ITF<br>~~e~~|
|1, 49<br>~~a ~~<br>~~eG~~|Minimum module 2 dots<br> ~~**e**ee~~<br>~~eG~~|Narrow: Wide=2:6 dots<br>~~eG~~|Narrow: Wide=2:5 dots<br>~~eG~~|
|2, 50<br>~~a~~|Minimum module 3 dots|Narrow: Wide=3:9 dots|Narrow: Wide= 4:10 dots|
|3, 51<br>~~a~~|Minimum module4dots<br>|Narrow: Wide= 4:12dots<br>|Narrow: Wide=6:15 dots<br>|
|4, 52<br>~~eG~~<br>~~es~~|- - -<br>~~eG~~<br>|Narrow: Wide= 2:5 dots<br>~~eG~~<br>|Narrow: Wide= 2:4dots<br>~~eG~~<br>|
|5, 53<br>~~es~~|- - -<br>|Narrow: Wide=3:8 dots<br>|Narrow: Wide=4:8 dots<br>|
|6, 54<br>~~essD~~|- - -<br>~~sD~~|Narrow: Wide= 4:10 dots<br>~~sD~~|Narrow: Wide=6:12dots<br>~~sD~~|
|7, 55<br>~~a~~|- - -|Narrow: Wide= 2:4dots|Narrow: Wide= 2:6 dots|
|8, 56<br>~~a~~<br>~~a~~|- - -|Narrow: Wide=3:6 dots|Narrow: Wide=3:9 dots|
|9, 57<br>~~a~~|- - -|Narrow: Wide= 4:8 dots|Narrow: Wide= 4:12dots|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-42 

• n4 bar code height (dot count) 

Specification A 

When the height of the bar code is more than the form feed amount, the form feed amount is automatically doubled. 

Specification B 

Form feed at (Bar code height + underbar characters) 

• k (Bar code data count), d (Bar code data) 

|Barcode type<br>~~a~~|Defined area of k|Defined area ofd|
|---|---|---|
|UPC-E<br>~~a~~|11≤<br>k≤<br>12|48≤<br>d≤<br>57 (”0”≤<br>d≤<br>”9”)|
|UPC-A<br>~~a~~<br>~~a~~|11≤<br>k≤<br>12<br>~~a~~|57 (<br>)<br>48≤<br>d≤<br>57(”0”≤<br>d≤<br>”9”)|
|JAN/EAN8<br>~~a ~~<br>~~a~~|7≤<br>k≤<br>8<br> ~~a~~<br>~~a~~|(<br>)<br>48≤<br>d≤<br>57(”0”≤<br>d≤<br>”9”)|
|JAN/EAN13<br>~~a~~|12≤<br>k≤<br>13<br>~~a~~|(<br>)<br>48≤<br>d≤<br>57(”0”≤<br>d≤<br>”9”)|
|Code39<br>~~ee~~|1≤<br>k<br>~~ee~~|(<br>)<br>48≤<br>d≤<br>57 (”0”≤<br>d≤<br>”9”)<br>65≤<br>d≤<br>90 (”A”≤<br>d≤<br>”Z”)<br>32, 36, 37,43,45,46,47(SP,”$”,”%”,”+”,”-“,”.”,”/”)<br>~~eee~~|
|ITF<br>~~ee ~~|1≤<br>k<br>When an odd number: 0 is<br>automatically applied to the<br>top.<br> ~~ee~~|48≤<br>d≤<br>57 (“0”≤<br>d≤<br>”9”)<br>~~eee~~|
|Code128<br>~~a~~|1≤<br>k|0≤<br>d≤<br>127|
|Code93<br>~~a~~|1≤<br>k|0≤<br>d≤<br>127|
|NW-7|1≤<br>k|48≤<br>d≤<br>57 (”0”≤<br>d≤<br>”9”)<br>65≤<br>d≤<br>68 (”A”≤<br>d≤<br>”D”)<br>36, 43, 45, 46, 47, 58 (”$”, ”+”, ”-“, ”.”, ”/”, ”:”)<br>97, 98, 99,100 (”a”,”b”,”c”,”d”)|



- UPC – E: k = 11 (or 12) 

The 12[th] check digit is automatically applied, so it is specified and ignored. The command is ignored for data that cannot be shortened. Automatically converts data to shortened form. 

• UPC – A: k = 11 (or 12) 

The 12[th] check digit is automatically applied, so it is specified and ignored. 

• JAN/EAN – 8: k = 7 (or 8) 

The 8[th] check digit is automatically applied, so it is specified and ignored. 

• JAN/EAN -13: k = 12 (or 13) 

The 13[th] check digit cannot be automatically applied, so it is specified and ignored. 

• CODE 39: k is freely set, and maximum value differs according to the mode. Start/stop code (“*”) is automatically applied. 

• ITF: k is freely set, and maximum value differs according to the mode. If data is oddly numbered, a 0 is applied to the top. 

• CODE 128: k is freely set, and maximum value differs according to the mode and the print character type. 

The check character is automatically applied. 

• CODE 93: k is freely set, and maximum value differs according to the mode and the print character type. 

The check character (“□”) is automatically applied. 

• NW7: k is freely set, and maximum value differs according to the mode and the print character type. 

Start/stop codes included in the data (not automatically applied). 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-43 

## **3.3.11. Cu tter Control** 

## **ESC d n** 

[Name] Auto-cutter [Code] ASCII ESC d n Hex. 1B 64 n Decimal 27 100 n 

[Defined Area] 0≤d≤3 48≤d≤51 (”0”≤d≤”3”) [Initial Value] - - - [Function] Executes the auto-cutter. 

After auto-cutter is executed, the printer considers that to be the top of the page. 

|n|Auto cutter|
|---|---|
|0, 48|Full cut at the current position.<br>Print data in line buffer is printed before a full cut.<br>This command is ignored if the printer is not equipped with an auto-cutter.|
|1, 49|Partial cut at the current position.<br>Print data in line buffer is printed before a partial cut.<br>This commandisignoredifthe printer isnot equippedwithanauto-cutter.|
|2, 50|Paper is fed to cutting position, then a full cut.<br>Print data in line buffer is printed before the operation described above.<br>This commandisignoredifthe printer isnot equippedwithanauto-cutter.|
|3, 51|Paper is fed to cutting position, then a partial cut.<br>Print data in line buffer is printed before the operation described above.<br>This commandisignoredifthe printer isnot equippedwithanauto-cutter.|



(*) When connected with a presenter, executes a full cut when instructed for a partial cut. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-44 

## **3.3.12. External Device Drive** 

**ESC BEL n1 n2** [Name] Set external drive device 1 pulse width [Code] ASCII ESC BEL n1 n2 Hex. 1B 07 n1 n2 Decimal 27 7 n1 n2 [Defined Area] 1≤n1≤127 1≤n2≤127 [Initial Value] n1 = 20 (Energizing time: 200 msec) n2 = 20 (Delay time: 200 msec) [Function] Sets the energizing and delay times for drive of the external device. • Energizing time = 10 x n1 (ms) • Delay time = 10 x n2 (ms) 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-45 

|**BEL**|||
|---|---|---|
|[Name]|External device 1 drive instruction|External device 1 drive instruction|
|[Code]|ASCII|BEL|
||Hex.|07|
||Decimal|Decimal<br>7|
|[Defined Area]||- - -|
|[Initial Value]||- - -|
|[Function]|[Function]|Executes the external device drive conditions set according to the command to set the external|
|||drive device pulse width (ESC BEL n1 n2).|
|||As with other commands, it temporarily stores data in the data buffer, then executes in the order|
|||received.|
|||External device 1 and external device 2 cannot be executed simultaneously.|



|**FS**|||
|---|---|---|
|[Name]|External device 1 drive instruction|External device 1 drive instruction|
|[Code]|ASCII|FS|
||Hex.|1C|
||Decimal|Decimal<br>28|
|[Defined Area]||- - -|
|[Initial Value]||- - -|
|[Function]|[Function]|Executes the external device drive conditions set according to the command to set the external|
|||drive device pulse width (ESC BEL n1 n2).|
|||As with other commands, it temporarily stores data in the data buffer, then executes in the order|
|||received.|
|||External device 1 and external device 2 cannot be executed simultaneously.|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-46 

## **SUB** 

[Name] External device 2 drive instruction [Code] ASCII SUB Hex. 1A Decimal 26 [Defined Area] - - - [Initial Value] - - - [Function] Drives external device 2. The energizing time and delay time for the external device 2 are fixed at 200 ms each. As with other commands, it temporarily stores data in the data buffer, then executes in the order received. External device 1 and external device 2 cannot be executed simultaneously. 

**EM** [Name] External device 2 drive instruction [Code] ASCII EM Hex. 19 Decimal 25 [Defined Area] - - - [Initial Value] - - - [Function] Drives external device 2. The energizing time and delay time for the external device 2 are fixed at 200 ms each. As with other commands, it temporarily stores data in the data buffer, then executes in the order received. External device 1 and external device 2 cannot be executed simultaneously. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-47 

## **ESC GS BEL m t1 t2** 

|[Name]|Ring buzzer|Ring buzzer||||||
|---|---|---|---|---|---|---|---|
|[Code]|ASCII|ESC|GS BEL||m|t1|t2|
||Hex.|1B|1D|07|m|t1|t2|
||Decimal|27|29|7|m|t1|t2|
|[Defined Area]||1≤<br>m≤<br>2, 49≤<br>m≤<br>50 (”1”≤<br>m≤<br>“2”)||||||
|||1≤<br>t1≤<br>255|255|||||
|||1≤<br>t2≤<br>255|255|||||
|[Initial Value]||- - -||||||
|[Function]|[Function]|Rings the buzzer.|Rings the buzzer.|||||
|||m specifies the drive terminal of the buzzer.|||m specifies the drive terminal of the buzzer.|||



|m|Buzzer DriveTerminal|
|---|---|
|1, 49|Buzzer Drive Terminal 1|
|2, 50|Buzzer DriveTerminal 2|



t1 specifies energizing time; t2 specifies the delay time. 

• Energizing time = 20 msec x t1 

• Delay time = 20 msec x t2 The buzzer will not ring while printing. Use of this command other than for ringing the buzzer is prohibited. (There is the possibility of damage if using this command for driving the drawer on models that support external device terminals.) 

ON Drive Pulse OFF 20 × t1 (msec) 20 × t2 (msec) (Energizing Time) (Delay Time) Print Operation Lo Printing and Paper Feed Prohibited 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-48 

**ESC GS EM DC1 m n1 n2** 

|[Name]|External buzzer drive pulse condition settings|External buzzer drive pulse condition settings|External buzzer drive pulse condition settings|External buzzer drive pulse condition settings||
|---|---|---|---|---|---|
|[Code]|ASCII|ESC GS EM DC1|m|n1|n2|
||Hex.|1B<br>1D<br>19<br>11|m|n1|n2|
||Decimal|Decimal<br>27<br>29<br>25<br>17|m|n1|n2|
|[Defined Area]||1≤<br> m≤<br> 2<br>49≤<br>|m≤<br>|50||
|||0≤<br> n1≤<br> 255||||
|||0≤<br> n2≤<br> 255||||
|[Initial Value]||n1=0<br>n2=0||||
|[Function]||Sets external buzzer derive pulse condition.||||
|||m specifies the buzzer drive terminal toperform the condition settings.||||
||m|Buzzer DriveTerminal||||
||1, 49|Buzzer Drive Terminal 1||||
||2, 50|Buzzer DriveTerminal 2||||



n1 specifies the energizing time; n2 specifies the delay time. 

- Energizing time: =20msec x n1 

- Delay time: =20msec x n2 

Drives for external buzzers set using this command is performed by <ESC> <GS> <EM> <DC2> m n1 n2. The setting value is not initialized by <ESC> “@” and <CAN>. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-49 

**ESC GS EM DC2 m n1 n2** 

|[Name]|External buzzer drive execution|External buzzer drive execution|||||
|---|---|---|---|---|---|---|
|[Code]|ASCII|ESC GS EM DC2|m|n1|n2||
||Hex.|1B<br>1D<br>19<br>12|m|n1|n2||
||Decimal|Decimal<br>27<br>29<br>25<br>18|m|n1|n2||
|[Defined Area]||1≤<br> m≤<br> 2<br>49≤<br>|m≤<br>|50|||
|||1≤<br> n1≤<br> 20|||||
|||n2=0|||||
|[Initial Value]||---|||||
|[Function]||Repeatedly drives the buzzer according to the ON/OFF conditions set by the external buzzer drive|||||
|||pulse conditions command <ESC> <GS> <EM> <DC1> m t1 t2.|||pulse conditions command <ESC> <GS> <EM> <DC1> m t1 t2.||
|||m specifies the buzzer drive terminal to drive.|||||
||m|Buzzer DriveTerminal|||||
||1,49|Buzzer DriveTerminal 1|||||
||2, 50|Buzzer DriveTerminal 2|||||



Specifies the number of repetitions of the buzzer drive with (n2 x 256 + n1). The buzzer will not ring while printing. 

This command is prohibited for uses other than to ring the buzzer. 

(If this command is used to drive the cash drawer on models that have an external device terminal, the system will be damaged. Absolutely never use it for other purposes.) 

The buzzer can be stopped by pressing the paper feed switch or opening the cover when it is ringing. 

Example: 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-50 

## **3.3.13. Prin t Settings** 

## **ESC RS d n** 

[Name] Set print density [Code] ASCII ESC RS d n Hex. 1B 1E 64 n Decimal 27 30 100 n 

[Defined Area] 0≤n≤ 6 48≤n≤57 (”0”≤n≤”6”) [Initial Value] Memory switch setting [Function] Sets print density. This command executes after stopping the printing operation. When in 2-color mode, only print density for red printing can be set by this command. When in low peak current mode, print density using this command is invalid. 

## Spec. A. 

|[Function]<br>Spec. A.pec. A.ec. A.|Sets print density.<br>This command executes after stopping the printing operation.<br>When in 2-color mode, only print density for red printing can be set by this command.<br>When in low peak current mode, print density using this command is invalid.|
|---|---|
|n|Print Density<br>Single Color Printing Mode<br>Two Color Printing Mode  Red Print Density<br>Double Resolution Mode<br>(*) Installed print mode depends on the<br>model.|
|0,48|Print density1.3<br>Print density1.2|
|1, 49<br>~~a~~|Print density 1.2<br>Print density 1.2<br>~~a~~|
|2, 50|Print density1.1<br>Print density1.0|
|3, 51<br>~~a~~|Print density1.0<br>Print density1.0<br>~~a~~|
|4, 52|Print density 0.9<br>Print density1.0|
|5, 53<br>~~a~~|Print density 0.8<br>Print density 0.8<br>~~a~~|
|6, 54|Print density 0.7<br>Print density 0.8|



Spec. B. 

|Spec. B.pec. B.ec. B.||
|---|---|
|n|Print Density<br>Single Color Printing Mode<br>2-color Printing Mode  Red Print Density<br>Double Resolution Mode<br>*1|
|0, 48<br>~~a~~|Print density+3<br>Print density+1<br>~~a~~|
|1,49<br>~~|~~|Print density+ 2<br>Print density+ 1<br>~~|~~|
|2, 50|Print density+ 1<br>Standard print density (Standard)|
|3, 51<br>~~a~~|Standard print density (Standard)<br>Standard print density (Standard)<br>~~a~~|
|4, 52|Print density- 1<br>Standard print density (Standard)|
|5, 53<br>~~A~~|Print density- 2<br>Print density-1<br>~~A~~|
|6, 54<br>~~A~~|Print density-3<br>Print density- 1<br>~~A~~|



*1) See the appropriate printer specifications manual for details on the print modes that are available. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-51 

## **ESC RS r n** 

[Name] Set print speed [Code] ASCII ESC RS r n Hex. 1B 1E 72 n Decimal 27 30 114 n 

[Defined Area] 0≤n≤3 48≤n≤51 (”0”≤n≤”3”) [Initial Value] Memory switch setting [Function] Sets print speed. This command stops printing to be executed. 

Because two-color print mode, low peak current mode, and double resolution mode print in one speed, the speed settings with this command are invalid. 

This command setting becomes valid when returned from the two-color print mode, low peak current mode, and double resolution mode to the single color print mode. Invalid in page mode. 

Spec. A 

**==> picture [411 x 117] intentionally omitted <==**

**----- Start of picture text -----**<br>
|||||||
|---|---|---|---|---|---|
|n|Print Speed|
|Single Color Printing Mode|Two Color Printing Mode|
|Low Peak Current Mode|
|Double Resolution|
|(*) Installed print mode depends on the|
|model.|
|a|0, 48|High speed|Each print mode speed|
|a|1, 49|Mid-speed|Each print mode|speed|
|a|2,|50|Slow speed|Each print mode|speed|
|3, 51|Option-speed|Each print mode speed|
|(*) Print|speed|depends|on the model.|

**----- End of picture text -----**<br>


## Spec. B 

**==> picture [411 x 110] intentionally omitted <==**

**----- Start of picture text -----**<br>
|||||||
|---|---|---|---|---|---|
|n|Print Speed|
|Single Color Printing Mode|Two Color Printing Mode|
|Low Peak Current Mode|
|Double Resolution|
|(*) Installed print mode depends on the|
|model.|
|0, 48|Standard|Each print mode speed|
|a|1, 49|Mid-speed|Each print mode|speed|
|a|2,|50|Slow speed|Each print mode|speed|
|3,|51|High speed|Each print mode|speed|
|Rs|

**----- End of picture text -----**<br>


――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-52 

## **3.3.14. Statu s** 

## **ESC RS a n** 

[Name] Set status transmission conditions [Code] ASCII ESC RS a n Hex. 1B 1E 61 n Decimal 27 30 97 n [Defined Area] For Specifications A and B 0≤n≤3, 48≤n≤51(”0”≤n≤”3”) For Specification C 0≤n≤3, 48≤n≤51(”0”≤n≤”3”) [Initial Value] Set by DIP switches and memory switches. [Function] Sets the status transmission conditions. See Appendix 2 for details regarding ASB status. Settings of this command are unaffected by the ESC @ command. 

See each printer's product specifications manual for details on the DIP SW and memory switch settings. When the printer uses a wireless LAN I/F, this command is ignored. Specification A 

|n|Status transmissionconditions|
|---|---|
|0, 48|ASB invalid|
|1,49|ASB valid|



Specification B 

||n|Status transmissionconditionsettings|
|---|---|---|
|0, 48|0, 48|ASB invalid|
|1,4|49|ASB valid|



Specification C. 

|n|Status transmission conditions|
|---|---|
|0,48|ASB Invalid•   NSB Invalid|
|1,49|ASB Valid•   NSB Invalid|
|2, 50|ASB Invalid•   NSB Valid|
|3, 51|ASB Valid•   NSB Valid|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-53 

|**ESC ACK SOH**|**ESC ACK SOH**|**ESC ACK SOH**||
|---|---|---|---|
|[Name]|Real-time printer status (ASB status)||Real-time printer status (ASB status)|
|[Code]|ASCII|ESC|ESC<br>ACK SOH|
||Hex.|1B|1B<br>06<br>01|
||Decimal|27|27<br>6<br>1|
|[Defined Area]||- - -||
|[Initial Value]||- - -||
|[Function]|[Function]|Sends ASB status information to the host.|Sends ASB status information to the host.|
|||This command is not used when ASB is valid.||
|||See Appendix 2, Automatic Status for details regarding ASB status.||



## **ENQ** 

|**ENQ**|||
|---|---|---|
|[Name]|Real-time printer status  (1)|Real-time printer status  (1)|
|[Code]|ASCII|ENQ|
||Hex.|05|
||Decimal|5|
|[Defined Area]||- - -|
|[Initial Value]||- - -|
|[Function]|[Function]|Sends 1 byte of the following the printer status|
|||This command is not used when ASB is valid.|
|||See Appendix 2, ENQ Command Status for details regarding status.|
|**EOT**|||
|[Name]|Real-time printer status  (2)|Real-time printer status  (2)|
|[Code]|ASCII|EOT|
||Hex.|04|
||Decimal|4|
|[Defined Area]||- - -|
|[Initial Value]||- - -|
|[Function]|[Function]|Sends 1 byte of the following the printer status|
|||This command is not used when ASB is valid.|
|||See Appendix 2, EOT Command Status for details regarding status.|



## **ESC ACK CAN** 

[Name] Execute real-time printer reset [Code] ASCII ESC ACK CAN Hexadecimal 1B 06 18 Decimal 27 6 24 [Defined Area] --[Initial Value] --[Function] Execute real-time printer reset. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-54 

|**ETB**|||
|---|---|---|
|[Name]|Update ASB ETB status||
|[Code]|ASCII|ETB|
||Hex.|17|
||Decimal|23|
|[Defined Area]||- - -|
|[Initial Value]||- - -|
|[Function]|[Function]|Spec. Aifications|
|||Sets the ASB ETB status when reading this command from the reception buffer, then sends ASB.|
|||See Appendix 2, ASB Status for details.|
|||Spec. Bifications|
|||Sets the ASB ETB status when reading this command from the reception buffer.  Then, after|
|||updating the ASB ETB counter, sends the ASB status.|
|||See Appendix 2, ASB Status for details.|
|||The following outlines the details of processes in this command.|
|||(1) Reads ETB command from reception buffer.|
|||(2) Waits for printing of the print data before the ETB command to end.|
|||(3) Increments the ASB ETB counter by 1 after checking that printing has ended, then sets the ASB|
|||ETB status.|
|||(4) Sends ASB (only when ASB is enabled).|
||• Precautions when using Ethernet||
|||When multi-session is valid the ASB (ETB counter) sent by <ETB> is sent to all hosts that are|
|||connected.|
|||For that reason, sending ETB from multiple sessions, can cause mis-recognition of the ETB|
|||counter.|
|||Therefore, we recommend the <ESC><GS><ETX> commands to confirm the print end counter.|
|||See the Command List by Model.|



**ESC RS E n** [Name] Initialize ASB ETB counter and ETB status [Code] ASCII ESC RS E n Hex. 1B 1E 45 n Decimal 27 30 69 n 

[Defined Area] n = 0 n = 48 (“0”) [Initial Value] ASB ETB counter = 0 [Function] Clears the ASB ETB counter to zero, then clears the ETB status. However, ASB status is not send when clearing the ETB counter to zero using this command.  The ETB counter and ETB status are initialized by the following command, not this command. • Cancel print data and initialize command <CAN> 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-55 

**ESC GS ETX s n1 n2** 

[Name] Send print-end counter, initialize [Code] ASCII ESC GS ETX s n1 n2 Hexadecimal 1B 1D 03 s n1 n2 Decimal 27 30 3 s n1 n2 [Defined Area] 0 ≤ s ≤ 4 0 ≤ n1 ≤ 255, 0 ≤ n2 ≤ 255 

[Function] This command is run when reading from the reception buffer. Processes the print end counter according to the s parameter. 

|s|Name|Function|
|---|---|---|
|0|Print end counter reference|Sends the current print end counter to the host.<br>(Does not wait for print end. Does not count up.)|
|1|Print end counter update|Runs the following operations.<br>(1) Prints data in line buffer, if data exists.<br>(2) Waits until printing ends (motor stops).<br>(3) Updates the print end counter (increments by 1).<br>(4) Sends print end counter to host.|
|2|Print end counter clear|Returns the print end counter to its default value (zero clear).<br>(Does not wait for print end. Does not send the print end counter to<br>thehost.|
|3|Start document<br>n1, n2 = 0|(1) Sets data intake mode<br>(2) Initialize|
|4|End document<br>n1, n2 = 0|(1) Prints data in line buffer, if data exists.<br>(2) Waits until printing ends (motor stops).<br>(3) Cancels data intake mode|



The data formats sent to the host when s = 0 or s =1 are shown below. 

|<Returned Data Formats>|<Returned Data Formats>|<Returned Data Formats>||||||||
|---|---|---|---|---|---|---|---|---|---|
|[Code]|ASCII|ESC GS|ESC GS|ETX|s|n1|n2|[Print end counter] NUL|[Print end counter] NUL|
||Hexadecima<br>l|1B|1D|03|s|n1|n2|[Print end counter]|00<br>[Print end counter]|
||Decimal|27|30|3|s|n1|n2|[Print end counter]|[Print end counter]<br>0|



* Echoes back the specified contents from the host as is until ESC GS ETX s n1 n2, and then sends the print end counter value and NUL. 

When [Print end counter] is 1 byte in length, the initial value is 0x00. When s = 1, increments by 1 each time the command is processed. After 0xFF, returns to 0x00. There is one [Print end counter] in the printer that is unrelated to the n1, n2 values. (There is no counter for the n1, n2 values.) 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-56 

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

## Restrictions 

1) Sleep mode decrease 

- 2) Invalid when in Page mode 

When s = 3, initialize the following settings using the initializing process. 

- Set slash zero 

- Set specify/cancel external character (external register character data is retained) 

- Page length 

- Current position (move to top of page, top of line) 

- Horizontal tab/Vertical tab 

- Set upside-down, position alignment 

- Left/right margins 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-58 

## **3.3.15. Kanji characters** 

**ESC p** [Name] Specify JIS Kanji character mode [Code] ASCII ESC p Hex. 1B 70 Decimal 27 112 [Defined Area] - - - [Initial Value] JIS Kanji character mode cancelled [Function] Specifies JIS Kanji character mode When in JIS Kanji character mode, character codes are all handled as 2 byte Kanji characters (First byte: upper code; second byte: lower code). This command is ignored for models not equipped with Japanese and Kanji characters and when the specification for the location of use is specified as SBCS (single byte countries) by the memory switch.  In such a case, this is handled as the ANK font 14 dot pitch specification command. 

## **ESC q** 

[Name] Cancel JIS Kanji character mode [Code] ASCII ESC q Hex. 1B 71 Decimal 27 113 [Defined Area] - - - [Initial Value] JIS Kanji character mode cancelled [Function] Cancel JIS Kanji character mode 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-59 

## **ESC $ n** 

[Name] Specify/cancel Shift JIS Kanji character mode [Code] ASCII ESC $ n Hex. 1B 24 n Decimal 27 36 n 

[Defined Area] - - - [Initial Value] Memory switch setting [Function] Specifies and cancels the shift JIS Kanji character mode. When in shift JIS Kanji character mode, character codes are all handled as 2 byte Kanji characters (First byte: upper code; second byte: lower code). 

This command is ignored for models not equipped with Japanese and Kanji characters and when the specification for the location of use is specified as SBCS (single byte countries) by the memory switch. 

||n|Shift JISKanjicharacter mode|
|---|---|---|
|0, 48|0, 48|Cancels shift JIS Kanji character mode|
|1,4|49|Specifies shift JISKanjicharacter mode|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-60 

## **ESC s n1 n2** 

[Name] Set 2 byte Kanji character left/right spaces [Code] ASCII ESC s n1 n2 Hex. 1B 73 n1 n2 Decimal 27 115 n1 n2 [Defined Area] 0≤n1≤7 48≤n1≤55 (”0”≤n1≤”7”) 0≤n2≤15 48≤n2≤57 (”0”≤n2≤”9”) 65≤n2≤70 (”A”≤n2≤”F”) [Initial Value] Memory switch setting [Function] Adds n1 dots left space amount and n2 dots right space amount to Kanji characters. The Kanji character width is "left space amount” + "Kanji font dot count” + "right space amount.” (See the information on character specifications in the appropriate printer specifications manual for details on the Kanji font dot count.) This command is ignored for models not equipped with Chinese fonts (for overseas) and when the specification for the location of use is specified as SBCS (single byte countries) by the memory switch. Standard mode and page mode can be set independently of each other. 

|**ESC t n1 n2**|**ESC t n1 n2**|**ESC t n1 n2**|
|---|---|---|
|[Name]|Set 1 byte Kanji character left/right spaces||
|[Code]|ASCII|ESC<br>t<br>n1<br>n2|
||Hex.|1B<br>74<br>n1<br>n2|
||Decimal|27 116<br>n1<br>n2|
|[Defined Area]||0≤<br>n1≤<br>7|
|||48≤<br>n1≤<br>55 (”0”≤<br>n1≤<br>”7”)|
|||0≤<br>n2≤<br>15|
|||48≤<br>n2≤<br>57 (”0”≤<br>n2≤<br>”9”)|
|||65≤<br>n2≤<br>70 (”A”≤<br>n2≤<br>”F”)|
|[Initial Value]||Memory switch setting|
|[Function]|[Function]|Adds n1 dots left space amount and n2 dots right space amount to single-byte Kanji characters.|
|||The single-byte Kanji character width is "left space amount” + "single-byte Kanji font dot count” +|
|||"right space amount.”|
|||(See the information on character specifications in the appropriate printer specifications manual|
|||for details on the single-byte Kanji font dot count.)|
|||This command is ignored for models not equipped with Chinese fonts (for overseas) and when the|
|||specification for the location of use is specified as SBCS (single byte countries) by the memory|
|||switch.|
|||Standard mode and page mode can be set independently of each other.|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-61 

## **ESC r c1 c2 d1...dk** 

[Name] Register Chinese download characters [Code] ASCII ESC r c1 c2 d1 ... dk Hex. 1B 72 c1 c2 d1 ... dk Decimal 27 114 c1 c2 d1 ... dk 

[Defined Area] 0≤d≤255 k=72 

c1 and c2 differ according to specifications and code type (see table below). [Initial Value] All spaces 

[Function] Registers Chinese download characters to c1 and c2 addresses. 

Those already registered to these addresses are overwritten.  If c1 and c2 are outside of the defined are or the printer is model not equipped with Chinese fonts (for overseas) and when the specification for the location of use is specified as SBCS (single byte countries) by the memory switch, the printer discards up to d1 and dk. 

This command exists in models that have the specifications of A and B below.  (See the “Special Appendix, Command Table per Model” for details.) 

Specification A 

|Specification<br>c1<br>c2<br>Registrationcount|
|---|
|Japanese char./JIS type<br>c1=77h<br>30h≤<br>c2≤<br>4Fh<br>32characters|
|Specification B|
|Specification<br>c1<br>c2<br>Registrationcount<br>~~RQ~~|
|Japanese char./JIS type<br>c1=77h<br>21h≤<br>c2≤<br>7Eh<br>94characters<br>Japanese char./Shift JIS type<br>c1=ECh<br>40h≤<br>c2≤<br>7Eh<br>80h≤<br>c2≤<br>9Eh<br>94 characters<br>Kanjicharacters<br>c1=FEh<br>A1h≤<br>c2≤<br>FEh<br>94characters<br>~~es~~<br>~~ee~~<br>~~RG~~|



- (*) The registration region is the same for Japanese characters in JIS or shift JIS. 

||<)||||||Horizontal<br>24 Dots|Horizontal<br>24 Dots|Horizontal<br>ee|Horizontal<br>ee|Horizontal<br>ee|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Vertical<br>24 Dots|d1 ●<br>●<br>d4 ●<br>●<br>d7 ●<br>●<br>d10 ●<br>●<br>d13 ●<br>●<br>d16 ●<br>●<br>d19 ●<br>●<br>d22 ●<br>●<br>d25 ●<br>●<br>d28 ●<br>●<br>d31 ●<br>●<br>d34 ●<br>●<br>d37 ●<br>●<br>d40 ●<br>●<br>d43 ●<br>●<br>d46 ●<br>●<br>d49 ●<br>●<br>d52 ●<br>●<br>d55 ●<br>●<br>d58 ●<br>●<br>d61 ●<br>●<br>d64 ●<br>●<br>d67 ●<br>●<br>d70 ●<br>●<br>bit7 bit6 <br>~~fT~~<br>~~|~~<br>~~| |~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~P|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>|<br>|<br>~~|~~ ~~**|**~~<br>~~**|**~~<br>~~|~~<br>~~P|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~P|~~<br>~~|~~<br>~~|~~ ~~|~~<br>~~|~~<br>~~| ~~|<br>|<br>~~|~~ ~~**|**~~<br>~~**|**~~<br>~~|~~<br>~~P|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>|<br>|<br>~~|~~ ~~**|**~~<br>~~**|**~~<br>~~|~~<br>~~P|~~<br>~~|~~<br>~~|~~ ~~tT~~<br>~~|~~|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br> bit5 Bit4 bit3 bit2 bit1<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>|<br>~~**|**~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>|<br>~~**|**~~<br>~~|~~<br>~~|~~<br>|<br>~~**|**~~<br>~~|~~<br>~~|~~||●<br>●<br>●<br>●<br>●<br>d2<br>●<br>●<br>●<br>●<br>●<br>d5<br>●<br>●<br>●<br>●<br>●<br>d8<br>●<br>●<br>●<br>●<br>●<br>d11<br>●<br>●<br>●<br>●<br>●<br>d14 <br>●<br>●<br>●<br>●<br>●<br>d17 <br>●<br>●<br>●<br>●<br>●<br>d20 <br>●<br>●<br>●<br>●<br>●<br>d23 <br>●<br>●<br>●<br>●<br>●<br>d26 <br>●<br>●<br>●<br>●<br>●<br>d29 <br>●<br>●<br>●<br>●<br>●<br>d32 <br>●<br>●<br>●<br>●<br>●<br>d35 <br>●<br>●<br>●<br>●<br>●<br>d38 <br>●<br>●<br>●<br>●<br>●<br>d41 <br>●<br>●<br>●<br>●<br>●<br>d44 <br>●<br>●<br>●<br>●<br>●<br>d47 <br>●<br>●<br>●<br>●<br>●<br>d50 <br>●<br>●<br>●<br>●<br>●<br>d53 <br>●<br>●<br>●<br>●<br>●<br>d56 <br>●<br>●<br>●<br>●<br>●<br>d59 <br>●<br>●<br>●<br>●<br>●<br>d62 <br>●<br>●<br>●<br>●<br>●<br>d65 <br>●<br>●<br>●<br>●<br>●<br>d68 <br>●<br>●<br>●<br>●<br>●<br>d71 <br>bit5 Bit4 bit3 bit2 bit1 bit0<br>~~tT~~<br>~~tT~~<br>~~|~~<br>~~tT] ~~<br>~~|~~<br>~~|~~<br>|<br>~~tT~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~ttPty)~~<br>~~|~~<br>~~|~~<br>~~| |} ~~<br>|<br>~~fT~~<br>| ~~Ty} ~~<br>~~**|**~~<br>~~|~~<br>~~| hth~~~~**}** ~~<br>~~[|~~<br>~~|~~<br>~~ft~~<br>~~tT~~<br>~~tTPty}~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|}~~<br>~~ttPty)~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~tT~~<br>~~| ~~<br>|<br>[|<br>|<br>ft<br>}<br>~~**|**~~<br>~~**|**~~<br>~~| hth} ~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~ttPty)~~<br>~~|~~<br>~~|~~<br>~~| |} ~~<br>|<br>~~fT~~<br>| ~~Ty} ~~<br>~~**|**~~<br>~~|~~<br>~~| hth~~~~**}** ~~<br>~~[|~~<br>~~|~~<br>~~ft~~<br>~~tT~~<br>~~tTPty}~~<br>~~Tt~~<br>~~tT PT hr~~} hv~~ET~~|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>d3<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>d6<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>d9<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d12 ●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d15 ●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d18●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d21 ●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d24 ●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d27 ●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d30●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d33 ●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d36●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d39●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d42 ●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d45●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d48●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d51 ●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d54 ●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d57 ●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d60 ●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d63●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d66●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d69 ●<br>●<br>●<br>●<br>●<br>●<br> ●<br>●<br>●<br>●<br>●<br>●<br>●<br>●d72 ●<br>●<br>●<br>●<br>●<br>●<br>bit7 bit6 bit5 bit4 bit3 bit2 bit1 bit0<br>bit7 bit6 bit5 bit4 bit3 bit2 <br> ~~Et~~<br>~~fT~~<br>~~tT fT ft ft~~<br>~~ft ft~~<br>~~tT fT ft yt fT~~<br>~~ET tT~~<br>~~Tr EE~~<br>~~Et~~<br>~~tT~~<br>~~tT~~<br>~~|~~<br>~~tT ft ft tr~~<br>~~Th~~<br>~~hr~~<br>~~Ef~~<br>~~tT eT Tr~~<br>~~TT~~<br>~~Ef~~<br>~~tT~~<br>~~tT~~<br>~~|~~<br>~~yt ft~~<br>~~ft tt~~<br>~~Ef tT et tT th TT hr TT~~<br> ~~Ef ft~~<br>~~tT ty tT et tt re~~<br> ~~Ef~~ ft<br>tT ~~ft~~ yt et ~~Tt rT~~<br>~~hr~~<br> ~~**Ef** tT PT TT~~<br>~~tT~~<br>~~tT~~<br>~~|~~<br>~~tT ft~~<br>~~ft ft~~<br>~~**Ef** tT pt tT ~~~~**t**T Th~~<br>~~ft~~<br>~~tT~~<br>~~ty~~<br>~~T~~<br>~~et tt re~~<br>~~Ef~~ ~~tT~~ et ~~tT th TT~~ ~~hr TT~~<br> ~~ET tT Tr EE~~<br>~~Ef~~<br>tT tT<br>|<br>~~tT~~ ~~ft~~ ~~ft~~ ~~ft~~<br> ~~**Ef** tT PT TT~~<br>~~tT~~<br>~~tT~~<br>~~|~~<br>~~yt ft~~<br>~~ft tt~~<br>~~Ef tT et tT th TT hr TT~~<br> ~~Ef ft~~<br>~~tT ty tT et tt re~~<br> ~~Ef~~ ft<br>tT ~~ft~~ yt et ~~Tt rT~~<br>~~hr~~<br> ~~**Ef** tT PT TT~~<br>~~tT~~<br>~~tT~~<br>~~|~~<br>~~tT ft~~<br>~~ft ft~~<br>~~Ef~~ ~~tT~~ pt ~~tT tT Th~~<br>~~ET~~<br>~~tT PE tT ht hE hE ht hE hE hE hE rT rT~~|||||●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br> bit1|●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br>●<br> bit0|
||●: Font data/○: Invalid data||●: Font data/○: Invalid data|||||||||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-62 

## **3.3.16. Oth ers** 

|**CAN**|||
|---|---|---|
|[Name]|Cancel print data and initialize commands||
|[Code]|ASCII|CAN|
||Hex.|18|
||Decimal|24|
|[Defined Area]||- - -|
|[Initial Value]||- - -|
|[Function]|[Function]|When the reception buffer and line buffer are cleared, the set commands are initialized.|
|||Immediately executed not when taking out from the reception buffer, but when received from the|
|||host.|
|||DIPSW re-reading is not performed.|
|||The following shows the specifications that are not initialized by this command.|
|||• Set print density|
|||• Set print speed|
|||• Set 2 color print mode|
|||• Print color in 2 color print mode|
|||• External device drive condition|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-63 

**ESC @** [Name] Command initialization [Code] ASCII ESC @ Hex. 1B 40 Decimal 27 64 

[Defined Area] - - - [Initial Value] - - - [Function] Initializes each command after printing data in the line buffer. However, printers with memory switch settings are initialized to the memory switch settings. DIPSW re-reading is not performed. • ANK characters, Kanji character adornment, expansion • Kanji character mode • ANK right space • Kanji character left/right spaces • Character pitch • International characters • Code page • Set slash zero • Set specify/cancel external character (external register character data is retained) • Page length • Current position (move to top of page, top of line) • Horizontal tab/Vertical tab • Line feed amount • Set upside-down, position alignment • Left/right margins The following shows the specifications that are not initialized by this command. • Set print density 

- Set print speed 

- Set 2 color print mode 

- Print color in 2 color print mode 

- External device drive condition 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-64 

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

## **ESC ? LF NUL** 

[Name] Reset printer (execute self print) [Code] ASCII ESC ? LF NUL Hex. 1B 3F 0A 00 Decimal 27 63 10 0 [Defined Area] - - - [Initial Value] - - - [Function] Hardware resets the printer and executes on self print. 

After sending this command, the next data is not sent until the printer is online (in a state wherein it can receive data). 

When resetting the printer, the following processes are performed. 

|I/F<br>~~a ~~|Mode<br> ~~SC~~|Process<br>~~SC~~|
|---|---|---|
|Parallel<br>~~sss~~<br>~~ee~~|- - -<br>~~sss~~<br>~~a~~<br>|BUSY output<br>~~sss~~<br>|
|RS-232C<br>~~ee~~|DTR mode<br>~~a~~<br>~~T,__H~~|DTR mark output<br>~~T,__H~~|
||Xon/Xoff mode<br>~~a~~<br>~~T,__H~~|Xoffoutput<br>~~T,__H~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-66 

**ESC GS + m [t1 nL1 nH1 d11 d12 … d1k] 1 [t2 nL2 nH2 d21 d22 … d2k] 2  [tm nLm nHm dm1 dm2 … dmk] m** 

[Name] Register macro 

[Code] ASCII ESC GS + m t1 nL1 nH1 d11 d12 .. d1k Hex. 1B 1D 2B m t1 nL1 nH1 d11 d12 .. d1k Decimal 27 29 43 m t1 nL1 nH1 d11 d12 .. d1k [Code] ASCII t2 nL2 nH2 d21 d22 .. d2k .. tm nLm nHm dm1 dm2 .. dmk .. Hex. t2 nL2 nH2 d21 d22 .. d2k .. tm nLm nHm dm1 dm2 .. dmk .. Decimal t2 nL2 nH2 d21 d22 .. d2k .. tm nLm nHm dm1 dm2 .. dmk .. [Defined Area] 1 ≤ m ≤ 9,  0 ≤ t ≤ 8 k = (nL + nH x 256), 0 ≤ k ≤ 7936 0 ≤ d ≤ 255 

[Initial Value] - - - [Function] This command registers macro data in the following macro registration regions. 

|Registration<br>Region|Registration<br>DataType|Registration<br>Block No.|Size (Bytes)|Details|
|---|---|---|---|---|
|Registration<br>Information|Initialization<br>Macro|0|2|Registration data type 0 x 0000 =<br>Initialization macro, 0xffff=No reg. data|
||||2|Registration data count|
||||4|Registration data address|
||||8|(Reserved)|
||Macro|1|2|Registration data type 0 x 0001 to 0x 0008<br>=macro, 0xffff=No reg. data|
||||2|Registration data count|
||||4|Registrationdata address|
||||8|(Reserved)|
|||**:**|||
|||8|2|Registration data type 0 x 0001 to 0 x<br>0008= macro, 0xffff = Noreg.data|
||||2|Registration data count|
||||4|Registration data address|
||||8|(Reserved)|
|Registration<br>Data|||7936|Registration Data|



- m specifies the registration black count. 

- t specifies the registration data type. 

||t||Registration Data Type|
|---|---|---|---|
||0||Initialization Macro|
|1 to 8|1 to 8|1 to 8|Macro(t is the macro number.)|



- (nL + nH x 256) specifies the data count to be registered. When (nL + nH x 256) = 0, the macro data specified by t is deleted. 

- d is the macro data to be registered. 

- After the macro data is written to the non-volatile memory, the printer is reset. 

- If the volume of all macros exceeds the capacity for registration, it is written to the non-volatile memory up to the data block that exceed the capacity and the command analysis is ended after that. 

- If there is unprinted data in the line buffer, this command is executed after the print data in the line buffer is printed. 

- When registering, all of the current macro regions are cleared, so if previous macro data is necessary, rewrite it. 

- When performing a Hex Dump, initialization macro region data is added in the same way as the current specifications. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-67 

## **3.4. Raster Graphics Command Details** 

Raster graphics are command types and incidental specifications that enable high speed and high quality printing of graphics. 

The following shows the characteristics and specifications for raster graphics. 

- Defines the raster mode command as the STAR line mode extension set. 

Basically no restrictions set in use of conventional STAR line mode. 

STAR Page Mode cannot be used. 

- Handles high speed data transmission 

When using IEEE 1284, data transmission rate of 80 to 100 KB /sec ensured. 

- Handles IEEE 1284, USB and Ethernet I/F (RS-232C not applicable) 

- Handles both fixed length/variable length mode 

- Print speed selectable 

- Post printing cut operation selectable 

- All settings possible by Raster commands. Most settings are possible without DIPSW/memory switch settings. 

- Supports printer driver handling raster mode 

The following shows the raster command details. 

Note that if not specifically noted, the following commands are effective only in raster mode and the commands are ignored (4 bytes ignored) when other than the raster mode.  The raster image buffer in the command details described below indicate the raster dedicated image buffer, the length thereof (vertical direction dot count) differing between models. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-68 

**ESC * r R** [Name] Initialize raster mode [Code] ASCII ESC *     r R Hex. 1B 2A 72 52 Decimal 27 42 114 82 [Defined Area] - - - [Initial Value] - - - [Function] Initializes raster mode. This command is also effective when not in the raster mode. However, initialization of the raster mode with this command is executed when entering the raster mode. The following settings are initialized using this command. 

• Raster page length setting (ESC * r P n NUL) 

• Raster print quality setting (ESC * Q n NUL) • Raster print color setting (ESC * r K n NUL) • Raster left margin setting (ESC * r m l n NUL) • Raster right margin setting (ESC * r m r n NUL) • Raster EOT mode setting (ESC FF EOT) • Raster FF mode setting (ESC FF NUL) • Raster image buffer clear Note that when entering the raster mode, it executes the same process as initialization of the raster mode using this command. 

However, because initialization is not performed when entering the raster mode only for the following settings, when initializing the following it sends this initialization command. 

• Raster data print color setting (ESC * r K n NUL) Invalid in page mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-69 

**ESC * r A** [Name] Enter raster mode [Code] ASCII ESC * r A Hex. 1B 2A 72 41 Decimal 27 42 114 65 [Defined Area] - - - [Initial Value] - - - [Function] Enters raster mode. This command is ignored when in the raster mode. The following shows the details regard processing of this command. 

(1) Reception of this command. (2) When using parallel I/F, IEEE 1284 reverse mode is prohibited. (3) All data remaining in the reception buffer and image buffer is printed equivalent to the FF command. (4)  Initialize raster mode 

(5)  Enter raster mode 

When in the raster mode, the raster mode is initialized. The following shows the contents of the initialization. 

- Raster page length setting (ESC * r P n NUL) 

- Raster print quality setting (ESC * Q n NUL) 

- Raster left margin setting (ESC * r m l n NUL) 

- Raster right margin setting (ESC * r m r n NUL) 

- Raster EOT mode setting (ESC FF EOT) 

- Raster FF mode setting (ESC FF NUT) 

- Raster image buffer clear 

(*) Only raster data print color setting is not initialized when entering the raster mode. Invalid in page mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-70 

## **ESC * r B** 

[Name] Quit raster mode [Code] ASCII ESC * r B Hex. 1B 2A 72 42 Decimal 27 42 114 66 

[Defined Area] - - - [Initial Value] - - - [Function] Quits raster mode. 

When quitting the raster mode, if there is raster data remaining in the image buffer of the raster mode, it quits the raster mode after executing the raster EOT mode. 

Note that with this command, IEEE 1284 reverse mode is allowed in parallel I/F and it sets the top of page with the line mode. Invalid in page mode. 

## **ESC * r C** 

[Name] Clear raster data [Code] ASCII ESC * r C Hex. 1B 2A 72 43 Decimal 27 42 114 67 

[Defined Area] - - - [Initial Value] - - - [Function] Clears image buffer data in the raster mode. Invalid in page mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-71 

**ESC * r D n NUL** [Name] Drawer drive [Code] ASCII ESC * r D n NUL Hex. 1B 2A 72 44 n 00 Decimal 27 42 114 68 n 0 

[Defined Area] 0≤n≤3 [Initial Value] n = 0 [Function] Drives the drawer in the raster mode. 

Drawer drive conditions conform to setting command (<ESC> <BEL> n1 n2) of the line mode. n is a decimal description (max. 255 digits) using ASCII characters. 

|n||Drive circuits|
|---|---|---|
|0||None|
|1||Externaldevice drive1drive|
|2||Externaldevice drive2drive|
|3||Externaldevice drive1drive and externaldevice drive2drive|
||Invalid in page mode.||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-72 

**ESC * r E n NUL** [Name] Set raster EOT mode [Code] ASCII ESC * r E n NUL Hex. 1B 2A 72 45 n 00 Decimal 27 42 114 69 n 0 

[Defined Area] n = 0, 1, 2, 3, 8, 9, 12, 13, 36, 37 [Initial Value] Models handling full cut: n = 9 Models connected with a presenter: n = 37 [Function] Sets the raster EOT mode. 

The EOT mode operates to execute using the raster document quit command (ESC FF EOT). n is a decimal description (max. 255 digits) using ASCII characters. Invalid in page mode. 

|n<br>~~a~~<br>~~es~~|FormFeed<br>~~es~~<br>~~eG~~|Cut Feed<br>~~Df~~<br>~~eG~~|Cutter<br>~~Df~~|Presenter|
|---|---|---|---|---|
|0<br>~~a ~~<br>~~es~~<br>~~es~~|SetToDefault<br> ~~es~~<br>~~eG~~<br>~~GG~~|SetToDefault<br>~~Df~~<br>~~eG~~<br>~~GG~~|SetToDefault<br>~~Df~~<br>~~GG~~|SetToDefault<br>~~GG~~|
|1<br>~~es~~<br>~~es~~<br>~~ee~~|○<br>~~eG~~<br>~~GG~~<br>~~ee~~|--<br>~~eG~~<br>~~GG~~<br>~~GG~~|--<br>~~GG~~<br>~~GG~~|--<br>~~GG~~|
|2<br>~~es~~<br>~~ee~~<br>~~Rs~~<br>~~a~~|○<br>~~GG~~<br>~~ee~~<br>~~GD~~|○<br>~~GG~~<br>~~GG~~<br>~~GD~~|--<br>~~GG~~<br>~~GG~~<br>~~GD~~<br>~~QO~~|--<br>~~GG~~<br>~~GD~~|
|3<br>~~ee~~<br>~~Rs~~<br>~~a~~|○<br>~~ee~~<br>~~GD~~|TearBar<br>~~GG~~<br>~~GD~~|--<br>~~GG~~<br>~~GD~~<br>~~QO~~|--<br>~~GD~~|
|8<br>~~Rs~~<br>~~a~~|○<br>~~GD~~|--<br>~~GD~~|FullCut<br>~~GD~~<br>~~QO~~|--<br>~~GD~~|
|9<br>~~a~~<br>~~a eG~~<br>~~es~~|○<br>~~eG~~<br>~~GG~~|○<br>~~eG~~<br>~~GG~~|FullCut<br>~~QO~~<br>~~eG~~<br>~~GG~~|--<br>~~eG~~<br>~~GG~~|
|12<br>~~es~~<br>~~ee~~|○<br>~~GG~~<br>~~ee~~|--<br>~~GG~~<br>~~GG~~|PartialCut<br>~~GG~~<br>~~GG~~|--<br>~~GG~~|
|13<br>~~es~~<br>~~ee~~|○<br>~~GG~~<br>~~ee~~|○<br>~~GG~~<br>~~GG~~|PartialCut<br>~~GG~~<br>~~GG~~|--<br>~~GG~~|
|36<br>~~ee~~<br>~~a~~|○<br>~~ee~~<br>|--<br>~~GG~~<br>|FullCut<br>~~GG~~<br>|Eject<br>|
|37<br>~~GF~~|○<br>~~GF~~|○<br>~~GF~~|FullCut<br>~~GF~~|Eject<br>~~GF~~|



Specification B <EOT mode setting format> 

|n<br>~~a~~<br>~~Rs~~|FormFeed<br>~~se~~|CutFeed<br>~~se~~|Cutter<br>~~se~~|Presenter<br>~~se~~|
|---|---|---|---|---|
|0<br>~~Rs~~|SetToDefault|SetToDefault|SetToDefault|SetToDefault|
|1<br>~~Rs~~<br>~~a~~|○(*1)<br>~~eG~~|--<br>~~eG~~|--<br>~~eG~~|--<br>~~eG~~|
|2<br>~~a eG~~<br>~~es~~|○(*1)<br>~~eG~~<br>~~GG~~|○<br>~~eG~~<br>~~GG~~|--<br>~~eG~~<br>~~GG~~|--<br>~~eG~~<br>~~GG~~|
|3<br>~~es~~<br>~~ee~~|○(*1)<br>~~GG~~<br>~~ee~~|TearBar<br>~~GG~~<br>~~GG~~|--<br>~~GG~~<br>~~GG~~|--<br>~~GG~~|
|8<br>~~es~~<br>~~ee~~|○(*1)<br>~~GG~~<br>~~ee~~|--<br>~~GG~~<br>~~GG~~|FullCut<br>~~GG~~<br>~~GG~~|--<br>~~GG~~|
|9<br>~~ee~~<br>~~a~~|○(*1)<br>~~ee~~|○<br>~~GG~~|FullCut<br>~~GG~~|--|
|12<br>~~a~~|○(*1)<br>~~eG~~|--<br>~~eG~~|PartialCut<br>~~eG~~|--<br>~~eG~~|
|13<br>~~es~~|○(*1)<br>~~GG~~|○<br>~~GG~~|Partial Cut<br>~~GG~~|--<br>~~GG~~|
|36<br>~~es~~<br>~~es~~|○(*1)<br>~~GG~~<br>~~GG~~|--<br>~~GG~~<br>~~GG~~|FullCut<br>~~GG~~<br>~~GG~~|Eject<br>~~GG~~<br>~~GG~~|
|37<br>~~es~~<br>~~es~~|○(*1)<br>~~GG~~<br>~~GG~~|○<br>~~GG~~<br>~~GG~~|FullCut<br>~~GG~~<br>~~GG~~|Eject<br>~~GG~~<br>~~GG~~|



When the printer is a model handling BM and is set for BM to be effective, the set raster mode page length is ignored and BM detecting is performed. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-73 

## **ESC * r F n NUL** 

[Name] Set raster FF mode [Code] ASCII ESC * r F n NUL Hex. 1B 2A 72 46 n 00 Decimal 27 42 114 70 n 0 

[Defined Area] n = 0, 1, 2, 3, 8, 9, 12, 13, 36, 37 [Initial Value] Models handling full cut: n = 9 

Models connected with a presenter: n = 37 [Function] Sets raster FF mode. 

The FF mode operates to execute using the raster document quit command (ESC FF NUL). n is a decimal description (max. 255 digits) using ASCII characters. Invalid in page mode. 

|n<br>~~a~~<br>~~es~~|FormFeed<br>~~es~~<br>~~eG~~|Cut Feed<br>~~Df~~<br>~~eG~~|Cutter<br>~~Df~~|Presenter|
|---|---|---|---|---|
|0<br>~~a ~~<br>~~es~~<br>~~es~~|SetToDefault<br> ~~es~~<br>~~eG~~<br>~~GG~~|SetToDefault<br>~~Df~~<br>~~eG~~<br>~~GG~~|SetToDefault<br>~~Df~~<br>~~GG~~|SetToDefault<br>~~GG~~|
|1<br>~~es~~<br>~~es~~<br>~~ee~~|○<br>~~eG~~<br>~~GG~~<br>~~ee~~|--<br>~~eG~~<br>~~GG~~<br>~~GG~~|--<br>~~GG~~<br>~~GG~~|--<br>~~GG~~|
|2<br>~~es~~<br>~~ee~~<br>~~Rs~~<br>~~a~~|○<br>~~GG~~<br>~~ee~~<br>~~GD~~|○<br>~~GG~~<br>~~GG~~<br>~~GD~~|--<br>~~GG~~<br>~~GG~~<br>~~GD~~<br>~~QO~~|--<br>~~GG~~<br>~~GD~~|
|3<br>~~ee~~<br>~~Rs~~<br>~~a~~|○<br>~~ee~~<br>~~GD~~|TearBar<br>~~GG~~<br>~~GD~~|--<br>~~GG~~<br>~~GD~~<br>~~QO~~|--<br>~~GD~~|
|8<br>~~Rs~~<br>~~a~~|○<br>~~GD~~|--<br>~~GD~~|FullCut<br>~~GD~~<br>~~QO~~|--<br>~~GD~~|
|9<br>~~a~~<br>~~a eG~~<br>~~es~~|○<br>~~eG~~<br>~~GG~~|○<br>~~eG~~<br>~~GG~~|FullCut<br>~~QO~~<br>~~eG~~<br>~~GG~~|--<br>~~eG~~<br>~~GG~~|
|12<br>~~es~~<br>~~ee~~|○<br>~~GG~~<br>~~ee~~|--<br>~~GG~~<br>~~GG~~|PartialCut<br>~~GG~~<br>~~GG~~|--<br>~~GG~~|
|13<br>~~es~~<br>~~ee~~|○<br>~~GG~~<br>~~ee~~|○<br>~~GG~~<br>~~GG~~|PartialCut<br>~~GG~~<br>~~GG~~|--<br>~~GG~~|
|36<br>~~ee~~<br>~~a~~|○<br>~~ee~~<br>|--<br>~~GG~~<br>|FullCut<br>~~GG~~<br>|Eject<br>|
|37<br>~~GF~~|○<br>~~GF~~|○<br>~~GF~~|FullCut<br>~~GF~~|Eject<br>~~GF~~|



Specification B <FF mode setting format> 

|n<br>~~a~~<br>~~Rs~~|FormFeed<br>~~se~~|CutFeed<br>~~se~~|Cutter<br>~~se~~|Presenter<br>~~se~~|
|---|---|---|---|---|
|0<br>~~Rs~~|SetToDefault|SetToDefault|SetToDefault|SetToDefault|
|1<br>~~Rs~~<br>~~a~~|○(*1)<br>~~eG~~|--<br>~~eG~~|--<br>~~eG~~|--<br>~~eG~~|
|2<br>~~a eG~~<br>~~es~~|○(*1)<br>~~eG~~<br>~~GG~~|○<br>~~eG~~<br>~~GG~~|--<br>~~eG~~<br>~~GG~~|--<br>~~eG~~<br>~~GG~~|
|3<br>~~es~~<br>~~ee~~|○(*1)<br>~~GG~~<br>~~ee~~|TearBar<br>~~GG~~<br>~~GG~~|--<br>~~GG~~<br>~~GG~~|--<br>~~GG~~|
|8<br>~~es~~<br>~~ee~~|○(*1)<br>~~GG~~<br>~~ee~~|--<br>~~GG~~<br>~~GG~~|FullCut<br>~~GG~~<br>~~GG~~|--<br>~~GG~~|
|9<br>~~ee~~<br>~~a~~|○(*1)<br>~~ee~~|○<br>~~GG~~|FullCut<br>~~GG~~|--|
|12<br>~~a~~|○(*1)<br>~~eG~~|--<br>~~eG~~|PartialCut<br>~~eG~~|--<br>~~eG~~|
|13<br>~~es~~|○(*1)<br>~~GG~~|○<br>~~GG~~|Partial Cut<br>~~GG~~|--<br>~~GG~~|
|36<br>~~es~~<br>~~es~~|○(*1)<br>~~GG~~<br>~~GG~~|--<br>~~GG~~<br>~~GG~~|FullCut<br>~~GG~~<br>~~GG~~|Eject<br>~~GG~~<br>~~GG~~|
|37<br>~~es~~<br>~~es~~|○(*1)<br>~~GG~~<br>~~GG~~|○<br>~~GG~~<br>~~GG~~|FullCut<br>~~GG~~<br>~~GG~~|Eject<br>~~GG~~<br>~~GG~~|



When the printer is a model handling BM and is set for BM to be effective, the set raster mode page length is ignored and BM detecting is performed. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-74 

**ESC * r P n NUL** [Name] Set raster page length [Code] ASCII ESC * r P n NUL Hex. 1B 2A 72 50 n 00 Decimal 27 42 114 80 n 0 [Defined Area] - - - [Initial Value] Raster image buffer length [Function] Sets raster page length. n is a decimal description (max. 255 digits) using ASCII characters. Invalid in page mode. n 0 Continuous print mode (no page length setting) 1≤n Specify page length 

## **ESC * r Q n NUL** 

[Name] Set raster print quality [Code] ASCII ESC * r Q n NUL Hex. 1B 2A 72 51 n 00 Decimal 27 42 114 81 n 0 [Defined Area] 0≤n≤2 [Initial Value] n = 0 [Function] Sets raster print quality. n is a decimal description (max. 255 digits) using ASCII characters. Invalid in page mode. 

|n|Print quality|
|---|---|
|0|Specifyhighspeed printing|
|1|Normal print quality|
|2|Highprintquality|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-75 

## **ESC * r m l n NUL** 

[Name] Set raster left margin [Code] ASCII ESC * r m l n NUL Hex. 1B 2A 72 6D 6C n 00 Decimal 27 42 114 109 108 n 0 [Defined Area] - - - [Initial Value] n = 0 [Function] Sets raster left margin. This command sets the left margin to (n x 8). When the left margin exceeds the printable area, or if the left margin specification eliminates the print area (printable region to right margin) to the left margin specified value, this command is ignored. n is a decimal description (max. 255 digits) using ASCII characters. Invalid in page mode. 

## **ESC * r m r n NUL** 

|[Name]|Set raster right margin|Set raster right margin||||
|---|---|---|---|---|---|
|[Code]|ASCII|ESC<br>*<br>r<br>m|r|n|NUL|
||Hex.|1B<br>2A<br>72<br>6D|72|n|00|
||Decimal|27<br>42 114 109|114|n|0|
|[Defined Area]||- - -||||
|[Initial Value]||n = 0||||
|[Function]|[Function]|Sets raster right margin.|Sets raster right margin.|||
|||This command sets the right margin to (n x 8).||||
|||When the right margin exceeds the printable area, or if the right margin specification eliminates the||||
|||print area (printable region to left margin) to the right margin specified value, this command is||print area (printable region to left margin) to the right margin specified value, this command is||
|||ignored.||||
|||n is a decimal description (max. 255 digits) using ASCII characters.||||
|||Invalid in page mode.||||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-76 

## **ESC * r T n NUL** 

[Name] Set raster top margin [Code] ASCII ESC * r T n NUL Hex. 1B 2A 72 54 n 00 Decimal 27 42 114 84 n 0 

[Defined Area] 0≤n≤2 [Initial Value] --[Function] Sets the raster top margin. 

n is a decimal description (max. 255 digits) using ASCII characters. 

|n|Topmargin|
|---|---|
|0|Set To Default|
|1|Set topmarginusingreverse paper feed.|
|2|Set standard topmargin.|



(*) This differs according to the model handling this command. 

The line mode top margin setting continues after entering the raster mode. 

Also, the top margin setting of the raster mode continues after ending the raster mode, and returning to the line mode. 

Invalid in page mode. 

## **ESC * r K n NUL** 

[Name] Set raster print color [Code] ASCII ESC * r K n NUL Hex. 1B 2A 72 4B n 00 Decimal 27 42 114 75 n 0 [Defined Area] 0≤n≤3 [Initial Value] n = 0 [Function] Sets raster print color. 

This command is effective only when specifying the 2 color mode using the line mode. 

This command is ignored when not in the 2 color print mode. 

n is a decimal description (max. 255 digits) using ASCII characters. Invalid in page mode. 

|n|Print color|
|---|---|
|0|Black|
|1|Cyan|
|2|Magenta|
|3|Yellow|



(*) This command is effective only when using a model handling 2 color printing. This command is ignored on non-compatible models. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-77 

## **b  n1 n2 data** 

[Name] Send raster data (auto line feed) [Code] ASCII b n1 n2 d1 d2 ... dk Hex. 62 n1 n2 d1 d2 ... dk Decimal 98 n1 n2 d1 d2 ... dk 

[Defined Area] 0≤n1≤255 0≤n2≤255 0≤d≤255 k= n1+n2 x 256 1≤k 

[Initial Value] - - - [Function] Sends raster data (auto line feed). 

Raster data is sent in (n1 + n2 x 256) byte counts as binary data. Raster data exceeding the print area currently set is discarded. 

The image buffer expanded position is automatically line fed one dot row and moved to the left margin on the next line after expanded the image buffer data 1 dot row using this command. Also, data expansion is duplicated on the data in the current image buffer (OR process). The following shows expanded image buffer for the set raster print color. n is a decimal description (max. 255 digits) using ASCII characters. Invalid in page mode. 

|Print color|Expandedimage buffer|
|---|---|
|Black|Image buffer for black|
|Cyan|Image buffer forcolor|
|Magenta|Image buffer forcolor|
|Yellow|Image buffer forcolor|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-78 

**k  n1 n2 data** [Name] Transfer raster data [Code] ASCII k n1 n2 d1 d2 ... dk Hex. 6B n1 n2 d1 d2 ... dk Decimal 107 n1 n2 d1 d2 ... dk 

[Defined Area] 0≤n1≤255 0≤n2≤255 0≤d≤255 k≤ n1+n2 x 256 1≤k 

[Initial Value] - - - [Function] Sends raster data. Raster data is sent in (n1 + n2 x 256) byte counts as binary data. Raster data exceeding the print area currently set is discarded. 

The image buffer expanded position returns to the head of the current dot row without an automatic line fed after expanding the image buffer data 1 dot row using this command. 

Also, data expansion is duplicated on the data in the current image buffer (OR process). The following shows expanded image buffer for the set raster print color. n is a decimal description (max. 255 digits) using ASCII characters. Invalid in page mode. 

|Print color|Expandedimage buffer|
|---|---|
|Black|Image buffer for black|
|Cyan|Image buffer forblack|
|Magenta|Image buffer forblack|
|Yellow|Image buffer forblack|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-79 

## **ESC * r Y n NUL** 

[Name] Move vertical direction position (Line feed for specified dots) [Code] ASCII ESC * r Y n NUL Hex. 1B 2A 72 59 n 00 Decimal 27 42 114 89 n 0 [Defined Area] - - - [Initial Value] - - - [Function] Moves vertical direction position. Moves position n dots with this command. When the current page length setting is in continuous print mode, and the n dots exceed the remaining dot count of the raster image buffer length, this moves up to the remaining dot count and ignores the overflow. If the page length is set, it moves to the current page length and ignores the overflow. Note that when there is overflow, this expands the next raster data after printing the raster image buffer data with the next raster data transfer and move vertical direction position command. n is a decimal description (max. 255 digits) using ASCII characters. Invalid in page mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-80 

## **ESC FF NUL** 

[Name] Execute FF mode [Code] ASCII ESC FF NUL Hex. 1B 0C 00 Decimal 27 12 0 [Defined Area] - - - [Initial Value] - - - [Function] Executes FF mode. Executes operation specified by the FF mode setting command (ESC * r F n NUL). Invalid in page mode. 

## **ESC FF EOT** 

[Name] Execute EOT mode [Code] ASCII ESC FF EOT Hex. 1B 0C 04 Decimal 27 12 4 [Defined Area] - - - [Initial Value] - - - [Function] Executes EOT mode. Executes operation specified by the EOT mode setting command (ESC * r E n NUL). Invalid in page mode. 

## **ESC * r N n NUL** 

[Name] Discard data for specified byte count [Code] ASCII ESC * r N n NUL Hex. 1B 2A 72 4E n 0 Decimal 27 42 114 78 n 0 [Defined Area] 1 ≤ n≤ 2 55 [Initial Value] - - - [Function] Discards data for the specified byte count. Discards data received after a byte count specified by n. n is expressed in decimal (maximum 4 digits) using ASCII characters. This command is effective only in raster mode. Invalid in page mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-81 

## **ESC * r V m n NUL** 

[Name] Execute external buzzer drive [Code] ASCII ESC * r V m n NUL Hex. 1B 2A 72 56 m n 0 Decimal 27 42 114 86 4m n 0 [Defined Area] m=49,50 1≤n≤20 [Initial Value] - - - [Function] Repeatedly drives the buzzer according to the ON/OFF conditions set by the external buzzer drive pulse conditions command <ESC> <GS> <EM> <DC1> m n1 n2. 

||m specifies the buzzer drive terminal to drive.|m specifies the buzzer drive terminal to drive.|
|---|---|---|
|m|m|Buzzer DriveTerminal|
|49||Buzzer DriveTerminal 1|
|50||Buzzer DriveTerminal 2|



Specifies the number of repetitions of the buzzer drive with n. The buzzer will not ring while printing. 

This command is prohibited for uses other than to ring the buzzer. 

(If this command is used to drive the cash drawer on models that have an external device terminal, the system will be damaged. Absolutely never use it for other purposes.) 

The buzzer can be stopped by pressing the paper feed switch or opening the cover when it is ringing. 

Conditions must not be set in advance with the external buzzer drive pulse condition command <ESC> <GS> <EM> <DC1> m n1 n2 prior to entering the raster mode. 

n is expressed in decimal (maximum 255 digits) using ASCII characters. Invalid in page mode. 

Example: 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-82 

**ESC * r e s NUL** [Name] Set/cancel data intake mode [Code] ASCII ESC * r e s NUL Hexadecimal 1B 2A 72 65 s 00 Decimal 27 42 114 101 s 0 

[Defined Area] s = 33H, 34H [Function] This command is run when reading from the reception buffer. Processes for document start and end according to the s parameter. 

n is a decimal (max. 255 digits) using ASCII characters. 

|s|Name|Function|
|---|---|---|
|33H|Start document|(1) Sets data intake mode<br>(2) Initialize|
|34H|End document|(1) Prints data in line buffer, if data exists.<br>(2) Waits until printing ends (motor stops).<br>(3) Cancels data intake mode|



(1)  Receive and discard all data being received. 

(Document start command) 

(2) Receive and discard only the current page. (Document start command + document end command) 

If there is an error after receiving the document start command, reception data is received and discarded until the document end command is received when the printer is recovered from the error. If the document end command cannot be recognized, all reception data is destroyed. Timeouts are two seconds. Automatically cancels the data intake mode. 

Restrictions 

1) Sleep mode decrease 

2) Invalid when in Page mode 

When s = 33H, initialize the following settings using the initializing process. 

• Left/right margins 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-83 

## **ESC * r S** 

[Name] Raster mode NV audio playback [Code] ASCII ESC * r S Hexadecim 1B 2A 72 53 al Decimal 27 42 114 83 

[Defined Area] --[Initial Value] --[Function] Plays back the specified NV audio. 

You must set the operating conditions using the audio playback setting command before sending this command. 

(1) ESC * r s 0 a n NUL Number 

(2) ESC * r s 1 n NUL Number of times 

(3) ESC * r s 2 n NUL Delay time 

(4) ESC * r s 3 n NUL Interval time 

(5) ESC * r S Playback 

((1) to (4) can be in any order.) 

Delay time is the time from processing this command to the start of audio playback. Interval time is the time from the end of audio to the start of the next audio. 

If audio is already being played back, run after waiting for the end of the audio. If the printer is printing, run after printing is ended. 

If the audio data of the specified audio number has not been registered, there will be no playback. Audio will stop by inputting the FEED switch while this command is running. Invalid in page mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-84 

## **ESC * r s 0 a n NUL** 

[Name] Set raster mode NV audio playback number [Code] ASCII ESC * r s 0 a n NUL Hexadecim 1B 2A 72 73 30 a n 00 al Decimal 27 42 114 115 48 a n 0 [Defined Area] a = 48, 49 ‘1’ ≤ n ≤ ’255’ [Initial Value] No audio playback number setting. [Function] Set the audio playback number to play in the raster mode audio playback command (ESC * r S). a specifies the area where the audio data to playback is stored. a Audio data storage area 49 User area n is a decimal description (max. 5 digits) using ASCII characters. No setting when the parameter is not defined. Invalid in Page Mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-85 

## **ESC * r s 1 n NUL** 

[Name] Set raster mode NV audio playback count [Code] ASCII ESC * r s 1 n NUL Hexadecim 1B 2A 72 73 31 n 00 al Decimal 27 42 114 115 49 n 0 [Defined Area] ‘1’ ≤ n ≤ ’65535’ [Initial Value] No audio playback count setting. [Function] Set the audio playback count to n times in the raster mode audio playback command (ESC * r S). n is a decimal description (max. 5 digits) using ASCII characters. No setting when the parameter is not defined. Invalid in page mode. 

## **ESC * r s 2 n NUL** 

[Name] Set raster mode NV audio playback delay time [Code] ASCII ESC * r s 2 n NUL Hexadecimal 1B 2A 72 73 32 n 00 Decimal 27 42 114 115 50 n 0 [Defined Area] ‘0’ ≤ n ≤ ’65535’ [Initial Value] n = ‘0’ [Function] Set the audio playback delay time to n second in the raster mode audio playback command (ESC * r S). Delay time is the time from starting processing of the raster mode audio playback command (ESC * r S) to the start of audio playback. n is a decimal description (max. 5 digits) using ASCII characters. No setting when the parameter is not defined. Invalid in page mode. 

## **ESC * r s 3 n NUL** 

[Name] Set raster mode NV audio playback interval time [Code] ASCII ESC * r s 3 n NUL Hexadecimal 1B 2A 72 73 33 n 00 Decimal 27 42 114 115 51 n 0 [Defined Area] ‘0’ ≤ n ≤ ’65535’ [Initial Value] n = ‘0’ [Function] Set the audio playback interval time to n second in the raster mode audio playback command (ESC * r S). Interval time is the time from the end of audio to the start of the next audio. n is a decimal description (max. 5 digits) using ASCII characters. No setting when the parameter is not defined. Invalid in page mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-86 

## **3.5. Black Mark Related Command Details** 

The following commands control top of form functions using black mark paper. The following commands are effective only when black mark is set to be effective. 

## **ESC d n** 

|[Name]|Auto cutter|Auto cutter||
|---|---|---|---|
|[Code]|ASCII|ESC<br>d|n|
||Hex.|1B<br>64|n|
||Decimal|27 100|n|
|[Defined Area]||0≤<br>d≤<br>3||
|||48≤<br>d≤<br>51 (”0”≤<br>d≤<br>”3”)||
|[Initial Value]||- - -||
|[Function]|[Function]|Executes the auto-cutter.|Executes the auto-cutter.|



After auto-cutter is executed, the printer considers that to be the top of the page. 

|n|Auto cutter||
|---|---|---|
|0, 48|Full cut at the current position.||
||Print data in line buffer is printed before a full cut.||
||This commandisignoredifthe printer isnot equippedwithanauto-cutter.||
|1, 49|Partial cut at the current position.||
||Print data in line buffer is printed before a partial cut.||
||This commandisignoredifthe printer isnot equippedwithanauto-cutter.||
|2, 50|After executing top of form, paper is fed to cutting position, then a full cut.||
||Print data in line buffer is printed before the operation described above.||
||This command is ignored if the printer is not equipped with an auto-cutter.||
|3, 51|After executing top of form, paper is fed to cutting position, then a partial cut.||
||Print data in line buffer is printed before the operation described above.||
||This commandisignoredif the printer isnotequippedwithanauto-cutter.||
||(*) The auto-cutter function operates in the following ways on models that only have a full cut or a|(*) The auto-cutter function operates in the following ways on models that only have a full cut or a|
||partial cut.||
||• Models that perform only a full cut:<br>Executes a full cut when for instructions calling||
||for a partial cut.||
||• Models that perform only a partial cut:<br>Executes a partial cut when there are for||
||instructions calling for a full cut.||
||(*) When connected with a presenter, executes a full cut when instructed for a partial cut.||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-87 

## **FF** 

[Name] Execute top of form [Code] ASCII FF Hex. 0C Decimal 12 [Defined Area] - - - [Initial Value] - - - [Function] Executes top of form. 

## **ESC C n** 

[Name] Set page length to n lines [Code] ASCII ESC C n Hex. 1B 43 n Decimal 27 67 n 

[Defined Area] 1≤n≤127 [Initial Value] (Form feed amount initial value x 42) [Function] When black mark is effective, this command is ignored. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-88 

**ESC C 0 n** [Name] Set page length to n x 24 mm units [Code] ASCII ESC C 0 n Hex. 1B 43 0 n Decimal 27 67 0 n [Defined Area] 1≤n≤22 [Initial Value] (Form feed amount initial value x 42) [Function] When black mark is effective, this command is ignored. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-89 

## **VT** 

[Name] Feed paper to vertical table position [Code] ASCII VT Hex. 0B Decimal 11 [Defined Area] - - - [Initial Value] - - - [Function] When black mark is effective, this command is ignored. 

## **ESC B n1 n2...nk NUL** 

[Name] Set vertical tab position [Code] ASCII ESC B n1 n2 ... nk NUL Hex. 1B 42 n1 n2 ... nk 00 Decimal 27 66 n1 n2 ... nk 0 [Defined Area] 1≤n≤255 0≤k≤16 [Initial Value] - - - [Function] When black mark is effective, this command is ignored. 

## **ESC B NUL** 

[Name] Clear vertical tab position [Code] ASCII ESC B NUL Hex. 1B 42 00 Decimal 27 66 0 [Defined Area] - - - [Initial Value] - - - [Function] When black mark is effective, this command is ignored. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-90 

## **3.6. USB Related Command Details** 

The following commands control USB I/F functions. There are no corresponding commands. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-91 

## **3.7. 2 Color Printing Command Details** 

The following commands control 2 color printing functions. 

The following commands are effective only when using a model handling 2 color printing. 

|**ESC RS c n**|**ESC RS c n**|**ESC RS c n**|**ESC RS c n**||
|---|---|---|---|---|
|[Name]|Set print color in 2 color print mode|Set print color in 2 color print mode|Set print color in 2 color print mode||
|[Code]|ASCII||ESC RS<br>c<br>n||
||Hex.||1B<br>1E<br>63<br>n||
||Decimal||Decimal<br>27<br>30<br>99<br>n||
|[Defined Area]|||0≤<br>n≤<br>1||
||||48≤<br>n≤<br>49 (”0”≤<br>n≤<br>”1”)||
|[Initial Value]|||n = 0, 48 (When in 2 color print mode)||
|[Function]|||Specifies print color in 2 color print mode.||
||||This command is ignored when not in the 2 color print mode.||
||||Specifies black for the print color when in 2 color print mode.||
||||This command is cleared only when the printer is reset.||
||||The specification of this command is not cleared by ESC @ CAN.||
||||However, print color is initialized to black by the ESC @ and CAN only when in the compatible 2|However, print color is initialized to black by the ESC @ and CAN only when in the compatible 2|
||||color print mode.||
|||n|Specifies2colorprintmode color||
||0,4|48|Black||
||1,4|49|Red||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-92 

|**ESC RS C n**|**ESC RS C n**|**ESC RS C n**|
|---|---|---|
|[Name]|Select/cancel 2 color print mode||
|[Code]|ASCII|ESC RS<br>C<br>n|
||Hex.|1B<br>1E<br>43<br>n|
||Decimal|27<br>30<br>67<br>n|
|[Defined Area]||Specification A|
|||0≤<br>n≤<br>2|
|||48≤<br>n≤<br>50 (”0”≤<br>n≤<br>”2”)|
|||Specification B|
|||0≤<br>n≤<br>1|
|||48≤<br>n≤<br>49 (”0”≤<br>n≤<br>”1”)|
|||Specification C|
|||0≤<br>n≤<br>2|
|||48≤<br>n≤<br>50 (”0”≤<br>n≤<br>”2”)|
|||n = 16, n = 32|
|[Initial Value]||n = 0, 48|
|[Function]||Specification A|
||n|Select/cancel 2colorprintmode|
||0, 48|Cancel 2-color printing mode|
|||When in two-color print mode, this command cancels 2-color printing mode.|
|||This command is ignored when the 2-color print mode is already cancelled.|
|||The specification of this command is not cleared by ESC @, CAN.|
|||The following processes are executed by canceling the 2-color print mode using this|
|||command.|
|||• Prints data in line buffer in 2-color print mode, if unprinted data exists in the line buffer.|
|||• Waits to stop printing when printing in 2-color print mode.|
|||• Recovers logo print setting to single color mode setting.|
||1, 49|Select 2-color printing mode|
|||This command selects 2-color print mode, when in single color print mode.|
|||This command is ignored already in the 2-color print mode.|
|||The specification of this command is not cleared by ESC @, CAN.|
|||The following processes are executed by selecting the 2-color print mode using this command.|
|||• Prints data in line buffer in the single color print mode, if unprinted data exists in the line|
|||buffer.|
|||• Waits to stop printing when printing in single-color print mode.|
|||• Initializes print color setting (2-color print mode setting)|
|||•Setslogo printsettingto2color mode setting.|



Invalid in page mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-93 

## Specification B 

|n|Select/cancel 2colorprintmode|
|---|---|
|0, 48|Cancel 2-color printing mode<br>When in two-color print mode, this command cancels 2-color printing mode.<br>This command is ignored when the 2-color print mode is already cancelled.<br>The specification of this command is not cleared by ESC @, CAN.<br>The following processes are executed by canceling the 2-color print mode using this<br>command.<br>• Prints data in line buffer in 2-color print mode, if unprinted data exists in the line buffer.<br>• Waits to stop printing when printing in 2-color print mode.<br> •Recovers logo print setting to single color mode setting.|
|1, 49|Select 2-color printing mode<br>This command selects 2-color print mode, when in single color print mode.<br>This command is ignored already in the 2-color print mode.<br>The specification of this command is not cleared by ESC @, CAN.<br>The following processes are executed by selecting the 2-color print mode using this command.<br>• Prints data in line buffer in the single color print mode, if unprinted data exists in the line<br>buffer.<br>• Waits to stop printing when printing in single-color print mode.<br>• Initializes print color setting (2-color print mode setting)<br>•Setslogo print setting to2color mode setting.|



## Specification C 

|n|Specify printmode|
|---|---|
|0, 48|Single color print mode|
|1,49|2-colorprintmode|
|2, 50|Dot compatible2-color mode|
|16|Lowpowerconsumption mode|
|32|Doubleresolution mode|



- If set to the low power consumption mode using the DIP switches, this command is ignored. 

- This command is not cleared by ESC @, CAN. 

- When there is unprinted data in the line buffer, print the line buffer data. 

- This command is processed after ending the current print job. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-94 

## **ESC 4** 

[Name] Select white/black inverted printing [Code] ASCII ESC 4 Hex. 1B 34 Decimal 27 52 [Defined Area] - - - [Initial Value] White/black inversion cancelled [Function] Specifies white/black inversion for ANK characters and Kanji characters. IBM block ignores white/black inversion. 

## **ESC 5** 

[Name] Cancel white/black inversion [Code] ASCII ESC 5 Hex. 1B 35 Decimal 27 53 [Defined Area] - - - [Initial Value] White/black inversion cancelled [Function] Cancels white/black inversion for ANK characters and Kanji characters. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-95 

## **ESC RS d n** 

[Name] Set print density [Code] ASCII ESC RS d n Hex. 1B 1E 64 n Decimal 27 30 100 n [Defined Area] 0≤n≤15 48≤n≤57 (”0”≤n≤”9”) 65≤n≤70 (”0”≤n≤”F”) [Initial Value] Memory switch setting [Function] Sets print density. This command stops printing to be executed. When in two-color print mode, this can set the print density of red print. 

|n|Print Density<br>Single Color PrintingMode<br>Two Color PrintingModeRedPrintDensity|
|---|---|
|0,48|Print density1.3<br>Print density1.2|
|1, 49<br>~~es~~|Print density 1.2<br>Print density 1.2<br>|
|2, 50<br>~~es~~|Print density1.1<br>Print density1.0<br>|
|3, 51<br>~~esa~~|Print density1.0<br>Print density1.0<br>~~a~~|
|4, 52<br>~~a~~|Print density 0.9<br>Print density1.0<br>~~a~~|
|5, 53|Print density 0.8<br>Print density 0.8|
|6, 54<br>~~a~~|Print density 0.7<br>Print density 0.8<br>~~a~~|
|7, 55<br>~~a~~|(Reserved)<br>(Reserved)<br>~~a~~|
|8, 56<br>~~a~~|(Reserved)<br>(Reserved)<br>~~a~~|
|9, 57|(Reserved)<br>(Reserved)|
|10, 65|(Reserved)<br>(Reserved)|
|11, 66|(Reserved)<br>(Reserved)|
|12, 67<br>~~a~~|(Reserved)<br>(Reserved)<br>~~a~~|
|13, 68<br>~~a~~|(Reserved)<br>(Reserved)<br>~~a~~|
|14, 69|(Reserved)<br>(Reserved)|
|15,70|(Reserved)<br>(Reserved)|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-96 

**ESC RS r n** [Name] Set printing speed [Code] ASCII ESC RS r n Hex. 1B 1E 72 n Decimal 27 30 114 n 

[Defined Area] 0≤n≤3 48≤n≤51 (”0”≤n≤”3”) [Initial Value] Memory switch setting [Function] Sets print speed. 

This command stops printing to be executed. 

Because two-color print mode prints in one speed, the speed settings with this command are invalid.  This command setting becomes valid when returned from the two-color print mode to the single color print mode. 

|N|Print Speed<br>Single Color PrintingMode<br>Two Color PrintingMode|
|---|---|
|0,48|Highspeed<br>Two Color PrintingMode Speed|
|1,49<br>~~a~~|Mid-speed<br>Two Color PrintingMode Speed|
|2, 50<br>~~a~~|Slow speed<br>Two Color Printing Mode Speed|
|3, 51<br>~~a~~|Optionspeed (differs accordingtothemodel)<br>Two Color PrintingMode Speed|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-97 

**ESC FS q n [x11 x12 y11 y12 d1...dk]1...[xn1 xn2 yn1 yn2 d1...dk]n** [Name] Register logo [Code] ASCII ESC FS q n [x11 x12 y11 y12 d1 … dk]1 … [xn1 xn2 yn1 yn2 d1 ... dk]n Hex. 1B 1C 71 n [x11 x12 y11 y12 d1 … dk]1 … [xn1 xn2 yn1 yn2 d1 ... dk]n Decimal 27 28 113 n [x11 x12 y11 y12 d1 … dk]1 … [xn1 xn2 yn1 yn2 d1 ... dk]n 

[Defined Area] 1≤n≤255 0≤xn1≤255,  0≤xn2≤3 1≤(xn1 + xn2 x 256)≤1023 0≤yn1≤255,  0≤yn2≤1 1≤yn1 + yn2 x 256)≤288 0≤d≤255 k = {(xn1 + xn2 x 256) x (yn1 + yn2 x 256) x 8} [Initial Value] - - - [Function] Parameter details • n: Specifies registered logo count • xn1, xn2:  Horizontal size of registered logo {(xn1 + xn2 x 256) x 8} dots • yn1, yn2:  Vertical size of registered logo {(yn1 + yn2 x 256) x 8} dots • d: Registered logo data • k: Logo data count 

This command should be specified at the top of the line. 

When the first parameter is determined to be free of error, the printer starts processing this command. 

When logo register processing starts, all previously defined data is deleted. (It is not possible to reregister a portion of a plurality of defined logo data.) Logo registration numbers are defined in rising order from 1. 

If the defined area specified by the parameter is not empty, or if there is an error in the parameter specification, register processing is aborted.  (The pre-registered and complete data is effective.) The printer should be initialized if logo registration is completed or register processing is aborted. If an error occurs while performing register processing (the time from when the first parameter is OK until th printer initialization is completed after registering a logo), error processing, mechanical operation and status processing cannot be performed. 

The relationships between input data and the actual print are shown on the next page. 

<When registering logos for 2 color printing> 

Registration is possible regardless of the 2 color printing mode being specified or cancelled. Register logos with the same capacity as the logo register number n (odd number) and n + 1 (even number). 

If the capacity differs or the logo register number is 255, this command is ignored by the logo print command in the 2 color print mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-98 

**==> picture [464 x 688] intentionally omitted <==**

**----- Start of picture text -----**<br>
Relationships of logo and registered data<br>xn = xn1 + xn2 x 256 yn = yn1 + yn2 x 256<br>{(xn1 + xn2 x 256) x 8} dots<br>Data<br>MSB<br>d[11]  d[21]  d[n1]<br>(yn1 + yn2 x 256) bytes<br>(yn1 + yn2 x 256) x 8 d[12]  d[22]  d[n2]<br>dots<br>LSB<br>ITE<br>d[x1]  d[x2]  d[xn]<br>ee<br>―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――<br>STAR Line Mode Command Specifications  3-99<br>**----- End of picture text -----**<br>

## **ESC FS p n m** 

[Name] Print logo [Code] ASCII ESC FS p n m Hex. 1B 1C 70 n m Decimal 27 28 112 n m 

[Defined Area] 1≤n≤255 0≤m≤3 48≤m≤51 (”0”≤m≤”3”) [Initial Value] - - - [Function] Prints the logo of registration number n registered using the logo registration command (ESC FS q) according to the print mode m. 

|m|Logo printmode|
|---|---|
|0,48|Normal mode|
|1, 49|Double wide mode|
|2, 50|Doublehigh mode|
|3, 51|Doublehigh/widemode|



If there is unprinted data in the line buffer, this command is executed after printing that data. Therefore, it is not possible to print with other data in the same line (characters, bit images, bar codes). 

Form feed obeys the vertical print size of the logo. Adornments other than upside-down printing and expansion settings are unaffected. The horizontal printing start position conforms to the left margin position and the horizontal print area conforms to the left and right margin settings. 

If the logo horizontal print size exceeds the horizontal print region, the portion exceeding the area is not printed. 

<When using the 2 color print mode> When the logo register number n is odd: 

Register number n is printed in black; register number n + 1 is printed in red and overlapped. The command is ignored when the capacity of the register number n and the capacity of the register number n + 1 are different. 

The command is ignored when the register number n = 255 is specified. When the logo register number n is even: Register number n is printed in black; register number n - 1 is printed in red and overlapped. The command is ignored when the capacity of the register number n and the capacity of the register number n - 1 are different. 

The command is ignored when the register number n = 255 is specified. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-100 

## **3.8. Presenter Related Command Details** 

The following commands control the presenter functions. 

The following commands are effective only on models equipped with a presenter. 

## **ESC SYN 0 n** 

[Name] Execute presenter paper recovery [Code] ASCII ESC SYN 0 n Hex. 1B 16 30 n Decimal 27 22 48 n [Defined Area] n = 0, n = 48 (“0”) [Initial Value] - - - [Function] Executes presenter paper recovery. This command is ignored when a presenter is not connected. Also, this command is executed when paper is supplied by the presenter, exists in the presenter and the paper has been cut.   This command is ignored with under all other conditions.   (Ignored when paper is being recovered.) 

## **ESC SYN 1 n** 

[Name] Set presenter paper automatic recovery function and automatic recovery time [Code] ASCII ESC SYN 1 n Hex. 1B 16 31 n Decimal 27 22 49 n [Defined Area] 0≤n≤255 [Initial Value] Memory switch setting [Function] Sets presenter paper automatic recovery function and automatic recovery time. This command is ignored when a presenter is not connected. Settings using this command are effective from the next sheet when the printer processes this command and paper has already been supplied to the presenter. 

|N|Functions|
|---|---|
|n =0|Paperautomaticrecoveryfunction invalid.|
|1≤<br>n≤<br>255|Paper automatic recovery function valid.<br>Automaticrecoverytime: n x0.5 sec (0.5 secto127.5 sec)|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-101 

## **ESC SYN 3 n** 

[Name] Acquire presenter paper counter [Code] ASCII ESC SYN 3 n Hex. 1B 16 33 n Decimal 27 22 51 n [Defined Area] n = 0, 1 n = 48, 49 (”0”,  “1”) [Initial Value] - - - [Function] Acquires presenter paper counter. This command is ignored when a presenter is not connected. Counter can count to 0xFFFFFFFF sheets. Counter is cleared to zero when the following conditions are met. • At a printer reset • At the <CAN> command • At the <ESC> <SYN> 4 n command The paper counter using this command sends the counter value at the time this command is processed. The counter is counted up when paper is completely recovered or when pulled out. The counter counts from when the power is turned ON, excluding the following. • When paper is discharged because of an error • When printing using self-print • When paper in the presenter is discharged when the power is turned ON 

||N||Counter|
|---|---|---|---|
|n=0, 48|0, 48|0, 48|Acquires paper reel counter|
|n = 1|n = 1,4|49|Acquires paper recovery counter|



<Counter transmission format from printer:  When using the paper reel counter> Printer transmission:  ESC SYN  3  n  c1  c2  c3  c4 

Reel counter:   c4 + (c3 x 256) + (c2 x 256 x 256) + (c1 x 256 x 256 x256) 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-102 

## **ESC SYN 4 n** 

|[Name]|Initialize presenter paper counter|Initialize presenter paper counter|Initialize presenter paper counter|Initialize presenter paper counter|
|---|---|---|---|---|
|[Code]|ASCII|ESC SYN|4|n|
||Hex.|1B<br>16|34|n|
||Decimal|Decimal<br>27<br>22|52|n|
|[Defined Area]||n = 0|||
|[Initial Value]||- - -|||
|[Function]|[Function]|Initializes the presenter paper counter (paper reel counter/paper recovery counter).|||
|||Initialization of the paper counter using this command is executed when this command is||Initialization of the paper counter using this command is executed when this command is|
|||processed.|||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-103 

**ESC GS SUB DC1 m t1 t2** 

|**ESC GS SUB DC1 m t1 t2**|**ESC GS SUB DC1 m t1 t2**|**ESC GS SUB DC1 m t1 t2**|**ESC GS SUB DC1 m t1 t2**|**ESC GS SUB DC1 m t1 t2**|||
|---|---|---|---|---|---|---|
|[Name]|Specify snout operation mode||||||
|[Code]|ESC GS SUB DC1<br>m<br>ASCII||||t1|t2|
||1B<br>Hexadecimal|||1D<br>1A<br>11<br>m|t1|t2|
||Decimal<br>27|||29<br>26<br>17<br>m|t1|t2|
|[Defined Area]|||0≤<br> m≤<br>3, 48≤|≤<br> m≤<br> 51 (“0”≤<br> m≤<br> “3”)|||
||||t1 = 0, t2 =0||||
|[Initial Value]|||MSW Setting|MSW Setting|||
|[Function]|[Function]||Specifythe snout operation mode usingthe mparameter.||||
||||m<br>Snout Operating Mode|Snout Operating Mode|||
||||0, 48<br>Snout LED output OFF|Snout LED output OFF|||
||||1, 49<br>Snout LED output ON (while printing, or during presenter operation)|Snout LED output ON (while printing, or during presenter operation)|Snout LED output ON (while printing, or during presenter operation)||
||||2, 50<br>SnoutLED|LEDoutput ON(during an||nerror)|
||||3, 51<br>Snout LED output ON (while printing, or during presenter operation or an error)|Snout LED output ON (while printing, or during presenter operation or an error)|Snout LED output ON (while printing, or during presenter operation or an error)||
||||This command is valid when a presenter is connected.|||This command is valid when a presenter is connected.|
||||When the snout is not connected, this command is prohibited from use.||||



|**ESC GS SUB DC2 m t1 t2**|**ESC GS SUB DC2 m t1 t2**|**ESC GS SUB DC2 m t1 t2**|**ESC GS SUB DC2 m t1 t2**|
|---|---|---|---|
|[Name]|Specify Snout LED ON/OFF|||
|[Code]|ESC GS SUB<br>DC2<br>m<br>t1<br>t2<br>ASCII|||
||1B 1D<br>1A<br>12<br>m<br>t1<br>t2<br>Hexadecimal|||
||Decimal<br>27<br>29<br>26<br>18<br>m<br>t1<br>t2|||
|[Defined Area]|||1≤<br> m≤<br>2, 49≤<br> m≤<br> 50, (“1”≤<br> m≤<br> “2”)|
||||0≤<br> t1≤<br>255, 0≤<br> t2≤<br> 255|
|[Initial Value]|||t1 = 2, t2 = 2|
|[Function]|[Function]||Specify Snout LED ON/OFF times.|
||||m specifies the snout operation mode.|
||||m<br>Snout OperatingMode|
||||1, 49<br>This command specifies the LED ON/OFF times while the presenter is operating.|
||||(LED lights in orange while the printer is printing.)|
||||2, 50<br>This command specifies the LED ON/OFF times for recoverable and non-recoverable|
||||errors.|
||||t1 specifies the snout LED ON time.|
||||When 1≤<br> t1≤<br>255:  ON time = t1 x 50 msec|
||||When t1 = 0:   When ON time is default value (t1=2)|
||||T2 specifies the snout LED OFF time.|
||||When 1≤<br> t2≤<br>255:  OFF time = t2 x 50 msec|
||||When t2 = 0:   When OFF time is default value (t2=2)|
||||This command is valid when a presenter is connected.|
||||When the snout is not connected, this command is prohibited from use.|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-104 

**ESC GS SUB DC3 m t1 t2** [Name] Snout LED output [Code] ASCII ESC GS SUB DC3 m t1 t2 Hexadecimal 1B 1D 1A 13 m t1 t2 Decimal 27 29 26 19 m t1 t2 [Defined Area] 1 ≤ m ≤ 2, 49 ≤ m ≤ 50, (“1” ≤ m ≤ “2”) 0 ≤ t1 ≤ 255, 0 ≤ t2 ≤ 255 [Initial Value] --[Function] Outputs Snout LED. m specifies the snout LED output terminal. m LED output terminal 1, 49 External output terminal 1 2, 50 External output terminal 2 t1 specifies the ON time for snout LED output. When 1 ≤ t1 ≤ 255:  ON time = t1 x 50 msec When t1 = 0:   When ON time is default value (t1=2) t2 specifies the OFF time for snout LED output. When 0 ≤ t2 ≤ 255:  OFF time = t2 x 50 msec When t2 = 0:   When OFF time is default value (t2=2) This command is valid when a presenter is connected. When the snout is not connected, this command is prohibited from use. 

This command has priority if received while outputting the snout LED in the operation mode specified by the <ESC><GS><EM><DC1> m t1 t2 command. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-105 

## **3.9. Mark Command Details** 

This command is specialized for printing mark sheets for lotteries. This command can print lines. 

<Print Sample> 

**LOTTERY 10 01 05 32 85 86 50 70 77 08 50 21 42 46 40 12 02 06 78** Printed Marks 2003/04/08  STAR micronics.co,ltd No. 0304081254896 ~~srcas~~ 7 

<Example of Command Transmission> 

- Mark Format 

Mark Height h = 10 dots, mark line feed amount v = 20 dots 

Mark number 0: Mark Color c = White, Mark horizontal width w = 16 dots 

Mark number 1: Mark Color c = Black, Mark horizontal width w = 40 dots Mark number 2: Mark Color c = White, Mark horizontal width w = 40 dots 

|Mark||||Mark|||Mark||
|---|---|---|---|---|---|---|---|---|
|number 1||||number 0|||number 2||
|Horizontal||||Horizontal|||Horizontal||
|width w||||width w|||width w||
|Mark|Mark|Mark||Mark|Mark|Mark|Mark|Mark height h<br>Mark line feed|
|number 1|number 0|number 1||number 0|number 1|number 0|number 2|amount v|
||||||||||
|Mark|Mark|Mark||Mark|Mark|Mark|Mark|Mark height h<br>Mark line feed|
|number 1|number 0|number 2||number 0|number 1|number 0|number 1|amount v|
||||||||||
|Mark|Mark|Mark||Mark|Mark|Mark|Mark|Mark height h<br>Mark line feed|
|number 1|number 0|number 1||number 0|number 2|number 0|number 2|amount v|



- Example Transmission 

1. Mark height, Line feed amount setting 

<ESC> <GS> *1 h v (h = “010”, v = “020”) 

2. Color of each mark number, Horizontal width setting 

   - <ESC> <GS> *2 m c w  (Mark number 0 setting: m = “0”, c = “0”, w = “016”) <ESC> <GS> *2 m c w  (Mark number 0 setting: m = “1”, c = “1”, w = “040”) <ESC> <GS> *2 m c w  (Mark number 0 setting: m = “2”, c = “0”, w = “040”) 

3. Register the mark format specified by 1 and 2 in advance in the non-volatile memory (it is possible to print marks that are not registered in the non-volatile memory.) 

<ESC> <GS> * W 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-106 

## 4. Printing Marks 

<ESC><GS> * 0  n  m1 m2 m3 m4 m5 m6 m7 (n=”007”, m1=”1”, m2=”0”, m3=”1”, m4=”0”, m5=”1”, m6=”0”, m7=”2”) <ESC><GS> * 0  n  m1 m2 m3 m4 m5 m6 m7 (n=”007”, m1=”1”, m2=”0”, m3=”2”, m4=”0”, m5=”1”, m6=”0”, m7=”1”) <ESC><GS> * 0  n  m1 m2 m3 m4 m5 m6 m7 (n=”007”, m1=”1”, m2=”0”, m3=”1”, m4=”0”, m5=”2”, m6=”0”, m7=”2”) 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-107 

|**ESC GS* 0  n  m1  m2  m3 … mk**|**ESC GS* 0  n  m1  m2  m3 … mk**|**0  n  m1  m2  m3 … mk**||
|---|---|---|---|
|[Name]|Print mark|||
|[Code]|ASCII|ESC GS<br>*<br>0<br>n<br>m1<br>m2|m3<br>…<br>mk|
||Hex.|1B<br>1D<br>2A<br>30<br>n<br>m1<br>m2|m3<br>…<br>mk|
||Decimal|Decimal<br>27<br>29<br>42<br>48<br>n<br>m1<br>m2|m3<br>…<br>mk|
|[Defined Area]||“001”≤<br> n≤<br> ”255”||
|||“0”≤<br> m≤<br> ”9”||
|||k = n||
|[Initial Value]||- - -||
|[Function]|[Function]|Prints the mark number specified by m, based on the mark format (mark height, mark line feed||
|||amount, each mark color, and each mark horizontal width) that is preset.|amount, each mark color, and each mark horizontal width) that is preset.|
|||n indicates the number of marks to print; If the number of marks is 10 (m1 to m10), n = “010.”||
|||m specifies the mark number to print.||
|||n and m are ASCII character strings that are represented by decimals; They are composed of||
|||character codes “0” to “9.”||
|||This command is ignored if there is print data in the image buffer. Therefore, other characters||
|||cannot be included (characters, bit images, bar codes, etc.).||
|||If there is no mark specified in the remaining print region, the number of bytes specified by n are||
|||discarded.||
|||Also, if the value of n is out of the defined range, subsequent data are processed as normal data.|is out of the defined range, subsequent data are processed as normal data.|
|||This command is affected by position alignment, left margin, moved position, positions such as||
|||horizontal tab and upside down printing.||
|||Invalid in page mode.||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-108 

## **ESC GS * 1  h  v** 

Name] Specify mark height and line feed [Code] ASCII ESC GS * 1 h v Hex. 1B 1D 2A 31 h v Decimal 27 29 42 49 h v [Defined Area] “001” ≤ h ≤ ”255” “001” ≤ v ≤ ”255” h ≤ v [Initial Value] Non-volatile memory [Function] Specifies mark height and line feed amount h is the mark height (number of dots); v is the line feed amount for the mark (number of dots) h and v are ASCII character strings that are represented by decimals; They are composed of character codes “0” to “9.” If a small line feed amount is specified, missing print can occur, so more than v = 16 dots is recommended. Invalid in page mode. 

## **ESC GS * 2  m  c  w** 

|[Name]|Specify mark color and mark horizontal width for each mark number|Specify mark color and mark horizontal width for each mark number|Specify mark color and mark horizontal width for each mark number|Specify mark color and mark horizontal width for each mark number|
|---|---|---|---|---|
|[Code]|ASCII|ESC GS<br>*<br>2<br>m|c|w|
||Hex.|1B<br>1D<br>2A<br>32<br>m|c|w|
||Decimal|27<br>29<br>42<br>50<br>m|c|w|
|[Defined Area]||“0”≤<br> m≤<br> ”9”|||
|||“0”≤<br> c≤<br> ”1”|||
|||“001”≤<br> w≤<br> ”999”|||
|[Initial Value]||Non-volatile memory|||
|[Function]|[Function]|Specifies mark color and mark horizontal width for each mark number.|Specifies mark color and mark horizontal width for each mark number.||
|||m specifies the mark number.|||
|||c specifies the mark color.|||
|||w specifies the mark horizontal width (number of dots).|||
|||If w exceeds the currently set print region, this command is ignored.|||
|||m, c and w are ASCII character strings that are represented by decimals; They are composed of|||
|||character codes “0” to “9.”|||
|||Invalid in page mode.|||



|c|MarkColor|
|---|---|
|“0”(48)|White|
|“1”(49)|Black|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-109 

## **ESC GS * W** 

[Name] Register mark format to non-volatile memory [Code] ASCII ESC GS * W Hex. 1B 1D 2A 57 Decimal 27 29 42 87 [Defined Area] - - - [Initial Value] - - - [Function] Registers the mark format (mark height, mark line feed amount, each mark color, and each mark horizontal width) to the non-volatile memory. After registering to the non-volatile memory, the printer is reset. Invalid in page mode. 

## **ESC GS * C** 

[Name] Initialize mark format in the non-volatile memory [Code] ASCII ESC  GS * C Hex. 1B  1D 2A 43 Decimal 27 29 42 67 

[Defined Area] - - - [Initial Value] - - - [Function] Initializes the registered mark format (mark height, mark line feed amount, each mark color, and each mark horizontal width) in the non-volatile memory. After initialization, the printer is reset. 

Initial Value of the Mark Format • Mark Height:: “016” 16 dots • Mark line feed amount:: “032” 32 dots • Mark color: “0” (White → All mark numbers) • Mark horizontal width: “080” 80 dots → All mark numbers) Invalid in page mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-110 

## **3.10. AUTO LOGO Function Command Details** 

This command functions to print logos, like the one below, by only changing the product name, when only product names can be changed in systems that are already in use.  Also, this function has two operating modes. 

## 1) Standard Auto Logo Function 

The Auto Logo function is preset and executes the following operations using the print cut command under the current system as a trigger. 

1. Starts up the Auto Logo function using the current system cut command as a trigger 

2. Prints if there is print data in the image buffer 

3. Executes user macro 1 

4. Prints the Auto Logo 

5. Executes user macro 2 

**==> picture [471 x 419] intentionally omitted <==**

**----- Start of picture text -----**<br>
Logo 2 is printed by #4 Auto Logo printing according to the command character “/” that was preset in the current print<br>data and embedding the logo number “2” to print. Specifically, if the product is registered with “CHEESE BURGER/2”<br>the logo 2 coupon ticket is automatically printed for the purchaser of a cheese burger. Also, Logo 1 for the header is<br>used for company logos.  By registering to the user macro 2 of #5, cut command + Logo 1 print command, the company<br>logo of logo1 will be printed. User macro 1 of #3 is used when it is necessary to position the Auto Logo in the center.<br>When doing so, register the left alignment command using the user macro 2 of #5 and return to its original setting.<br>Header Logo 1<br>********************<br> MACDONALDS<br>********************  *************** ********************<br>1.CHEESEBURGER  $2.00 2.COKE                      $1.00   MACDONALDS  MACDONALDS<br>*************** ********************<br>--------------------------------------  1.CHEESEBURGER  $2.00 1.CHEESBUGER       $2.00<br>TOTAL                       $3.00 2.COKE                      $1.00 2.COKE                    $1.00<br>--------------------------------------  Current<br>---------------------- TOTAL                       $3.00 System<br>TOTAL                     $3.00  Print Data<br>1. Starts Auto Logo with trigger<br>    of cutting command. Partial Cut<br>2. Executes user macro 1.<br>Current System Print Data Logo 2<br>     Header Cheeseburger<br>Partial Cut<br>3. Prints Auto Logo.<br>COKE Logo 3<br>‘o<br>4. Executes user macro 2.<br>     - Executes cut.<br>     - Executes Header logo  Header<br>       printing.<br>********************<br> MACDONALDS<br>Si an<br>**----- End of picture text -----**<br>


――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-111 

## 2) Simple Auto Logo Function 

The simple Auto Logo function is preset and executes the following operations using the print cut command under the current system as a trigger. 

1. Start up the simple Auto Logo function using the current system cut command as a trigger 

2. Center alignment command process 

3. Print Logo 2 

4. Feed paper to cutting position and execute a partial cut 

5. Print Logo 1 

6. Recovers position alignment command to setting prior to execution of the simple Auto Logo 

**==> picture [424 x 340] intentionally omitted <==**

**----- Start of picture text -----**<br>
With the simple Auto Logo function, the logo number of the logo to be printed is decided in advance.<br>Header Logo 1<br>********************<br> MACDONALDS<br>********************  *************** ********************<br>1.CHEESEBURGER  $2.00   MACDONALDS<br>2.COKE                     $1.00   MACDONALDS<br>*************** ********************<br>--------------------------------------  1.CHEESBUGER       $2.00 1.CHEESEBURGER  $2.00<br>TOTAL                      $3.00 2.COKE                     $1.00 2.COKE                    $1.00<br>--------------------------------------  Current<br>---------------------- TOTAL                      $3.00 System<br>TOTAL                   $3.00  Print Data<br>1. Easy Auto Logo startup by trigger<br>Current System Print Data     of cutting command.<br>2. Center alignment Footer Logo 2<br>3. Executes Logo 2 printing<br>P G<br>4. Feeds paper to cutting position<br>    and performs partial cut.<br>5. Executes Logo 1 printing Header Logo 1<br>6. Recovery of position alignment<br>********************<br> MACDONALDS<br>T I<br>**----- End of picture text -----**<br>


――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-112 

<Example of Command Transmission> 

1) Set the Auto Logo function in advance and register it to the non-volatile memory. ESC GS / 1 n (n=0x01) Auto Logo Function ON ESC GS / 2 n ( n=“/” ) Specify Auto Logo Command Character (“/”) ESC GS / 3 nL nH d1 d2... dk User Macro 1 Definition nL=4  nH=0 Registered Macro Count = 4 Bytes d1=0x1b  d2=0x1d  d2=0x61  d3=0x01 Registered Macro <ESC GS a 1: Center Alignment> ESC GS / 4 nL nH d1 d2... dk User Macro 2 Definition nL=12  nH=0 Registered Macro Count = 12 Bytes d1=0x1b  d2=0x64  d3=0x03 Registered Macro <ESC d 3: Cutting position partial cut> d4=0x1b  d5=0x1c  d6=0x70  d7=0x01  d8=0x00 <ESC FS p 1 0: Print Logo 1 d9=0x1b  d10=0x1d  d11=0x61  d12=0x00 <ESC GS a 0: Left Alignment> ESC GS / 5 n (n=0x01) Auto Logo Command Character, Space Switch ESC GS / 6 n ( n=0x01) Partial Cut Before Auto Logo Printing Valid ESC GS / W Register Auto Logo Definition Data to Non-volatile Memory 

2) Send registered command character embedded in print data “CHEESE BURGER /2” → “/” is recognized as a command character. Command characters are replaced by spaces. “2” specifies Logo 2. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-113 

## **ESC GS / W** 

[Name] Register Auto Logo setting to non-volatile memory [Code] ASCII ESC GS / W Hex. 1b 1d 2f 57 Decimal 27 29 47 87 [Defined Area] - - - [Initial Value] - - - [Function] Registers Auto Logo setting to non-volatile memory After registration, the printer is reset. This command is ignored when Auto Logo is being executed. 

## **ESC GS / C** 

[Name] Initialize Auto Logo setting to non-volatile memory [Code] ASCII ESC GS / C Hex. 1b 1d 2f 43 Decimal 27 29 47 67 [Defined Area] - - - [Initial Value] - - - [Function] Initializes registered data in the non-volatile memory of the Auto Logo function. After initialization, the printer is reset. 

This command is ignored when Auto Logo is being executed. 

The default values of the Auto Logo function are below. 

|Setting|Initial Value|
|---|---|
|Auto Logo Function|OFF|
|Command Character|None|
|User Macro1|None|
|User Macro2|None|
|Command CharacterSwitch|No print|
|PartialCutBeforeAutoLogoPrinting|Disabled|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-114 

**ESC GS / 1  n** [Name] Auto Logo Function On/Off Setting [Code] ASCII ESC GS / 1 n Hex. 1b 1d 2f 31 n Decimal 27 29 47 49 n 

[Defined Area] 0 ≤ n ≤ 2 [Initial Value] n = 0 [Function] Turns the Auto Logo function on and off. 

This command is registered to the non-volatile memory by the <ESC> <GS> / W command. When in raster mode, the Auto Logo function is invalid. 

This command is ignored when Auto Logo is being executed. 

|n|Setting|
|---|---|
|0|AutoLogoFunctionOFF|
|1|Standard Auto Logo Function ON<br><Operation Specifications><br>1. Start up the Auto Logo function using the current system cut command<br>as a trigger<br>2. Prints if there is print data in the image buffer<br>3. Executes user macro 1<br>4. Prints the Auto Logo<br>5. Executes user macro 2|
|2|Simple Auto Logo Function ON<br><Operation Specifications><br>1. Start up the Auto Logo function using the current system cut command<br>as a trigger<br>2. Prints if there is print data in the image buffer<br>3. Execute center alignment<br>4. Print Logo 2 (When 2 color printing is set: Logo3)<br>5. Feed paper to cutting position and executes a partial cut<br>6. Print Logo 1<br>7. Recover position alignment setting<br>Note:<br>• With this setting, user macro and command character are invalid.<br>(“/” is printed as a character if the command character is set to “/” when<br>setting.)|



The commands that are the triggers for the Auto Logo function are below. 

When the standard Auto Logo Function is turned on by n = 1, the following trigger commands function only as triggers and do not cut paper. Therefore, it is necessary to register any cut command to the user macro 2. When the simple Auto Logo Function is turned on by n = 2, the following cut commands are executed and are the triggers for the simple Auto Logo function. 

- <ESC> d n: Cut command 

- <FF>: When allocated to the cutting function 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-115 

|**ESC GS / 2  n**|**ESC GS / 2  n**|**ESC GS / 2  n**||
|---|---|---|---|
|[Name]|Set command character|||
|[Code]|ASCII<br>ESC GS<br>/<br>3<br>n|||
||Hex.|Hex.<br>1b<br>1d<br>2f<br>32<br>n||
||Decimal<br>27<br>29<br>47<br>50<br>n|||
|[Defined Area]||32≤<br> n≤<br> 127, n = 0||
|[Initial Value]||n = 0||
|[Function]||Sets the Auto Logo function command character.||
|||This command is registered to the non-volatile memory by the “<ESC> <GS> / W” command.||
|||This command is ignored when Auto Logo is beingexecuted.||
|||n<br>Setting||
|||32 to 127<br>Command Character||
|||0<br>No Command CharacterSetting||
|||A command character is a character that is a command for specifying the logo number to print with||
|||the Auto Logo printing.||
|||When “/” is specified as the command character, “/2/3” is embedded in the print data.||
|||The printer does not process the “/” as character data but as a command and stores number that||
|||follows at the end and prints it as an Auto Logo in the order that it is stored.  Therefore, if “/2/3” is||
|||embedded, Auto Logo will print Logo2 and Logo3 in that order. If the specified logo has not been||
|||registered, logo printing will be ignored.||
|||Also, if there is no set command character setting, a logo will not be printed.||
|||Note that “/2/3” is processed as a command is not printed.||
|||However, using the “<ESC> <GS> /5 n ” command it is possible to switch “/2/3” to a space.||
|||In the same way as with “/2/3/2/2” if a logo is duplicated, only the initial logo is printed.||
|||A maximum of 32 logos can be stored as Auto Logos.||
|||Continuing after the command character, the following shows the defined area of the character d|Continuing after the command character, the following shows the defined area of the character d|
|||that specifies the logo number.||
|||“1”≤<br> d≤<br> “9”<br>(49≤<br> d≤<br> 57) → Logo number 1 to 9||
|||“A”≤<br> d≤<br> “F”<br>(65≤<br> d≤<br> 70) → Logo number 10 to 16||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-116 

|**ESC GS /  3  nL  nH  d1 d2 … dk**|**ESC GS /  3  nL  nH  d1 d2 … dk**|**ESC GS /  3  nL  nH  d1 d2 … dk**|**ESC GS /  3  nL  nH  d1 d2 … dk**|**ESC GS /  3  nL  nH  d1 d2 … dk**||||
|---|---|---|---|---|---|---|---|
|[Name]|Set user macro 1|||||||
|[Code]|ASCII|ESC GS<br>/|3<br>nL<br>nH|d1|d2|...|dk|
||Hex.|1b<br>1d<br>2f|33<br>nL<br>nH|d1|d2|...|dk|
||Decimal<br>27<br>29<br>47||51<br>nL<br>nH|d1|d2|...|dk|
|[Defined Area]||1≤<br> n≤<br>64||||||
|||nH = 0||||||
|||1≤<br> (nL + nH x 256)≤<br>|64|||||
|||dk = (nL + nH x 256)|dk = (nL + nH x 256)|||||
|||0≤<br> d≤<br>255||||||
|[Initial Value]||No user macro 1 setting||||||
|[Function]||Sets the user macro 1 of the Auto Logo function.|Sets the user macro 1 of the Auto Logo function.|||||
|||This command is registered to the non-volatile memory by the “<ESC> <GS> / W” command.|||||This command is registered to the non-volatile memory by the “<ESC> <GS> / W” command.|
|||This command is ignored when Auto Logo is being executed.||||This command is ignored when Auto Logo is being executed.||
|||Registers print data in user macro 1.|Registers print data in user macro 1.|||||
|||A maximum of 64 bytes of data can be registered.||||||
|||Note that it is prohibited to register Auto Logo command characters in a user macro.||||||



|**ESC GS /  4  nL  nH  d1 d2 … dk**|**ESC GS /  4  nL  nH  d1 d2 … dk**|**ESC GS /  4  nL  nH  d1 d2 … dk**|**ESC GS /  4  nL  nH  d1 d2 … dk**|**ESC GS /  4  nL  nH  d1 d2 … dk**||||
|---|---|---|---|---|---|---|---|
|[Name]|Set user macro 2|||||||
|[Code]|ASCII|ESC GS<br>/|4<br>nL<br>nH|d1|d2|...|dk|
||Hex.|1b<br>1d<br>2f|34<br>nL<br>nH|d1|d2|...|dk|
||Decimal<br>27<br>29<br>47||52<br>nL<br>nH|d1|d2|...|dk|
|[Defined Area]||1≤<br> nL≤<br> 64||||||
|||nH = 0||||||
|||1≤<br> (nL + nH x 256)≤<br>|64|||||
|||dk = (nL + nH x 256)|dk = (nL + nH x 256)|||||
|||0≤<br> d≤<br>255||||||
|[Initial Value]||No user macro 2 setting||||||
|[Function]||Sets the user macro 2 of the Auto Logo function.|Sets the user macro 2 of the Auto Logo function.|||||
|||This command is registered to the non-volatile memory by the “<ESC> <GS> / W” command.|||||This command is registered to the non-volatile memory by the “<ESC> <GS> / W” command.|
|||This command is ignored when Auto Logo is being executed.||||This command is ignored when Auto Logo is being executed.||
|||Registers print data in user macro 2.|Registers print data in user macro 2.|||||
|||A maximum of 64 bytes of data can be registered.||||||
|||Note that it is prohibited to register Auto Logo command characters in a user macro.||||||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-117 

## **ESC GS / 5  n** 

|[Name]|Set command character switching method|Set command character switching method|Set command character switching method|Set command character switching method|Set command character switching method|Set command character switching method|
|---|---|---|---|---|---|---|
|[Code]|ASCII||ESC GS|ESC GS||ESC GS<br>/<br>5<br>n|
||Hex.||1b|1d||1d<br>2f<br>35<br>n|
||Decimal||27|29||29<br>47<br>53<br>n|
|[Defined Area]||0≤<br>|n≤<br>1||||
|[Initial Value]||n = 0|n = 0||||
|[Function]||Sets the Auto Logo function command character switching method.|||Sets the Auto Logo function command character switching method.||
|||This command is registered to the non-volatile memory by the “<ESC> <GS> / W” command.|||||
|||This command is ignored when Auto Logo is beingexecuted.|||||
|||n||||Setting|
|||0||||Does not print the command character and the following logo number|
|||1||||Switches the command character and the following logo number into a space|
|||||||character(0x 20)|



When “/” is specified as the command character, the “/2” embedded in the print data is not a character string, but processed as a command. 

At this time, “/2” is processed as a command is not printed. 

However, by specifying n = 1 in this command, it is possible to switch “/2” to a space. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-118 

## **ESC GS / 6  n** 

[Name] Set partial cut before Auto Logo printing [Code] ASCII ESC GS / 6 n Hex. 1b 1d 2f 36 n Decimal 27 29 47 54 n 

**==> picture [471 x 528] intentionally omitted <==**

**----- Start of picture text -----**<br>
[Defined Area]  0 ≤ n ≤ 1<br>[Initial Value]  n = 0<br>[Function]  Sets a partial cut before the Auto Logo printing.<br>This command is registered to the non-volatile memory by the “<ESC> <GS> / W” command.<br>This command is ignored when Auto Logo is being executed.<br>n  Setting<br>0  Does not execute a partial cut before the Auto Logo printing.<br>1  Executes a partial cut before the Auto Logo printing.<br>a<br>When printing Logo2 and Logo3 as Auto Logo printing like the one in the drawing below, this<br>command selects to execute a partial cut before printing Logo2 of the Auto Logo and Logo3.<br>If a partial cut is executed using this function, it is possible to provide coupons, etc., that are printed<br>using Auto Logo with a partial cut.<br>Header<br>oT<br>***************<br>********************<br> MACDONALDS<br> MACDONALDS<br>******************** ***************<br>1.CHEESEBURGER  $2.00 1.CHEESBUGER       $2.00<br>2.COKE                      $1.00 2.COKE                    $1.00<br>--------------------------------------<br>TOTAL                       $3.00----------------------<br>TOTAL                   $3.00<br>1. Starts Auto Logo with trigger<br>    of cutting command. Partial Cut<br>2. Executes user macro 1.<br>     Header Cheeseburger  Prints Logo 2<br>Partial Cut<br>3. Prints Auto Logo<br>COKE Prints Logo 3<br>|<br>4. Executes user macro 2.- Executes cut. __<br>- Executes Header logo  Header<br>       printing.<br>********************<br> MACDONALDS<br>**----- End of picture text -----**<br>


――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-119 

## **3.11. Two-dimensional Bar Code PDF417 Command Details** 

This command prints two-dimensional bar code PDF417. 

There are four types of commands, according to functions, for two-dimensional bar code PDF417. 

- (1) Bar code type setting 

- (2) Bar code data setting 

- (3) Bar code printing 

- (4) Bar code expansion information acquisition 

(<ESC> <GS> “x” “S”) 

- (<ESC> <GS> “x” “D”) (<ESC> <GS> “x” “P”) (<ESC> <GS> “x” “I”) 

The following describes the functions in detail. 

## (1) Bar code type setting 

These commands set the bar code type. Because these are all set with default values, they should be used only when it is necessary to change.  (Refer to section below for details on each setting.) 

**==> picture [312 x 89] intentionally omitted <==**

**----- Start of picture text -----**<br>
p1<br>START  p2  STOP<br>**----- End of picture text -----**<br>


PDF417 is configured by a fixed bar pattern for starting and stopping, and a bar pattern called a code word. Code words are configured by 17 modules. 

**==> picture [115 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
4  1 1 1 1 1 3   5<br>**----- End of picture text -----**<br>


Code Word 

<ESC> <GS> “x” “S” “0” specifies values of p1 and p2. 

USE_LIMITS mode specify the ratio of p1 and p2.  USE_FIXED mode specifies p1 (line count) and p2 (code word count per line). 

<ESC> <GS> “x” “S” “1” specifies values of error correction levels. 

PDF417 can read information even if a portion of the data is corrupted by using the error correction. 

By increasing this level, the bar code size increases because there is more preparatory information. 

<ESC> <GS> “x” “S” “2” and <ESC> <GS> “x” “S” “3” specify the size of the module that configures the code word. The X direction size (in dot increments) is determined by <ESC> <GS> “x” “S” “2” for the module, and <ESC> <GS> “x” “S” “3” specifies the Y direction size from the aspect. 

Module size setting is the basis for the bar code image that is generated, so the resulting print will vary according to that setting. 

Printable size of bar code 

Vertical Size [dots] Horizontal Size [dots] ~~—~~ 640 640 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-120 

The settings above are set individually, so the errors described below may be generated even if there is no particular problem in those settings.  In such case, if the bar code is generated the (3) print command (<ESC> <GS> “x” “P”) is ignored. 

- Error is generated when generating a bar code, due to the combination of the bar code setting commands. 

- The bar code data that is generated exceeds the printable size of PDF417. 

- Print data exceeds the currently set print region. 

It is recommended to use (4) Bar code expansion information acquisition (<ESC> <GS> “x” “I”) as a means for checking these errors prior to printing. 

## (2) Bar code data setting command 

This command sets the print data of the bar code. 

## (3) Bar code print command 

This command prints the bar code according to the settings of (1) and (2). 

## (4) Bar code expansion information acquisition 

This command checks whether it is possible to print the bar code according to the settings of (1) and (2). 

- Precautions for use of commands - 

- Unless the following operations are performed, the setting values are maintained for (1) and (2). 

- Sending of new setting commands 

- Sending an initializing command (<ESC> @, <CAN>) 

- The power is turned off 

- Sending (3) and (4) when needed 

- Printing 

- When printing, position shifting according to the horizontal tab, absolute position specification, relative position specification, and position alignment is valid. 

- Upside-down printing and two-color printing are possible. 

- When a bar code is printed, always verify it by actual use. 

Send the command transmission example last. 

## 1. Bar code type setting 

<ESC> <GS> “x” “S” “0” 0 2 3: Sets the bar code size to USE_LIMITS = 2:3 <ESC> <GS> “x” “S” “1” 3: Sets ECC level to 3 <ESC> <GS> “x” “S” “2” 3: Sets the module X direction size to 3 dots <ESC> <GS> “x” “S” “3” 3: Sets module aspect ratio to 3 

2. Bar code data setting 

<ESC> <GS> “x” “D” 10 0 “0123456789”: Sets the bar code data 

## 3. Printing bar code 

To verify whether printing is possible with the current settings, check the bar code expansion information <ESC> <GS> “x” “I”: Bar code expansion information check <ESC> <GS> “x” “P”: Print 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-121 

## **ESC GS x S 0 n p1 p2** 

[Name] Set PDF417 bar code size [Code] ASCII ESC GS x S 0 n p1 p2 Hex. 1B 1D 78 53 30 n p1 p2 Decimal 27 29 120 83 48 n p1 p2 [Defined Area] n = 0, 1 

When n = 0: 1 ≤ p1 ≤ 99, 1 ≤ p2 ≤ 99 When n = 1: p1 = 0 or 3 ≤ p1 ≤ 90, p2 = 0 or 1 ≤ p2 ≤ 30 (However, this excludes p1 = p2 = 0) 

[Initial Value] n = 0, p1 = 1, p2 = 2 [Function] Parameter details 

|n<br>(SpecifyMethod to SpecifyBar Code Size)|p1, p2<br>(Size Specification)|
|---|---|
|0<br>USE_LIMITS<br>(Specify<br>ratio<br>of<br>bar<br>code<br>horizontallyand vertically)|p1:  p2:  Proportions of Vertical (p1) and Horizontal (p2)<br>However, p1:  p2 = 1:  99 to 10 : 1 (p1/p2 = 0.01 to 10)|
|1<br>USE_FIXED<br>(Specifies number of lines and<br>number of columns of bar code.)|p1:  Number of lines (0, 3 to 90), p2: Number of columns (0, 1<br>to 30)<br>However, p1 * p2≤<br> 928<br>When either p1 or p2 specifies 0, it indicates that that setting<br>value is variable.|



Setting the bar code size using this command specifies the general size of the bar code.  The size will automatically be corrected according to the other settings. 

## **ESC GS x S 1 n** 

[Name] Set PDF417 ECC (security level) [Code] ASCII ESC GS x S 1 n Hex. 1B 1D 78 53 31 n Decimal 27 29 120 83 49 n [Defined Area] 0 ≤ n ≤ 8 [Initial Value] n = 1 [Function] Parameter details • n: ECC level (0 to 8) 

## **ESC GS x S 2 n** 

[Name] Set PDF417 module X direction size [Code] ASCII ESC GS x S 2 n Hex. 1B 1D 78 53 32 n Decimal 27 29 120 83 50 n 

[Defined Area] 1 ≤ n ≤ 10 [Initial Value] n = 2 [Function] Parameter details 

• n: Sets the module X direction size (x-dim). Units: Dots It is recommended that 2 ≤ n when specifying using this command. When using with n = 1, check by actual use. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-122 

**ESC GS x S 3 n** 

[Name] Set PDF417 module aspect ratio [Code] ASCII ESC GS x S 3 n Hex. 1B 1D 78 53 33 n Decimal 27 29 120 83 51 n [Defined Area] 1 ≤ n ≤ 10 [Initial Value] n = 3 [Function] Parameter details • n: Sets the module aspect ratio (asp). The module Y direction size (x-dim x asp) is set using this command. It is recommended that 2 ≤ n when specifying using this command. When using with n = 1, check by actual use. 

**ESC GS x D nL nH d1 d2 … dk** 

[Name] Set PDF417 bar code data [Code] ASCII ESC GS x D nL nH d1 d2 … dk Hex. 1B 1D 78 44 nL nH d1 d2 … dk Decimal 27 29 120 68 nL nH d1 d2 … dk [Defined Area] 0 ≤ nL ≤ 255, 0 ≤ nH ≤ 255 1 ≤ (nL + nH x 256) ≤ 1024 0 ≤ d ≤ 255 1 ≤ k ≤ 1024 [Initial Value] --[Function] Parameter details • nL + nH x 256 : Bar code data count • dk : Bar code data (Maximum 1024 data) When [nL + nH x 256] is outside of the definition, data of [nL + nH x 256] bytes is discarded. 

|**ESC GS x P**|**ESC GS x P**|**ESC GS x P**||
|---|---|---|---|
|[Name]|Print PDF417 bar code|||
|[Code]|ASCII|ESC<br>GS<br>x|P|
||Hex.|1B<br>1D<br>78|50|
||Decimal|Decimal<br>27<br>29<br>120|80|
|[Defined Area]||---||
|[Initial Value]||---||
|[Function]|[Function]|Prints the bar code data.|Prints the bar code data.|
|||If there is unprinted data in the line buffer, this command is executed after printing that data in the|If there is unprinted data in the line buffer, this command is executed after printing that data in the|
|||line buffer. Therefore, it is not possible to print with other data in the same line (characters, bit||
|||images, bar codes).||
|||Also, this command is ignored if the following errors occur.||
|||• When an error is generated when generating a bar code, due to the combination of the bar code||
|||setting commands||
|||• When the bar code data that is generated exceeds the printable size of PDF417||
|||• When the print data exceeds the currently set print region||
|||When a bar code is printed, always verify it by actual use.||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-123 

## **ESC GS x I** 

[Name] Get PDF417 bar code expansion information [Code] ASCII ESC GS x I Hex. 1B 1D 78 49 Decimal 27 29 120 73 

[Defined Area] --[Initial Value] --[Function] When printing a bar code with the current settings and at the print starting position using this command, error information is sent to the printer.  Therefore, it is possible to check whether it is possible to print before actually printing, by using this command. 

If an error occurs, this command is discarded even if the print command (<ESC> <GS> “x” “P”) is sent. 

If the following errors occur, “Error” information is sent to the printer. 

• When an error is generated when generating a bar code, due to the combination of the bar code setting commands. 

- When the bar code data that is generated exceeds the printable size of PDF417. 

- When the print data exceeds the currently set print region 

Transmission format: <ESC> <GS> “x” “I” n 

|n||
|---|---|
|0|No Error|
|1|Error|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-124 

## **3.12. Details of the Print Starting Trigger Control Command** 

This command is for models equipped with an expansion control function for page control of line unit commands, by controlling the image buffer by page. 

## **ESC GS g 0 m n** 

[Name] Print starting trigger [Code] ASCII ESC GS g 0 m n Hex. 1B 1D 67 30 m n Decimal 27 29 103 48 m n [Defined Area] m = 0, n = 0 [Initial Value] --[Function] Starts printing when there is unprinted data in the image buffer. It is prohibited to send this command while in the raster mode. 

## **ESC GS g 1 m n** 

[Name] Print starting timer [Code] ASCII ESC GS g 1 m n Hex. 1B 1D 67 31 m n Decimal 27 29 103 49 m n [Defined Area] m = 0, 0 ≤ n ≤ 255 [Initial Value] Depends on the model [Function] Sets the print starting timer specified at n x 10 msec. 

The print starting timer starts measuring from the point where the print data reception stops, and measures up to the set print starting timer. 

When the set print starting timer is reached, the printer starts printing if there is unprinted data in the image buffer. 

It is prohibited to send this command while in the raster mode. 

|n|OperatingMode|
|---|---|
|0|Print starting timer=initial value|
|1 to255|Printstartingtimer  n x 10msec.|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-125 

## **3.13. Two-Dimensional Bar Code QR Code Command Details** 

* Note that QR code is a registered trademark of DENSO WEB. 

This command is for printing 2-dimensional bar code QR codes.  There are four functions of the commands relating to the 2-dimensional bar code QR codes, shown below. 

(1) Set bar code type (<ESC> <GS> “y” “S”) (2) Set bar code data (<ESC> <GS> “y” “D”) (3) Set page mode (Reserved) (4) Print Bar code (<ESC> <GS> “y” “P”) (5) Set bar code type (<ESC> <GS> “y” “I”) 

The details of each function are described below. 

## (1) Set bar code type 

These commands set the bar code type.  Because all initial values are set, use these only to make changes.  (See the details for each setting below.) 

**==> picture [75 x 56] intentionally omitted <==**

**----- Start of picture text -----**<br>
Cell<br>Alignment Pattern<br>**----- End of picture text -----**<br>


<ESC> <GS> “y” “S” “0” Sets the model 

Currently supported models are model 1 and model 2.  Model 2 has a configuration including an alignment bar to improve its support of weight to handle skewing when codes are large. 

<ESC> <GS> “y” “S” “1”  Sets the error correction level 

QR codes can be read even if a part of the data is corrupted, by using error correction.  Raising this level increases the size of the bar code because there is an increase in preparatory information. 

<ESC> <GS> “y” “S” “2”  Specifies the size of the cell (One four squared region configuring the QR code) The QR code is formed into a square of an equivalent size in the vertical and horizontal directions, but the size of the bar code image that is generated depends on the cell size setting.  See Appendix 7 for details on the actual printed size of the QR code. 

These settings are individual settings.  Therefore, even though there may not be any particular problem in each of them, there is the potential for an error to be generated.  (See the descriptions below.)  In such cases, the bar code will not be generated and the (4) Print command (<ESC> <GS> “y” “P”) is ignored.  With the (5) Get bar code expansion information command, an error code is returned. 

- Error is generated when generating a bar code by the combination of each setting command. 

- Print data exceeds the currently set print region 

Therefore, it is recommended to use (5) Get bar code expansion information command (<ESC> <GS> “y” “I”) as a means for checking for these errors prior to printing. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-126 

## (2) Set bar code data 

This command sets the bar code print data.  There are four types of data that can be set using QR codes.  They are: numbers; English characters; binary; and Kanji.  Furthermore, there are two types of data setting methods.  One is to specify these along with the bar code data (data manual analysis), and the other is to specify only the bar code data (data automatic analysis). 

## (3) Set page mode 

This command is not used. 

## (4) Print Bar code 

This command prints bar codes based on the settings of (1) to (3). 

## (5) Set bar code type 

This command confirms whether to print bar codes based on the settings of (1) to (3). 

- = Precautions on using these commands = 

- The setting values for (1) to (3) are held unless any of the following operations are performed. 

   - Sending a new setting command 

   - Sending an initialize command (<ESC> @, <CAN>) 

   - Turning the power OFF 

- When there is an error in sending a command with (2), the set data is cleared and the command itself is disabled. 

- (4) and (5) are sent when necessary. 

## • Printing: 

   - When printing, position movement using specify absolute position, specify relative position, and align position are enabled. 

   - Upside down printing and 2-color printing are possible. 

- Printed bar codes should always be checked in an actual use. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-127 

The following is an example showing the sending of the commands. 

|(1)|Set bar code type|||
|---|---|---|---|
||<ESC> <GS> “y” “S” “0” 1|Sets to model 1.||
||<ESC> <GS> “y” “S” “1” 0|Sets mistake correction level to L.||
||<ESC> <GS> “y” “S” “2” 3|Sets cell size to 3 dots.||
|(2)|Set bar code data|||
||• <ESC> <GS> “y” “D” “1” 0 20 0  “2005, January, 1 (SAT)” <LF>|• <ESC> <GS> “y” “D” “1” 0 20 0  “2005, January, 1 (SAT)” <LF>||
|||Sets bar code data (Data automatic analysis)|Sets bar code data (Data automatic analysis)|
|||Sets bar code data (Data manual analysis)|Sets bar code data (Data manual analysis)|
||• <ESC> <GS> “y” “D” “2” 10|1 4 0|“2005” “,”|
||4 2 0|“Year” “,”||
||1 1 0|“1” “,”||
||4 2 0|“Month” “,”||
||1 1 0|“1” “,”||
||4 2 0|“Day” “,”|“Day” “,”|
||4 2 0|“(” “,”||
||2 3 0|“SAT” “,”|“SAT” “,”|
||4 2 0|“)” “,”||
||3 1 0|<LF>||



## (3) Print bar code 

To verify whether to print with the current settings, check the bar code expansion information. 

<ESC> <GS> “y” “I” Check bar code expansion information <ESC> <GS> “y” “p” Print 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 3-128 

## **ESC GS y S 0 n** 

[Name] Set QR code model [Code] ASCII ESC GS y S 0 n Hex. 1B 1D 79 53 30 n Decimal 27 29 121 83 48 n [Defined Area] 1 ≤ n ≤ 2 [Initial Value] n = 2 [Function] Sets the model. • Parameter details 

|n|SetModel|
|---|---|
|1|Model 1|
|2|Model 2|



## **ESC GS y S 1 n** 

[Name] Set QR code mistake correction level [Code] ASCII ESC GS y S 1 n Hex. 1B 1D 79 53 31 n Decimal 27 29 121 83 49 n [Defined Area] 0 ≤ n ≤ 3 [Initial Value] n = 0 [Function] Sets the mistake correction level. • Parameter details 

|n|Mistake Correction Level|Mistake Correction Rate (%)|
|---|---|---|
|0|L|7|
|1|M|15|
|2|Q|25|
|3|H|30|



## **ESC GS y S 2 n** 

[Name] Set QR code cell size [Code] ASCII ESC GS y S 2 n Hex. 1B 1D 79 53 32 n Decimal 27 29 121 83 50 n [Defined Area] 1 ≤ n ≤ 8 [Initial Value] n = 3 [Function] Sets the cell size. • Parameter details 

• n: Cell size (Units: Dots) 

• It is recommended that the specification using this command be 3 ≤ n. If n = 1 or 2, check by actually using. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-129 

|**ESC GS y D 1 m nL nH d1 d2 … dk**|**ESC GS y D 1 m nL nH d1 d2 … dk**|**ESC GS y D 1 m nL nH d1 d2 … dk**|||||
|---|---|---|---|---|---|---|
|[Name]|Set QR code cell size (Auto Setting)||||||
|[Code]|ASCII|ESC GS<br>y<br>D<br>1<br>m<br>nL<br>nH|d1|d2|…|dk|
||Hex.|1B<br>1D<br>79<br>44<br>31<br>m<br>nL<br>nH|d1|d2|…|dk|
||Decimal|Decimal<br>27<br>29 121<br>68<br>49<br>m<br>nL<br>nH|d1|d2|…|dk|
|[Defined Area]||m = 0|||||
|||0≤<br> nL≤<br> 255, 0≤<br> nH≤<br> 255|||||
|||1≤<br> nL + nH x 256≤<br> 7089 (k = nL + nH x 256)|||||
|||0≤<br> d≤<br> 255|||||
|[Initial Value]||---|||||
|[Function]|[Function]|Automatically expands the data type of the bar code and sets the data.|||Automatically expands the data type of the bar code and sets the data.||
|||• Parameter details|||||
|||• nL + nH x 256: Byte count of bar code data|||||
|||• dk: Bar code data (Max. 7089 bytes)|||||
|||• When using this command, the printer receives data for the number of bytes (k) specified by nL|||||
|||and nH.  The data automatically expands to be set as the bar code data.|||||
|||• Indicates the number bytes of data specified by the nL and nH.|• Indicates the number bytes of data specified by the nL and nH.|||• Indicates the number bytes of data specified by the nL and nH.|
|||Bar code data is cleared at this time.|||||
|||• The data storage region of this command is shared with the manual setting command so data is|||||
|||updated each time either command is executed.|||||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-130 

**ESC GS y D 2 a m1 n1L n1H d11 d12 • • • d1k m2 n2L n2H d21 d22 • • • d2k ml • • • dlk** [Name] Set QR code cell size (Manual setting) [Code] ASCII E S C G S y D 2 a m 1 n 1 L n 1 H d 11 d 1 2 … d 1 K Hex. 1 B 1 D 7 9 4 4 3 2 a m 1 n 1 L n 1 H d 11 d 1 2 … d 1 K Decimal 2 7 2 9 1 2 1 6 8 5 0 a m 1 n 1 L n 1 H d 11 d 1 2 … d 1 K ASCII m 2 n 2 L n 2 H D 2 1 d 2 2 … d 2 K m l … d k l Hex. m 2 n 2 L n 2 H D 2 1 d 2 2 … d 2 K m l … d k l Decimal m 2 n 2 L n 2 H D 11 d 2 2 … d 2 K m l … d k l 

[Defined Area] 1 ≤ a ≤ 255 1 ≤ m ≤ 4 0 ≤ nL ≤ 255, 0 ≤ nH ≤ 255 1 ≤ nL + nH x 256 ≤ 7089 (k = nL + nH x 256) 0 ≤ d ≤ 255 1 ≤ I ≤ 255 [Initial Value] --[Function] Specifies the bar code data type and sets the data. • Parameter details • a: Block count • m: Input data type • nL + nH x 256: Bar code data byte count • dk: Bar code data (Max. 7089 bytes) 

|m|Data Type|Data Definition Region(d)|
|---|---|---|
|1|Numbers|“0” to “9”|
|2|English Characters|“”,“$”,“%” “*”,“+”,“-“ “.” “/”,“:”,“0” to “9”,“A” to “Z”,|
|3|Binary|0x00 to 0xFF|
|4|Kanji(Shift JIS)|0x8140 to 0x9FFC, 0xE040 to 0xEBBF<br>However, the lower 8 bits are 0x40 to 0x7E, and 0x80<br>to 0xFC|
||||



- The printer receives the data type specified by m, and the data of the number of bytes (k) specified by nL and nH, based on the block count specified by a. 

• 1 block specified by a indicates m1, n1L, n1H, d11 • • • d1k (data type + data count + bar code data), and by continuously sending these a multiple of times, one bar code data can mix data types. • It is possible to set a maximum of 255 blocks with one command transmission. 

• nL and nH specify the number of bytes of the data, so when using Kanji, calculate that 1 character has 2 bytes. 

- If this command is outside of the definition region, immediately stop the command analysis process. 

When doing so, the bar code data is cleared. 

- This command data storage region is shared with the automatic setting command, so data is updated each time either command is executed. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-131 

## **ESC GS y P** 

[Name] Print QR code [Code] ASCII ESC GS y P Hex. 1B 1D 79 50 Decimal 27 29 121 80 

[Defined Area] --[Initial Value] --[Function] Prints bar code data. 

When receiving this command, if there is unprinted data in the image buffer, the printer will print the bar code after printing the unprinted print data. 

A margin of more than 4 cells is required around the QR code.  The user should ensure that space. Always check printed bar codes in actual use. 

## **ESC GS y I** 

[Name] Get QR code expansion information [Code] ASCII ESC GS y I Hex. 1B 1D 79 49 Decimal 27 29 121 73 

[Defined Area] --[Initial Value] --[Function] Sends information on generated image sizes and errors in bar code expansion using the current settings.  Therefore, it is possible to check whether printing is possible prior to actual printing.  If there is an error in the expanded bar code, this command is ignored even if the expand command (<ESC> <GS> “y” “P”) is sent. 

In the even that errors like the ones below occurs, “Error” information is sent to the printer. 

• When there is an error in generating a bar code by the combination of bar code setting commands. 

- When the generated bar code data exceeds the printable size 

Sending Format: <ESC> <GS> “y” “I” n1 n2 

|Sending Format: <ESC> <GS> “y” “I” n1 n2g Format: <ESC> <GS> “y” “I” n1 n2Format: <ESC> <GS> “y” “I” n1 n2|Sending Format: <ESC> <GS> “y” “I” n1 n2g Format: <ESC> <GS> “y” “I” n1 n2Format: <ESC> <GS> “y” “I” n1 n2y” “I” n1 n2” “I” n1 n2|
|---|---|
|n1 n2|Bar Code Information|
|0x0000|Error|
|0x0001 to 0xffff|Size aroundgenerated bar code(Units: Dots)|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-132 

## **3.14. Page Function Command Details** 

## **ESC GS h 0 k m n** 

[Name] 180 degree turnover [Code] ASCII ESC GS h 0 k m n Hex. 1B 1D 68 30 k m n Decimal 27 29 104 48 k m n 

[Defined Area] 0 ≤ k ≤ 1, m = 0, n = 0 [Initial Value] --[Function] Sets 180 degree turnover function to be valid/invalid. 

|n|180 Degree Turnover Function|
|---|---|
|0|Invalid|
|1|Valid|



<180 Degree Turnover Function> 

When set to the 180 degree turnover function, that function is executed at the trigger. However, this function is effective for print data that can be contained in the image buffer length. Print data beyond the image buffer length is unaffected by this function. 

Printing that is started other than the 180 degree turnover trigger ignores this function. 

## 180 degree turnover triggers 

- Cutter command: <ESC> d n • FF command: <FF> • BM detection command: <ESC> d n, <FF> • Print start command: <ESC> <GS> g 0 m n • Raster mode: When <FF> is executed. 

Use example 

1) When 180 degree turnover function is enabled: <ESC> <GS> h 0 k m n (k = 0x01, m = 0x00, n = 0x00) 2) Print data transfer: Print data (Print length is less than length of image buffer.) 3) Trigger command transfer: <ESC> d n (Cutter command is 180 degree turnover trigger.) 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-133 

## **3.15. Reduced Printing Function Command Details** 

## **ESC GS c h v** 

|**ESC GS c h v**|**ESC GS c h v**|**ESC GS c h v**|||
|---|---|---|---|---|
|[Name] Set reduced printing|[Name] Set reduced printing||||
|[Code]|ASCII|ESC GS<br>c|h|v|
||Hexadecima<br>1B<br>1D<br>63||h|v|
||l||||
||Decimal|27<br>29<br>99|h|v|
|[Defined Area]||0≤<br> h≤<br>255|||
|||0≤<br> v≤<br> 255|||
|[Initial Value]||h = 0 (Horizontal direction reduced printing setting invalid)|||
|||v = 0 (Vertical direction reduced printing setting invalid)|||
|[Function]||Set reduced printing|||
||h|Set horizontal direction reducedprinting|||
||0|Invalid|||
||1|Valid(67%)|||
||2 to 255|Command ignored|||
||||||
||v|Set vertical direction reduced|Set vertical direction reducedprinting||
||0|Invalid|||
||1|Valid(50%)|||
||2 to 255|Command ignored|||



• Reduced printing in the horizontal direction compresses the entire horizontal direction 67%. 

- Reduced printing in the vertical direction prints in Double Resolution mode, so this is invalid in low peak current mode and powered USB I/F. 

- Disabled in Page Mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-134 

## **3.16. Page Mode Command Details** 

## **ESC GS P 0** 

|**ESC GS P 0**|**ESC GS P 0**|**ESC GS P 0**||
|---|---|---|---|
|[Name] Selects page mode|[Name] Selects page mode|||
|[Code]|ASCII|ESC GS|P<br>0|
||Hexadecima<br>1B<br>1D||50<br>30|
||l|||
||Decimal|27<br>29|80<br>48|
|[Function]||Switches from standard mode to page mode.|Switches from standard mode to page mode.|
|||• Valid only when input at the top of the line.||
|||• Invalid when input in page mode.||
|||• Returns to standard mode after running this command.||
|||• ESC GS P 1 (selects standard mode)|• ESC GS P 1 (selects standard mode)|
|||• ESC GS P 7 (prints in page mode and recovers)|• ESC GS P 7 (prints in page mode and recovers)|
|||• The character expansion position uses the starting point specified by ESC GS P2 (selection of||
|||character print direction in page mode) in the print region specified by ESC GS P 3 (set print|character print direction in page mode) in the print region specified by ESC GS P 3 (set print|
|||region in page mode).|region in page mode).|
|||• Switches the following command setting values that have independent values for both page and|• Switches the following command setting values that have independent values for both page and|
|||standard modes to the setting values of page mode.||
|||• Set space amount:<br>ESC SP , ESC : , ESC M, ESC P, ESC g, ESC p, ESC s, ESC t||
|||• Set the line feed amount:<br>ESC z, ESC 0, ESC 1, ESC 2,||
|||• Set horizontal tab:<br>ESC D||
|||• The following commands are invalid in page mode.||
|||• VT:|Vertical tab|
|||• FF:|Form feed|
|||• ESC GS c:|Reduced Printing|
|||• ESC GS ) B:|• ESC GS ) B:<br>Text Search|
|||• ESC RS m:|BM setting|
|||• ESC RS A:|Printing Region Setting|
|||• ESC GS M:|Maintenance counter control|
|||• ESC GS r:|Get CRC|
|||• ESC GS %:|User ID|
|||• ESC GS *:|Print Mark|
|||• ESC RS C:|Set printing mode|
|||• ESC * r:|Related to raster mode|
|||• ESC RS r:|Set print speed|
|||• ESC RS L:|Lump print of logos|
|||• ESC FS p:|Print logo|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-135 

## **ESC GS P 1** 

[Name] Cancel page mode [Code] ASCII ESC GS P 1 Hexadecimal 1B 1D 50 31 Decimal 27 29 80 49 [Function] Cancels page mode. 

- Valid only when input in page mode. 

• Data expanded in page mode is erased. • After execution, the top of the line is positioned at the next print starting position. • Print region set by ESC GS P 3 (Set print region in page mode) is initialized. • Switches the following command setting values that have independent values for both standard and page modes to the setting values of standard mode. • Set space amount: ESC SP , ESC: , ESC M, ESC P, ESC g, ESC p, ESC s, ESC t • Set the line feed amount: ESC z, ESC 0, ESC 1, ESC 2, • Set horizontal tab: ESC D • The following commands are valid only when set in standard mode. • ESC GS P 3: Set print region in page mode • ESC GS P 2: Select character print direction in page mode • The following commands are ignored in standard mode. • ESC GS P 4: Specify character vertical direction absolute position in page mode • ESC GS P 5: Specify character vertical direction relative position in page mode • ESC GS P 6: Print data in page mode • ESC GS P 7: Print in page mode and recover • ESC GS P 8: Cancel print data in page mode 

- When power is turned on and when a reset is implemented, standard mode is selected when executing initialization (ESC @) of the printer. 

**ESC GS P 2 n** [Name] Select character print direction in page mode [Code] ASCII ESC GS P 2 Hexadecimal 1B 1D 50 32 Decimal 27 29 80 50 [Defined Area] 0 ≤ n ≤ 3, 48 ≤ n ≤ 51 [Initial Value] n = 0 [Function] Select character print direction and starting point in page mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-136 

|n|Printing<br>Direction|Starting Point|
|---|---|---|
|0, 48|Left to<br>Right|Upper Left<br>(Drawing at<br>Right A)|
|1, 49|Bottom to<br>Top|Bottom Left<br>(Drawing at<br>Right B)|
|2, 50|Right to<br>Left|Bottom Right<br>(Drawing at<br>Right C)|
|3, 51|Top to<br>Bottom|Top Right<br>(Drawing at<br>Right D)|



• When standard mode is selected, only internal printer flag operations are executed when this command is entered. 

In that case, printing in standard mode is unaffected. 

- The starting point in the print region specified by ESC GS P 3 (Set print region in page mode) is used for the start of character expansion. 

## **ESC GS P 3 xL xH yL yH dxL dxH dyL dyH** 

[Name] Select character print direction in page mode 

[Code] ASCII ESC GS P 3 Hexadecimal 1B 1D 50 33 Decimal 27 29 80 51 [Defined Area] 0 ≤ xL, xH, yL, yH, dxL, dxH, dyL, dyH ≤ 255 However, this excludes dxL = dxH = 0 or dyL = dyH = 0. [Initial Value] xL = xH = yL = yH = 0 See the table below for dxL, dxH, dyL, and dyH. [Function] Set print region in page mode Sets the position and size of the print region. • Horizontal starting point = [(xL + xH x 256) x 1/8] mm • Vertical starting point = [(yL + yH x 256) x 1/8] mm • Horizontal direction length = [(dxL + dxH x 256) x 1/8] mm • Vertical direction length = [(dyL + dyH x 256) x 1/8] mm 

• When standard mode is selected, only internal printer flag operations are executed when this command is entered. Has no affect on printing. • If the horizontal or vertical starting point is outside of the print region, invalidate all settings. • If the horizontal or vertical length direction is 0, invalidate all settings. 

- The character expansion stating point is the one specified by the selection of the character printing direction (ESC GS P 2) in page mode in the print region. 

• If the (horizontal direction starting point + horizontal direction length) exceeds the horizontal direction printable region, the (horizontal direction printable region – horizontal direction starting point) becomes the horizontal direction length. 

• If the (vertical direction starting point + vertical direction length) exceeds the vertical direction printable region, the (vertical direction printable region – vertical direction starting point) becomes the vertical direction length. 

• If the calculated results is a fraction, that is corrected to the minimum mechanical pitch and excess is discarded. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-137 

|Printing<br>Region<br>Set<br>(Memory<br>Switch<br>Setting)<br>~~|~~<br>~~po~~|Initial Value<br>~~{TJ} a~~|Initial Value<br>~~{TJ} a~~|Initial Value<br>~~{TJ} a~~|Initial Value<br>~~{TJ} a~~|Initial Value<br>~~{TJ} a~~|Initial Value<br>~~{TJ} a~~|Maximum Value<br>~~a~~|Maximum Value<br>~~a~~|
|---|---|---|---|---|---|---|---|---|
||dxL<br>~~{TJ}~~|dxH<br>~~{TJ}~~|dyL<br>~~{TJ}~~|dyH<br>~~{TJ} a~~|Printable Region Width<br>~~a~~||Printable Region Width<br>~~a~~||
||||||X<br>Direction<br>~~a~~|Y Direction<br>~~a~~|X<br>Direction<br>~~a~~|Y<br>Direction<br>~~a~~|
|72mm<br>~~| ~~<br>~~po~~<br>~~ee~~|64<br> ~~{TJ}~~<br>~~se~~|2<br>~~{TJ}~~<br>~~se~~|AA<br>~~{TJ}~~|3<br>~~{TJ} a~~|72mm<br>~~a~~|117.3mm<br>~~a~~|72mm<br>~~a~~|300mm<br>~~a~~|
|52.5mm<br>~~po~~<br>~~ee~~<br>~~ee es~~|164<br>~~se~~<br>~~es~~|1<br>~~se~~<br>~~eG~~|AA<br>~~eG~~|3<br>~~eG~~|52.5mm|117.3mm|52.5mm|300mm|
|50.8mm<br>~~ee ~~<br>~~ee es~~<br>~~Re~~|150<br> ~~se~~<br>~~es~~<br>~~se~~|1<br>~~se~~<br>~~eG~~<br>~~se~~|AA<br>~~eG~~<br>~~eG~~|3<br>~~eG~~<br>~~eG~~|50.8mm|117.3mm|50.8mm|300mm|
|52mm<br>~~ee es~~<br>~~Re~~<br>~~po~~|160<br>~~es ~~<br>~~se~~|1<br> ~~eG~~<br>~~se~~|AA<br>~~eG~~<br>~~eG~~|3<br>~~eG~~<br>~~eG~~|52mm|117.3mm|52mm|300mm|
|30mm<br>~~Re ~~<br>~~po~~|240<br> ~~se~~|0<br>~~se ~~|AA<br> ~~eG~~|3<br>~~eG~~|30mm|117.3mm|30mm|300mm|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

3-138 

## **ESC GS P 4 nL nH** 

|**ESC GS P 4 nL nH**|**ESC GS P 4 nL nH**|**ESC GS P 4 nL nH**|
|---|---|---|
|[Name] Specify character vertical direction absolute position in page mode|[Name] Specify character vertical direction absolute position in page mode||
|[Code]|ASCII|ESC GS<br>P<br>4|
||Hexadecima<br>1B<br>1D<br>50<br>34||
||l||
||Decimal|Decimal<br>27<br>29<br>80<br>52|
|[Defined Area]|[Defined Area]|0≤<br> nL≤<br> 255, 0≤<br> nH≤<br> 255|
|[Initial Value]||- - -|
|[Function]||Specify the position for character vertical direction of the data expansion starting position in page|
|||mode with the absolute position that uses the starting point as a reference.|
|||The position of the character vertical direction of the starting position for subsequent data|
|||expansion uses the position from the starting point [(nL + nH x 256) x 1/8]mm.|
|||• This command is ignored when page mode is not selected.|
|||• Absolute position specifications that exceed the specified print region are ignored.|
|||• The position of the character horizontal direction of the data expansion starting position does not|
|||move.|
|||• Specify the reference starting point using ESC GS P 2.|
|||• The following operations will occur depending on the starting point of ESC GS P 2|
|||(select character print direction in page mode).|
||a. When the starting point is “upper left” or “bottom right,” specify the absolute position of the paper feed||
||direction.||
||b. When the starting point is “upper right” or “bottom left,” specify the absolute position of the|b. When the starting point is “upper right” or “bottom left,” specify the absolute position of the|
||perpendicular direction to the paper feed.||



• If the calculated results is a fraction, that is corrected to the minimum mechanical pitch and excess is discarded. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-139 

## **ESC GS P 5 nL nH** 

[Name] Specify character vertical direction relative position in page mode [Code] ASCII ESC GS P 5 Hexadecima 1B 1D 50 35 l Decimal 27 29 80 53 [Defined Area] 0 ≤ nL ≤ 255, 0 ≤ nH ≤ 255 [Initial Value] - - - [Function] Specify the position for character vertical direction of the data expansion starting position in page mode with the relative position that uses the current position as a reference. The subsequent data expansion starting position uses the position moved [(nL + nH x 256) x 1/8] mm from the current position. • This command is ignored when page mode is not selected. • When specifying the characters downward from the current position the value is positive (plus); when specifying upward, the value is negative (minus). • Negative numbers are represented by a complement of 65536. For example, use the following to move upward N pitches. nL + nH x 256 = 65536-N • Relative position specifications that exceed the specified print region are ignored. • The following operations will occur depending on the ESC GS P 2 (select character print direction in page mode). a. When the starting point is “upper left” or “bottom right,” specify the absolute position of the paper feed direction. b. When the starting point is “upper right” or “bottom left,” specify the relative position of the perpendicular direction to the paper feed. • If the calculated results is a fraction, that is corrected to the minimum mechanical pitch and excess is discarded. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-140 

## **ESC GS P 6** 

[Name] Print data in page mode [Code] ASCII ESC GS P 6 Hexadecimal 1B 1D 50 36 Decimal 27 29 80 54 [Function] Lump-prints data expanded to the entire print region in page mode. • Valid only when page mode is selected. • After printing, the following information is maintained. a. Expanded data b. Selection of character print direction in page mode (ESC GS P 2) c. Setting of print region in page mode (ESC GS P 3) d. Character expansion position 

## **ESC GS P 7** 

[Name] Print in page mode and recover [Code] ASCII ESC GS P 7 Hexadecima 1B 1D 50 37 l Decimal 27 29 80 55 [Function] Lump-prints data expanded to the entire print region and recovers to standard mode. • All expanded data is erased after printing. • Print region set by ESC GS P 3 (Set print region in page mode) is initialized. • No paper cut is executed. • After execution, the top of the line is positioned at the next print starting position. • Valid only when page mode is selected. 

## **ESC GS P 8** 

[Name] Cancel print data in page mode [Code] ASCII ESC GS P 8 Hexadecimal 1B 1D 50 38 Decimal 27 29 80 56 [Function] Erases all data in presently set print region, in page mode. • Valid only when page mode is selected. 

• Portion included in the currently set print region is deleted even if data of the print region set previously. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-141 

## **3.17. Text Search Command Details** 

## **ESC GS ) B pL pH fn [parameter]** 

[Name] Set text search [Code] ASCII ESC ) B pL pH fn [parameter] Hexadecimal 1B 29 42 pL pH fn [parameter] Decimal 27 41 66 pL pH fn [parameter] [Function] Runs processes related to text search. 

• pL and pH specify the parameter count (pL + pH x 256) in bytes after fn. 

- See the function specifications for details on [parameter]. 

|fn|Function No.|Function Name|
|---|---|---|
|48|Function 48|Enable and disables text search|
|49|Function 49|Set the number of times to run the text search macro|
|50|Function 50|Set toprint the stringthat matches in the text search|
|64|Function 64|Define the text search string|
|65|Function 65|Define the text search macro|
|80|Function 80|Register text search settings and definitions in the non-volatile memory|
|81|Function 81|Initialize text search settings and definitions|
|96|Function 96|Print the text search settings and definitions|
|97|Function 97|Run the text search macro|



## **<Function 48> ESC GS ) B pL pH fn m  (fn = 48)** 

|[Name]|Enable and disables text search|Enable and disables text search|Enable and disables text search|Enable and disables text search||||||
|---|---|---|---|---|---|---|---|---|---|
|[Code]|ASCII|ESC GS||)|B|pL|pH|fn|m|
||Hexadecimal||1B<br>1D|29|42|pL|pH|fn|m|
||Decimal||27<br>29|41|66|pL|pH|fn|m|
|[Defined Area]||pL = 2, pH = 0|pL = 2, pH = 0|||||||
|||fn = 48|fn = 48|||||||
|||m = 0, 1|m = 0, 1|||||||
|[Initial Value]||Depends on setting registered in the non-volatile memory (At the time of shipment: m = 0)|||||Depends on setting registered in the non-volatile memory (At the time of shipment: m = 0)|Depends on setting registered in the non-volatile memory (At the time of shipment: m = 0)||
|[Function]|[Function]|Makes text searches valid or invalid.|Makes text searches valid or invalid.|||Makes text searches valid or invalid.||Makes text searches valid or invalid.||



m Set 0 Invalid 1 Valid When text search is valid, determines whether a string registered in the printer in advance is in the print data. If it is included, run a text search macro that corresponds to that string after running the following trigger command. • Execute cuts by continous <LF>. • <ESC> “d” No setting when the parameter is not a valid value. This setting is applied to printer operations when this command is processed. This setting is registered to non-volatile memory by the ESC GS ) B <Function 80) command. This command is ignored when the text search macro is running. Disabled in Page Mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-142 

## **<Function 49> ESC GS ) B pL pH fn m  (fn = 49)** 

[Name] Set the number of times to run the text search macro [Code] ASCII ESC GS ) B pL pH fn m Hexadecimal 1B 1D 29 42 pL pH fn m Decimal 27 29 41 66 pL pH fn m 

[Defined Area] pL = 2, pH = 0 fn = 49 m = 0, 1 [Initial Value] Depends on setting registered in the non-volatile memory (At the time of shipment: m = 0) [Function] Sets the number of times to run the text search macro when the strings match. 

|m|Set|
|---|---|
|0|Run one time|
|1|Run for the number of times strings match|



No setting when the parameter is not a valid value. 

This setting is applied to printer operations when this command is processed. This setting is registered to non-volatile memory by the ESC GS ) B <Function 80) command. This command is ignored when the text search macro is running. Disabled in Page Mode. 

**<Function 50> ESC GS ) B pL pH fn m  (fn = 50)** 

[Name] Set to print the string that matches in the text search [Code] ASCII ESC GS ) B pL pH fn m Hexadecimal 1B 1D 29 42 pL pH fn m Decimal 27 29 41 66 pL pH fn m 

[Defined Area] pL = 2, pH = 0 fn = 50 m = 0, 1, 2 

[Initial Value] Depends on setting registered in the non-volatile memory (At the time of shipment: m = 0) [Function] Sets the string print operation when strings match. 

|m|Set|
|---|---|
|0|Prints the string|
|1|Does notprint the string|
|2|Switches the stringwith a blank character|



No setting when the parameter is not a valid value. 

This setting is applied to printer operations when this command is processed. 

This setting is registered to non-volatile memory by the ESC GS ) B <Function 80) command. This command is ignored when the text search macro is running. 

Disabled in Page Mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-143 

**<Function 64> ESC GS ) B pL pH fn m k d1…dk (fn = 64)** 

|[Name]|Define the text search string|Define the text search string||||||
|---|---|---|---|---|---|---|---|
|[Code]|ASCII|ESC GS<br>)<br>B<br>pL|pH<br>fn<br>n|m|k|d1|... dk|
||Hexadecimal<br>1B<br>1D<br>29<br>42<br>pL||pH<br>fn<br>n|m|k|d1|... dk|
||Decimal|27<br>29<br>41<br>66<br>pL|pH<br>fn<br>n|m|k|d1|... dk|
|[Defined Area]||4≤<br> (pL + pH x 256)≤<br> 65535  (0≤<br>|pL≤<br> 255, 0≤<br>|pH≤<br>|255)|||
|||fn = 64||||||
|||1≤<br> n≤<br> 100||||||
|||1≤<br> m≤<br> 100||||||
|||0≤<br> k≤<br> 32||||||
|||32≤<br>d≤<br> 255||||||
|[Initial Value]||Depends on setting registered in the non-volatile memory (At the time of shipment: no string|Depends on setting registered in the non-volatile memory (At the time of shipment: no string||||Depends on setting registered in the non-volatile memory (At the time of shipment: no string|
|||definition)||||||
|[Function]|[Function]|Defines the text search string for number n.||||||
|||If the text search string for number n is already defined, it is overwritten.||If the text search string for number n is already defined, it is overwritten.||||
|||M specifies the text search macro number to run.|M specifies the text search macro number to run.|||||
|||K specifies the size of the defined data in bytes.|K specifies the size of the defined data in bytes.|||||
|||D specifies the defined data.||||||
|||When the parameter has an invalid value, no definition.||||||
|||This definition is applied to printer operations when this command is processed.|This definition is applied to printer operations when this command is processed.|||||
|||This definition is registered to non-volatile memory by the ESC GS ) B <Function 80) command.||||||
|||This command is ignored when the text search macro is running.||This command is ignored when the text search macro is running.||||
|||Disabled in Page Mode.||||||



**<Function 65> ESC GS ) B pL pH fn m k1 k2 d1…dk (fn = 65)** 

|[Name]|Define the text search macro|Define the text search macro|||||||
|---|---|---|---|---|---|---|---|---|
|[Code]|ASCII|ESC<br>GS<br>)<br>B<br>pL<br>pH|fn<br>m|k1||k2|d1|... dk|
||Hexadecimal<br>1B<br>1D 29<br>42<br>pL<br>pH||fn<br>m|k1||k2|d1|... dk|
||Decimal|27<br>29 41<br>66<br>pL<br>pH|fn<br>m|k1||k2|d1|... dk|
|[Defined Area]||4≤<br> (pL + pH x 256)≤<br> 65535  (0≤<br> pL≤<br>|255, 0≤<br>|pH≤<br>|255)||||
|||fn = 65|||||||
|||1≤<br> m≤<br> 100|||||||
|||0≤<br> (k = k1 + k2 x 256)≤<br> 7680  (0≤<br> k1≤|≤<br> 255, 0≤|≤<br> k2≤|≤<br>|30)|||
|||(Size of defined area = 7,680 bytes)|||||||
|||0≤<br> d≤<br> 255|||||||
|[Initial Value]||Depends on setting registered in the non-volatile memory (At the time of shipment: no text|Depends on setting registered in the non-volatile memory (At the time of shipment: no text||||||
|||search macro definition)|||||||
|[Function]|[Function]|Defines the text search macro for number m.|||||||
|||If the text search macro for number m is already defined, it is overwritten.|If the text search macro for number m is already defined, it is overwritten.||||If the text search macro for number m is already defined, it is overwritten.||
|||(k = k1 + k2 x 256) specifies the size of the defined data in bytes.|||||(k = k1 + k2 x 256) specifies the size of the defined data in bytes.|(k = k1 + k2 x 256) specifies the size of the defined data in bytes.|
|||d specifies the defined data.|||||||
|||If the parameter has an invalid value, processing of this command ends at that point.|||||||
|||This definition is applied to printer operations when this command is processed.|||||||
|||This definition is registered to non-volatile memory by the ESC GS ) B <Function 80) command.|||||||
|||This command is ignored when the text search macro is running.||This command is ignored when the text search macro is running.||This command is ignored when the text search macro is running.||This command is ignored when the text search macro is running.|
|||Disabled in Page Mode.|||||||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-144 

**<Function 80> ESC GS ) B pL pH fn m  (fn = 80)** 

[Name] Register text search settings and definitions in the non-volatile memory [Code] ASCII ESC GS ) B pL pH fn m Hexadecimal 1B 1D 29 42 pL pH fn m Decimal 27 29 41 66 pL pH fn m [Defined Area] pL = 2, pH = 0 fn = 80 m = 0 --[Initial Value] [Function] Registers the text search setting to non-volatile memory. The following shows the contents to register. Function No. Contents Function 48 Enable and disables text search Function 49 Set the number of times to run the text search macro Function 50 Set to print the string that matches in the text search Function 64 Define the text search string Function 65 Define the text search macro Function 81 Initialize text search settings and definitions After registration ends, resets the printer. The printer operates by reading the setting registered using this command the next time the printer power is turned on. This command is ignored when the text search macro is running. Consider the life of the non-volatile memory and avoid over-sue of this command. Disabled in Page Mode. 

**<Function 81> ESC GS ) B pL pH fn m  (fn = 81)** 

|[Name]|Initialize text search settings and definitions|Initialize text search settings and definitions|Initialize text search settings and definitions|Initialize text search settings and definitions|Initialize text search settings and definitions|||
|---|---|---|---|---|---|---|---|
|[Code]|ASCII|ESC<br>GS<br>)|B|pL|pH|fn|m|
||Hexadecimal<br>1B<br>1D 29||42|pL|pH|fn|m|
||Decimal|Decimal<br>27<br>29 41|66|pL|pH|fn|m|
|[Defined Area]||pL = 2, pH = 0||||||
|||fn = 81||||||
|||m = 0||||||
|[Initial Value]||---||||||
|[Function]|[Function]|Initialize text search settings and definitions||Initialize text search settings and definitions|Initialize text search settings and definitions|||
|||The followingshows the contents to initialize.|||shows the contents to initialize.|shows the contents to initialize.||



|Function No.|Contents|Initial Value|
|---|---|---|
|Function 48|Enable and disables text search|Invalid|
|Function 49|Set the number of times to run the text search macro|1 times|
|Function 50|Set toprint the stringthat matches in the text search|Prints the string|
|Function 64|Define the text search string|No text search stringdefinition|
|Function 65|Define the text search macro|No text search macro definition|
|This setting is applied to printer operations when this command is processed.||This setting is applied to printer operations when this command is processed.|
|This setting is registered to non-volatile memory by the ESC GS ) B <Function 80) command.|||
|This command is ignored when the text search macro is running.|||
|Disabled in Page Mode.|Disabled in Page Mode.||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-145 

**<Function 96> ESC GS ) B pL pH fn m  (fn = 96)** 

[Name] Print the text search settings and definitions [Code] ASCII ESC GS ) B pL pH fn m Hexadecimal 1B 1D 29 42 pL pH fn m Decimal 27 29 41 66 pL pH fn m [Defined Area] pL = 2, pH = 0 fn = 96 m = 0 --[Initial Value] [Function] Prints text search settings and definitions The following shows the contents to print. Function No. Contents Function 48 Enable and disables text search Function 49 Set the number of times to run the text search macro Function 50 Set to print the string that matches in the text search Function 64 Define the text search string Function 65 Define the text search macro The text search macro is not run at this time. This command is ignored when the text search macro is running. Disabled in Page Mode. 

**<Function 97> ESC GS ) B pL pH fn m  (fn = 97)** 

[Name] Run the text search macro [Code] ASCII ESC GS ) B pL pH fn m Hexadecimal 1B 1D 29 42 pL pH fn m Decimal 27 29 41 66 pL pH fn m [Defined Area] pL = 2, pH = 0 fn = 97 1 ≤ m ≤ 100 --[Initial Value] [Function] Runs the text search macro for number m. This command is ignored when the text search macro is running. Disabled in Page Mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-146 

## **3.18. Audio Command Details** 

**ESC GS s O z a n c1 c2 d1 d2 t1 t2** 

|[Name]|Playback NV audio|Playback NV audio|||||||
|---|---|---|---|---|---|---|---|---|
|[Code]|ASCII<br>ESC<br>GS<br>s<br>O<br>z<br>a<br>n||c1|c2|d1|d2|t1|t2|
||Hexadecimal<br>1B<br>1D<br>73<br>4F<br>z<br>a<br>n||c1|c2|d1|d2|t1|t2|
||Decimal<br>27<br>29<br>115<br>79<br>z<br>a<br>n||c1|c2|d1|d2|t1|t2|
|[Defined Area]<br>Z = 0|||||||||
|||a = 0, 1, 48, 49|||||||
|||1≤<br> n≤<br> 255|||||||
|||1≤<br> c1 + c2x256≤<br> 65535|||||||
|||0≤<br> d1 + d2x256≤<br> 65535|||||||
|||0≤<br> t1 + t2x256≤<br> 65535|||||||
|[Initial Value]||---|||||||
|[Function]||Plays back the specified NV audio.|||||||
|||a specifies the area where the audio data toplayback is stored.|||||back is stored.||
|||a<br>Audio data storage area|||||||
||1,49|49<br>User area|||||||
|||n specifies the audio number to playback.|||||||
|||(c1 + c2 x 256) specifies the number of times.|||||||
|||(d1 + d2 x 256) specifies the delay time.|||||||
|||Delay time is the time from starting to process this command to the start of audio playback|||||Delay time is the time from starting to process this command to the start of audio playback|Delay time is the time from starting to process this command to the start of audio playback|
|||(in seconds).|||||||
|||(t1 + t2 x 256) specifies the interval time.|||||||
|||Interval time is the time from the end of the previous audio to the start of the next audio|Interval time is the time from the end of the previous audio to the start of the next audio|Interval time is the time from the end of the previous audio to the start of the next audio|||Interval time is the time from the end of the previous audio to the start of the next audio|Interval time is the time from the end of the previous audio to the start of the next audio|
|||(in seconds).|||||||
|||If audio is already being played back, playback after waiting for the end of the audio.|||||||
|||If the printer is printing, playback after printing is ended.|||||||
|||When the parameter has an invalid value, there is no audio playback.||When the parameter has an invalid value, there is no audio playback.|||||
|||If the audio data of the specified audio number has not been registered, there will be no|||If the audio data of the specified audio number has not been registered, there will be no||||
|||playback.|||||||
|||Audio will stop by inputting the FEED switch while there is audio playback using this command.|||||||
|||Audio will stop using the NV audio stop command (ESC GS s P) while there is audio playback||||||Audio will stop using the NV audio stop command (ESC GS s P) while there is audio playback|
|||using this command.|||||||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-147 

## **ESC GS s P** 

[Name] Stop NV audio [Code] ASCII ESC GS s P Hexadecimal 1B 1D 73 50 Decimal 27 29 115 80 --[Defined Area] --[Initial Value] [Function] Stops audio playback for the following reasons. O NV audio playback command ESC GS s O 0 NV audio lump playback command ESC GS s T When run in real-time when this command is received This command is ignored with there is no audio playback. 

## **ESC GS s R z n1 n2 n3 d1 … dn** 

|[Name]|Playback received audio|Playback received audio|Playback received audio|||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|
|[Code]|ASCII|ESC|GS<br>s|R|z|n1|n2|n3|d1|…|dn|
||Hexadecimal<br>1B||1D 73|52|z|n1|n2|n3|d1|…|dn|
||Decimal|27|29 115|82|z|n1|n2|n3|d1|…|dn|
|[Defined Area]||Z = 0||||||||||
|||1≤<br> (n = n1 + n2 x 256 + n3 * 65536)||(n = n1 + n2 x 256 + n3 * 65536)≤<br>|||16777215|||||
|||0≤<br> d≤<br> 255||||||||||
|[Initial Value]||---||||||||||
|[Function]|[Function]|Does not register audio data in the non-volatile memory and plays back one time while receiving||||Does not register audio data in the non-volatile memory and plays back one time while receiving|||||Does not register audio data in the non-volatile memory and plays back one time while receiving|
|||data.||||||||||
|||(n1 + n2 x 256 + n3 x 65536) specifies the number of bytes of the audio data.|||||(n1 + n2 x 256 + n3 x 65536) specifies the number of bytes of the audio data.||(n1 + n2 x 256 + n3 x 65536) specifies the number of bytes of the audio data.|||
|||d is audio data in sampling frequency of 11.025 kHz, ADPCM format in quantization bit rate of 4|||||d is audio data in sampling frequency of 11.025 kHz, ADPCM format in quantization bit rate of 4|||||
|||bits.||||||||||
|||When data transfer from the host is slow (theoretical value: 44,100 bps or lower), playback is||||When data transfer from the host is slow (theoretical value: 44,100 bps or lower), playback is||||||
|||intermittent.||||||||||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-148 

## **ESC GS s I z e a n c1 c2 d1 d2 t1 t2 … 0xFF** 

[Name] Register automatic audio setting information [Code] ASCII ESC GS s I z e a n c1 c2 d1 d2 t1 t2 … 0xFF Hexadecimal 1B 1D 73 49 z e a n c1 c2 d1 d2 t1 t2 … FF Decimal 27 29 115 73 z e a n c1 c2 d1 d2 t1 t2 … 255 

[Defined Area] z = 0, 1 0 ≤ e ≤ 63(0x3F) a = 1, 49 0 ≤ n ≤ 255 0 ≤ c1 + c2 x 256 ≤ 65535 0 ≤ d1 + d2 x 256 ≤ 65535 0 ≤ t1 + t2 x 256 ≤ 65535 

|e<br>Printer Internal Status<br>~~a~~<br>~~aa~~|a<br>~~OC~~<br>~~OO~~|n<br>~~OC~~<br>~~OO~~|c1 + c2x256<br>~~OC~~<br>~~OO~~|d1 + d2x256<br>~~OO~~|t1 + t2x256<br>~~OO~~|
|---|---|---|---|---|---|
|0x00<br>Cutter error<br>~~aa~~|0<br>~~OO~~|1<br>~~OO~~|1<br>~~OO~~|0<br>~~OO~~|0<br>~~OO~~|
|0x01<br>Flash ROM error<br>~~a a ~~<br>~~SC~~<br>~~**a**~~<br>~~a~~|0<br> ~~OO~~<br>~~SC~~<br>~~a~~|2<br>~~OO~~<br>~~SC~~<br>|1<br>~~OO~~<br>~~SC~~<br>|0<br>~~OO~~<br>~~SC~~|0<br>~~OO~~<br>~~SC~~|
|0x02<br>EE-PROM error<br>~~SC~~<br>~~**a**~~<br>~~a~~<br>~~—~~|0<br>~~SC~~<br>~~a~~<br>|3<br>~~SC~~<br>~~SC~~<br>|1<br>~~SC~~<br>~~SC~~<br>|0<br>~~SC~~<br>|0<br>~~SC~~<br>|
|0x03<br>SRAM error<br>~~**a**~~<br>~~a~~<br>~~—~~|0<br>~~a ~~<br>|4<br> ~~SC~~<br>|1<br>~~SC~~<br>|0<br>|0<br>|
|0x04<br>Head<br>temperature<br>detection error<br><br>~~— |~~<br>~~a~~|0<br> <br>~~|~~|5<br> ~~SC~~<br>~~|~~<br>~~CO~~|1<br>~~SC~~<br>~~|~~<br>~~CO~~|0<br>~~|~~|0<br>~~|~~|
|0x05<br>Power voltage error<br><br>~~— |~~<br>~~a~~<br>~~a~~|0<br> <br>~~|~~<br>~~a~~|6<br> ~~SC~~<br>~~|~~<br>~~a~~<br>~~CO~~|1<br>~~SC~~<br>~~|~~<br>~~a~~<br>~~CO~~|0<br>~~|~~<br>~~a~~|0<br>~~|~~<br>~~a~~|
|0x06 to 0x0F<br>(Reserved)<br>~~a~~|0<br>~~CC~~|0<br>~~CO~~<br>~~CC~~|0<br>~~CO~~<br>~~CC~~|0<br>~~CC~~|0<br>~~CC~~|
|0x10<br>BM Error<br>~~CC~~|0<br>~~CC~~|7<br>~~CC~~|1<br>~~CC~~|0<br>~~CC~~|0<br>~~CC~~|
|0x11<br>PE error<br>~~a~~|0<br>~~OC~~|8<br>~~OC~~|1<br>~~OC~~|0<br>~~OC~~|0<br>~~OC~~|
|0x12<br>Cover open<br>~~SC~~|0<br>~~SC~~|9<br>~~SC~~|1<br>~~SC~~|5<br>~~SC~~|0<br>~~SC~~|
|0x13<br>NE error<br>~~SC~~|0<br>~~SC~~|10<br>~~SC~~|1<br>~~SC~~|0<br>~~SC~~|0<br>~~SC~~|
|0x14 to 0x1F<br>(Reserved)<br>~~a~~<br>~~a~~<br>~~ee ee~~|0<br>~~ee~~|0<br>~~C~~<br>~~ee~~|0<br>~~C~~<br>~~ee~~|0|0|
|0x20<br>Head<br>high<br>temperature stoperror<br>~~a~~<br>~~ee ee~~|0<br>~~ee~~|11<br>~~ee~~|1<br>~~ee~~|0|0|
|0x21 to 0x2F<br>(Reserved)<br>~~a~~<br>~~ee ee~~<br>~~CC~~|0<br>~~ee~~<br>~~CC~~|0<br>~~ee~~<br>~~CC~~|0<br>~~ee~~<br>~~CC~~|0<br>~~CC~~|0<br>~~CC~~|
|0x30<br>Idling<br>~~A~~|0<br>~~OC~~|0<br>~~OC~~<br>~~SC~~|0<br>~~OC~~<br>~~SC~~|0|0|
|0x31 to 0x3F<br>(Reserved)<br>~~a~~|0<br>~~a~~|0<br>~~a~~<br>~~SC~~|0<br>~~a~~<br>~~SC~~|0<br>~~a~~|0<br>~~a~~|



[Function] When z = 1, the automatic audio setting information returns to the default factory setting. (At this time, do not send parameters after e.) 

When z = 0, register the automatic audio setting information to playback when the printer’s internal status occurs. e specifies the printer’s internal status assigned to audio. a specifies the area where the audio data to set is stored. a Audio data storage area 1, 49 User area n specifies the audio number to playback. However, when n = 0, or audio data of a specified number is not registered, automatic audio is invalid. (c1 + c2 x 256) specifies the number of times. (d1 + d2 x 256) specifies the delay time. Delay time is the time from the occurrence of the printer’s internal status to the start of audio playback (in seconds). (t1 + t2 x 256) specifies the interval time. Interval time is the time from the end of the previous audio to the start of the next audio (in seconds). You can register multiple times by repeating parameters e to t2. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-149 

Perform lump registration until 0xFF which is the end code. 

When the parameter is determined to be free of error, the printer starts processing this command. When the parameter has an invalid value, there is no setting. (Sets already determined to be free of problems are valid.) 

This command should be specified at the top of the line. After registering automatic audio setting information, reset the printer. 

Error processing mechanical operations or status processing and the like are not possible while registering automatic audio setting information (the time from receiving 0xFF which is the end code until printer reset is completed after automatic audio registration ends). 

Audio will stop by inputting the FEED switch while there is audio playback using this setting. 

Command Transmission Example Cutter error: User area 12[th] /3 times/delay 2 seconds/interval 1 second, Flash ROM error: User area 13[th] /4 times/delay 5 seconds/interval 6 seconds ESC GS s  I  z e  a  n  c1 c2 d1 d2 t1 t2 1B  1D 73 49 00 00 01 0C 03 00 02 00 01 00 01 01 0D 04 00 05 00 06 00 FF 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-150 

## **ESC GS s U z n [k1 k2 k3 d1 … dk]1 … [k1 k2 k3 d1 … dk]n** 

[Name] Register user area NV audio data [Code] ASCII ESC GS s U z n [k1 k2 k3 d1 .. dk]1 .. [k1 k2 k3 d1 .. dk]n Hexadecimal 1B 1D 73 55 z n [k1 k2 k3 d1 .. dk]1 .. [k1 k2 k3 d1 .. dk]n Decimal 27 29 115 85 z n [k1 k2 k3 d1 .. dk]1 .. [k1 k2 k3 d1 .. dk]n [Defined Area] Z = 0 0 ≤ n ≤ 255 0 ≤ [ k1 + k2x256 + k3x65536 ]1 + … +  [ k1 + k2x256 + k3x65536 ]n ≤ 1701888 0 ≤ d ≤ 255 [Initial Value] Japanese or English (See table below) n English Audio 1 Welcome ! 2 Thank you ! 3 Order coming in. 4 Drink Order coming in. 5 Food Order coming in. 6 Order has been Cancelled. 7 New order coming in. 8 Order to go coming in. 9 Print finished. 10 Please take your receipt. 11 Please come again. 12 Please give your receipt to the operator. 13 Now printing, please wait a moment. 14 Please do not pull the paper until printing finishes. 15 Thank you for visiting. 16 Please take the number ticket. 17 Please have a seat and wait a moment. 18 Thank you for your purchase. 19 Please wait here, we will guide you shortly. 

[Function] 

All data already registered in the user area is erased when starting processing of this command. Registers n audio data to the user area. (However, when n = 0, nothing is registered.) 

Audio numbers are set in ascending order in the order they are registered from user area audio number 1 to n. 

(k1 + k2 x 256 + k3 x 65536) specifies the number of bytes of the audio data. 

d is audio data in sampling frequency of 11.025 kHz, monaural ADPCM format in quantization bit rate of 4 bits. 

The size of the registration region is 1,662 KB (approx. 308 seconds). This command should be specified at the top of the line. 

When the first parameter is determined to be free of error, the printer starts processing this command. 

If the defined area specified by the parameter is not empty, or if there is an error in the parameter specification, register processing is aborted. (The pre-registered and complete data is effective.) The printer should be reset if audio data registration is completed or register processing is forcibly aborted. 

Error processing, mechanical operations and status processing and the like cannot executed while registering audio data (the time from when the first parameter is determined to be OK until printer initialization is completed after registering audio data). 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-151 

## **ESC GS s T a t1 t2** 

|[Name]|Batch playback of NV audio|Batch playback of NV audio|Batch playback of NV audio||||
|---|---|---|---|---|---|---|
|[Code]|ASCII|ESC<br>GS|s<br>T|t1|t2||
||Hexadecimal<br>1B<br>1D||73<br>54|t1|t2||
||Decimal|27<br>29|115<br>84|t1|t2||
|[Defined Area]||a = 1, 49|||||
|||0≤<br> t1 + t2 x 256≤<br>|65535||||
|[Initial Value]||---|||||
|[Function]||Lump-playback of NV audio registered in the non-volatile memory from #1 in ascending order.|Lump-playback of NV audio registered in the non-volatile memory from #1 in ascending order.|||Lump-playback of NV audio registered in the non-volatile memory from #1 in ascending order.|
|||a specifies the audio data registration area.|||||
||a|Audio data storage area|||||
||1,49|User area|||||
|||(t1 + t2 x 256) specifies how many seconds from the top to playback each audio data.||(t1 + t2 x 256) specifies how many seconds from the top to playback each audio data.|(t1 + t2 x 256) specifies how many seconds from the top to playback each audio data.||
|||However, when () = 0, plays back each audio data completely without specifying the number of|However, when () = 0, plays back each audio data completely without specifying the number of||However, when () = 0, plays back each audio data completely without specifying the number of||
|||seconds.|||||
|||Insert 1 second of interval time between the previous audio and the next audio.|Insert 1 second of interval time between the previous audio and the next audio.||||
|||Audio will stop by inputting the FEED switch while this command is running.|||||
|||Audio will stop using the NV audio stop command (ESC GS s P) while running this command.||Audio will stop using the NV audio stop command (ESC GS s P) while running this command.|Audio will stop using the NV audio stop command (ESC GS s P) while running this command.||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-152 

**ESC GS h 1 k m n** 

[Name] Water mark function [Code] ASCII ESC GS h 1 k m n Hex. 1B 1D 68 31 k m n Decimal 27 29 104 49 k m N 

[Defined Area] 0 ≤ k ≤ 2, 0 ≤ m ≤ 2, 1 ≤ n ≤ 255 [Initial Value] --[Function] Sets the water mark function to be valid/invalid. 

|k|Water Mark Function|
|---|---|
|0|Invalid|
|1|Valid<br>Prints one specified logo at a position centered<br>horizontallyand vertically.|
|2|Valid<br>Repeats printing of the specified logo from the top edge to<br>the bottom edge atpositions centered horizontally.|



• To set to an appropriate image as the water mark using this setting, set the method for forming The logo data to be printed as the water mark. 

If it is not possible to set an appropriate image with this setting, form the logo data registered as the water mark into the appropriate data and reregister it. 

|m|Water Mark Data Forming|
|---|---|
|0|Prints the logo data specified byn as it is.|
|1|Prints the logo data specified byn thinned 25%.|
|2|Prints the logo data specified byn thinned 12.5%.|
|• Specify the registered logo in the water mark.||
|n|Logo Number|
|1 to 255|Registered logo numbers.|
||If the specified logo number is not registered, the water|
||mark will not beprinted.|



- Specify the registered logo in the water mark. 

## <Water Mark Function> 

When the water mark function is valid, the water mark is printed by its trigger. 

However, this function is effective for print data that can be contained in the image buffer length. Print data  beyond the image buffer length is unaffected by this function. 

Printing that is started other than the water mark trigger ignores the water mark print. When in 2-color printing, this function is ignored. 

Water mark printing triggers 

• Cutter command: <ESC> d n • FF command: <FF> • BM detection command: <ESC> d n, <FF> • Print start command: <ESC> <GS> g 0 m n • Raster mode: When <FF> is executed. Use example 

- 1) Register logo to use as water mark in logo number 1. 

2) Water mark function is enabled: <ESC> <GS> h 1 k m n (k = 0x02, m = 0x01, n = 0x01) 2) Print data transfer: Print data (Print length is less than length of image buffer.) 3) Trigger command transfer: <ESC> d n (Cutter command is water mark printing trigger.) 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 3-153 

## **4. CHARACT ER CODE TABLES** 

Refer to the separate ”Character Code Tables” . 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

4-1 

## **5. APP ENDIX** 

## **5.1. Appendix 1: Bar Code Specification Details** 

Refer to the dedicated manuals for characteristics and methods of use for each bar code symbol. This section describes precautions and methods for setting when printing with the printer. 

Bar code widths are set for each bar code according to the mode.  The following describes each mode and the dot counts. 

The user must ensure the specified printing position and quiet zone at the position where the bar code begins. 

## **5.1.1. Co de 39** 

Code 39 represents numbers 0 to 9 and the letters of the alphabet from A to Z. These are the symbols most frequently used today in industry. 

|Items<br>~~es~~<br>~~a~~|Mode1<br>~~es~~<br>~~ee~~|Mode2<br>~~es~~<br>~~ee~~|Mode 3<br>~~QO~~<br>~~ee~~|Mode4<br>~~QO~~<br>~~ee~~|Mode 5<br>~~G~~<br>~~ee~~|Mode 6<br>~~ee~~|Mode7<br>~~ee~~|Mode 8|Mode 9|
|---|---|---|---|---|---|---|---|---|---|
|Narrow<br>Element Width<br>~~es~~<br>~~a~~<br>~~a~~|th<br>2 dots<br>~~es~~<br>~~ee~~<br>~~ee~~|3 dots<br>~~es~~<br>~~ee~~<br>~~ee~~|4 dots<br>~~QO~~<br>~~ee~~<br>~~ee~~|2 dots<br>~~QO~~<br>~~ee~~<br>~~ee~~|3 dots<br>~~G~~<br>~~ee~~<br>~~ee~~|4 dots<br>~~ee~~|2 dots<br>~~ee~~|3 dots|4 dots|
|Wide Element<br>Width<br>~~a~~<br>~~a~~<br>~~es~~|6 dots<br>~~ee ~~<br>~~ee~~<br>~~Rs ns~~|9 dots<br> ~~ee~~<br>~~ee~~<br>~~ns~~|12 dots<br>~~ee ~~<br>~~ee~~<br>~~QO~~|5 dots<br> ~~ee~~<br>~~ee~~<br>~~QO~~|8 dots<br>~~ee ~~<br>~~ee~~<br>~~QO~~|10 dots<br> ~~ee ~~|4 dots<br> ~~ee~~<br>~~GO~~|6 dots|8 dots|
|Ratio<br>~~a~~<br>~~es~~<br>~~a~~|1:3<br>~~ee~~<br>~~Rs ns~~<br>~~ee~~|1:3<br>~~ee ~~<br>~~ns~~<br>~~ee~~|1:3<br> ~~ee~~<br>~~QO~~<br>~~ee~~|1:2.5<br>~~ee ~~<br>~~QO~~<br>~~ee~~|1:2.7<br> ~~ee~~<br>~~QO~~<br>~~ee~~|1:2.5<br>~~ee~~|1:2<br>~~GO~~<br>~~ee~~|1:2|1:2|
|Character<br>Spacing<br>~~es~~<br>~~a~~|2 dots<br>~~Rs ns~~<br>~~ee~~|3 dots<br>~~ns ~~<br>~~ee~~|4 dots<br> ~~QO~~<br>~~ee~~|2 dots<br>~~QO~~<br>~~ee~~|3 dots<br>~~QO~~<br>~~ee~~|4 dots<br>~~ee~~|2 dots<br>~~GO~~<br>~~ee~~|3 dots|4 dots|
|Length of 1<br>Character<br>~~a~~<br>~~a~~|4 mm<br>~~ee ~~<br>~~ee~~|6 mm<br> ~~ee~~<br>~~ee ~~|8 mm<br>~~ee ~~<br> ~~ee~~|3.625 mm <br> ~~ee~~<br>~~ee ~~|5.625 mm <br>~~ee ~~<br> ~~ee~~|7.25 mm<br> ~~ee ~~<br>~~ee~~|3.25 mm 4.875 mm<br> ~~ee~~|3.25 mm 4.875 mm|6.5 mm|



(*) The length of 1 character includes the character spacing. 

## 2.  Regulations 

The start and stop bar code (*) in Code 39 are automatically inserted. 

## **5.1.2. Interleaved 2 of 5** 

Interleaved 2 of 5 represents numbers 0 to 9.  Higher density of characters is possible and with JIS and EAN, and printing to cardboard for distribution has been standardized. 

- 1)  Narrow element width and length of symbols per 2 characters 

|Items<br>~~es~~<br>~~ee~~|Mode1<br>~~se~~<br>~~ee~~|Mode2<br>~~se~~<br>~~es~~|Mode 3<br>~~ee~~|Mode4<br>~~QO~~<br>~~ee~~|Mode 5<br>~~QO~~<br>~~ee~~|Mode 6|Mode7|Mode 8|Mode 9|
|---|---|---|---|---|---|---|---|---|---|
|Narrow Element<br>Width<br>~~es ~~<br>~~ee~~<br>~~a~~|2 dots<br> ~~se~~<br>~~ee~~<br>~~ee~~|4 dots<br>~~se~~<br>~~es~~<br>~~ee~~|6 dots<br>~~ee~~<br>~~ee~~|2 dots<br>~~QO~~<br>~~ee~~<br>~~ee~~|4 dots<br>~~QO~~<br>~~ee~~|6 dots|2 dots|3 dots|4 dots|
|Wide Element<br>Width<br>~~ee~~<br>~~a~~<br>~~es~~|5 dots<br>~~ee ~~<br>~~ee~~<br>~~sn~~|10 dots<br> ~~es ~~<br>~~ee~~<br>~~sn~~|15 dots<br> ~~ee~~<br>~~ee~~|4 dots<br>~~ee ~~<br>~~ee~~|8 dots<br> ~~ee~~|12 dots|6 dots|9 dots|12 dots|
|Ratio<br>~~a~~<br>~~es~~<br>~~ee~~|1:2.5<br>~~ee~~<br>~~sn~~<br>~~ee~~|1:2.5<br>~~ee ~~<br>~~sn~~<br>~~es~~|1:2.5<br> ~~ee ~~<br>~~ee~~|1:2<br> ~~ee~~<br>~~ee~~|1:2<br>~~ee~~|1:2|1:3|1:3|1:3|
|Length of 1<br>Character<br>~~es ~~<br>~~ee~~|4mm<br> ~~sn~~<br>~~ee~~|8mm<br>~~sn~~<br>~~es~~|12mm<br>~~ee~~|3.5mm<br>~~ee~~|7mm<br>~~ee~~|10.5mm|4.5mm|6.75mm|9mm|



## 2.  Regulations 

- By selecting interleaved 2 of 5 bar code symbols, start and stop patterns are automatically inserted. 

- When the bar code data digit count is odd, a zero is added to the highest value digit. 

- Details conform to standards for AIM, USS-12/5, ANSI and JIS x 0502. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-1 

## **5.1.3. J AN/EAN/UPC** 

Used numbers, not only the bar code symbols, are controlled using JAN, EAN and UPC as shared common commercial codes. Mainly, they are used for supermarkets such as shops and grocery stores. 

1.  Each mode and bar code width 

|1.  Each mode and bar code width|1.  Each mode and bar code width||||
|---|---|---|---|---|
|Items||Mode 1|Mode 2|Mode 3|
|ModuleWidth||2dots|3 dots|4dots|
|Barcodewidth(*)|JAN/EAN-8|16.75mm|25.125mm|33.5mm|
||JAN/EAN-13|23.75mm|35.625mm|47.5mm|
||UPC-A|23.75mm|35.625mm|47.5mm|
||UPC-E|12.75mm|19.125mm|25.5mm|



- (*) Includes the guard bar (left/right/center) but not the white space. 

## 2.  Regulations 

## • JAN/EAN -8: 

Data is in 7 or 8 digits.  The command is ignored for others. 

The check digit uses a modulus weight of 10/3 and is automatically applied. 

When the calculated value and the numerical value of the 8[th] digit differ, the calculated value has priority. 

- JAN/EAN -13: 

Data is in 12 or 13 digits.  The command is ignored for others. 

The check digit uses a modulus weight of 10/3 and is automatically applied. 

- When the calculated value and the numerical value of the 13[th] digit differ, the calculated value has priority. 

- • UPC – A: 

Data is in 11 or 12 digits.  The command is ignored for others. 

The check digit uses a modulus weight of 10/3 and is automatically applied. 

When the calculated value and the numerical value of the 12[th] digit differ, the calculated value has priority. 

## • UPC – E: 

Data is in 11 or 12 digits.  The command is ignored for others. 

The check digit uses a modulus weight of 10/3 and is automatically applied. 

When the calculated value and the numerical value of the 12[th] digit differ, the calculated value has priority. Data conversion to rectangles is automatic. 

Data that cannot be shortened is processed as invalid data. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-2 

## **5.1.4. Co de 128** 

These are bar code symbols that can print ASCII 128 characters.  For that reason, use thereof is increasing. 

1.  Each module and module width 

|Items|Mode1|Mode2|Mode 3|
|---|---|---|---|
|ModuleWidth|2dots|3 dots|4dots|
|Length of 1<br>Character(*)|2.75 mm|4.125 mm|5.5 mm|



(*) Start and stop bars not included. 

## 2.  Regulations 

When using <LF> with the command, control codes are not sent by the host PC, so the control codes are sent as data, as shown below. 

- When sending the following data, it represents a 2 character set. 

- % (25H) represents %0 (25H 30H). 

Control codes (00H to 1FH) represent 40H to 5FH applied behind %. Control code (7FH) represents %5 (25H 35H). 

Function codes represent 1 to 4 (31H to 34H) applied behind %. Start codes represent 6 to 8 (36H to 38H) applied behind %. 

- Stop code (SC)/Check character (CK) are automatically applied. 

- When start code is omitted: 

Uses START C when more than 4 digits continue after header. 

Uses START A when initial data other than numbers are the control code. 

Uses START B for other cases. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-3 

• 2 Character set code table 

<Control Codes> 

<Control Codes> Code Format ~~—Fs~~ NUL 00H %@ 25H 40H ~~ee ee~~ SOH 01H %A 25H 41H ~~ee ee~~ STX 02H %B 25H 42H ~~ee ee~~ ETX 03H %C 25H 43H ~~ee ee~~ EOT 04H %D 25H 44H ~~ee eee~~ ENQ 05H %E 25H 45H ~~po~~ ACK 06H %F 25H 46H ~~po~~ BEL 07H %G 25H 47H ~~po~~ BS  08H %H 25H 48H ~~es ee~~ HT  09H %I 25H 49H ~~es ee~~ LF  0AH %J 25H 4AH ~~ee ee~~ VT  0BH %K 25H 4BH ~~ee ee~~ FF  0CH %L 25H 4CH ~~ee ee~~ CR  0DH %M 25H 4DH ~~ee ee~~ SO  0EH %N 25H 4EH ~~es ee~~ SI  0FH %O 25H 4FH ~~ee eee~~ DLE 10H %P 25H 50H ~~ee eee po~~ DC1 11H %Q 25H 51H ~~po~~ DC2 12H %R 25H 52H ~~po~~ DC3 13H %S 25H 53H DC4 14H %T 25H 54H ~~es ee~~ NAK 15H %U 25H 55H ~~es ee~~ SYN 16H %V 25H 56H ~~ee ee~~ ETB 17H %W 25H 57H ~~ee ee~~ CAN 18H %X 25H 58H ~~ee ee~~ EM  19H %Y 25H 59H ~~ee ee~~ SUB 1AH %Z 25H 5AH ~~ee ee~~ ESC 1BH %[ 25H 5BH ~~ee ee~~ FS  1CH % ¥25H 5CH ~~ee eee po~~ GS  1DH %] 25H 5DH ~~po~~ RS  1EH %^ 25H 5EH ~~po~~ US  1FH %_ 25H 5FH DEL 7FH %5 25H 35H ~~es ee~~ 

|<ControlCodes>|
|---|
|Code<br>Format<br>% 25H<br>%0 25H 30H<br>~~EE~~|
|<Function Codes>|
|Code<br>Format<br>FNC1<br>%1 25H31H<br>FNC2<br>%2 25H 32H<br>FNC3<br>%3 25H 33H|
|FNC4<br>%4 25H34H|



|Code|Format|
|---|---|
|START A|%6 25H 36H|
|START B|%7 25H 37H|
|STARTC|%825H38H|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-4 

## **5.1.5. Co de 93** 

## 1.  Each mode and module width 

|Items|Mode1|Mode2|Mode 3|
|---|---|---|---|
|ModuleWidth|2dots|3 dots|4dots|
|Lengthof 1Character(*)|2.25mm|3.375mm|4.5mm|



- (*) Start and stop bars not included. 

## 2.  Regulations 

- Start/stop codes are automatically applied. 

- Check character (C, K) is automatically applied. 

- 2 character set expression conforms to Code 128. 

However, items marked with a star are codes that can only be used with Code 128, and not with Code 93. 

## **5.1.6. NW 7 (CODERBAR)** 

NW7 normally uses either A through D as the start/stop codes and represents special symbols (- (minus sign)/$ (dollar sign)/: (colon)// (slash)/. (period)/+ (plus sign) between 0 to 9. 

These are used as carrier package marking bar codes, DPE (photo prints) and for medical related industries (USA). 

1.  Length of 1 character in each mode 

|~~pO~~||||||||||
|---|---|---|---|---|---|---|---|---|---|
|Items<br>~~pO~~<br>~~po~~|Mode 1|Mode 2|Mode 3|Mode 4|Mode 5|Mode 6|Mode 7|Mode 8|Mode 9|
|Narrow Element Width<br>~~pO~~<br>~~po~~<br>~~po~~|2|3|4|2|3|4|2|3|4|
|WideElement Width<br>~~po~~<br>~~po~~<br>~~po~~|6|9|12|5|8|10|4|6|8|
|Ratio<br>~~po~~<br>~~po~~<br>~~ee~~|1:3<br>~~ee~~|1:3<br>~~es~~|1:3<br>~~se~~|1:2.5<br>~~se~~|1:2.7<br>~~se~~|1:2.5|1:2|1:2|1:2|
|Character Spacing<br>(Dots)<br>~~po~~<br>~~ee~~|2<br>~~ee~~|3<br>~~es~~|4<br>~~se~~|2<br>~~se~~|3<br>~~se~~|4|2|3|4|
|Length of 1 Character<br>(Normally mm)<br>(Width mm)<br>~~ee ~~|3<br>3.5<br> ~~ee ~~|4.5<br>5.25<br> ~~es~~|6<br>7<br>~~se~~|2.75<br>3.125<br>~~se~~|4.25<br>5.125<br>~~se~~|5.5<br>6.25|2.5<br>2.75|3.75<br>4.125|5<br>5.5|



- With NW7, lengths differ because narrow elements and wide elements are included according to the characters. 

- Normal characters (narrow: 5, wide: 2) and numbers (0 to 9), - and $ 

- Wide characters (narrow: 4, wide: 3) ,/,.,+, A to D 

- Character spaces are included in 1 character length. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-5 

## **5.2. Appendix 2: Status Specifications** 

## **5.2.1. ENQ Command Status** 

This status is the one the printer transmits using the ENQ command. 

|~~FS~~||~~eeeee~~<br>|~~eeeee~~<br>|~~eeeeeee~~<br>|~~eeeeeee~~<br>|~~eeeeeee~~<br>|~~eeeeeee~~<br>|~~eeeeeee~~<br>|~~eeeeeee~~<br>|~~eeeeeee~~<br>|~~eeeeeee~~<br>|~~eeeeeee~~<br>|~~eeeeeee~~<br>|~~eeeeeee~~<br>|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Bit<br>~~ee~~<br>~~FS~~|Contents<br>~~ee ~~<br>|Status<br>~~a~~<br>~~eeeee~~<br>||ModelCompatability<br>~~a~~<br>~~eeeeeee~~<br>|||||||||||
|||“0”<br>~~a~~<br> ~~ee~~<br>|“1”<br>~~a~~<br>~~eee~~<br>|TSP800<br>~~a~~<br>~~eee~~<br>|TSP700<br>~~a~~<br>~~eee~~<br>|TSP600<br>~~a~~<br>~~ee~~<br>|TUP900 <br>~~a~~<br>~~ee~~<br>|TSP1000 <br>~~a~~<br>~~ee~~<br>|TSP828L T<br>~~a~~<br>~~ee~~<br>|L TSP700II T<br>~~a~~<br>~~ee~~<br>|II TSP650T<br>~~a~~<br>~~ee~~<br>|TUP500<br>~~a~~<br>~~ee~~<br>|TSP800<br>~~a~~<br>~~ee~~<br>|FVP10<br>~~a~~<br>~~ee~~<br>|
|7<br><br>~~FS~~|ConversionSW<br> <br>~~OO~~|OPEN<br> ~~ee~~<br>~~OO~~|CLOSE<br>~~eee~~<br>~~OO~~|OK<br>~~eee~~<br>~~OO~~|OK<br>~~eee~~<br>~~OO~~|OK<br>~~ee~~<br>~~OO~~|No<br>~~ee~~<br>~~OO~~|NO<br>~~ee~~<br>~~OO~~|NO<br>~~ee~~<br>~~OO~~|OK<br>~~ee~~<br>~~OO~~|OK<br>~~ee~~<br>~~OO~~|NO<br>~~ee~~<br>~~OO~~|OK<br>~~ee~~<br>~~OO~~|OK<br>~~ee~~<br>~~OO~~|
|6<br><br>~~FS~~<br>~~pr~~|Overrun Error<br> <br><br>~~pr~~|No<br> ~~ee ~~<br><br>~~pr~~|Yes<br> ~~eee ~~<br><br>~~pr~~|OK<br> ~~eee~~<br><br>~~pr~~|OK<br>~~eee ~~<br><br>~~pr~~|OK<br> ~~ee~~<br><br>~~pr~~|OK<br>~~ee~~<br><br>~~pr~~|OK<br>~~ee~~<br><br>~~pr~~|OK<br>~~ee~~<br><br>~~pr~~|OK<br>~~ee~~<br><br>~~pr~~|OK<br>~~ee~~<br><br>~~pr~~|OK<br>~~ee~~<br><br>~~pr~~|OK<br>~~ee~~<br><br>~~pr~~|OK<br>~~ee~~<br><br>~~pr~~|
|5<br>~~rp~~|Reception Buffer Empty<br>~~rp~~|HasData<br>~~rp~~|Empty<br>~~rp~~|OK<br>~~rp~~|OK<br>~~rp~~|OK<br>~~rp~~|OK<br>~~rp~~|OK<br>~~rp~~|OK<br>~~rp~~|OK<br>~~rp~~|OK<br>~~rp~~|OK<br>~~rp~~|OK<br>~~rp~~|OK<br>~~rp~~|
|4<br>~~rp~~|Fixed at ”0”<br>~~rp~~|~~rp~~|-<br>~~rp~~|-<br>~~rp~~|-<br>~~rp~~|-<br>~~rp~~|-<br>~~rp~~|-<br>~~rp~~|-<br>~~rp~~|-<br>~~rp~~|-<br>~~rp~~|-<br>~~rp~~|-<br>~~rp~~|-<br>~~rp~~|
|3<br>~~pr~~|Paper end<br>~~pr~~|Paper<br>~~pr~~|No Paper<br>~~pr~~|OK<br>~~pr~~|OK<br>~~pr~~|OK<br>~~pr~~|OK<br>~~pr~~|OK<br>~~pr~~|OK<br>~~pr~~|OK<br>~~pr~~|OK<br>~~pr~~|OK<br>~~pr~~|OK<br>~~pr~~|OK<br>~~pr~~|
|2<br>~~rr~~|Other Errors<br>~~rr~~|No<br>~~rr~~|Yes<br>~~rr~~|OK<br>~~rr~~|OK<br>~~rr~~|OK<br>~~rr~~|OK<br>~~rr~~|OK<br>~~rr~~|OK<br>~~rr~~|OK<br>~~rr~~|OK<br>~~rr~~|OK<br>~~rr~~|OK<br>~~rr~~|OK<br>~~rr~~|
|1<br>~~rr~~|FramingError<br>~~rr~~|No<br>~~rr~~|Yes<br>~~rr~~|OK<br>~~rr~~<br>~~O~~|OK<br>~~rr~~<br>~~O~~|OK<br>~~rr~~<br>~~O~~|OK<br>~~rr~~|OK<br>~~rr~~|OK<br>~~rr~~|OK<br>~~rr~~|OK<br>~~rr~~|OK<br>~~rr~~|OK<br>~~rr~~|OK<br>~~rr~~|
|0<br>~~S~~|ParityError<br>~~S~~|No<br>~~S~~|Yes<br>~~S~~|OK<br>~~S~~<br>~~O~~|OK<br>~~S~~<br>~~O~~|OK<br>~~S~~~~**O**~~<br>~~O~~|OK<br>~~**O**~~|OK<br>~~**O**~~|OK<br>~~**O**~~|OK<br>~~**O**~~|OK<br>~~**O**~~|OK<br>~~**O**~~|OK<br>~~**O**~~|OK<br>~~**O**~~|



These errors occur when using a serial I/F. 

These errors are after holding the error and using this command to inquire the status and the error status is sent. 

- Other Errors 

Indicates non-recoverable errors and cover open errors. 

## **5.2.2. EOT Command Status** 

This status is the one the printer transmits using the EOT command. 

|Bit<br>~~ee~~<br>~~a~~|Contents<br>~~—~~<br>~~ee~~<br>~~a~~|Status<br>~~—~~<br>~~r>~~<br>~~ee~~<br>~~ee~~|Status<br>~~—~~<br>~~r>~~<br>~~ee~~<br>~~ee~~|ModelCompatability<br>~~ee~~<br>~~ee~~|ModelCompatability<br>~~ee~~<br>~~ee~~|ModelCompatability<br>~~ee~~<br>~~ee~~|ModelCompatability<br>~~ee~~<br>~~ee~~|ModelCompatability<br>~~ee~~<br>~~ee~~|ModelCompatability<br>~~ee~~<br>~~ee~~|ModelCompatability<br>~~ee~~<br>~~ee~~|ModelCompatability<br>~~ee~~<br>~~ee~~|ModelCompatability<br>~~ee~~<br>~~ee~~|ModelCompatability<br>~~ee~~<br>~~ee~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||“0”<br>~~—~~<br>~~ee~~|“1”<br>~~r>~~<br>~~ee~~<br>~~ee~~|TSP800<br>~~ee~~<br>~~ee~~|TSP700<br>~~ee~~<br>~~ee~~|TSP600<br>~~ee~~<br>~~ee~~|TUP900 <br>~~ee~~|TSP1000T<br>~~ee~~|TSP828L T<br>~~ee~~|L TSP700II T<br>~~ee~~|II TSP650<br>~~ee~~<br>~~rr~~|TSP800<br>~~ee~~<br>~~rr~~|FVP10<br>~~ee~~<br>~~rr~~|
|7<br>~~sess~~<br>~~a~~|CompulsionSW<br>~~sess~~<br>~~a~~|OPEN<br>~~sess~~|CLOSE -<br>~~ee ~~<br>~~sess~~|OK<br> ~~ee~~<br>~~sess~~|OK<br>~~ee~~<br>~~sess~~|OK<br>~~ee~~<br>~~sess~~|-<br>~~sess~~|-<br>~~sess~~|-<br>~~sess~~|OK<br>~~sess~~|OK<br>~~sess~~<br>~~rr~~|NO<br>~~sess~~<br>~~rr~~|NO<br>~~sess~~<br>~~rr~~|
|6<br>~~a~~<br>~~a~~|Presenter Paper Jam Error<br>~~a~~<br>~~a~~|No<br>~~OO~~|Yes<br>~~OC~~<br>~~OO~~|No<br>~~OC~~<br>~~OO~~|No<br>~~OC~~<br>~~CC~~|No<br>~~OC~~<br>~~CC~~|OK<br>~~OO~~<br>~~CC~~|No<br>~~OO~~<br>~~CC~~|NO<br>~~OO~~<br>~~OE~~|NO<br>~~OO~~<br>~~OE~~|NO<br>~~rr~~|NO<br>~~rr~~|NO<br>~~rr~~|
|5<br>~~a~~<br>~~a~~|Paper Near-end (OuterSide)<br>~~a~~<br>~~a~~|Paper<br>~~OO~~<br>~~OO~~|NoPaper<br>~~OO~~<br>~~OO~~|No<br>~~OO~~<br>~~OO~~|No<br>~~CC~~<br>~~CC~~|No<br>~~CC~~<br>~~CC~~|No<br>~~CC~~<br>~~CC~~|No<br>~~CC~~<br>~~CC~~|NO<br>~~OE~~<br>~~OE~~|NO<br>~~OE~~<br>~~OE~~|NO|-|-|
|4<br>~~a~~<br>~~a~~|Fixed at “1”<br>~~a~~<br>~~a~~|~~OO~~<br>~~OO~~|-<br>~~OO~~<br>~~OO~~|-<br>~~OO ~~<br>~~OO~~|-<br> ~~CC~~<br>~~CC~~|-<br>~~CC~~<br>~~CC~~|-<br>~~CC~~<br>~~CC~~|-<br>~~CC~~<br>~~CC~~|-<br>~~OE~~<br>~~OE~~|-<br>~~OE~~<br>~~OE~~|-|-|-|
|3<br>~~a~~<br>~~a~~|Paper end<br>~~a~~<br>~~a~~|Paper<br>~~OO~~|No Paper<br>~~OO~~<br>~~OC~~|OK<br>~~OO ~~<br>~~OC~~|OK<br> ~~CC~~<br>~~OC~~|OK<br>~~CC~~<br>~~OC~~|OK<br>~~CC~~<br>~~OO~~|OK<br>~~CC~~<br>~~OO~~|OK<br>~~OE~~<br>~~OO~~|OK<br>~~OE~~<br>~~OO~~|OK|OK|OK|
|2<br>~~a~~|Paper Near-end (InnerSide)<br>~~a~~|Paper|NoPaper<br>~~SC~~|OK<br>~~SC~~|OK<br>~~SC~~|OK<br>~~SC~~|OK<br>~~CO~~|OK<br>~~CO~~|NO<br>~~CO~~|OK<br>~~CO~~|OK|OK|OK|
|1<br>~~a~~<br>~~To~~|BINDINGMEDIA Error<br>~~a~~|No|Yes<br>~~SC~~|No<br>~~SC~~|No<br>~~SC~~|No<br>~~SC~~|OK<br>~~CO~~|OK<br>~~CO~~|OK<br>~~CO~~|OK<br>~~CO~~|NO|OK|OK|
|0<br>~~To~~|Fixed at “0”||-|-|-|-|-|-|-|-|-|-|-|



## • BM Error 

On models that use a common PE and BM sensor, if a continuous error is detected beyond a determined amount, it indicates not a black mark error, but a paper out error. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-6 

## **5.2.3. A utomatic Status** 

Automatic status is a group of states that are automatically returned from the printer to the host when the printer’s status has changed.  Automatic status is composed of “Header – 1,” “Header – 2” and “plurality of bytes of the printer status and is continuously returned to the host.  The host always uses an identifying method to identify the data for every byte received. 

(It is possible that Xon/Xoff codes are exceptionally mixed in the automatic status in the Xon/Xoff mode (when using a serial I/F), so it is necessary to consider that on the receiving side.) 

The valid/invalid conditions of the automatic status abide by the DIPSW settings for the initial values. It is possible to change the conditions using the ESC RS a n command after turning ON the power. Also, it is possible to get the automatic status using the ESC ACK SOH command, regardless of the valid/invalid conditions. 

## 1. Header – 1 

Header – 1 is the 1 byte length information transmitted at the head of the automatic status. 

The table below shows the composition of the Header – 1.  Header – 1 represents the entire status transmission byte count, including Header – 1, using bit 1 to bit 3 and bit 5.  The host gets the transmission byte information and always receives the status data for that amount transmission bytes.  For reference, the table below shows the relationship of actual transmission bytes and the Header – 1.  Because the bit 0 that indicates that this is the Header – 1 is normally 1 (the second byte and beyond is 0), to detect the Header – 1, it is acceptable to verify that bit 0 is 1 and bit 4 = 0 for this data.  Note that bit 6 is for future expansion and is ignored in host-side processes. 

<Header – 1 (First Byte)> 

|Bit<br>~~ee~~|Contents<br>~~ee~~|Status<br>~~ee~~|Status<br>~~ee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|ModelCompatability<br>~~ee~~<br>~~eeeee~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||“0”<br>~~ee~~<br>~~ee~~|“1”<br>~~ee~~<br>~~ee~~|TSP800<br>~~ee~~<br>~~ee~~|TSP700<br>~~ee~~<br>~~ee~~|TSP600<br>~~ee~~<br>~~ee~~|TUP900<br>~~ee~~<br>~~ee~~|TSP1000 <br>~~ee~~<br>~~ee~~|TSP828L <br>~~ee~~<br>~~ee~~|TSP700II T<br>~~ee~~<br>~~ee~~|II TSP650<br>~~ee~~<br>~~ee~~|TUP500T<br>~~ee~~<br>~~ee~~<br>~~ee~~|TSP800II<br>~~ee~~<br>~~ee~~<br>~~eee~~|FVP10<br>~~ee~~<br>~~ee~~<br>~~eee~~|
|7<br>~~ee~~<br>~~po~~<br>~~pot~~|Fixed at “0”<br>~~ee ~~<br>~~po~~<br>~~pot~~|~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~ee ~~<br>~~po~~|-<br>~~ee~~<br> ~~eee~~<br>~~po~~|-<br>~~ee~~<br>~~eee~~<br>~~po~~|
|6<br>~~pot~~<br>~~poof~~|Reserved(Fixed at “0”)<br>~~pot~~<br>~~poof~~||-|-|-|-|-|-|-|-|-|-|-|-|
|5<br>~~pot~~<br>~~poof~~<br>~~poof~~|PrinterStatusByte Count<br>~~pot~~<br>~~poof~~<br>~~poof~~|||OK<br>~~Ge~~|OK|OK|OK|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK|
|4<br>~~poof~~<br>~~eG~~<br>~~poof~~|Fixed at “0”<br>~~poof~~<br>~~eG~~<br>~~poof~~|~~eG~~|-<br>~~eG~~|-<br>~~eG~~<br>~~Ge~~|-<br>~~eG~~|-<br>~~eG~~|-<br>~~eG~~|-<br>~~eG~~<br>~~OO~~|-<br>~~eG~~<br>~~OO~~|-<br>~~eG~~<br>~~OO~~|-<br>~~eG~~<br>~~OO~~|-<br>~~eG~~<br>~~OO~~|-<br>~~eG~~<br>~~OO~~|-<br>~~eG~~|
|3<br>~~poof~~<br>~~pot~~|Printer Status  Byte Count<br>~~poof~~<br>~~pot~~|||OK<br>~~Ge~~|OK|OK|OK|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK|
|2<br>~~poof~~<br>~~pot~~<br>~~pot~~|PrinterStatusByte Count<br>~~poof~~<br>~~pot~~<br>~~pot~~|||OK<br>~~Ge~~|OK|OK|OK|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|OK|
|1<br>~~pot~~<br>~~pot~~|PrinterStatusByte Count<br>~~pot~~<br>~~pot~~|||OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
|0<br>~~pot~~<br>~~pot~~|Fixed at “1”<br>~~pot~~<br>~~pot~~|-<br>~~pot~~|~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|



Actual transmission byte count and header – 1 table 

|Transmission Byte Count n<br>(7 ≤<br>n ≤<br>15)|Header – 1|
|---|---|
|(7 ≤<br>15)<br>7|00001111B (0F Hex)|
|8|00100001B (21 Hex)|
|9|00100011B (23 Hex)|
|10|00100101B (25 Hex)|
|11|00100111B (27 Hex)|
|12|00101001B (29 Hex)|
|13|00101011B (2B Hex)|
|14|00101101B (2D Hex)|
|15|00101111B (2F Hex)|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-7 

## 2. Header -2 

Header -2 is the 1 byte length information transmitted from the second byte of the automatic status.  The table below shows the composition of the Header -2. 

Header -2 represents the automatic status version (called automatic status version below) using bit 1 to bit 3 and bit 5. For reference, the table below shows the relationship of actual version bytes and the Header -2.  The automatic status version will be used as new information is added to the printer status bit positions that were empty, by adding new functions in the future. 

When the host does not control the automatic status version, it is acceptable to ignore Header – 2 received. 

|Bit<br>~~|~~<br>~~poof~~|Contents<br>~~poof~~|Status<br>~~Ge~~<br>~~|~~<br>~~poof~~|Status<br>~~Ge~~<br>~~|~~<br>~~poof~~|Model Compatability<br>~~Ge~~<br>~~|~~|<br>|~~hd}~~|Model Compatability<br>~~Ge~~<br>~~|~~|<br>|~~hd}~~|Model Compatability<br>~~Ge~~<br>~~|~~|<br>|~~hd}~~|Model Compatability<br>~~Ge~~<br>~~|~~|<br>|~~hd}~~|Model Compatability<br>~~Ge~~<br>~~|~~|<br>|~~hd}~~|Model Compatability<br>~~Ge~~<br>~~|~~|<br>|~~hd}~~|Model Compatability<br>~~Ge~~<br>~~|~~|<br>|~~hd}~~|Model Compatability<br>~~Ge~~<br>~~|~~|<br>|~~hd}~~|Model Compatability<br>~~Ge~~<br>~~|~~|<br>|~~hd}~~|Model Compatability<br>~~Ge~~<br>~~|~~|<br>|~~hd}~~|Model Compatability<br>~~Ge~~<br>~~|~~|<br>|~~hd}~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||“0”<br>~~Ge~~<br>~~poof~~|“1”<br>~~Ge~~<br>~~|~~<br>~~poof~~|TSP800<br>~~Ge~~<br>~~|~~||TSP700<br>~~Ge~~<br>||TSP600<br>~~Ge~~<br>~~hd}~~|TUP900 <br>~~Ge~~<br>~~hd}~~|TSP1000 <br>~~Ge~~|TSP828L T<br>~~Ge~~|L TSP700II T<br>~~Ge~~|II TSP650T<br>~~Ge~~|TUP500 <br>~~Ge~~|TSP800II<br>~~Ge~~|FVP10<br>~~Ge~~|
|7<br>~~poof~~|ASBStatusExpansion<br>~~poof~~|NoExpansion<br>~~poof~~|Expansion<br>~~|~~<br>~~poof~~|-<br>~~|~~ ||-<br>||-<br> ~~hd}~~|-<br>~~hd}~~|-|-|-|-|-|-|-|
|6<br>~~pot~~|NotUsed (Fixed at “0”)<br>~~pot~~|~~pot~~|-<br>~~pot~~|-|-|-|-|-|-|-|-|-|-|-|
|5<br>~~poof~~|Version No.<br>~~poof~~|~~poof~~|~~poof~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
|4<br>~~poof~~|Fixed at “0”<br>~~poof~~|~~poof~~|-<br>~~poof~~|-|-|-|-|-|-|-|-|-|-|-|
|3<br>~~poof~~|Version No.<br>~~poof~~|~~poof~~|~~poof~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
|2<br>~~po~~|Version No.<br>~~po~~|~~po~~|~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
|1<br>~~po~~<br>~~pot~~|Version No.<br>~~po~~<br>~~pot~~|~~po~~<br>~~pot~~|~~po~~<br>~~pot~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
|0<br>~~pot~~<br>~~po~~|Fixed at “0”<br>~~pot~~<br>~~po~~|-<br>~~pot~~<br>~~po~~|~~pot~~<br>~~po~~|-|-|-|-|-|-|-|-|-|-|-|



Actual automatic status version and header -2 table 

||Version No. n||Header-2|
|---|---|---|---|
||1||00000010B (02 Hex)|
||2||00000100B (04 Hex)|
||3||00000110B (06 Hex)|
||4||00001000B (08 Hex)|
||5||00001010B (0A Hex)|
||6||00001100B (0C Hex)|
||7||00001110B (0E Hex)|
||8||00100000B (20 Hex)|
||9||00100010B (22 Hex)|
||•||•|
||•||•|
||•||•|
||30||01101100B (6C Hex)|
||31||01101110B (6E Hex)|
||Printer Status Version|||
||Model Name|Version No.|Status|
|TSP800<br>1 (02 Hex)<br>1 (02 Hex)<br>3 (06 Hex)<br>TSP700<br>1 (02 Hex)<br>~~PE~~|||Up to printer status 5 (7thbyte) loaded<br>Up to printer status 6 (8thbyte) loaded, Ver 4.0 and later<br>Up to printer status 7 (9thbyte) loaded, Ver 4.3 and later<br>Up to printer status 5 (7thbyte) loaded|
|||1 (02 Hex)|Up to printer status 6 (8thbyte) loaded, Ver 3.0 and later|
|TSP600<br>~~a~~||3 (06 Hex)<br>1 (02 Hex)<br>1 (02 Hex)<br>3 (06 Hex)<br>~~See eee~~|Up to printer status 7 (9thbyte) loaded, Ver 3.2 and later<br>Up to printer status 5 (7thbyte) loaded<br>Up to printer status 6 (8thbyte) loaded, Ver 3.0 and later<br>Up to printer status 7 (9thbyte) loaded, Ver 3.2 and later<br>~~eee~~|
||TUP900|2 (04 Hex)|Up to printer status 6 (8thbyte) loaded|
|||3 (06Hex)|Up to printerstatus7(9th byte)loaded,Ver 1.2andlater|
||TSP1000, TSP800L,|3 (06 Hex)|Up to printer status 7 (9thbyte) loaded|
||TSP700II, TSP650,|||
||TUP500|||



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-8 

## 3. Printer Status 

Printer status is the status of the printer sent from the third byte of the automatic status. Printer status is returned for (transmitted byte count – 2 in Header – 1). 

Printer status is always updated for new information.  (No log exists.)  The following shows the composition of the status. 

|Bit<br>~~yp~~|Contents<br>~~yp~~|Status<br>~~yp~~<br>~~a~~<br>~~ee~~|Status<br>~~yp~~<br>~~a~~<br>~~ee~~|ModelCompatability<br>~~yp~~<br>~~a~~<br>~~ee~~<br>~~eee~~|ModelCompatability<br>~~yp~~<br>~~a~~<br>~~ee~~<br>~~eee~~|ModelCompatability<br>~~yp~~<br>~~a~~<br>~~ee~~<br>~~eee~~|ModelCompatability<br>~~yp~~<br>~~a~~<br>~~ee~~<br>~~eee~~|ModelCompatability<br>~~yp~~<br>~~a~~<br>~~ee~~<br>~~eee~~|ModelCompatability<br>~~yp~~<br>~~a~~<br>~~ee~~<br>~~eee~~|ModelCompatability<br>~~yp~~<br>~~a~~<br>~~ee~~<br>~~eee~~|ModelCompatability<br>~~yp~~<br>~~a~~<br>~~ee~~<br>~~eee~~|ModelCompatability<br>~~yp~~<br>~~a~~<br>~~ee~~<br>~~eee~~|ModelCompatability<br>~~yp~~<br>~~a~~<br>~~ee~~<br>~~eee~~|ModelCompatability<br>~~yp~~<br>~~a~~<br>~~ee~~<br>~~eee~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||“0”<br>~~yp~~<br>~~a~~|“1”<br>~~yp~~<br>~~ee~~|TSP800<br>~~yp~~<br>~~ee~~|TSP700<br>~~yp~~<br>~~ee~~|TSP600<br>~~yp~~<br>~~ee~~|TUP900 <br>~~yp~~<br>~~ee~~|TSP1000 <br>~~yp~~<br>~~ee~~|TSP828L T<br>~~yp~~<br>~~ee~~|L TSP700II T<br>~~yp~~<br>~~ee~~|II TSP650T<br>~~ee~~|TUP500 <br>~~a~~<br>~~ee~~<br>~~eee~~|TSP800II<br>~~a~~<br>~~ee~~<br>~~eee~~|FVP10<br>~~a~~<br>~~ee~~<br>~~eee~~|
|7<br>~~yp~~<br>~~pot~~<br>~~pot~~|Fixed at “0”<br>~~yp~~<br>~~pot~~<br>~~pot~~|~~yp~~<br>~~a~~<br>~~pot~~|-<br>~~yp~~<br>~~ee~~<br>~~pot~~|-<br>~~yp~~<br>~~ee~~<br>~~pot~~|-<br>~~yp~~<br>~~ee~~<br>~~pot~~|-<br>~~yp~~<br>~~ee~~<br>~~pot~~|-<br>~~yp~~<br>~~ee~~<br>~~pot~~|-<br>~~yp~~<br>~~ee~~<br>~~pot~~|-<br>~~yp~~<br>~~ee~~<br>~~pot~~|-<br>~~yp~~<br>~~ee~~<br>~~pot~~|-<br>~~ee~~<br>~~pot~~|-<br>~~a~~<br>~~ee~~<br>~~eee~~<br>~~pot~~|-<br>~~a~~<br>~~ee~~<br>~~eee~~<br>~~pot~~|-<br>~~a~~<br>~~ee~~<br>~~eee~~<br>~~pot~~|
|6<br>~~pot~~<br>~~pot~~|OFFLINE BySwitch Input<br>~~pot~~<br>~~pot~~|No|Yes|No|No|No|No|No|NO|NO|NO|-|NO|NO|
|5<br>~~pot~~<br>~~pot~~<br>~~**p**~~|CoverStatus<br>~~pot~~<br>~~pot~~<br>~~**p**ot~~|Closed|Open|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
|4<br>~~pot~~<br>~~**p**~~|Fixed at “0”<br>~~pot~~<br>~~**p**ot~~||-|-|-|-|-|-|-|-|-|-|-|-|
|3<br>~~**p**~~<br>~~pot~~|ONLINE/OFFLINE Status<br>~~**p**ot~~<br>~~pot~~|ONLINE|OFFLINE|OK|OK|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|
|2<br>~~pot~~<br>~~**p**~~|ConversionSW<br>~~pot~~<br>~~**p**ot~~|Open|Closed|OK|OK|OK|No|No|NO|OK|OK|NO|OK|OK|
|1<br>~~pot~~<br>~~**p**~~|<ETB>Command<br>~~pot~~<br>~~**p**ot~~|Not Executed|Executed|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
|0<br>~~**p**~~|Fixed at “0”<br>~~**p**ot~~||-|-|-|-<br>~~o~~|-<br>~~o~~|-<br>~~o~~|-<br>~~o~~|-<br>~~o~~|-<br>~~o~~|-<br>~~o~~|-<br>~~o~~|-<br>~~o~~|



- <ETB> Command 

Cleared when received at the host (by clearing bit 1 to 0, automatic status is not targeted to occur). 

|Bit<br>~~a~~|Contents<br>~~a~~|Status<br>~~e~~<br>~~a~~<br>~~ee~~|Status<br>~~e~~<br>~~a~~<br>~~ee~~|ModelCompatability<br>~~e~~~~**e**~~<br>~~ee~~<br>~~ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~e~~~~**e**~~<br>~~ee~~<br>~~ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~e~~~~**e**~~<br>~~ee~~<br>~~ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~e~~~~**e**~~<br>~~ee~~<br>~~ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~e~~~~**e**~~<br>~~ee~~<br>~~ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~e~~~~**e**~~<br>~~ee~~<br>~~ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~e~~~~**e**~~<br>~~ee~~<br>~~ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~e~~~~**e**~~<br>~~ee~~<br>~~ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~e~~~~**e**~~<br>~~ee~~<br>~~ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~e~~~~**e**~~<br>~~ee~~<br>~~ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~e~~~~**e**~~<br>~~ee~~<br>~~ee~~<br>~~e~~<br>~~ee eee~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||“0”<br>~~a~~|“1”<br>~~e~~<br>~~ee~~|TSP800<br>~~e~~~~**e**~~<br>~~ee~~<br>~~ee~~|TSP700<br>~~**e**~~<br>~~ee~~|TSP600<br>~~**e**~~<br>~~ee~~|TUP900<br>~~ee~~|TSP1000 <br>~~ee~~|TSP828L T<br>~~ee~~|L TSP700II T<br>~~ee~~<br>~~e~~|II TSP650<br>~~ee~~<br>~~e~~|TUP500 <br>~~ee~~<br>~~e~~<br>~~ee eee~~|TSP800II<br>~~ee~~<br>~~e~~<br>~~eee~~|FVP10<br>~~ee~~<br>~~e~~<br>~~eee~~|
|7<br>~~a~~<br>~~|~~|Fixed at “0”<br>~~a~~<br>~~|~~|~~|~~|-<br>~~e~~<br>~~ee ~~<br>~~|}~~|-<br>~~e~~~~**e**~~<br> ~~ee~~<br>~~|}~~|-<br>~~**e**~~<br>~~|}tT}?~~|-<br>~~**e**~~<br>~~tT}?~~|-<br>~~tT}?~~|-<br>~~tT}?~~|-<br>~~tT}?~~|-<br>~~e~~|-<br>~~e~~<br>~~tt~~|-<br>~~e~~<br>~~ee eee~~<br>~~tt~~|-<br>~~e~~<br>~~eee~~<br>~~ty~~|-<br>~~e~~<br>~~eee~~<br>~~ty~~|
|6<br>~~|~~|Stopped by high head<br>temperature<br>~~|~~|Not stopped<br>~~|~~|Stopped<br>~~|}~~|OK<br>~~|}~~|OK<br>~~|}tT}?~~|OK<br>~~tT}?~~|OK<br>~~tT}?~~|OK<br>~~tT}?~~|OK<br>~~tT}?~~|OK|OK<br>~~tt~~|OK<br>~~tt~~|OK<br>~~ty~~|OK<br>~~ty~~|
|5<br>~~|~~<br>~~pot~~|Non-recoverableError<br>~~|~~<br>~~pot~~|No<br>~~|~~<br>~~pot~~|Yes<br>~~|}~~<br>~~pot~~|OK<br>~~|}~~<br>~~pot~~|OK<br>~~|} tT}?~~<br>~~pot~~|OK<br>~~tT}?~~<br>~~pot~~|OK<br>~~tT}?~~<br>~~pot~~|OK<br>~~tT}?~~<br>~~pot~~|OK<br>~~tT}?~~<br>~~pot~~|OK<br>~~pot~~|OK<br>~~tt~~<br>~~pot~~|OK<br>~~tt ~~<br>~~pot~~|OK<br> ~~ty~~<br>~~pot~~|OK<br>~~ty~~<br>~~pot~~|
|4<br>~~pot~~|Fixed at “0”<br>~~pot~~|~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|-<br>~~pot~~|
|3<br>~~po~~<br>~~CO~~|Auto-cutter Error<br>~~po~~<br>~~ec~~|No<br>~~po~~<br>~~ec~~|Yes<br>~~po~~<br>~~ec~~|OK<br>~~po~~<br>~~ee ee~~|OK<br>~~po~~<br>~~ee~~|OK<br>~~po~~<br>~~ee~~|OK<br>~~po~~<br>~~ee~~|OK<br>~~po~~|NO<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|
|2<br>~~CO~~<br>~~po~~|Mechanical Error<br>~~ec~~<br>~~po~~|No<br>~~ec~~|Yes<br>~~ec~~|No<br>~~ee ee~~|No<br>~~ee~~|No<br>~~ee~~|No<br>~~ee~~|No|NO|NO|NO|-|NO|NO|
||HeadThermistor Error<br>~~ec~~<br>~~po~~|No<br>~~ec~~|Yes<br>~~ec~~|-<br>~~ee ee~~|-<br>~~ee~~|-<br>~~ee~~|-<br>~~ee~~|-|-|-|-|OK|-|-|
|1<br>~~CO~~<br>~~po~~<br>~~po~~|Not Used(Fixed at “0”)<br>~~ec~~<br>~~po~~<br>~~po~~|~~ec~~<br>~~po~~|~~ec~~<br>~~po~~|-<br>~~ee ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~ee~~<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|
|0<br>~~po~~|Fixed at “0”<br>~~po~~|~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|



<Printer status 3  Error Information (Fifth Byte)> 

|Bit<br>~~a~~|Contents<br>~~a~~|Status<br>~~ee~~<br>~~a~~<br>~~ee~~|Status<br>~~ee~~<br>~~a~~<br>~~ee~~|ModelCompatability<br>~~ee~~<br>~~**e**ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~ee~~<br>~~**e**ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~ee~~<br>~~**e**ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~ee~~<br>~~**e**ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~ee~~<br>~~**e**ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~ee~~<br>~~**e**ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~ee~~<br>~~**e**ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~ee~~<br>~~**e**ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~ee~~<br>~~**e**ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~ee~~<br>~~**e**ee~~<br>~~e~~<br>~~ee eee~~|ModelCompatability<br>~~ee~~<br>~~**e**ee~~<br>~~e~~<br>~~ee eee~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||“0”<br>~~ee~~<br>~~a~~|“1”<br>~~ee~~<br>~~ee~~|TSP800<br>~~ee~~<br>~~**e**~~|TSP700<br>~~ee~~<br>~~**e**~~|TSP600<br>~~ee~~<br>~~**e**~~|TUP900<br>~~**e**ee~~|TSP1000 <br>~~ee~~|TSP828L T<br>~~ee~~<br>~~e~~|L TSP700II T<br>~~ee~~<br>~~e~~|II TSP650<br>~~ee~~<br>~~e~~|TUP500 <br>~~ee~~<br>~~e~~<br>~~ee eee~~|TSP800II<br>~~ee~~<br>~~e~~<br>~~eee~~|FVP10<br>~~ee~~<br>~~e~~<br>~~eee~~|
|7<br>~~a~~<br>~~poof~~|Fixed at “0”<br>~~a~~<br>~~poof~~|~~ee~~<br>~~poof~~|-<br>~~ee~~<br>~~ee~~<br>~~poof~~|-<br>~~ee~~<br>~~poof~~|-<br>~~ee~~<br>~~poof~~|-<br>~~ee~~<br>~~poof~~|-<br>~~poof~~|-<br>~~poof~~|-<br>~~e~~<br>~~poof~~|-<br>~~e~~<br>~~poof~~|-<br>~~e~~<br>~~poof~~|-<br>~~e~~<br>~~ee eee~~<br>~~poof~~|-<br>~~e~~<br>~~eee~~<br>~~poof~~|-<br>~~e~~<br>~~eee~~<br>~~poof~~|
|6|Receive Buffer Overflow|No|Yes|OK|OK|OK|OK|OK|OK<br>~~TT}~~|OK<br>~~TT}~~|OK<br>~~TT}~~|OK<br>~~TT}~~<br>~~ft~~|OK<br>~~ftyt~~|OK<br>~~yt~~|
|5<br>~~|~~|Command Error (in Page<br>Mode)<br>||No<br>||Yes<br>~~|}T}T}T?T?T~~|OK<br>~~|}T}T}T?T?T~~|No<br>~~|}T}T}T?T?T~~|No<br>~~|}T}T}T?T?T~~|No<br>~~|}T}T}T?T?T~~|No<br>~~|}T}T}T?T?T~~|NO<br>~~|}T}T}T?T?T~~<br>~~TT}~~|NO<br>~~|}T}T}T?T?T~~<br>~~TT}~~|NO<br>~~|}T}T}T?T?T~~<br>~~TT}~~|X<br>~~|}T}T}T?T?T~~<br>~~TT}~~<br>~~ft~~|NO<br>~~|}T}T}T?T?T~~<br>~~ftyt~~|NO<br>~~|}T}T}T?T?T~~<br>~~yt~~|
|4<br>~~po~~|Fixed at “0”<br>~~po~~|~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~TT}~~<br>~~po~~|-<br>~~TT}~~<br>~~po~~|-<br>~~TT}~~<br>~~po~~|-<br>~~TT}~~<br>~~ft~~<br>~~po~~|-<br>~~ft yt~~<br>~~po~~|-<br>~~yt~~<br>~~po~~|
|3<br>~~pot~~|BM Error<br>~~pot~~|No<br>~~pot~~|Yes<br>~~pot~~|No<br>~~pot~~|No<br>~~pot~~|No<br>~~pot~~|OK<br>~~pot~~|OK<br>~~pot~~|OK*<br>~~pot~~|OK<br>~~pot~~|NO<br>~~pot~~|OK<br>~~pot~~|OK<br>~~pot~~|OK<br>~~pot~~|
|2<br>~~pot~~<br>~~ee~~|Presenter PaperJam Error<br>~~pot~~<br>~~ee~~|No<br>~~pot~~<br>~~ee~~|Yes<br>~~pot~~<br>~~ee~~|No<br>~~pot~~<br>~~ee~~|No<br>~~pot~~|No<br>~~pot~~|OK<br>~~pot~~|No<br>~~pot~~|NO<br>~~pot~~|NO<br>~~pot~~|NO<br>~~pot~~|OK<br>~~pot~~|NO<br>~~pot~~|NO<br>~~pot~~|
|1<br>~~ee~~<br>~~po~~|Head UpError<br>~~ee~~<br>~~po~~|No<br>~~ee~~|Yes<br>~~ee~~|No<br>~~ee~~|No|No|No|No|NO|NO|NO|-|NO|NO|
||Electric Voltage Error<br>~~ee~~<br>~~po~~|No<br>~~ee~~|Yes<br>~~ee~~|-<br>~~ee~~|-|-|-|-|-|-|-|OK|-|-|
|0<br>~~ee~~<br>~~po~~<br>~~po~~|Fixed at “0”<br>~~ee ~~<br>~~po~~<br>~~po~~|~~ee~~<br>~~po~~|-<br>~~ee ~~<br>~~po~~|-<br> ~~ee~~<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|-<br>~~po~~|



- Receive Buffer Overflow 

Overflow errors cleared to 0 when returned to host. 

- Command Error (in Page Mode) 

Command errors cleared to 0 when returned to host. 

- BM Error 

On models that use a common PE and BM sensor, if a continuous error is detected beyond a determined amount, it indicates not a black mark error, but a paper out error. 

- (*) TSP828L (Label Printer) BM errors occur for the following reasons. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-9 

|TSP828L Operation Mode|Sensor Used|Cause of BM Errors|
|---|---|---|
|Tear Bar Mode|Transmissive Type|Detected label paper over 400 mm<br>Detected base paper over 400 mm<br>Detected page error (When MSW is valid)<br>When lengtherrordetected (When MSW isvalid)|
||Reflective Type|Detected label paper over 400 mm<br>Detected page error (When MSW is valid)<br>When lengtherrordetected (When MSW isvalid)|
|Peel Mode|Transmissive Type|Detected label paper over 400 mm<br>Detected base paper over 400 mm<br>Detected page error<br>When lengtherrordetected (When MSW isvalid)|
||Reflective Type|Detected label paper over 400 mm<br>Detected page error<br>When lengtherrordetected (When MSW isvalid)|



<Printer status 4  Sensor Information (Sixth Byte)> 

|Bit<br>~~ee~~<br>~~Fs~~|Contents<br>~~ee~~<br>|Status<br>~~ee~~|Status<br>~~ee~~|Model Compatability<br>~~ee~~|Model Compatability<br>~~ee~~|Model Compatability<br>~~ee~~|Model Compatability<br>~~ee~~|Model Compatability<br>~~ee~~|Model Compatability<br>~~ee~~|Model Compatability<br>~~ee~~|Model Compatability<br>~~ee~~|Model Compatability<br>~~ee~~|Model Compatability<br>~~ee~~|Model Compatability<br>~~ee~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||“0”<br>~~ee~~<br>~~SC~~<br>|“1”<br>~~ee~~<br>~~SC~~<br>|TSP800<br>~~ee~~<br>~~CO~~<br>|TSP700<br>~~ee~~<br>~~CO GO~~<br>|TSP600<br>~~ee~~<br>~~GO~~<br>|TUP900 <br>~~ee~~<br>~~GO~~<br>|TSP1000 <br>~~ee~~<br>~~GO~~<br>|TSP828L T<br>~~ee~~<br>~~GO~~<br>|L TSP700II T<br>~~ee~~<br>~~GO~~<br>|II TSP650T<br>~~ee~~<br>~~GO~~<br>|TUP500 <br>~~ee~~<br>~~GO~~<br>|TSP800II<br>~~ee~~<br>~~GO~~<br>|FVP10<br>~~ee~~<br>~~GO~~<br>|
|7<br>~~Fs~~|Fixed at “0”<br>~~OO~~|~~SC~~<br>~~OO~~|-<br>~~SC~~<br>~~OO~~|-<br>~~CO~~<br>~~OO~~|-<br>~~CO GO~~<br>~~OO~~|-<br>~~GO~~<br>~~OO~~|-<br>~~GO~~<br>~~OO~~|-<br>~~GO~~<br>~~OO~~|-<br>~~GO~~<br>~~OO~~|-<br>~~GO~~<br>~~OO~~|-<br>~~GO~~<br>~~OO~~|-<br>~~GO~~<br>~~OO~~|-<br>~~GO~~<br>~~OO~~|-<br>~~GO~~<br>~~OO~~|
|6<br>~~Fs~~<br>~~a~~|NotUsed (Fixed at “0”)<br>~~OO~~<br>~~a~~|~~SC~~<br>~~OO~~|-<br>~~SC ~~<br>~~OO~~<br>~~CO~~|-<br> ~~CO~~<br>~~OO~~<br>~~CO~~|-<br>~~CO GO~~<br>~~OO~~<br>~~CO~~|-<br>~~GO~~<br>~~OO~~<br>~~CO~~|-<br>~~GO~~<br>~~OO~~|-<br>~~GO~~<br>~~OO~~|-<br>~~GO~~<br>~~OO~~<br>~~CO~~|-<br>~~GO~~<br>~~OO~~<br>~~CO~~|-<br>~~GO~~<br>~~OO~~<br>~~CO~~|-<br>~~GO~~<br>~~OO~~|-<br>~~GO~~<br>~~OO~~|-<br>~~GO~~<br>~~OO~~|
|5<br>~~a~~<br>~~a~~|Not Used(Fixed at “0”)<br>~~a~~<br>~~a~~||-<br>~~CO~~<br>~~CO~~|-<br>~~CO~~<br>~~CO~~|-<br>~~CO~~<br>~~CO~~|-<br>~~CO~~<br>~~CO~~|-|-<br>~~CO~~|-<br>~~CO~~<br>~~CO~~|-<br>~~CO~~<br>~~CO~~|-<br>~~CO~~<br>~~CO~~|-|-|-|
|4<br>~~a~~|Fixed at “0”<br>~~a~~||-<br>~~CO~~|-<br>~~CO~~|-<br>~~CO~~|-<br>~~CO~~|-|-<br>~~OO~~|-<br>~~OO~~|-<br>~~OO~~|-<br>~~OO~~|-|-|-|
|3<br>~~A~~|Paperend<br>~~A~~|Paper|NoPaper<br>~~CO~~|OK<br>~~CO~~|OK<br>~~CO~~|OK<br>~~CO~~|OK|OK|OK<br>~~CO~~|OK<br>~~CO~~|OK<br>~~CO~~|OK|OK|OK|
|2<br>~~A~~|Paper Near-end(Inner Side)<br>~~A~~|Paper|No Paper<br>~~CO~~|OK<br>~~CO~~|OK<br>~~CO~~|OK<br>~~CO~~|OK<br>~~CO~~|OK|NO<br>~~CO~~|OK<br>~~CO~~|OK<br>~~CO~~|OK|OK|OK|
|1<br>~~a~~|Paper Near-end (OuterSide)<br>~~a ~~|Paper<br> ~~OC~~|NoPaper<br>~~OC~~|No<br>~~OC~~|No<br>~~OC~~|No<br>~~OC~~|No<br>~~OC~~|No<br>~~OC~~|NO<br>~~OC~~|NO<br>~~OC~~|NO<br>~~OC~~|NO<br>~~OC~~|NO<br>~~OC~~|NO<br>~~OC~~|
|0<br>~~a~~|Fixed at “0”<br>~~a~~||-|-<br>~~A~~|-<br>~~A~~|-<br>~~A~~|-<br>~~A~~|-|-<br>~~CG~~|-<br>~~CG~~|-<br>~~CG~~|-|-|-|



<Printer status 5  Sensor Information (Seventh Byte)> 

|Bit<br>~~ee~~<br>~~FS~~|Contents<br>~~ee~~<br>~~SS~~|Status<br>~~eeee~~<br>~~SSCO~~|Status<br>~~eeee~~<br>~~SSCO~~|Model Compatability<br>~~eeeee eee eee~~<br>~~CO~~~~**O**O~~|Model Compatability<br>~~eeeee eee eee~~<br>~~CO~~~~**O**O~~|Model Compatability<br>~~eeeee eee eee~~<br>~~CO~~~~**O**O~~|Model Compatability<br>~~eeeee eee eee~~<br>~~CO~~~~**O**O~~|Model Compatability<br>~~eeeee eee eee~~<br>~~CO~~~~**O**O~~|Model Compatability<br>~~eeeee eee eee~~<br>~~CO~~~~**O**O~~|Model Compatability<br>~~eeeee eee eee~~<br>~~CO~~~~**O**O~~|Model Compatability<br>~~eeeee eee eee~~<br>~~CO~~~~**O**O~~|Model Compatability<br>~~eeeee eee eee~~<br>~~CO~~~~**O**O~~|Model Compatability<br>~~eeeee eee eee~~<br>~~CO~~~~**O**O~~|Model Compatability<br>~~eeeee eee eee~~<br>~~CO~~~~**O**O~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||“0”<br>~~ee~~<br>~~SS~~|“1”<br>~~ee~~<br>~~CO~~|TSP800<br>~~eee~~<br>~~CO~~|TSP700<br>~~ee eee~~<br>~~CO~~|TSP600<br>~~eee~~<br>~~CO~~|TUP900<br>~~eee~~<br>~~**O**~~|TSP1000 <br>~~eee~~<br>~~**O**~~|TSP828L T<br>~~eee eee~~<br>~~**O**O~~|L TSP700II T<br>~~eee~~<br>~~O~~|II TSP650T<br>~~eee~~|TUP500<br>~~eee~~|TSP800II<br>~~eee~~|FVP10<br>~~eee~~|
|7<br>~~ee~~<br>~~FS~~|Fixed at “0”<br>~~ee ~~<br>~~SS~~<br>~~A~~|~~ee ~~<br>~~SS~~<br>~~A~~|-<br> ~~ee ~~<br>~~CO~~<br>~~A~~|-<br> ~~eee ~~<br>~~CO~~<br>~~O~~|-<br> ~~ee eee~~<br>~~CO~~<br>~~O~~|-<br>~~eee~~<br>~~CO~~<br>~~O~~|-<br>~~eee~~<br>~~**O**~~<br>~~O~~|-<br>~~eee~~<br>~~**O**~~|-<br>~~eee eee~~<br>~~**O**O~~|-<br>~~eee~~<br>~~O~~|-<br>~~eee~~<br>~~O~~|-<br>~~eee~~<br>~~O~~|-<br>~~eee~~<br>~~O~~|-<br>~~eee~~<br>~~O~~|
|6<br>~~FS~~<br>~~A~~|NotUsed (Fixed at “0”)<br>~~SS~~<br>~~A~~|~~SS ~~<br>~~A~~|-<br> ~~CO~~<br>~~A~~|-<br>~~CO~~<br>~~A~~|-<br>~~CO~~<br>~~CC~~|-<br>~~CO ~~<br>~~CC~~|-<br> ~~**O**~~<br>~~CC~~|-<br>~~**O**~~<br>~~CC~~|-<br>~~**O**O~~<br>~~OO~~|-<br>~~O~~<br>~~OO~~|-<br>~~OO~~|-<br>~~OO~~|-|-|
|5<br>~~a~~|Not Used(Fixed at “0”)<br>~~a~~|~~A~~|-<br>~~A~~|-<br>~~A~~|-<br>~~CC~~|-<br>~~CC~~|-<br>~~CC~~|-<br>~~CC~~|-<br>~~OO~~|-<br>~~OO~~|-<br>~~OO~~|-<br>~~OO~~|-|-|
|4<br>~~a ~~|Fixed at “0”<br> ~~a~~|~~A~~|-<br>~~A~~|-<br>~~A~~|-<br>~~CC~~|-<br>~~CC~~|-<br>~~CC~~|-<br>~~CC~~|-<br>~~CE~~|-<br>~~CE~~|-|-|-|-|
|3<br>~~a ~~|SlipBOF Detector<br> ~~a~~|Paper<br>~~A~~|NoPaper<br>~~A~~|No<br>~~A~~|No<br>~~CC~~|No<br>~~CC~~|No<br>~~CC~~|No<br>~~CC~~|NO<br>~~CE~~|NO<br>~~CE~~|NO|No|NO|No|
|2<br>~~a~~<br>~~ee~~|SlipTOF Detector<br>~~a~~<br>~~ee~~|Paper<br>~~CA~~<br>~~ee~~|No Paper<br>~~CA~~<br>~~ce~~|No<br>~~CA~~<br>~~ee~~|No<br>~~CC~~<br>~~ee~~|No<br>~~CC~~<br>~~ee~~|No<br>~~CC~~|No<br>~~CC~~|NO<br>~~CE~~|NO<br>~~CE~~|NO|No|NO|No|
|1<br>~~ee~~<br>~~2~~|Presenter Paper Detector<br>~~ee~~<br>~~ee~~|NoPaper<br>~~ee~~<br>~~ee~~|Paper<br>~~ce~~<br>~~ee~~|No<br>~~ee~~|No<br>~~ee~~|No<br>~~ee~~|No|||NO|NO|No|NO|No|
||Stack Sensor Detector<br>Peel Sensor Detector<br>~~ee~~<br>~~ee~~|No Paper<br>No Paper<br>~~ee~~<br>~~ee~~|Paper<br>Paper<br>~~ce~~<br>~~ee~~|~~ee~~|~~ee~~|~~ee~~||OK|OK|NO<br>NO|NO<br>NO|NO<br>NO|NO<br>NO|NO<br>NO|
|0<br>~~ee~~<br>~~2~~|Fixed at “0”<br>~~ee~~<br>~~ee~~|~~ee ~~<br>~~ee~~|-<br> ~~ce ~~<br>~~ee~~|-<br> ~~ee ~~|-<br> ~~ee~~|-<br>~~ee~~|-|-|-|-|-|-|-|-|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-10 

## <Printer status 6  ETB Counter (Eighth Byte)> 

|~~Ue~~<br>~~FS~~|~~Se~~<br>~~Ue cee~~|~~Se~~<br>~~ceecee~~|~~Se~~<br>~~ceecee~~|~~eeeeeeeeeeeeeee~~|~~eeeeeeeeeeeeeee~~|~~eeeeeeeeeeeeeee~~|~~eeeeeeeeeeeeeee~~|~~eeeeeeeeeeeeeee~~|~~eeeeeeeeeeeeeee~~|~~eeeeeeeeeeeeeee~~|~~eeeeeeeeeeeeeee~~|~~eeeeeeeeeeeeeee~~|~~eeeeeeeeeeeeeee~~|~~eeeeeeeeeeeeeee~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Bit<br>~~Ue~~<br>~~FS~~|Contents<br>~~Se~~<br>~~Ue cee~~|Status<br>~~Se~~<br>~~ceecee~~||ModelCompatability<br>~~eeeeeeeeeeeeeee~~|||||||||||
|||“0”<br>~~Se~~<br>~~cee~~|“1”<br>~~Se~~<br>~~cee~~|TSP800<br>~~ee~~|TSP700<br>~~eee~~|TSP600<br>~~eee~~|TUP900<br>~~ee~~|TSP1000 <br>~~ee~~|TSP828L TSP700II TSP650<br>~~ee~~|TSP828L TSP700II TSP650<br>~~eee~~|TSP828L TSP700II TSP650<br>~~eee~~|TUP500<br>~~eee~~|TSP800II<br>~~eee~~|FVP10<br>~~eee~~|
|7<br><br>~~FS~~|Fixed at0<br>~~cee~~|~~cee~~<br>~~SO~~|-<br>~~cee~~<br>~~SO~~|-<br>~~ee~~<br>~~SO~~|-<br>~~eee~~<br>~~SO~~|-<br>~~eee~~|-<br>~~ee~~|-<br>~~ee~~|-<br>~~ee~~|-<br>~~eee~~|-<br>~~eee~~|-<br>~~eee~~|-<br>~~eee~~|-<br>~~eee~~|
|6<br><br>~~FS~~<br>~~OC~~|ETBCounter  Bit-4<br>~~cee~~<br>~~OC~~|~~cee ~~<br>~~SO~~<br>~~OC~~|~~cee ~~<br>~~SO~~<br>~~OC~~|OK<br> ~~ee ~~<br>~~SO~~<br>~~OC~~|OK<br> ~~eee ~~<br>~~SO~~<br>~~OC~~|OK<br> ~~eee ~~<br>~~OC~~|OK<br> ~~ee~~<br>~~OC~~|OK<br>~~ee ~~<br>~~OC~~|OK<br> ~~ee~~<br>~~OC~~|OK<br>~~eee~~<br>~~OC~~|OK<br>~~eee~~<br>~~OC~~|OK<br>~~eee~~<br>~~OC~~|OK<br>~~eee~~<br>~~OC~~|OK<br>~~eee~~<br>~~OC~~|
|5<br>~~OC~~<br>~~OC~~|ETBCounter  Bit-3<br>~~OC~~<br>~~OC~~|~~OC~~<br>~~OC~~|~~OC~~<br>~~OC~~|OK<br>~~OC~~<br>~~OC~~|OK<br>~~OC~~<br>~~OC~~|OK<br>~~OC~~<br>~~OC~~|OK<br>~~OC~~<br>~~OC~~|OK<br>~~OC~~<br>~~OC~~|OK<br>~~OC~~<br>~~OC~~|OK<br>~~OC~~<br>~~OC~~|OK<br>~~OC~~<br>~~OC~~|OK<br>~~OC~~<br>~~OC~~|OK<br>~~OC~~<br>~~OC~~|OK<br>~~OC~~<br>~~OC~~|
|4<br>~~OC~~<br>~~a~~|Fixed at 0<br>~~OC~~<br>~~a~~|~~OC~~|-<br>~~OC~~<br>~~GC~~|-<br>~~OC~~<br>~~GC~~|-<br>~~OC~~<br>~~GC~~|-<br>~~OC~~<br>~~GC~~|-<br>~~OC~~|-<br>~~OC~~|-<br>~~OC~~|-<br>~~OC~~|-<br>~~OC~~|-<br>~~OC~~|-<br>~~OC~~|-<br>~~OC~~|
|3<br>~~a CC~~|ETBCounter  Bit-2<br>~~CC~~|~~CC~~|~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|
|2<br>~~a CC~~|ETBCounter  Bit-1<br>~~CC~~|~~CC~~|~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|OK<br>~~CC~~|
|1<br>~~GC~~|ETB Counter  Bit-0<br>~~GC~~|~~GC~~|~~GC~~|OK<br>~~GC~~|OK<br>~~GC~~|OK<br>~~GC~~|OK<br>~~GC~~|OK<br>~~GC~~|OK<br>~~GC~~|OK<br>~~GC~~|OK<br>~~GC~~|OK<br>~~GC~~|OK<br>~~GC~~|OK<br>~~GC~~|
|0<br>~~CC~~|Fixed at0<br>~~CC~~|~~CC~~|-<br>~~CC~~|-<br>~~CC~~|-<br>~~CC~~|-<br>~~CC~~|-<br>~~CC~~|-<br>~~CC~~|-<br>~~CC~~|-<br>~~CC~~|-<br>~~CC~~|-<br>~~CC~~|-<br>~~CC~~|-<br>~~CC~~|



(*) ETB Counter 

## This counter is the 5 bit ETB counter. 

(It counts from 0 to 31.  When the counter overflows, it counts up from 31 to 0.) This counter is incremented by 1 using the <ETB> command. 

The ETB counter is initialized by the following commands.   When doing so, ASB ETB status is cleared. However, when initializing the ETB counter, ASB is not transmitted. 

## <ETB Counter Initialization Commands> 

• <ESC> <RS> E n : ETB Counter Initialization • <CAN> : Cancel print data and initialize commands 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-11 

|Bit<br>~~‘|~~<br>~~FS~~|Contents<br>~~‘|F711)~~<br>~~OO~~|Status<br>~~F711)~~|Status<br>~~F711)~~|Bymodel<br>~~F711)~~|Bymodel<br>~~F711)~~|Bymodel<br>~~F711)~~|Bymodel<br>~~F711)~~|Bymodel<br>~~F711)~~|Bymodel<br>~~F711)~~|Bymodel<br>~~F711)~~|Bymodel<br>~~F711)~~|Bymodel<br>~~F711)~~|Bymodel<br>~~F711)~~|Bymodel<br>~~F711)~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||“0”<br>~~F711)~~<br>~~OO~~|“1”<br>~~F711)~~<br>~~OO~~|TSP800<br>Ver. 4.3 or<br>later<br>~~F711)~~<br>~~OO~~|TSP700<br>Ver. 4.3 or<br>Ver. 3.2 or<br>later<br>~~F711)~~<br>~~OO~~|TSP600<br>Ver. 3.2 or<br>Ver. 3.2 or<br>later<br>~~F711)~~<br>~~OO~~|TUP900<br>Ver. 3.2 or<br>Ver. 1.2 or<br>later<br>~~F711)~~<br>~~OO~~|TSP1000 <br>Ver. 1.2 or<br>~~F711)~~<br>~~OO~~|TSP828L TSP700II TSP650<br>~~F711)~~<br>~~OO~~<br>~~OO~~|TSP828L TSP700II TSP650<br>~~F711)~~<br>~~OO~~<br>~~OO~~|TSP828L TSP700II TSP650<br>~~F711)~~<br>~~OO~~<br>~~OO~~|TUP500<br>~~F711)~~<br>~~OO~~|TSP800II<br>~~F711)~~<br>~~OO~~|FVP10<br>~~F711)~~<br>~~OO~~|
|7<br>~~‘|~~<br>~~FS~~|Fixed at “0”<br>~~‘| F711)~~<br>~~OO~~|~~F711)~~<br>~~OO~~|-<br>~~F711)~~<br>~~OO~~|-<br>~~F711)~~<br>~~OO~~|-<br>~~F711)~~<br>~~OO~~|-<br>~~F711)~~<br>~~OO~~|-<br>~~F711)~~<br>~~OO~~|-<br>~~F711)~~<br>~~OO~~|-<br>~~F711)~~<br>~~OO~~<br>~~OO~~|-<br>~~F711)~~<br>~~OO~~<br>~~OO~~|-<br>~~F711)~~<br>~~OO~~<br>~~OO~~|-<br>~~F711)~~<br>~~OO~~|-<br>~~F711)~~<br>~~OO~~|-<br>~~F711)~~<br>~~OO~~|
|6<br>~~FS~~<br>~~pp~~|Not Used(Fixed at “0”)<br>~~OO~~<br>~~pp~~|~~OO~~<br>~~pp~~|-<br>~~OO~~<br>~~pp~~|NO<br>~~OO~~<br>~~pp~~|NO<br>~~OO~~<br>~~pp~~|NO<br>~~OO~~<br>~~pp~~|OK<br>~~OO~~<br>~~pp~~|NO<br>~~OO~~<br>~~pp~~|NO<br>~~OO~~<br>~~OO~~<br>~~pp~~|NO<br>~~OO~~<br>~~OO~~<br>~~pp~~|NO<br>~~OO~~<br>~~OO~~<br>~~pp~~|NO<br>~~OO~~<br>~~pp~~|NO<br>~~OO~~<br>~~pp~~|NO<br>~~OO~~<br>~~pp~~|
|5<br>~~pp~~<br>~~a~~|NotUsed (Fixed at “0”)<br>~~pp~~<br>~~a~~|~~pp~~|-<br>~~pp~~<br>~~A~~|NO<br>~~pp~~<br>~~A CO~~|NO<br>~~pp~~<br>~~CO~~|NO<br>~~pp~~<br>~~CO~~|OK<br>~~pp~~<br>~~CO~~|NO<br>~~pp~~<br>~~CO~~|NO<br>~~pp~~<br>~~CO~~|NO<br>~~pp~~<br>~~CO~~|NO<br>~~pp~~<br>~~CO~~|NO<br>~~pp~~<br>~~CO~~|NO<br>~~pp~~<br>~~CO~~|NO<br>~~pp~~<br>~~CO~~|
|4<br>~~a~~<br>~~a~~<br>~~|~~|Fixed at “0”<br>~~a~~<br>~~a~~<br>~~|~~|~~|~~<br>~~|~~|-<br>~~A~~<br>~~A~~<br>~~|~~|-<br>~~A CO~~<br>~~A CO~~<br>~~ttt~~|-<br>~~CO~~<br>~~CO~~<br>~~ttt~~|-<br>~~CO~~<br>~~CO~~<br>~~ttt~~|-<br>~~CO~~<br>~~CO~~<br>~~yy~~|-<br>~~CO~~<br>~~CO~~<br>~~yy~~|-<br>~~CO~~<br>~~CO~~<br>~~yy~~<br>~~|~~|-<br>~~CO~~<br>~~CO~~<br>~~ft~~|-<br>~~CO~~<br>~~CO~~<br>~~fttt~~|-<br>~~CO~~<br>~~CO~~<br>~~tt~~|-<br>~~CO~~<br>~~CO~~<br>~~tt~~|-<br>~~CO~~<br>~~CO~~|
|3<br>~~|~~<br>~~|~~|Presenter Paper Position<br>~~|~~<br>~~|~~|(See table<br>below)<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~|~~|~~<br>~~|}~~|NO<br>~~ttt~~<br>~~|}~~|NO<br>~~ttt~~<br>~~|}tty~~|NO<br>~~ttt~~<br>~~tty~~|OK<br>~~yy~~<br>~~tty~~|NO<br>~~yy~~<br>~~tty~~|NO<br>~~yy~~<br>~~|~~<br>~~|~~|NO<br>~~ft~~<br>~~ft~~|NO<br>~~fttt~~<br>~~ft~~|OK<br>~~tt~~<br>~~yt~~|NO<br>~~tt~~<br>~~yt~~|NO|
|2<br>~~|~~<br>~~|~~<br>~~|~~|Presenter Paper Position<br>~~|~~<br>~~|~~<br>~~|~~|(See table<br>below)<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~|~~| ~~<br>~~|}~~<br>~~|}~~|NO<br> ~~ttt~~<br>~~|}~~<br>~~|}~~|NO<br>~~ttt~~<br>~~|}tty~~<br>~~|}tty~~|NO<br>~~ttt ~~<br>~~tty~~<br>~~tty~~|OK<br> ~~yy~~<br>~~tty~~<br>~~tty~~|NO<br>~~yy~~<br>~~tty~~<br>~~tty~~|NO<br>~~yy~~<br>~~|~~<br>~~|~~<br>~~|~~|NO<br>~~ft~~<br>~~ft~~<br>~~ft~~|NO<br>~~ft tt~~<br>~~ft~~<br>~~ft~~|OK<br>~~tt~~<br>~~yt~~<br>~~yt~~|NO<br>~~tt~~<br>~~yt~~<br>~~yt~~|NO|
|1<br>~~|~~<br>~~|~~|Presenter Paper Position<br>~~|~~<br>~~|~~|(See table<br>below)<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~|~~|}~~<br>~~|}~~|NO<br>~~|}~~<br>~~|}~~|NO<br>~~|} tty~~<br>~~|}tty~~|NO<br>~~tty~~<br>~~tty~~|OK<br>~~tty~~<br>~~tty~~|NO<br>~~tty~~<br>~~tty~~|NO<br>~~|~~<br>~~|~~|NO<br>~~ft~~<br>~~ft~~|NO<br>~~ft ~~<br>~~ft~~|OK<br> ~~yt~~<br>~~yt~~|NO<br>~~yt~~<br>~~yt~~|NO|
|0<br>~~|~~<br>~~CC~~|Fixed at “0”<br>~~|~~<br>~~CC~~|~~|~~<br>~~|~~<br>~~CC~~|-<br>~~|}~~<br>~~CC~~|-<br>~~|}~~<br>~~CC~~|-<br>~~|} tty~~<br>~~CC~~|-<br>~~tty~~<br>~~CC~~|-<br>~~tty~~<br>~~CC~~|-<br>~~tty~~<br>~~CC~~|-<br>~~|~~<br>~~CC~~|-<br>~~ft~~<br>~~CC~~|-<br>~~ft ~~<br>~~CC~~|-<br> ~~yt~~<br>~~CC~~|-<br>~~yt~~<br>~~CC~~|-<br>~~CC~~|



- This status is made valid and invalid using the memory switch only on models provided with a presenter. 

When valid, the presenter paper position status is updated, but when invalid, the presenter paper position status is fixed at “0” and there is no change in status. 

- Details of the Presenter Paper Position 

|Operating<br>Mode|Paper|Presenter paper position state transition|
|---|---|---|
|Loop<br>Take-up<br>Internal<br>recovery|Recovery|Position 0 to Position 1 to (Paper cut) to Position 3 to (Paper recovery) to Position 6 to Position 0|
||Pull out|Position 0 to Position 1 to (Paper cut) to Position 3 to (Paper pull out) to Position 7 to Position 0|
|Loop<br>Take-up<br>Front<br>Discharge|Recovery|Position 0 to Position 1 to (Paper cut) to Position 3 to (Paper pull out) to Position 6 to Position 0|
||Pull out|Position 0 to Position 1 to (Paper cut) to Position 3 to (Paper pull out) to Position 7 to Position 0|
|No Loop<br>Internal<br>recovery|Recovery|Position0 toPosition 1to (Papercut) toPosition3 to (Paperpullout) toPosition6 toPosition0|
||Pull out|Position 0 to Position 1 to (Paper cut) to Position 3 to (Paper pull out) to Position 7 to Position 0|
|No Loop<br>Front<br>Discharge|Recovery|Position0 toPosition 1to (Papercut) toPosition3 to (Paperpullout) toPosition6 toPosition0|
||Pull out|Position 0 to Position 1 to (Paper cut) to Position 3 to (Paper pull out) to Position 7 to Position 0|
|Recovery<br>Invalid|Recovery|Position 0 to Position 1 to (Paper cut) to Position 6                                                        to Position 0|
||Pullout|Position0toPosition 1 to (Papercut)toPosition6toPosition0|



## 4. Note 

Do not use ENQ, EOT, and ESC ACK SOH when automatic status is valid.  Invalidate the automatic status in advance using the DIPSW (memory switch) or the ESC RS a n command to query these. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-12 

3) Status identification method Command/Functions Status ~~a Ce~~ bit7 bit6 bit5 ~~EEE~~ bit4 bit3 bit2 bit1 bit0 ~~Oe~~ XON 0 ~~GD~~ 0 0 ~~ID~~ 1 0 ~~OO~~ 0 0 1 ~~Gn~~ XOFF 0 0 0 1 ~~nD~~ 0 0 1 1 ~~sees~~ ENEOT Q * * * * ~~ss~~ * * ~~ss~~ 01 ~~ssI~~ * * * * * * 0 * ~~De~~ ASB (Header – 1) 0 * ~~DD~~ * 0 * * * 1 ~~Po~~ ASB (Other than Header – 1) 0 * * 0 * * * 0 Indicates “0” bit is fixed at 0/Indicates 1 is fixed at 1/Indicates * variable bit. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

5-13 

## **5.2.4 Prin ter status transmission specification when using Ethernet I/F and Wireless LAN I/F** 

The following describes printer status transmission specifications when using an Ethernet I/F and wireless LAN I/F. 

## 1) Transmission Format: 

• When transmitting only STAR ASB: ~~a~~ STAR ASB (Second Byte Bit 7 = 1) + Length (Length = 0x0000) 

## • When transmitting printer status other than STAR ASB: ~~7~~ STAR ASB (Second Byte Bit 7 = 1) + Length ~~6)~~ + Status Data 

## <Length Details> 

- 2 byte value indicating status data byte count (0x0000 ≤ Length ≤ 0x0200) 

- When the status data is 10 bytes: Length = 0x000a 

- Apply Length = 0x0000 to only transmit STAR ASB. 

- When STAR ASB Second Byte Bit-7 is applied with Length, set to Bit-7 = 1 

In analysis of printer statuses, the total number of bytes of the ASB according to the STAR ASB First byte is detected, and it is detected whether Length has been applied by the second byte Bit-7 of STAR ASB. Depending on the length, by acquiring subsequent status data byte counts, it is possible to analyze the status. 

## 2) ~~a~~ Status data transmission format 

~~PO~~ Status type + separator character 1 ~~SS~~ + data type + status length + _printer status_ + separator character 2 

1. Status Type (2byte or 4Byte) 

   - First and Second Bytes 

Indicate the cause to generate a printer status. • “00”: Reserved • “01” to ”09”: Star real-time status request command • ”10” to ”49”: Star status request command • “50”: Reserved • “51” to ”59”: Reserved • “60” to ”99”: Reserved • “A0” to “FF”: Reserved 

• Third and Fourth Bytes When a cause occurs, these indicate the command n parameter. If there is no n parameter, the third and fourth bytes can be omitted. <Ex.> When n = 0x31 using the ESC SYN 3 n command, the third and fourth bytes are “31.” 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-14 

2. Separator character 1 (1 Byte) Sends “:” 

## 3. Data Type (1byte) 

Indicate printer status data; sends “B” (binary type). 

## 4. Status Length (2 bytes) 

- 2 byte value indicating printer status byte count. 

## 5. Printer Status (Variable length) 

Status sent by printer. Status differs according to the cause. 

See the command causes and automatic status for details on the content of statuses. 

## 6. Separator character 2 (1 Byte) 

Sends “;” 

3) Status Transmission Specification List 

|Status Cause<br>~~|~~|STAR ASB<br>||Length<br>~~LLL~~|StatusData<br>~~|~~<br>~~LLL~~|StatusData<br>~~|~~<br>~~LLL~~|StatusData<br>~~|~~<br>~~LLL~~|StatusData<br>~~|~~<br>~~LLL~~|StatusData<br>~~|~~<br>~~LLL~~|StatusData<br>~~|~~<br>~~LLL~~|StatusData<br>~~|~~<br>~~LLL~~|
|---|---|---|---|---|---|---|---|---|---|
||||StatusType<br>~~|~~<br>~~LLL~~||Separated<br>Character 1<br>~~|~~<br>~~LLL~~|Data<br>Type<br>~~|~~<br>~~LLL~~|Status<br>Length<br>~~|~~<br>~~LLL~~|Printer<br>Status<br>~~|~~<br>~~LLL~~|Separated<br>Character 2<br>~~|~~<br>~~LLL~~|
||||First/Second<br>Bytes<br>Cause<br>~~|~~<br>~~LLL~~|Third/Fourth<br>Bytes<br>n Parameter<br>~~|~~<br>~~LLL~~||||||
|ASB<br>Automatic Status<br>~~es~~|ASB|0x0000|--|--|--|--|--|--|--|
|ESC ACK SOH<br>Printer<br>Status<br>Request<br>~~es~~|ASB|0x0000|--|--|--|--|--|--|--|
|ENQ<br>Printer<br>Status<br>Request|ASB|0x0008|“01”|Omitted|“:”|“B”|0x0001|Status|“;”|
|EOT<br>Printer<br>Status<br>Request|ASB|0x0008|“02”|Omitted|“:”|“B”|0x0001|Status|“;”|
|ESC SYN 3 n<br>Presenter Counter<br>Request|ASB|0x0011|“13”|“00”≤<br> n≤<br> “01”<br>“30”≤<br> n≤<br> ”31”|“:”|“B”|0x0008|Status|“;”|
|ESC GS x I<br>PDF417<br>Information<br>Request|ASB|0x000C|“16”|Omitted|“:”|“B”|0x0005|Status|“;”|
|ESC GS y I QR<br>Code<br>Information<br>Request|ASB|0x000D|“19”|Omitted|“:”|“B”|0x0006|Status|“;”|
|ESC GS ETS n1 n2<br>Print End Counter<br>Request|ASB|0x000F|“20”|Omitted|“:”|“B”|0x0008|Status|“;”|



(*1) Automatic status is distributed to all hosts connected to the TCP#9,100 port. 

*  Installed MSW region is different depending on the model. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-15 

## **5.3. Appendix 3: Blank Code Page Configuration** 

Blank code pages are character code tables that are empty from character code 80H to FFH.  They can be specified using the command below. 

## • ESC GS t  n (n=255) 

Also, it is possible to write data to the blank code page area using the command below. • ESC GS = ... ... 

## 1. Example configuration of Font A data.  (12 x 24 font) 

||MSB<br>LSB|MSB<br>LSB||MSB|MSB||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||LSB||
|d1|~~a~~||d2|||||0|0|0||0|
|d3|**•**<br>**•**<br>**•**<br>**•**<br>~~i~~||d4|||||0|0|0||0|
|d5|**•**<br>**•**<br>**•**<br>**•**<br>**•**<br>**•**<br>~~a~~||d6|•|•|||0|0|0||0|
|d7|**•**<br>**•**<br>~~i~~||d8|•|•|||0|0|0||0|
|d9|**•**<br>**•**<br>~~i~~||d10||•|•||0|0|0||0|
|d11|**•**<br>**•**<br>~~i~~||d12||•|•||0|0|0||0|
|d13|**•**<br>**•**<br>~~i~~||d14||•|•||0|0|0||0|
|d15|~~i~~||d16||•|•||0|0|0||0|
|d17|~~i~~||d18|•|•|||0|0|0||0|
|d19|~~a~~||d20|•|•|||0|0|0||0|
|d21|**•**<br>~~a~~||d22|•||||0|0|0||0|
|d23|**•**<br>**•**<br>~~a~~||d24|||||0|0|0||0|
|d25|**•**<br>**•**<br>~~a~~||d26|||||0|0|0||0|
|d27|**•**<br>**•**<br>~~i~~||d28|||||0|0|0||0|
|d29|**•**<br>**•**<br>**•**<br>~~a~~||d30|||||0|0|0||0|
|d31|**•**<br>**•**<br>**•**<br>~~i~~||d32|||||0|0|0||0|
|d33|**•**<br>**•**<br>~~i~~||d34|||||0|0|0||0|
|d35|**•**<br>**•**<br>~~i~~||d36|||||0|0|0||0|
|d37|**•**<br>**•**<br>**•**<br>~~i~~||d38|||||0|0|0||0|
|d39|**•**<br>**•**<br>**•**<br>**•**<br>**•**<br>**•**<br>**•**<br>~~i~~||d40|•|•|•||0|0|0||0|
|d41|**•**<br>**•**<br>**•**<br>**•**<br>**•**<br>**•**<br>**•**<br>~~i~~||d42|•|•|•||0|0|0||0|
|d43|~~a~~||d44|||||0|0|0||0|
|d45|~~a~~||d46|||||0|0|0||0|
|d47|~~a~~||d48|||||0|0|0||0|



Fig. A-1 12 x 24 Font 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-16 

## 2. Example configuration of Font B data.  (9 x 24 font) 

The STAR mode is not loaded with Font B.  However, when registering data, Font A and Font B must be registered as a set.  When doing so, Font B data can be zero data. 

||MSB|MSB|||||LSB|LSB|LSB||MSB|MSB||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||LSB||
|d1|~~a~~|||||||||d2||0|0|0|0|0|0||0|
|d3|~~a~~|||**•**|**•**|**•**||||d4||0|0|0|0|0|0||0|
|d5|~~a~~||**•**|**•**|**•**|**•**|**•**|**•**||d6||0|0|0|0|0|0||0|
|d7|~~a~~||**•**|**•**||**•**|**•**|**•**|**•**|d8||0|0|0|0|0|0||0|
|d9|**•**<br>~~i~~||**•**||||**•**|**•**|**•**|d10||0|0|0|0|0|0||0|
|d11|**•**<br>~~i~~||**•**||||**•**|**•**|**•**|d12||0|0|0|0|0|0||0|
|d13|**•**<br>~~a~~||**•**||||**•**|**•**|**•**|d14||0|0|0|0|0|0||0|
|d15|~~i~~||||||**•**|**•**|**•**|d16||0|0|0|0|0|0||0|
|d17|~~i~~||||||**•**|**•**|**•**|d18||0|0|0|0|0|0||0|
|d19|~~i~~||||||**•**|**•**|**•**|d20||0|0|0|0|0|0||0|
|d21|~~i~~|||||**•**|**•**|**•**|**•**|d22||0|0|0|0|0|0||0|
|d23|~~i~~||||**•**|**•**|**•**|**•**|**•**|d24||0|0|0|0|0|0||0|
|d25|~~i~~||||**•**|**•**|**•**|**•**||d26||0|0|0|0|0|0||0|
|d27|~~a~~|||**•**|**•**|**•**||||d28||0|0|0|0|0|0||0|
|d29|~~a~~||**•**|**•**|**•**|||||d30||0|0|0|0|0|0||0|
|d31|~~a~~||**•**|**•**||||||d32||0|0|0|0|0|0||0|
|d33|~~A~~||**•**|**•**||||||d34||0|0|0|0|0|0||0|
|d35|**•**<br>~~i~~||**•**|**•**||||||d36||0|0|0|0|0|0||0|
|d37|**•**<br>~~a~~||**•**|**•**||||||d38||0|0|0|0|0|0||0|
|d39|**•**<br>~~i~~||**•**|**•**|**•**|**•**|**•**|**•**|**•**|d40||0|0|0|0|0|0||0|
|d41|**•**<br>~~i~~||**•**|**•**|**•**|**•**|**•**|**•**|**•**|d42||0|0|0|0|0|0||0|
|d43|~~i~~|||||||||d44||0|0|0|0|0|0||0|
|d45|~~i~~|||||||||d46||0|0|0|0|0|0||0|
|d47|~~i~~|||||||||d48||0|0|0|0|0|0||0|



Fig. A-2 9 x 24 Font 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-17 

## • TSP700II 

|Counter Type|Maintenance<br>Counter|Estimated Life|Count Up<br>Predetermined<br>Times|Counter<br>Maximum Value|EEPROM Writing Timing|
|---|---|---|---|---|---|
|Permanent<br>Counter|Head<br>Energizing<br>Count|800<br>Million<br>dot lines|For<br>each<br>4,000<br>dot<br>lines<br>(500<br>mm)|0xF4240<br>(1<br>Million)|• When cutting paper<br>• Every 10 minutes (when idling) from<br>when power is turned on. However, one<br>condition<br>is<br>that<br>the<br>count<br>up<br>predetermined count is exceeded.|
||LF<br>Motor<br>Traveling<br>Distance|100 km; 800<br>Million<br>dot<br>lines|For<br>each<br>4,000<br>dot<br>lines<br>(500<br>mm)|0xF4240<br>(1<br>Million)|• When cutting paper<br>• Every 10 minutes (when idling) from<br>when power is turned on. However, one<br>condition<br>is<br>that<br>the<br>count<br>up<br>predetermined count is exceeded.|
||Cutter Drive<br>Count|200,000 cuts|Every 10 cuts|0xF4240<br>(1<br>Million)|• When cutting paper<br>• Every 10 minutes (when idling) from<br>when power is turned on. However, one<br>condition<br>is<br>that<br>the<br>count<br>up<br>predetermined count is exceeded.|
|User Counter|Head<br>Energizing<br>Count|800<br>Million<br>dot lines|For<br>each<br>4,000<br>dot<br>lines<br>(500<br>mm)|0xF4240<br>(1<br>Million)|• When cutting paper<br>• Every 10 minutes (when idling) from<br>when power is turned on. However, one<br>condition<br>is<br>that<br>the<br>count<br>up<br>predetermined count is exceeded.|
||LF<br>Motor<br>Traveling<br>Distance|100 km; 800<br>Million<br>dot<br>lines|For<br>each<br>4,000<br>dot<br>lines<br>(500<br>mm)|0xF4240<br>(1<br>Million)|• When cutting paper<br>• Every 10 minutes (when idling) from<br>when power is turned on. However, one<br>condition<br>is<br>that<br>the<br>count<br>up<br>predetermined count is exceeded.|
||Cutter Drive<br>Count|200,000 cuts|Every 10 cuts|0xF4240<br>(1<br>Million)|• When cutting paper<br>• Every 10 minutes (when idling) from<br>when power is turned on. However, one<br>condition<br>is<br>that<br>the<br>count<br>up<br>predetermined count is exceeded.|



- The head energizing count is sometimes counted even when there is not energizing data. (Such as when blank space data is included in the font data.) 

- The estimated life prescribes the number of count of the maintenance counter. It does not match the life specifications. 

- When the permanent counter exceeds the counter maximum value, thereafter the permanent counter and user counter both count up and then stop. 

- It is possible to clear the user counter, but it is not possible to clear the permanent counter. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-18 

## **5.4. Appendix 7 Maximum Number of Input Characters for Each Version of QR Code** 

|Version|Cell Count on<br>One Side|Mistake<br>Correction<br>Level|Number of<br>Characters|English<br>Characters|Binary|Kanji|
|---|---|---|---|---|---|---|
|1|21|L<br>~~es~~<br>~~es~~|40|24|17|10|
|||M<br>~~es~~<br>~~es~~|33|20|14|8|
|||Q<br>~~es~~<br>~~GG~~|25<br>~~GG~~|15<br>~~GG~~|11<br>~~GG~~|6<br>~~GG~~|
|||H<br>~~GG~~<br>~~pT~~|16<br>~~GG~~<br>~~pT~~|10<br>~~GG~~<br>~~pT~~|7<br>~~GG~~<br>~~pT~~|4<br>~~GG~~<br>~~pT~~|
|2|25|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|81<br>~~pT~~<br>~~Ge~~|49<br>~~pT~~<br>~~Ge~~|34<br>~~pT~~<br>~~Ge~~|20<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|66|40|28|17|
|||Q<br>~~es~~<br>~~GG~~|52<br>~~GG~~|31<br>~~GG~~|22<br>~~GG~~|13<br>~~GG~~|
|||H<br>~~pT~~|33<br>~~pT~~|20<br>~~pT~~|14<br>~~pT~~|8<br>~~pT~~|
|3|29|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|131<br>~~pT~~<br>~~Ge~~|79<br>~~pT~~<br>~~Ge~~|55<br>~~pT~~<br>~~Ge~~|33<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|100|60|42|25|
|||Q<br>~~es~~<br>~~GG~~|81<br>~~GG~~|49<br>~~GG~~|34<br>~~GG~~|20<br>~~GG~~|
|||H<br>~~pT~~|52<br>~~pT~~|31<br>~~pT~~|22<br>~~pT~~|13<br>~~pT~~|
|4|33|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|186<br>~~pT~~<br>~~Ge~~|113<br>~~pT~~<br>~~Ge~~|78<br>~~pT~~<br>~~Ge~~|48<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|138|84|58|35|
|||Q<br>~~es~~<br>~~GG~~|114<br>~~GG~~|69<br>~~GG~~|48<br>~~GG~~|29<br>~~GG~~|
|||H<br>~~pT~~|76<br>~~pT~~|46<br>~~pT~~|32<br>~~pT~~|19<br>~~pT~~|
|5|37|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|253<br>~~pT~~<br>~~Ge~~|154<br>~~pT~~<br>~~Ge~~|106<br>~~pT~~<br>~~Ge~~|65<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|191|116|80|49|
|||Q<br>~~es~~<br>~~GG~~|157<br>~~GG~~|95<br>~~GG~~|66<br>~~GG~~|40<br>~~GG~~|
|||H<br>~~pT~~|105<br>~~pT~~|63<br>~~pT~~|44<br>~~pT~~|27<br>~~pT~~|
|6|41|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|321<br>~~pT~~<br>~~Ge~~|194<br>~~pT~~<br>~~Ge~~|134<br>~~pT~~<br>~~Ge~~|82<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|249|151|104|64|
|||Q<br>~~es~~<br>~~GG~~|201<br>~~GG~~|122<br>~~GG~~|84<br>~~GG~~|51<br>~~GG~~|
|||H<br>~~pT~~|133<br>~~pT~~|81<br>~~pT~~|56<br>~~pT~~|34<br>~~pT~~|
|7|45|L<br>~~Ge~~<br>~~es~~|402<br>~~Ge~~|244<br>~~Ge~~|168<br>~~Ge~~|103<br>~~Ge~~|
|||M<br>~~es~~|311|188|130|80|
|||Q<br>~~es~~<br>~~GG~~|253<br>~~GG~~|154<br>~~GG~~|106<br>~~GG~~|65<br>~~GG~~|
|||H<br>~~pT~~|167<br>~~pT~~|101<br>~~pT~~|70<br>~~pT~~|43<br>~~pT~~|
|8|49|L<br>~~Ge~~<br>~~es~~|493<br>~~Ge~~|299<br>~~Ge~~|206<br>~~Ge~~|126<br>~~Ge~~|
|||M<br>~~es~~|378|229|158|97|
|||Q<br>~~es~~<br>~~GG~~|301<br>~~GG~~|183<br>~~GG~~|126<br>~~GG~~|77<br>~~GG~~|
|||H<br>~~pT~~|203<br>~~pT~~|123<br>~~pT~~|85<br>~~pT~~|52<br>~~pT~~|
|9|53|L<br>~~Ge~~<br>~~es~~|585<br>~~Ge~~|354<br>~~Ge~~|244<br>~~Ge~~|150<br>~~Ge~~|
|||M<br>~~es~~|441|267|184|113|
|||Q<br>~~es~~<br>~~GG~~|369<br>~~GG~~|223<br>~~GG~~|154<br>~~GG~~|94<br>~~GG~~|
|||H<br>~~pT~~|239<br>~~pT~~|145<br>~~pT~~|100<br>~~pT~~|61<br>~~pT~~|
|10|57|L<br>~~Ge~~<br>~~es~~|690<br>~~Ge~~|418<br>~~Ge~~|287<br>~~Ge~~|177<br>~~Ge~~|
|||M<br>~~es~~|526|319|219|135|
|||Q<br>~~es~~<br>~~GG~~|433<br>~~GG~~|262<br>~~GG~~|180<br>~~GG~~|111<br>~~GG~~|
|||H<br>~~pT~~|291<br>~~pT~~|176<br>~~pT~~|121<br>~~pT~~|74<br>~~pT~~|
|11|61|L<br>~~Ge~~<br>~~es~~|800<br>~~Ge~~|485<br>~~Ge~~|333<br>~~Ge~~|205<br>~~Ge~~|
|||M<br>~~es~~|608|368|253|156|
|||Q<br>~~es~~<br>~~GG~~|493<br>~~GG~~|299<br>~~GG~~|205<br>~~GG~~|126<br>~~GG~~|
|||H<br>~~pT~~|342<br>~~pT~~|207<br>~~pT~~|142<br>~~pT~~|87<br>~~pT~~|
|12|65|L<br>~~Ge~~<br>~~es~~|915<br>~~Ge~~|555<br>~~Ge~~|381<br>~~Ge~~|234<br>~~Ge~~|
|||M<br>~~es~~|694|421|289|178|
|||Q<br>~~es~~<br>~~GG~~|579<br>~~GG~~|351<br>~~GG~~|241<br>~~GG~~|148<br>~~GG~~|
|||H<br>~~pT~~|390<br>~~pT~~|236<br>~~pT~~|162<br>~~pT~~|100<br>~~pT~~|
|13|69|L<br>~~Ge~~<br>~~es~~|1030<br>~~Ge~~|624<br>~~Ge~~|429<br>~~Ge~~|264<br>~~Ge~~|
|||M<br>~~es~~|790|479|329|202|
|||Q<br>~~es~~<br>~~GG~~|656<br>~~GG~~|398<br>~~GG~~|273<br>~~GG~~|168<br>~~GG~~|
|||H<br>~~pT~~|454<br>~~pT~~|275<br>~~pT~~|189<br>~~pT~~|116<br>~~pT~~|
|14|73|L<br>~~Ge~~<br>~~es~~|1167<br>~~Ge~~|707<br>~~Ge~~|486<br>~~Ge~~|299<br>~~Ge~~|
|||M<br>~~es~~|877|531|365|225|
|||Q<br>~~es~~<br>~~GG~~|738<br>~~GG~~|447<br>~~GG~~|307<br>~~GG~~|189<br>~~GG~~|
|||H<br>~~pT~~|498<br>~~pT~~|302<br>~~pT~~|207<br>~~pT~~|127<br>~~pT~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-19 

2) Model 2 Version and Maximum Number of Input Characters 

|Version|Cell Count on<br>One Side|Mistake<br>Correction<br>Level|Number of<br>Characters|English<br>Characters|Binary|Kanji|
|---|---|---|---|---|---|---|
|1|21|L<br>~~es~~<br>~~es~~|41|25|17|10|
|||M<br>~~es~~<br>~~es~~|34|20|14|8|
|||Q<br>~~es~~<br>~~GG~~|27<br>~~GG~~|16<br>~~GG~~|11<br>~~GG~~|7<br>~~GG~~|
|||H<br>~~GG~~<br>~~pT~~|17<br>~~GG~~<br>~~pT~~|10<br>~~GG~~<br>~~pT~~|7<br>~~GG~~<br>~~pT~~|4<br>~~GG~~<br>~~pT~~|
|2|25|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|77<br>~~pT~~<br>~~Ge~~|47<br>~~pT~~<br>~~Ge~~|32<br>~~pT~~<br>~~Ge~~|20<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|63|38|26|16|
|||Q<br>~~es~~<br>~~GG~~|48<br>~~GG~~|29<br>~~GG~~|20<br>~~GG~~|12<br>~~GG~~|
|||H<br>~~pT~~|34<br>~~pT~~|20<br>~~pT~~|14<br>~~pT~~|8<br>~~pT~~|
|3|29|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|127<br>~~pT~~<br>~~Ge~~|77<br>~~pT~~<br>~~Ge~~|53<br>~~pT~~<br>~~Ge~~|32<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|101|61|42|26|
|||Q<br>~~es~~<br>~~GG~~|77<br>~~GG~~|47<br>~~GG~~|32<br>~~GG~~|20<br>~~GG~~|
|||H<br>~~pT~~|58<br>~~pT~~|35<br>~~pT~~|24<br>~~pT~~|15<br>~~pT~~|
|4|33|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|187<br>~~pT~~<br>~~Ge~~|114<br>~~pT~~<br>~~Ge~~|78<br>~~pT~~<br>~~Ge~~|48<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|149|90|62|38|
|||Q<br>~~es~~<br>~~GG~~|111<br>~~GG~~|67<br>~~GG~~|46<br>~~GG~~|28<br>~~GG~~|
|||H<br>~~pT~~|82<br>~~pT~~|50<br>~~pT~~|34<br>~~pT~~|21<br>~~pT~~|
|5|37|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|255<br>~~pT~~<br>~~Ge~~|154<br>~~pT~~<br>~~Ge~~|106<br>~~pT~~<br>~~Ge~~|65<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|202|122|84|52|
|||Q<br>~~es~~<br>~~GG~~|144<br>~~GG~~|87<br>~~GG~~|60<br>~~GG~~|37<br>~~GG~~|
|||H<br>~~pT~~|106<br>~~pT~~|64<br>~~pT~~|44<br>~~pT~~|27<br>~~pT~~|
|6|41|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|322<br>~~pT~~<br>~~Ge~~|195<br>~~pT~~<br>~~Ge~~|134<br>~~pT~~<br>~~Ge~~|82<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|255|154|106|65|
|||Q<br>~~es~~<br>~~GG~~|178<br>~~GG~~|108<br>~~GG~~|74<br>~~GG~~|45<br>~~GG~~|
|||H<br>~~GG~~|139<br>~~GG~~|84<br>~~GG~~|58<br>~~GG~~|36<br>~~GG~~|
|7|45|L<br>~~Ge~~<br>~~es~~|370<br>~~Ge~~|224<br>~~Ge~~|154<br>~~Ge~~|95<br>~~Ge~~|
|||M<br>~~es~~|293|178|122|75|
|||Q<br>~~es~~<br>~~GG~~|207<br>~~GG~~|125<br>~~GG~~|86<br>~~GG~~|53<br>~~GG~~|
|||H<br>~~pT~~|154<br>~~pT~~|93<br>~~pT~~|64<br>~~pT~~|39<br>~~pT~~|
|8|49|L<br>~~Ge~~<br>~~es~~|461<br>~~Ge~~|279<br>~~Ge~~|192<br>~~Ge~~|118<br>~~Ge~~|
|||M<br>~~es~~|365|221|152|93|
|||Q<br>~~es~~<br>~~GG~~|259<br>~~GG~~|157<br>~~GG~~|108<br>~~GG~~|66<br>~~GG~~|
|||H<br>~~pT~~|202<br>~~pT~~|122<br>~~pT~~|84<br>~~pT~~|52<br>~~pT~~|
|9|53|L<br>~~Ge~~<br>~~es~~|552<br>~~Ge~~|335<br>~~Ge~~|230<br>~~Ge~~|141<br>~~Ge~~|
|||M<br>~~es~~|432|262|180|111|
|||Q<br>~~es~~<br>~~GG~~|312<br>~~GG~~|189<br>~~GG~~|130<br>~~GG~~|80<br>~~GG~~|
|||H<br>~~pT~~|235<br>~~pT~~|143<br>~~pT~~|98<br>~~pT~~|60<br>~~pT~~|
|10|57|L<br>~~Ge~~<br>~~es~~|652<br>~~Ge~~|395<br>~~Ge~~|271<br>~~Ge~~|167<br>~~Ge~~|
|||M<br>~~es~~|513|311|213|131|
|||Q<br>~~es~~<br>~~GG~~|364<br>~~GG~~|221<br>~~GG~~|151<br>~~GG~~|93<br>~~GG~~|
|||H<br>~~pT~~|288<br>~~pT~~|174<br>~~pT~~|119<br>~~pT~~|74<br>~~pT~~|
|11|61|L<br>~~Ge~~<br>~~es~~|772<br>~~Ge~~|468<br>~~Ge~~|321<br>~~Ge~~|198<br>~~Ge~~|
|||M<br>~~es~~|604|366|251|155|
|||Q<br>~~es~~<br>~~GG~~|427<br>~~GG~~|259<br>~~GG~~|177<br>~~GG~~|109<br>~~GG~~|
|||H<br>~~pT~~|331<br>~~pT~~|200<br>~~pT~~|137<br>~~pT~~|85<br>~~pT~~|
|12|65|L<br>~~Ge~~<br>~~es~~|883<br>~~Ge~~|535<br>~~Ge~~|367<br>~~Ge~~|226<br>~~Ge~~|
|||M<br>~~es~~|691|419|287|177|
|||Q<br>~~es~~<br>~~GG~~|489<br>~~GG~~|296<br>~~GG~~|203<br>~~GG~~|125<br>~~GG~~|
|||H<br>~~pT~~|374<br>~~pT~~|227<br>~~pT~~|155<br>~~pT~~|96<br>~~pT~~|
|13|69|L<br>~~Ge~~<br>~~es~~|1022<br>~~Ge~~|619<br>~~Ge~~|425<br>~~Ge~~|262<br>~~Ge~~|
|||M<br>~~es~~|796|483|331|204|
|||Q<br>~~es~~<br>~~GG~~|580<br>~~GG~~|352<br>~~GG~~|241<br>~~GG~~|149<br>~~GG~~|
|||H<br>~~pT~~|427<br>~~pT~~|259<br>~~pT~~|177<br>~~pT~~|109<br>~~pT~~|
|14|73|L<br>~~Ge~~<br>~~es~~|1101<br>~~Ge~~|667<br>~~Ge~~|458<br>~~Ge~~|282<br>~~Ge~~|
|||M<br>~~es~~|871|528|362|223|
|||Q<br>~~es~~<br>~~GG~~|621<br>~~GG~~|376<br>~~GG~~|258<br>~~GG~~|159<br>~~GG~~|
|||H<br>~~pT~~|468<br>~~pT~~|283<br>~~pT~~|194<br>~~pT~~|120<br>~~pT~~|
|15|77|L<br>~~Ge~~<br>~~es~~|1250<br>~~Ge~~|758<br>~~Ge~~|520<br>~~Ge~~|320<br>~~Ge~~|
|||M<br>~~es~~|991|600|412|254|
|||Q<br>~~es~~<br>~~GG~~|703<br>~~GG~~|426<br>~~GG~~|292<br>~~GG~~|180<br>~~GG~~|
|||H<br>~~pT~~|530<br>~~pT~~|321<br>~~pT~~|220<br>~~pT~~|136<br>~~pT~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-20 

|Version|Cell Count on<br>One Side|Mistake<br>Correction<br>Level|Number of<br>Characters|English<br>Characters|Binary|Kanji|
|---|---|---|---|---|---|---|
|16|81|L<br>~~es~~<br>~~es~~|1408|854|586|361|
|||M<br>~~es~~<br>~~es~~|1082|656|450|277|
|||Q<br>~~es~~<br>~~GG~~|775<br>~~GG~~|470<br>~~GG~~|322<br>~~GG~~|198<br>~~GG~~|
|||H<br>~~GG~~<br>~~pT~~|602<br>~~GG~~<br>~~pT~~|365<br>~~GG~~<br>~~pT~~|250<br>~~GG~~<br>~~pT~~|154<br>~~GG~~<br>~~pT~~|
|17|85|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|1548<br>~~pT~~<br>~~Ge~~|938<br>~~pT~~<br>~~Ge~~|644<br>~~pT~~<br>~~Ge~~|397<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|1212|734|504|310|
|||Q<br>~~es~~<br>~~GG~~|876<br>~~GG~~|531<br>~~GG~~|364<br>~~GG~~|224<br>~~GG~~|
|||H<br>~~GG~~<br>~~pT~~|674<br>~~GG~~<br>~~pT~~|408<br>~~GG~~<br>~~pT~~|280<br>~~GG~~<br>~~pT~~|173<br>~~GG~~<br>~~pT~~|
|18|89|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|1725<br>~~pT~~<br>~~Ge~~|1046<br>~~pT~~<br>~~Ge~~|718<br>~~pT~~<br>~~Ge~~|442<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|1346|816|560|345|
|||Q<br>~~es~~<br>~~GG~~|948<br>~~GG~~|574<br>~~GG~~|394<br>~~GG~~|243<br>~~GG~~|
|||H<br>~~pT~~|746<br>~~pT~~|452<br>~~pT~~|310<br>~~pT~~|191<br>~~pT~~|
|19|93|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|1903<br>~~pT~~<br>~~Ge~~|1153<br>~~pT~~<br>~~Ge~~|792<br>~~pT~~<br>~~Ge~~|488<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|1500|909|624|384|
|||Q<br>~~es~~<br>~~GG~~|1063<br>~~GG~~|644<br>~~GG~~|442<br>~~GG~~|272<br>~~GG~~|
|||H<br>~~pT~~|813<br>~~pT~~|493<br>~~pT~~|338<br>~~pT~~|208<br>~~pT~~|
|20|97|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|2061<br>~~pT~~<br>~~Ge~~|1249<br>~~pT~~<br>~~Ge~~|858<br>~~pT~~<br>~~Ge~~|528<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|1600|970|666|410|
|||Q<br>~~es~~<br>~~GG~~|1159<br>~~GG~~|702<br>~~GG~~|482<br>~~GG~~|297<br>~~GG~~|
|||H<br>~~pT~~|919<br>~~pT~~|557<br>~~pT~~|382<br>~~pT~~|235<br>~~pT~~|
|21|101|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|2232<br>~~pT~~<br>~~Ge~~|1352<br>~~pT~~<br>~~Ge~~|929<br>~~pT~~<br>~~Ge~~|572<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|1708|1035|711|438|
|||Q<br>~~es~~<br>~~GG~~|1224<br>~~GG~~|742<br>~~GG~~|509<br>~~GG~~|314<br>~~GG~~|
|||H<br>~~pT~~|969<br>~~pT~~|587<br>~~pT~~|403<br>~~pT~~|248<br>~~pT~~|
|22|105|L<br>~~Ge~~<br>~~es~~|2409<br>~~Ge~~|1460<br>~~Ge~~|1003<br>~~Ge~~|618<br>~~Ge~~|
|||M<br>~~es~~|1872|1134|779|480|
|||Q<br>~~es~~<br>~~OG~~|1358<br>~~OG~~|823<br>~~OG~~|565<br>~~OG~~|348<br>~~OG~~|
|||H<br>~~pT~~|1056<br>~~pT~~|640<br>~~pT~~|439<br>~~pT~~|270<br>~~pT~~|
|23|109|L<br>~~Ge~~<br>~~es~~|2620<br>~~Ge~~|1588<br>~~Ge~~|1091<br>~~Ge~~|672<br>~~Ge~~|
|||M<br>~~es~~|2059|1248|857|528|
|||Q<br>~~es~~<br>~~OG~~|1468<br>~~OG~~|890<br>~~OG~~|611<br>~~OG~~|376<br>~~OG~~|
|||H<br>~~pT~~|1108<br>~~pT~~|672<br>~~pT~~|461<br>~~pT~~|284<br>~~pT~~|
|24|113|L<br>~~Ge~~<br>~~es~~|2812<br>~~Ge~~|1704<br>~~Ge~~|1171<br>~~Ge~~|721<br>~~Ge~~|
|||M<br>~~es~~|2188|1326|911|561|
|||Q<br>~~es~~<br>~~OG~~|1588<br>~~OG~~|963<br>~~OG~~|661<br>~~OG~~|407<br>~~OG~~|
|||H<br>~~pT~~|1228<br>~~pT~~|744<br>~~pT~~|511<br>~~pT~~|315<br>~~pT~~|
|25|117|L<br>~~Ge~~<br>~~es~~|3057<br>~~Ge~~|1853<br>~~Ge~~|1273<br>~~Ge~~|784<br>~~Ge~~|
|||M<br>~~es~~|2395|1451|997|614|
|||Q<br>~~es~~<br>~~GG~~|1718<br>~~GG~~|1041<br>~~GG~~|715<br>~~GG~~|440<br>~~GG~~|
|||H<br>~~pT~~|1286<br>~~pT~~|779<br>~~pT~~|535<br>~~pT~~|330<br>~~pT~~|
|26|121|L<br>~~Ge~~<br>~~es~~|3283<br>~~Ge~~|1990<br>~~Ge~~|1367<br>~~Ge~~|842<br>~~Ge~~|
|||M<br>~~es~~|2544|1542|1059|652|
|||Q<br>~~es~~<br>~~GG~~|1804<br>~~GG~~|1094<br>~~GG~~|751<br>~~GG~~|462<br>~~GG~~|
|||H<br>~~pT~~|1425<br>~~pT~~|864<br>~~pT~~|593<br>~~pT~~|365<br>~~pT~~|
|27|125|L<br>~~Ge~~<br>~~es~~|3514<br>~~Ge~~|2132<br>~~Ge~~|1465<br>~~Ge~~|902<br>~~Ge~~|
|||M<br>~~es~~|2701|1637|1125|692|
|||Q<br>~~es~~<br>~~GG~~|1933<br>~~GG~~|1172<br>~~GG~~|805<br>~~GG~~|496<br>~~GG~~|
|||H<br>~~pT~~|1501<br>~~pT~~|910<br>~~pT~~|625<br>~~pT~~|385<br>~~pT~~|
|28|129|L<br>~~Ge~~<br>~~es~~|3669<br>~~Ge~~|2223<br>~~Ge~~|1528<br>~~Ge~~|940<br>~~Ge~~|
|||M<br>~~es~~|2857|1732|1190|732|
|||Q<br>~~es~~<br>~~GG~~|2085<br>~~GG~~|1263<br>~~GG~~|868<br>~~GG~~|534<br>~~GG~~|
|||H<br>~~pT~~|1581<br>~~pT~~|958<br>~~pT~~|658<br>~~pT~~|405<br>~~pT~~|
|29|133|L<br>~~Ge~~<br>~~es~~|3909<br>~~Ge~~|2369<br>~~Ge~~|1628<br>~~Ge~~|1002<br>~~Ge~~|
|||M<br>~~es~~|3035|1839|1264|778|
|||Q<br>~~es~~<br>~~GG~~|2181<br>~~GG~~|1322<br>~~GG~~|908<br>~~GG~~|559<br>~~GG~~|
|||H<br>~~pT~~|1677<br>~~pT~~|1016<br>~~pT~~|698<br>~~pT~~|430<br>~~pT~~|
|30|137|L<br>~~Ge~~<br>~~es~~|4158<br>~~Ge~~|2520<br>~~Ge~~|1732<br>~~Ge~~|1066<br>~~Ge~~|
|||M<br>~~es~~|3289|1994|1370|843|
|||Q<br>~~es~~<br>~~GG~~|2358<br>~~GG~~|1429<br>~~GG~~|982<br>~~GG~~|604<br>~~GG~~|
|||H<br>~~pT~~|1782<br>~~pT~~|1080<br>~~pT~~|742<br>~~pT~~|457<br>~~pT~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-21 

|Version|Cell Count on<br>One Side|Mistake<br>Correction<br>Level|Number of<br>Characters|English<br>Characters|Binary|Kanji|
|---|---|---|---|---|---|---|
|31|141|L<br>~~es~~<br>~~es~~|4417|2677|1840|1132|
|||M<br>~~es~~<br>~~es~~|3486|2113|1452|894|
|||Q<br>~~es~~<br>~~GG~~|2473<br>~~GG~~|1499<br>~~GG~~|1030<br>~~GG~~|634<br>~~GG~~|
|||H<br>~~GG~~<br>~~pT~~|1897<br>~~GG~~<br>~~pT~~|1150<br>~~GG~~<br>~~pT~~|790<br>~~GG~~<br>~~pT~~|486<br>~~GG~~<br>~~pT~~|
|32|145|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|4686<br>~~pT~~<br>~~Ge~~|2840<br>~~pT~~<br>~~Ge~~|1952<br>~~pT~~<br>~~Ge~~|1201<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|3693|2238|1538|947|
|||Q<br>~~es~~<br>~~GG~~|2670<br>~~GG~~|1618<br>~~GG~~|1112<br>~~GG~~|684<br>~~GG~~|
|||H<br>~~GG~~<br>~~pT~~|2022<br>~~GG~~<br>~~pT~~|1226<br>~~GG~~<br>~~pT~~|842<br>~~GG~~<br>~~pT~~|518<br>~~GG~~<br>~~pT~~|
|33|149|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|4965<br>~~pT~~<br>~~Ge~~|3009<br>~~pT~~<br>~~Ge~~|2068<br>~~pT~~<br>~~Ge~~|1273<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|3909|2369|1628|1002|
|||Q<br>~~es~~<br>~~GG~~|2805<br>~~GG~~|1700<br>~~GG~~|1168<br>~~GG~~|719<br>~~GG~~|
|||H<br>~~pT~~|2157<br>~~pT~~|1307<br>~~pT~~|898<br>~~pT~~|553<br>~~pT~~|
|34|153|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|5253<br>~~pT~~<br>~~Ge~~|3183<br>~~pT~~<br>~~Ge~~|2188<br>~~pT~~<br>~~Ge~~|1347<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|4134|2506|1722|1060|
|||Q<br>~~es~~<br>~~GG~~|2949<br>~~GG~~|1787<br>~~GG~~|1228<br>~~GG~~|756<br>~~GG~~|
|||H<br>~~pT~~|2301<br>~~pT~~|1394<br>~~pT~~|958<br>~~pT~~|590<br>~~pT~~|
|35|157|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|5529<br>~~pT~~<br>~~Ge~~|3351<br>~~pT~~<br>~~Ge~~|2303<br>~~pT~~<br>~~Ge~~|1417<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|4343|2632|1809|1113|
|||Q<br>~~es~~<br>~~GG~~|3081<br>~~GG~~|1867<br>~~GG~~|1283<br>~~GG~~|790<br>~~GG~~|
|||H<br>~~pT~~|2361<br>~~pT~~|1431<br>~~pT~~|983<br>~~pT~~|605<br>~~pT~~|
|36|161|L<br>~~pT~~<br>~~Ge~~<br>~~es~~|5836<br>~~pT~~<br>~~Ge~~|3537<br>~~pT~~<br>~~Ge~~|2431<br>~~pT~~<br>~~Ge~~|1496<br>~~pT~~<br>~~Ge~~|
|||M<br>~~es~~|4588|2780|1911|1176|
|||Q<br>~~es~~<br>~~GG~~|3244<br>~~GG~~|1966<br>~~GG~~|1351<br>~~GG~~|832<br>~~GG~~|
|||H<br>~~pT~~|2524<br>~~pT~~|1530<br>~~pT~~|1051<br>~~pT~~|647<br>~~pT~~|
|37|165|L<br>~~Ge~~<br>~~es~~|6153<br>~~Ge~~|3729<br>~~Ge~~|2563<br>~~Ge~~|1577<br>~~Ge~~|
|||M<br>~~es~~|4775|2894|1989|1224|
|||Q<br>~~es~~<br>~~OG~~|3417<br>~~OG~~|2071<br>~~OG~~|1423<br>~~OG~~|876<br>~~OG~~|
|||H<br>~~pT~~|2625<br>~~pT~~|1591<br>~~pT~~|1093<br>~~pT~~|673<br>~~pT~~|
|38|169|L<br>~~Ge~~<br>~~es~~|6479<br>~~Ge~~|3927<br>~~Ge~~|2699<br>~~Ge~~|1661<br>~~Ge~~|
|||M<br>~~es~~|5039|3054|2099|1292|
|||Q<br>~~es~~<br>~~OG~~|3599<br>~~OG~~|2181<br>~~OG~~|1499<br>~~OG~~|923<br>~~OG~~|
|||H<br>~~pT~~|2735<br>~~pT~~|1658<br>~~pT~~|1139<br>~~pT~~|701<br>~~pT~~|
|39|173|L<br>~~Ge~~<br>~~es~~|6743<br>~~Ge~~|4087<br>~~Ge~~|2809<br>~~Ge~~|1729<br>~~Ge~~|
|||M<br>~~es~~|5313|3220|2213|1362|
|||Q<br>~~es~~<br>~~OG~~|3791<br>~~OG~~|2298<br>~~OG~~|1579<br>~~OG~~|972<br>~~OG~~|
|||H<br>~~pT~~|2927<br>~~pT~~|1774<br>~~pT~~|1219<br>~~pT~~|750<br>~~pT~~|
|40|177|L<br>~~Ge~~<br>~~es~~|7089<br>~~Ge~~|4296<br>~~Ge~~|2953<br>~~Ge~~|1817<br>~~Ge~~|
|||M<br>~~es~~|5596|3391|2331|1435|
|||Q<br>~~es~~<br>~~GG~~|3993<br>~~GG~~|2420<br>~~GG~~|1663<br>~~GG~~|1024<br>~~GG~~|
|||H<br>~~pT~~|3057<br>~~pT~~|1852<br>~~pT~~|1273<br>~~pT~~|784<br>~~pT~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-22 

## **5.5. Appendix 8 TSP828L Cut Command Specifications** 

<Line Mode> 

|<Line Mode>|<Line Mode>||||
|---|---|---|---|---|
|Command||Normal Thermal Paper|Label Paper||
||||Tear Bar|Peel Mode|
|<FF>||Form Feed|Label Gap Detection|Label Gap Detection<br>+<br>Peeling Position<br>Conveyance|
|<ESC> d n|n = 0, 48<br>n = 1, 49<br>n = 2, 50<br>n = 3, 51<br>n = 116<br>(“t”)|Tear<br>Bar<br>Position<br>Conveyance<br>Tear<br>Bar<br>Position<br>Conveyance|Label Gap Detection<br>+<br>Tear Bar Position<br>Conveyance<br>Label Gap Detection<br>+<br>Tear Bar Position<br>Conveyance|Label Gap Detection<br>+<br>Peeling Position<br>Conveyance<br>Label Gap Detection<br>+<br>Peeling Position<br>Conveyance|



<Raster Mode FF/EOT> 

|<Raster Mode FF/EOT>|<Raster Mode FF/EOT>||||
|---|---|---|---|---|
|Command||Normal Thermal Paper|Label Paper||
||||Tear Bar|Peel Mode|
|Form Feed|Valid<br>Invalid|Print<br>Print|Print<br>+<br>Label Gap Detection<br>Print<br>+<br>LabelGapDetection|Print<br>+<br>Label Gap Detection<br>Print<br>+<br>LabelGapDetection|
|Cut Feed|Valid<br>Invalid|Tear Bar Position<br>Conveyance<br>---|Tear Bar Position<br>Conveyance<br>---|Peeling Position<br>Conveyance<br>Peeling Position<br>Conveyance|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-23 

## **5.6. Appendix 6 Explanation of Page Mode** 

## **5-6-1. O verview** 

This printer is equipped with two print modes. They are standard and page mode. 

In standard mode, the printer prints and feeds paper each time it receives the print and paper feed instructions, but the print and paper feed instructions received in page mode are executed on the print region on the specified memory and the printer does not operate. Then, when the ESC GS P6 or ESC GS P7 commands are executed, the printer batch expands data to the printing region and prints. In other words, when printing and performing a line feed for data of “ABCDEF” <LF>, in standard mode, “ABCDEF” is printed and paper is fed one line. In page mode, however, “ABCDEF” is written to the print region specified on the memory, and one line is moved on the memory to write the next print data. This printer will enter page mode using ESC GS P 0. Commands received thereafter are all processed as page mode. By running ESC GS P 6, you can lump-print received data. Also, by running ESC GS P 7, you can return to standard mode after lump printing received data. You can return to standard mode without printing page mode print data using ESC GS P 1. However, print data will be cleared. 

<Transitioning to Standard Mode and Page Mode> 

## **5-6-2. Setting Values Using Each Command in Standard Mode and Page Mode** 

- The values set by each command are shared by both standard and page modes. However, only the settings of the following commands are independently set. 

- → ESC 0, ESC M, ESC P, ESC :, ESC g, ESC SP, ESC 0, ESC z, ESC 1, ESC D, ESC P, ESC s, ESC t,  ESC p 

## • The following commands are invalid in page mode. 

→ ESC GS c, ESC GS ) B, ESC RS m, ESC RS A, ESC GS M, ESC GS r, ESC GS %, ESC GS * 0, ESC RS C, ESC *, ESC RS r 

ESC RS L, ESC FS p, VT, FF, 

- The maximum number of dots is prescribed in standard mode, but the y directions (the x direction when there is no rotation) when printing is rotated 90 or 270º are larger than that. For details, see the setting (ESC GS P 3) command of the print region in page mode. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-24 

## **5-6-3. Print Data Expansion to the Print Region** 

Expanding print data to the print region is performed in the following way. 

- (1) The print region is set by ESC GS P 3, but when all printing and paper feeds are ended before the printer receives ESC GS P 3 the left edge when facing the printer becomes the origin of the print region (x0, y0). The print region is a square shape using dx pitch for the x direction (horizontal direction) and dy pitch for the y direction (perpendicular direction) as sides, including the origin point from the origin points (x0, y0). (When ESC GS P 3 is not set, the initial value is the print region.) 

- (2) When the print region is set by ESC GS P 3, and the printer receives print data after the print direction is set by ESC GS P 2, point A in Fig. 2.3.1 becomes the starting point initial value, and the print data is expanded in the print region. For characters, this starting point is the base line. Downloaded bit images and bar codes are expanded using the lower left-hand point of the image data as the baseline (Point B in Fig. 5.9.3.1). However, HRI characters with a bottom bar code are printed below the base line. When expanding characters (double-tall characters) higher than the standard character height and download bit images and the like at the starting point, the portion higher than the standard characters is not printed. 

- (3) If the print data is out of the print region (including character right spaces) before receiving commands that accompany line feeds (LF, ESC J and the like), the line feed is automatically performed in the print region, and the expansion position of the print data is moved one line so the next expansion position is at the top of the line. The line feed amount at that time uses the line feed amount set by ESC 0 and ESC 1. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-25 

Fig. 5.6.3.1 Expansion Position of Character Data 

**==> picture [404 x 202] intentionally omitted <==**

**----- Start of picture text -----**<br>
Expansion Direction<br>(x0, y0)<br>20 dot<br>Baseline<br>Ａ<br>4 dot<br>Point Ａ<br>Print Region<br>(dx, dy)<br>**----- End of picture text -----**<br>


Fig. 5.6.3.2 Expansion Position of Print Data 

**==> picture [323 x 253] intentionally omitted <==**

**----- Start of picture text -----**<br>
Bar Code<br>Height h dots<br>Bar code<br>40 dots  (GS k m)<br>Vertical<br>20 dots  double   24 dots<br>size<br>Expanded   Bit image<br>character   Baseline<br>Ａ<br>4 dots  8 dots<br>Ａ<br>HRI Character<br>Point B               Point B  Point B  24 Dots<br>**----- End of picture text -----**<br>


――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

5-26 

## **5.7. 5-7) Appendix 7 Explanation of Print Startup Control Starting Printing When Set to Page Units** 

When print startup control is set to page units, printing starts when the image buffer length is full or the following commands are run. 

If the following commands are not received, start printing after a 1-second timeout. 

For details on image buffer length and how to set print startup control, see the product specifications manual. 

Print starting trigger • Cutter command : <ESC> d n • FF command : <FF> • BM detection command : <ESC> d n, <FF> • Print startup command : <ESC><GS> g 0 m n • Raster mode : <ESC> <FF> <NUL> : <ESC> <FF> <EOT> 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 5-27 

## **6. SPECIAL APPENDIX COMMAND LIST FOR EACH MODEL IN EACH I/F** 

## **6.1. RS-232 C I/F** 

**==> picture [499 x 612] intentionally omitted <==**

**----- Start of picture text -----**<br>
• Standard Commands<br>Class Commands PT Model Name<br>TSP800  TSP700 TSP600 TUP900 TSP1000 TSP828L TSP700II  TSP650  TUP500  TSP800II FVP10<br>errr Font Style ESC RS F  NO  NO  NO  NO  OK  OK  OK  OK  OK  OK  re OK<br>and  ESC GS t   OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>Character Set<br>RR ESC GS = Ver. 3.0 or later  se Spec. A  Sp ee ec. A  Spec. A  Spec. A  OG Spec. A  Spec. B  Spec. B  Spec. B  Spec. B  Spec. B<br>PoRe ESC R   GD OK  OK  OK  OK  OK  OK  GU OK  OD OK  (OO OK  OK  OK<br>GO ESC /   OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>ESC SP  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>Po (OS<br>PoPoRe ESC M ESC P ESC :  GD OK OK OK  OK OK OK  OK OK OK  OK OK OK  OK OK OK  OK OK OK  GU OK OK OK  OD OK OK OK  (OO OK OK OK  OK OK OK  OK OK OK<br>ESC  p  (Not  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>recommended)<br>Character  P ESC iESC g  o SpOK ec. A  SpOK ec. A  SpOK ec. A  SpOK ec. B  SpOK ec. B o SpOK ec. B SpOK ec. A  SpOK ec. A  SpOK ec. B  SpOK ec. A  SpOK ec. A<br>expansion  Po ESC W   OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>settings  GG ESC h   OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>SO  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>Po OO OS<br>PoGO DC4 ESC SO  OK OK  OK OK  OK OK  OK OK  OK OK  OK OK  OK OK  OK OK  (OS OK OK  OK OK  OK OK<br>ESC DC4  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>Print Mode ESC E  Spec. A  Spec. A  Spec. A  Spec. B  Spec. B  Spec. B  Spec. A  Spec. A  Spec. A  Spec. B  Spec. B<br>Before Ver.  Before Ver.  Before Ver.<br>2.0  2.0  2.0<br>Spec. B  Spec. B  Spec. B<br>Ver. 2.0 or  Ver. 2.0 or  Ver. 2.0 or<br>later  later  later<br>ESC F  Spec. A  Spec. A  Spec. A  Spec. B  Spec. B  Spec. B  Spec. A  Spec. A  Spec. A  Spec. B  Spec. B<br>Before V. 2.0  Before V. 2.0  Before V. 2.0<br>Spec. B  Spec. B  Spec. B<br>V. 2.0 or later  V. 2.0 or later  V. 2.0 or later<br>Po ESC - OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>Re ESC _   ESC 4  GO OK OK  OK OK  OK OK  OK OK  OK OK  OK OK  OK OK  OK OK  OK OK  OK OK  OK OK<br>Po GD<br>P ESC 5 SI  o OK OK  OK OK  OK OK  OK OK  OK OK  o OK OK  OK OK  OK OK  OK OK  OK OK  OK OK<br>Po DC2  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>Line spacing Po LF  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>Po CR  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>GO ESC a   OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>ESC z   OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>Po (OS<br>PoRe ESC J  ESC 0  GD OK OK  OK OK  OK OK  OK OK  OK OK  OK OK  GU OK OK  OD OK OK  (OO OK OK  OK OK  OK OK<br>Po ESC I   OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>Page Control Rs FF  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>Po ESC C   OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>GOPo ESC C 0  VT  OK OK  OK OK  OK OK  OK OK  OK OK  OK OK  OK OK  OK OK  (OS OK OK  OK OK  OK OK<br>Po ESC B   OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>Horizontal  Po ESC l   Spec. A  Spec. A  Spec. A  Spec. B  Spec. B Spec. B Spec. A  Spec. A  Spec. B  Spec. A  Spec. A<br>direction  Po ESC Q   Spec. A  Spec. A  Spec. A  Spec. B  Spec. B Spec. B Spec. A  Spec. A  Spec. B  Spec. A  Spec. A<br>position  GO HT  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>ESC D   OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>Po (OS<br>PoRe ESC GS A  ESC GS R   GD OK OK  OK OK  OK OK  OK OK  OK OK  OK OK  GU OK OK  OD OK OK  (OO OK OK  OK OK  OK OK<br>Po ESC GS a   OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>Download ESC &   OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>eePo ESC %   OK  es OK  OK  OK  OK  OK  eee OK  OK  OK  OK  OK<br>Bit Image P ESC K   o OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>Graphics ESC L   OK  OK  OK  OK  OK  o OK  OK  OK  OK  OK  OK<br>Po ESC k   OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>Po ESC X   OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>Logo Po ESC FS q   OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>GO ESC FS p   OK  OK  OK  OK  OK  OK  OK  OK  (OS OK  OK  OK<br>ESC RS L  NO  NO  NO  NO  NO  NO  Spec. A for V.  Spec. B  Spec. B  Spec. B  Spec. B<br>1.2 or earier;<br>Spec. B for V.<br>1.3 or later<br>po Bar Codes ESC b   Spec. A  Spec. A  Spec. A  Spec. B  Spec. B Spec. B Spec. B  Spec. B  Spec. B  Spec. B  Spec. B<br>Po Cutter Control ESC d   OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>**----- End of picture text -----**<br>


――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-1 

|**Class**<br>~~yyy~~<br>~~pC~~|**Commands**<br>~~yyy~~<br>~~pC~~|**Model Name**<br>~~PT~~<br>~~yyy~~<br>~~ooo~~|**Model Name**<br>~~PT~~<br>~~yyy~~<br>~~ooo~~|**Model Name**<br>~~PT~~<br>~~yyy~~<br>~~ooo~~|**Model Name**<br>~~PT~~<br>~~yyy~~<br>~~ooo~~|**Model Name**<br>~~PT~~<br>~~yyy~~<br>~~ooo~~|**Model Name**<br>~~PT~~<br>~~yyy~~<br>~~ooo~~|**Model Name**<br>~~PT~~<br>~~yyy~~<br>~~ooo~~|**Model Name**<br>~~PT~~<br>~~yyy~~<br>~~ooo~~|**Model Name**<br>~~PT~~<br>~~yyy~~<br>~~ooo~~|**Model Name**<br>~~PT~~<br>~~yyy~~<br>~~ooo~~|**Model Name**<br>~~PT~~<br>~~yyy~~<br>~~ooo~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~PT~~<br>~~yyy~~|**TSP700**<br>~~PT~~<br>~~yyy~~|**TSP600**<br>~~PT~~<br>~~yyy~~|**TUP900**<br>~~PT~~<br>~~yyy~~|**TSP1000**<br>~~PT~~<br>~~yyy~~|**TSP828L**<br>~~PT~~|**TSP700II**<br>~~PT~~|**TSP650**<br>~~PT~~<br>~~ooo~~|**TUP500**<br>~~PT~~<br>~~ooo~~|**TSP800II**<br>~~PT~~<br>~~ooo~~|**FVP10**<br>~~PT~~<br>~~ooo~~|
|External<br>device drive<br>~~pC~~<br>~~Po~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~po~~|ESC BEL<br>~~pC~~<br>~~Po~~|OK|OK|OK|NO|NO|NO|NO|OK|NO|OK|OK|
||BEL<br>~~pC~~<br>~~Po~~<br>~~po~~|OK|OK|OK|NO|NO|NO|NO|OK|NO|OK|OK|
||FS<br>~~Po~~<br>~~po~~<br>~~po~~|OK|OK|OK|NO|NO|NO|NO|OK|NO|OK|OK|
||SUB<br>~~po~~<br>~~po~~<br>~~po~~|OK|OK|OK|NO|NO|NO|NO|OK|NO|OK|OK|
||EM<br>~~po~~<br>~~po~~<br>~~po~~|OK|OK|OK|NO|NO|NO|NO|OK|NO|OK|OK|
||ESC GS BEL<br>~~po~~<br>~~po~~<br>~~po~~|NO|Ver. 5.0 or<br>later|NO|NO|OK|NO|NO|OK|NO|OK|OK|
||ESC GS EM DC1<br>~~po~~<br>~~po~~|NO|NO|NO|NO|NO|NO|After Ver.<br>1.3|OK|NO|OK|OK|
||ESC GS EM DC2<br>~~po~~|NO|NO|NO|NO|NO|NO|After Ver.<br>1.3|OK|NO|OK|OK|
|Print Setting<br>~~ee~~|ESC RS d<br>~~ee~~|Spec. A<br>~~ee~~|Spec. A<br>~~ee~~|Spec. A<br>~~ee~~|Spec. A<br>~~ee~~|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. B|Spec. B|
||ESC RS r<br>~~ee ~~|Spec. A<br> ~~ee~~|Spec. A<br>~~ee ~~|Spec. A<br> ~~ee~~|Spec. A<br>~~ee~~|Spec. A|Spec. A|Spec. A|Spec. A|Spec. B|Spec. A|Spec. A|
|Status<br>~~po~~<br>~~po~~<br>~~Po~~<br>~~Po~~<br>~~po~~<br>~~Po~~<br>~~**P**~~|ESC RS a<br>~~po~~|Spec. A|Spec. A|Spec. A|Spec. A<br>Ver. 1.2 or<br>earlier<br>Spec. B<br>Ver. 1.2 or<br>later|Spec. B|Spec. B|Spec. B<br>Ver. 2.0 or<br>earlier<br>Spec. C<br>Ver. 2. or<br>later|Spec. B<br>Ver. 2.0 or<br>earlier<br>Spec. C<br>Ver. 2. or<br>later|Spec. C|Spec. C|Spec. C|
||ESC ACK SOH<br>~~po~~<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ENQ<br>~~po~~<br>~~po~~<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||EOT<br>~~po~~<br>~~Po~~<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC ACK CAN<br>~~Po~~<br>~~Po~~<br>~~po~~|No|No|No|No|No|NO|OK|OK|OK|OK|OK|
||ETB<br>~~Po~~<br>~~po~~<br>~~Po~~|Spec. A|Spec. A|Spec. A|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|
||ESC RS E<br>~~po~~<br>~~Po~~<br>~~**P**o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
|Kanji character <br>~~Po~~<br>~~**P**~~<br>~~Po~~<br>~~Po~~<br>~~Po~~<br>~~Po~~<br>~~Po~~|ESC p<br>~~Po~~<br>~~**P**o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC q<br>~~**P**o~~<br>~~Po~~|OK|OK|OK|OK|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|
||ESC $ ~~Po~~<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC s<br>~~Po~~<br>~~Po~~<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC t<br>~~Po~~<br>~~Po~~<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC r<br>~~Po~~<br>~~Po~~<br>~~Po~~|Spec. A|Spec. A|Spec. A|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|
|Others<br>~~Po~~<br>~~Po~~<br>~~—~~<br>~~Po~~|CAN<br>~~Po~~<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC @<br>~~Po~~<br>~~—~~<br>~~|~~|OK<br>~~|~~|OK<br>~~tt~~|OK<br>~~tt~~|OK<br>~~tt~~<br>~~te~~|OK<br>~~tett~~|OK<br>~~tt~~|OK<br>~~tt~~|OK|OK|OK|OK|
||ESC GS # m<br>~~—~~<br>~~|~~<br>~~Po~~|Spec. A<br>VER. 3.0<br>OR LATER<br>~~|~~<br>|Spec. A<br>~~tt~~<br>|Spec. A<br>~~tt~~<br>|Spec. B<br>~~tt~~<br>~~te~~<br>|Spec. B<br>~~tett~~<br>|Spec. B<br>~~tt~~<br>|Spec. B<br>~~tt~~<br>|Spec. B<br>|Spec. B<br>|Spec. C<br>|Spec. C<br>|
||ESC ?<br>~~—~~<br>~~|~~<br>~~Po~~|OK<br>~~| ~~<br>|OK<br> ~~tt~~<br>|OK<br>~~tt~~<br>|OK<br>~~tt~~<br>~~te~~<br>|OK<br>~~te tt~~<br>|OK<br>~~tt~~<br>|OK<br>~~tt~~<br>|OK<br>|OK<br>|OK<br>|OK<br>|



• Raster Commands 

|**Class**<br><br>~~yyy~~<br>~~Po~~|**Commands**<br> <br>~~yyy~~<br>~~Po~~|**Model Name**<br> ~~PT~~<br>~~yyy~~<br>~~yyy~~|**Model Name**<br> ~~PT~~<br>~~yyy~~<br>~~yyy~~|**Model Name**<br> ~~PT~~<br>~~yyy~~<br>~~yyy~~|**Model Name**<br> ~~PT~~<br>~~yyy~~<br>~~yyy~~|**Model Name**<br> ~~PT~~<br>~~yyy~~<br>~~yyy~~|**Model Name**<br> ~~PT~~<br>~~yyy~~<br>~~yyy~~|**Model Name**<br> ~~PT~~<br>~~yyy~~<br>~~yyy~~|**Model Name**<br> ~~PT~~<br>~~yyy~~<br>~~yyy~~|**Model Name**<br> ~~PT~~<br>~~yyy~~<br>~~yyy~~|**Model Name**<br> ~~PT~~<br>~~yyy~~<br>~~yyy~~|**Model Name**<br> ~~PT~~<br>~~yyy~~<br>~~yyy~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~yyy~~|**TSP700**<br>~~yyy~~|**TSP600**<br>~~yyy~~|**TUP900**<br>~~yyy~~|**TSP1000**<br>~~yyy~~|**TSP828L**<br>~~yyy~~|**TSP700II**<br>~~yyy~~|**TSP650**<br>~~yyy~~|**TUP500**<br>~~yyy~~|**TSP800II**|**FVP10**|
|Raster<br>~~yyy~~<br>~~Po~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~Po~~<br>~~Po~~<br>~~Po~~<br>~~po~~<br>~~po~~<br>~~Po~~<br>~~Po~~<br>~~Po~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~Po~~<br>~~Po~~<br>~~po~~<br>~~po~~<br>~~Po~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~Po~~<br>~~Po~~|ESC*r R<br>~~yyy~~<br>~~Po~~<br>~~po~~|NO<br>~~yyy~~|NO<br>~~yyy~~|NO<br>~~yyy~~|NO<br>~~yyy~~|OK<br>~~yyy~~|OK<br>~~yyy~~|OK<br>~~yyy~~|OK<br>~~yyy~~|OK<br>~~yyy~~|OK|OK|
||ESC*r A<br>~~Po~~<br>~~po~~<br>~~po~~|NO|NO|NO|NO|OK|OK|OK|OK|OK|OK|OK|
||ESC*r B<br>~~po~~<br>~~po~~<br>~~po~~|NO|NO|NO|NO|OK|OK|OK|OK|OK|OK|OK|
||ESC*r C<br>~~po~~<br>~~po~~<br>~~Po~~|NO|NO|NO|NO|OK|OK|OK|OK|OK|OK|OK|
||ESC*r D<br>~~po~~<br>~~Po~~<br>~~Po~~|NO<br>~~Po~~|NO|NO|NO|OK|OK|OK|OK|OK|OK|OK|
||ESC*r E<br>~~Po~~<br>~~Po~~<br>~~Po~~|NO<br>~~Po~~|NO|NO|NO|OK|OK|OK|OK|OK|OK|OK|
||ESC*r F<br>~~Po~~<br>~~Po~~<br>~~po~~|NO<br>~~Po~~|NO|NO|NO|OK|OK|OK|OK|OK|OK|OK|
||ESC*r P<br>~~Po~~<br>~~po~~<br>~~po~~|NO<br>|NO<br>|NO<br>|NO<br>|OK<br>|OK<br>|OK<br>|OK<br>|OK<br>|OK<br>|OK<br>|
||ESC*r Q<br>~~po~~<br>~~po~~|NO<br>|NO<br>|NO<br>|NO<br>|OK<br>|OK<br>|OK<br>|OK<br>|OK<br>|OK<br>|OK<br>|
||ESC*r m l<br>~~poPo~~<br>~~Po~~|NO<br>~~Po~~<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|
||ESC*r m r<br>~~Po~~<br>~~Po~~|NO<br>~~Po~~|NO|NO|NO|OK|OK|OK|OK|OK|OK|OK|
||ESC*r T<br>~~Po~~<br>~~Po~~<br>~~Po~~|NO<br>~~Po~~|NO|NO|NO|OK|OK|OK|OK|OK|OK|OK|
||ESC*r K<br>~~Po~~<br>~~Po~~<br>~~po~~|NO|NO|NO|NO|OK|OK|OK|OK|OK|OK|OK|
||b n1 n2 d1...dk<br>~~Po~~<br>~~po~~<br>~~po~~|NO|NO|NO|NO|OK|OK|OK|OK|OK|OK|OK|
||k n1 n2 d1...dk<br>~~po~~<br>~~po~~<br>~~po~~|NO|NO|NO|NO|OK|OK|OK|OK|OK|OK|OK|
||ESC*r Y<br>~~po~~<br>~~po~~<br>~~Po~~|NO|NO|NO|NO|OK|OK|OK|OK|OK|OK|OK|
||ESC FF NUL<br>~~po~~<br>~~Po~~<br>~~Po~~|NO<br>~~Po~~|NO|NO|NO|OK|OK|OK|OK|OK|OK|OK|
||ESC FF EOT<br>~~Po~~<br>~~Po~~<br>~~po~~|NO<br>~~Po~~<br>~~CE~~|NO<br>~~CE~~|NO|NO|OK|OK|OK|OK|OK|OK|OK|
||ESC * r N<br>~~Po~~<br>~~po~~<br>~~po~~|NO<br>~~Po~~<br>~~CE~~|NO<br>~~CE~~|NO|NO|NO|NO|Ver. 1.3 or<br>later|OK|OK|OK|OK|
||ESC * r V<br>~~po~~<br>~~po~~<br>~~Po~~|NO<br>~~CE~~|NO<br>~~CE~~|NO|NO|NO|NO|Ver. 1.3 or<br>later|OK|OK|OK|OK|
||ESC*r e<br>~~po~~<br>~~Po~~<br>~~po~~|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|OK|
||ESC*r S<br>~~Po~~<br>~~po~~<br>~~po~~|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|OK|
||ESC*r s 0<br>~~po~~<br>~~po~~<br>~~po~~|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|OK|
||ESC*r s 1<br>~~po~~<br>~~po~~<br>~~Po~~|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|OK|
||ESC*r s 2<br>~~po~~<br>~~Po~~<br>~~Po~~|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|OK|
||ESC*r s 3<br>~~Po~~<br>~~Po~~|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|OK|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-2 

|• Black Mark Related Commands||
|---|---|
|**Class**<br>**Commands**<br>**Model Name**<br>~~Ce~~||
|**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**||
|Black Mark<br>ESC d<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>NO<br>OK<br>OK<br>OK<br>Related<br>FF<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>NO<br>OK<br>OK<br>OK<br>Commands<br>ESC C<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>NO<br>OK<br>OK<br>OK<br>ESC C 0<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>NO<br>OK<br>OK<br>OK<br>VT<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>NO<br>OK<br>OK<br>OK<br>ESC B<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>NO<br>NO<br>OK<br>OK<br>OK<br>~~SSS~~<br>~~**P**o~~<br>~~o~~<br>~~Po~~<br>~~a~~<br>~~GG~~<br>~~GG~~<br>~~OO~~<br>~~Pe~~||
|• 2-Color PrintingRelated Commands||
|**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**<br>2-Color<br>ESC RS c<br>Ver. 4.0 or<br>Ver. 2.0 or<br>Ver. 2.0 or<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>~~eT~~<br>~~CS~~<br>~~OOOO~~||
|Printing<br>later<br>later<br>later<br>Related<br>Commands<br>ESC RS C<br>Spec. A<br>Ver. 4.0 or<br>later<br>Spec. A<br>Ver. 2.0 or<br>later<br>Spec. A<br>Ver. 2.0 or<br>later<br>Spec. B<br>Spec. B<br>Spec. B<br>Spec. C<br>Spec. A<br>Spec. C<br>Spec. C<br>Spec. C<br>ESC<br>4<br>(Not<br>Recommended)<br>Ver. 4.0 or<br>later<br>Ver. 2.0 or<br>later<br>Ver. 2.0 or<br>later<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>OK<br>NO<br>ESC<br>5<br>(Not<br>Recommended)<br>Ver. 4.0 or<br>later<br>Ver. 2.0 or<br>later<br>Ver. 2.0 or<br>later<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>OK<br>NO<br>ESC FS q<br>Ver. 4.0 or<br>later<br>Ver. 2.0 or<br>later<br>Ver. 2.0 or<br>later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>ESC FS p<br>Ver. 4.0 or<br>later<br>Ver. 2.0 or<br>later<br>Ver. 2.0 or<br>later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>~~tt~~<br>~~te tt tt~~<br>~~a a i eeee ee ee~~<br>~~es~~<br>~~es esee rs~~<br>~~es es~~<br>~~es~~<br>~~es es~~<br>~~aiee~~<br>~~esss~~||



## • Presenter Related Commands 

|• Presenter Related Commands||
|---|---|
|**Class**<br>**Commands**<br>**Model Name**||
|**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TP800II**<br>**FVP10**||
|Presenter<br>ESC SYN0<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>Related<br>ESC SYN 1<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>Commands<br>ESC SYN 3<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>ESC SYN 4<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>ESC GS SUB DC1<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>ESC GS SUB DC2<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>ESC GS SUB DC3<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>~~RsCC~~<br>~~pe~~<br>~~a CC~~<br>~~GCC~~<br>~~CO~~<br>~~esCC~~<br>=~~=S=======——~~<br>~~a CC~~||
|• Mark Commands||
|**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**<br>Mark<br>ESC GS * 0<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>Ver. 3.0 or<br>later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>Commands<br>ESC GS * 1<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>Ver. 3.0 or<br>later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>ESC GS * 2<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>Ver. 3.0 or<br>later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>ESC GS * W<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>Ver. 3.0 or<br>later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>ESC GS * C<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>Ver. 3.0 or<br>later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>~~ce~~<br>~~yyeeyaeaaaaa—a_an>a>ass~~<br>~~es es es ee ssGs~~<br>~~is es ee es~~<br>~~es ee es ee es~~<br>~~es~~<br>~~ee~~<br>~~es ee es ee es~~<br>~~es se~~<br>~~ee~~<br>~~eseseeesse~~||



• Auto Logo Commands 

|**Class**<br>~~Ce~~|**Commands**<br>~~Ce~~<br>~~uyeyaeao—_—_—_}_~~<br>~~es~~|**Model Name**<br>~~Ce~~<br>~~uyeyaeao—_—_—_}_IN~~|**Model Name**<br>~~Ce~~<br>~~uyeyaeao—_—_—_}_IN~~|**Model Name**<br>~~Ce~~<br>~~uyeyaeao—_—_—_}_IN~~|**Model Name**<br>~~Ce~~<br>~~uyeyaeao—_—_—_}_IN~~|**Model Name**<br>~~Ce~~<br>~~uyeyaeao—_—_—_}_IN~~|**Model Name**<br>~~Ce~~<br>~~uyeyaeao—_—_—_}_IN~~|**Model Name**<br>~~Ce~~<br>~~uyeyaeao—_—_—_}_IN~~|**Model Name**<br>~~Ce~~<br>~~uyeyaeao—_—_—_}_IN~~|**Model Name**<br>~~Ce~~<br>~~uyeyaeao—_—_—_}_IN~~|**Model Name**<br>~~Ce~~<br>~~uyeyaeao—_—_—_}_IN~~|**Model Name**<br>~~Ce~~<br>~~uyeyaeao—_—_—_}_IN~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~Ce~~<br>~~uyeyaeao—_—_—_}_~~<br>~~es~~|**TSP700**<br>~~uyeyaeao—_—_—_}_~~<br>~~es~~|**TSP600**<br>~~uyeyaeao—_—_—_}_~~<br>~~ee~~|**TUP900**<br>~~uyeyaeao—_—_—_}_~~<br>~~ss~~|**TSP1000**<br>~~uyeyaeao—_—_—_}_~~<br>~~ss~~|**TSP828L**<br>~~uyeyaeao—_—_—_}_~~<br>~~ss~~|**TSP700II**<br>~~uyeyaeao—_—_—_}_~~<br>~~Gs~~|**TSP650**<br>~~uyeyaeao—_—_—_}_~~<br>~~Gs~~|**TUP500**<br>~~uyeyaeao—_—_—_}_~~|**TSP800II**<br>~~uyeyaeao—_—_—_}_IN~~|**FVP10**<br>~~IN~~|
|Auto Logo<br>Commands<br>~~Ce~~|ESC GS / W<br>~~Ce~~<br>~~uyeyaeao—_—_—_}_~~<br>~~es~~<br>~~is~~|NO<br>~~Ce~~<br>~~uyeyaeao—_—_—_}_~~<br>~~es~~<br>~~is~~|Ver. 4.0 or<br>later<br>~~uyeyaeao—_—_—_}_~~<br>~~es~~<br>~~es~~|NO<br>~~uyeyaeao—_—_—_}_~~<br>~~ee~~<br>~~ee~~|NO<br>~~uyeyaeao—_—_—_}_~~<br>~~ss~~<br>~~es~~|NO<br>~~uyeyaeao—_—_—_}_~~<br>~~ss~~|NO<br>~~uyeyaeao—_—_—_}_~~<br>~~ss~~|OK<br>~~uyeyaeao—_—_—_}_~~<br>~~Gs~~|OK<br>~~uyeyaeao—_—_—_}_~~<br>~~Gs~~|NO<br>~~uyeyaeao—_—_—_}_~~|OK<br>~~uyeyaeao—_—_—_}_ IN~~|OK<br>~~IN~~|
||ESC GS / C<br>~~es ~~<br>~~is~~<br>~~es~~|NO<br> ~~es ~~<br>~~is~~<br>~~ee~~|Ver. 4.0 or<br>later<br> ~~es ~~<br>~~es~~<br>~~es~~|NO<br> ~~ee ~~<br>~~ee~~<br>~~ee~~|NO<br> ~~ss~~<br>~~es~~<br>~~es~~|NO<br>~~ss~~<br>~~es~~|NO<br>~~ss~~<br>~~ee~~|OK<br>~~Gs~~<br>~~ee~~|OK<br>~~Gs~~|NO|OK|OK|
||ESC GS / 1<br>~~is~~<br>~~es~~<br>~~es~~|NO<br>~~is ~~<br>~~ee~~<br>~~ee~~|Ver. 4.0 or<br>later<br> ~~es ~~<br>~~es~~<br>~~es~~|NO<br> ~~ee ~~<br>~~ee~~<br>~~ee~~|NO<br> ~~es~~<br>~~es~~<br>~~es~~|NO<br>~~es~~<br>~~es~~|NO<br>~~ee~~<br>~~se~~|OK<br>~~ee~~<br>~~se~~|OK|NO|OK|OK|
||ESC GS / 2<br>~~es ~~<br>~~es~~<br>~~ee~~|NO<br> ~~ee ~~<br>~~ee~~<br>~~es~~|Ver. 4.0 or<br>later<br> ~~es ~~<br>~~es~~<br>~~ee es~~|NO<br> ~~ee ~~<br>~~ee~~<br>~~es~~|NO<br> ~~es~~<br>~~es~~<br>~~es~~|NO<br>~~es~~<br>~~es~~|NO<br>~~ee~~<br>~~se~~|OK<br>~~ee~~<br>~~se~~|OK|NO|OK|OK|
||ESC GS / 3<br>~~es ~~<br>~~ee~~<br>~~is~~|NO<br> ~~ee ~~<br>~~es~~<br>~~is~~|Ver. 4.0 or<br>later<br> ~~es ~~<br>~~ee es~~<br>~~es~~|NO<br> ~~ee ~~<br>~~es~~<br>~~ee~~|NO<br> ~~es~~<br>~~es~~<br>~~es~~|NO<br>~~es ~~|NO<br> ~~se~~|OK<br>~~se~~|OK|NO|OK|OK|
||ESC GS / 4<br>~~ee ~~<br>~~is~~<br>~~es~~|NO<br> ~~es ~~<br>~~is~~<br>~~ee~~|Ver. 4.0 or<br>later<br> ~~ee es~~<br>~~es~~<br>~~es~~|NO<br>~~es~~<br>~~ee~~<br>~~ee~~|NO<br>~~es~~<br>~~es~~<br>~~es~~|NO<br>~~es~~|NO<br>~~ee~~|OK<br>~~ee~~|OK|NO|OK|OK|
||ESC GS / 5<br>~~is~~<br>~~es~~<br>~~es~~|NO<br>~~is ~~<br>~~ee~~<br>~~ee~~|Ver. 4.0 or<br>later<br> ~~es ~~<br>~~es~~<br>~~es~~|NO<br> ~~ee ~~<br>~~ee~~<br>~~ee~~|NO<br> ~~es~~<br>~~es~~<br>~~es~~|NO<br>~~es~~<br>~~es~~|NO<br>~~ee~~<br>~~se~~|OK<br>~~ee~~<br>~~se~~|OK|NO|OK|OK|
||ESC GS / 6<br>~~es ~~<br>~~es~~|NO<br> ~~ee ~~<br>~~ee~~|Ver. 4.0 or<br>later<br> ~~es ~~<br>~~es~~|NO<br> ~~ee ~~<br>~~ee~~|NO<br> ~~es~~<br>~~es~~|NO<br>~~es~~<br>~~es~~|NO<br>~~ee~~<br>~~se~~|OK<br>~~ee~~<br>~~se~~|OK|NO|OK|OK|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-3 

• PDF417 Commands 

**==> picture [498 x 209] intentionally omitted <==**

**----- Start of picture text -----**<br>
||||||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Class|Commands|Model Name|
|cree|TSP800|TSP700|TSP600|TUP900|TSP1000|TSP828L|TSP700II|TSP650|TUP500|TSP800II|FVP10|
|PDF417|ESC GS x S 0|NO|NO|NO|Ver. 3.1 or|OK|OK|OK|NO|OK|OK|OK|
|later|
|Commands|ee|ESC GS x S 1|NO|NO|cee|NO|Ver. 3.1 or|ees|ee|OK|ee|OK|ee|OK|NO|OK|OK|OK|
|later|
|ee|ESC GS x S 2|NO|Ge|NO|Ge|NO|GG|Ver. 3.1 or|OK|OK|eG|OK|NO|OK|OK|OK|
|later|
|ee|ESC GS x S 3|ee|NO|ee|NO|Ge|NO|GG|Ver. 3.1 or|OK|eG|OK|OK|NO|OK|OK|OK|
|later|
|Rs|ESC GS x D|ee|NO|ee|NO|Ge|NO|Ver. 3.1 or|df|OK|OK|eG|OK|NO|OK|OK|OK|
|later|
|Re|ESC GS x P|re|NO|NO|ee|Gs|NO|Ge|Ver. 3.1 or|ee|OK|OK|OK|GG|NO|OK|OK|OK|
|later|
|ee|ESC GS x I|ee|NO|eeee|NO|G|NO|se|G|Ver. 3.1 or|eeG|OK|eG|OK|GQ|OK|NO|OK|OK|OK|
|GeGe|later|dG|
|• Print Start Trigger Control Commands|
|Class|Commands|Model Name|
|TSP800|TSP700|TSP600|TUP900|TSP1000|TSP828L|TSP700II|TSP650|TUP500|TSP800II|FVP10|
|Print Start|ESC GS g 0|NO|NO|NO|NO|Ver. 1.1 or|OK|OK|OK|OK|OK|OK|
|later|
|Trigger Control ESC GS g 1|NO|NO|NO|NO|Ver. 1.1 or|OK|OK|OK|OK|OK|OK|
|later|

**----- End of picture text -----**<br>


**==> picture [498 x 203] intentionally omitted <==**

**----- Start of picture text -----**<br>
|||||||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|• QR Commands|
|Class|Commands|Model Name|
|re|TSP800|TSP700|TSP600|TUP900|TSP1000|TSP828L|TSP700II|TSP650|TUP500|TSP800II|FVP10|
|QR Code|ESC GS y S 0|NO|NO|NO|NO|Ver. 1.2 or|OK|OK|NO|OK|OK|OK|
|ee|ee|eee ees|later|es ee|
|ESC GS y S 1|NO|NO|NO|NO|Ver. 1.2 or|OK|OK|NO|OK|OK|OK|
|later|
|ee|ESC GS y S 2|NO|Ge|NO|Ge|NO|NO|dG|Ver. 1.2 or|eG|OK|OK|NO|OK|OK|OK|
|later|
|ee|ESC GS y D 1|NO|ee|NO|Ge|NO|NO|dG|Ver. 1.2 or|OK|eG|OK|NO|OK|OK|OK|
|later|
|Rs|ESC GS y D 2|NO|ee|NO|Gs|NO|NO|Ge|Ver. 1.2 or|OK|OK|NO|eG|OK|OK|OK|
|later|
|Re|ESC GS y P|r|NO|e|e|NO|ee|Gs|NO|G|NO|eee ee|Ver. 1.2 or|OK|GQ|OK|GG|NO|OK|OK|OK|
|later|
|ee|ESC GS y I|NO|ee|NO|Gs|NO|NO|dQ|Ver. 1.2 or|ee|OK|OK|NO|eG|OK|OK|OK|
|eeGe|ed|later|ee|
|• Page Function Commands|
|Class|Commands|Model Name|
|TSP800|TSP700|TSP600|TUP900|TSP1000|TSP828L|TSP700II|TSP650|TUP500|TSP800II|FVP10|
|Page Function|ESC GS h 0|NO|NO|NO|NO|NO|NO|OK|NO|OK|OK|OK|
|ESC GS h 1|NO|NO|NO|NO|NO|NO|OK|NO|OK|OK|OK|

**----- End of picture text -----**<br>


## • Reduced Printing Function Commands 

**==> picture [498 x 155] intentionally omitted <==**

**----- Start of picture text -----**<br>
||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Class|Commands|Model Name|
|TSP800|TSP700|TSP600|TUP900|TSP1000|TSP828L|TSP700II|TSP650|TUP500|TSP800II|FVP10|
|Reduced Printing|ESC GS c|No|No|No|No|No|No|No|No|No|No|Yes|
|Function|
|• Page Mode Commands|
|Class|Commands|Model Name|
|TSP800|TSP700|TSP600|TUP900|TSP1000|TSP828L|TSP700II|TSP650|TUP500|TSP800II|FVP10|
|Page Mode|GO|ESC GS P 0|No|No|No|No|No|No|No|No|No|No|Yes|
|ESC GS P 1|No|No|No|No|No|No|No|No|No|No|Yes|
|po|ESC GS P 2|No|No|No|No|No|No|No|No|No|No|Yes|
|GO|ESC GS P 3|No|No|No|No|No|No|No|No|No|No|Yes|
|ESC GS P 4|No|No|No|No|No|No|No|No|No|No|Yes|
|po|(OO|(OO|
|po|ESC GS P 5|No|No|No|No|No|No|No|No|No|No|Yes|
|po|ESC GS P 6|No|No|No|No|No|No|No|No|No|No|Yes|
|po|ESC GS P 7|No|No|No|No|No|No|No|No|No|No|Yes|
|-Po|ESC GS P 8|No|No|No|No|No|GO|No|No|No|(OO|No|No|Yes|

**----- End of picture text -----**<br>


――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-4 

|• Text Search Commands|
|---|
|**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP800II**<br>**FVP10**<br>Text Search<br>ESC GS)B(fn = 48)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS)B(fn = 49)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS)B(fn = 50)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS)B(fn = 64)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS)B(fn = 65)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS)B(fn = 80)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS)B(fn = 81)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS)B(fn = 96)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS)B(fn = 97)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>• Audio Commands<br>**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP800II**<br>**FVP10**<br>Audio<br>ESC GS s O<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS s P<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS s R<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS s I<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS s U<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS s T<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>~~Ce~~<br>~~eee~~<br>~~Po~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~GO~~<br>~~(OO~~<br>~~(OO~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~Po Ce~~<br>~~a~~<br>~~(~~<br>~~Ww~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~GO~~<br>~~GO~~<br>~~(OO~~<br>~~po~~<br>~~Poff~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-5 

## **6.2. Parallel I/F • USB I/F (Ver2.0)  • Powered USB I/F** 

|**Class**<br>~~errr~~|**Commands**<br>~~errr~~|**Model Name**<br>~~PT~~<br>~~errr~~|**Model Name**<br>~~PT~~<br>~~errr~~|**Model Name**<br>~~PT~~<br>~~errr~~|**Model Name**<br>~~PT~~<br>~~errr~~|**Model Name**<br>~~PT~~<br>~~errr~~|**Model Name**<br>~~PT~~<br>~~errr~~|**Model Name**<br>~~PT~~<br>~~errr~~|**Model Name**<br>~~PT~~<br>~~errr~~|**Model Name**<br>~~PT~~<br>~~errr~~|**Model Name**<br>~~PT~~<br>~~errr~~|**Model Name**<br>~~PT~~<br>~~errr~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~PT~~<br>~~errr~~|**TSP700**<br>~~PT~~<br>~~errr~~|**TSP600**<br>~~PT~~<br>~~errr~~|**TUP900**<br>~~PT~~<br>~~errr~~|**TSP1000**<br>~~PT~~<br>~~errr~~|**TSP828L**<br>~~PT~~<br>~~errr~~|**TSP700II**<br>~~PT~~<br>~~errr~~|**TSP650**<br>~~PT~~<br>~~errr~~|**TUP500**<br>~~PT~~<br>~~errr~~|**TSP800II**<br>~~PT~~<br>~~errr~~|**FVP10**<br>~~PT~~<br>~~errr~~|
|Font Style<br>and<br>Character Set<br>~~errr~~<br>~~Po~~<br>~~**P**~~<br>~~**P**~~|ESC RS F<br>~~errr~~<br>~~PT~~|NO<br>~~errr~~<br>~~PT~~|NO<br>~~errr~~<br>~~PT~~|NO<br>~~errr~~<br>~~PT~~|NO<br>~~errr~~<br>~~PT~~|OK<br>~~errr~~<br>~~PT~~|OK<br>~~errr~~<br>~~PT~~|OK<br>~~errr~~<br>~~PT~~|OK<br>~~errr~~<br>~~PT~~|OK<br>~~errr~~<br>~~PT~~|OK<br>~~errr~~<br>~~PT~~|OK<br>~~errr~~<br>~~PT~~|
||ESC GS t<br>~~PT~~<br>~~PT~~|OK<br>~~PT~~<br>~~PT~~|OK<br>~~PT~~<br>~~PT~~|OK<br>~~PT~~<br>~~PT~~|OK<br>~~PT~~<br>~~PT~~|OK<br>~~PT~~<br>~~PT~~|OK<br>~~PT~~<br>~~PT~~|OK<br>~~PT~~<br>~~PT~~|OK<br>~~PT~~<br>~~PT~~|OK<br>~~PT~~<br>~~PT~~|OK<br>~~PT~~<br>~~PT~~|OK<br>~~PT~~<br>~~PT~~|
||ESC GS =<br>~~Po~~|Ver. 3.0 or<br>later|Ver. 3.0 or<br>Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|
||ESC R<br>~~Po~~<br>~~**P**o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC /<br>~~Po~~<br>~~**P**o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC SP<br>~~**P**o~~|OK|OK|OK|OK|OK<br>~~T~~|OK<br>~~T~~|OK<br>~~T~~|OK<br>~~T~~|OK<br>~~T~~|OK<br>~~T~~|OK<br>~~T~~|
||ESC M<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|
||ESC P<br>~~Po~~<br>~~PO~~|OK<br>~~Po~~<br>~~PO~~|OK<br>~~Po~~<br>~~PO~~|OK<br>~~Po~~<br>~~PO~~|OK<br>~~Po~~<br>~~PO~~|OK<br>~~Po~~<br>~~PO~~|OK<br>~~Po~~<br>~~PO~~|OK<br>~~Po~~<br>~~PO~~|OK<br>~~Po~~<br>~~PO~~|OK<br>~~Po~~<br>~~PO~~|OK<br>~~Po~~<br>~~PO~~|OK<br>~~Po~~<br>~~PO~~|
||ESC:<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|
||ESC<br>p<br>(Not<br>recommended)|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESCg<br>~~Po~~<br>~~**P**O~~|Spec. A<br>~~Po~~<br>~~O~~|Spec. A<br>~~Po~~|Spec. A<br>~~Po~~|Spec. B<br>~~Po~~|Spec. B<br>~~Po~~|Spec. B<br>~~Po~~|Spec. A<br>~~Po~~|Spec. A<br>~~Po~~|Spec. B<br>~~Po~~|Spec. A<br>~~Po~~|Spec. A<br>~~Po~~|
|Character<br>expansion<br>settings<br>~~**P**~~<br>~~Po~~<br>~~Po~~<br>~~**P**~~|ESC i<br>~~Po~~<br>~~**P**O~~|OK<br>~~Po~~<br>~~O~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|
||ESCW<br>~~**P**O~~<br>~~Po~~|OK<br>~~O~~|OK|OK|OK|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|
||ESC h<br>~~Po~~<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||SO<br>~~Po~~<br>~~Po~~<br>~~**P**o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||DC4<br>~~Po~~<br>~~**P**o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC SO<br>~~**P**o~~|OK|OK|OK|OK|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|
||ESC DC4|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
|Print Mode<br>~~Po~~<br>~~**P**~~<br>~~Po~~|ESC E|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. B|Spec. A V.<br>2.0 or<br>earlier<br>Spec. B V.<br>2.0 or later|Spec. A V.<br>2.0 or<br>earlier<br>Spec. B V.<br>2.0 or later|Spec. A V.<br>2.0 or<br>earlier<br>Spec. B V.<br>2.0 or later|Spec. A|Spec. A|
||ESC F|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. B|Spec. A V.<br>2.0 or<br>earlier<br>Spec. B V.<br>2.0 or later|Spec. A V.<br>2.0 or<br>earlier<br>Spec. B V.<br>2.0 or later|Spec. A V.<br>2.0 or<br>earlier<br>Spec. B V.<br>2.0 or later|Spec. A|Spec. A|
||ESC-<br>~~PO~~<br>~~Po~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|
||ESC_<br>~~Po~~<br>~~**P**o~~|OK|OK|OK|OK|OK|OK<br>~~GG~~|OK<br>~~GG~~|OK|OK|OK|OK|
||ESC 4<br>~~Po~~<br>~~GGG~~<br>~~**P**o~~|OK<br>~~GGG~~|OK<br>~~GGG~~|OK<br>~~GGG~~|OK<br>~~GGG~~|OK<br>~~GGG~~|OK<br>~~GGG~~<br>~~GG~~|OK<br>~~GGG~~<br>~~GG~~|OK<br>~~GGG~~|OK<br>~~GGG~~|OK<br>~~GGG~~|OK<br>~~GGG~~|
||ESC 5<br>~~**P**o~~|OK|OK|OK|OK|OK|OK<br>~~GG~~|OK<br>~~GG~~|OK|OK|OK|OK|
||SI<br>~~**P**o~~|OK|OK|OK|OK|OK<br>~~O~~|OK<br>~~GG~~<br>~~O~~|OK<br>~~GG~~<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|
||DC2<br>~~Po~~<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|
|Line spacing<br>~~Po~~<br>~~Po~~<br>~~**P**~~<br>~~Po~~|LF<br>~~Po~~<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||CR<br>~~Po~~<br>~~Po~~<br>~~**P**o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC a<br>~~Po~~<br>~~**P**o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESCz<br>~~**P**o~~|OK|OK|OK|OK|OK<br>~~T~~|OK<br>~~T~~|OK<br>~~T~~|OK<br>~~T~~|OK<br>~~T~~|OK<br>~~T~~|OK<br>~~T~~|
||ESC 0<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|
||ESC J<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|
||ESCI<br>~~PT~~<br>~~Po~~|OK<br>~~PT~~|OK<br>~~PT~~|OK<br>~~PT~~|OK<br>~~PT~~|OK<br>~~PT~~|OK<br>~~PT~~|OK<br>~~PT~~|OK<br>~~PT~~|OK<br>~~PT~~|OK<br>~~PT~~|OK<br>~~PT~~|
|Page Control<br>~~Po~~<br>~~Po~~<br>~~**P**~~|FF<br>~~Po~~<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC C<br>~~Po~~<br>~~Po~~<br>~~**P**o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC C 0<br>~~Po~~<br>~~**P**o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||VT<br>~~**P**o~~|OK|OK|OK|OK|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|
||ESC B<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|
|Horizontal<br>direction<br>position<br>~~Po~~<br>~~**P**~~<br>~~Po~~|ESCl<br>~~Po~~<br>~~Po~~|Spec. A<br>~~Po~~|Spec. A<br>~~Po~~|Spec. A<br>~~Po~~|Spec. B<br>~~Po~~|Spec. B<br>~~Po~~|Spec. B<br>~~Po~~|Spec. A<br>~~Po~~|Spec. A<br>~~Po~~|Spec. B<br>~~Po~~|Spec. A<br>~~Po~~|Spec. A<br>~~Po~~|
||ESCQ<br>~~Po~~<br>~~**P**o~~|Spec. A|Spec. A|Spec. A|Spec. B|Spec. B|Spec. B|Spec. A|Spec. A|Spec. B|Spec. A|Spec. A|
||HT<br>~~Po~~<br>~~**P**o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESCD<br>~~**P**o~~|OK|OK|OK|OK|OK<br>~~T~~|OK<br>~~T~~|OK<br>~~T~~|OK<br>~~T~~|OK<br>~~T~~|OK<br>~~T~~|OK<br>~~T~~|
||ESC GS A<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|
||ESC GS R<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|
||ESC GS a<br>~~PT~~<br>~~Po~~|OK<br>~~PT~~|OK<br>~~PT~~|OK<br>~~PT~~|OK<br>~~PT~~|OK<br>~~PT~~|OK<br>~~PT~~|OK<br>~~PT~~|OK<br>~~PT~~<br>~~ee~~|OK<br>~~PT~~|OK<br>~~PT~~|OK<br>~~PT~~|
|Download<br>~~ee~~<br>~~Po~~<br>~~**P**~~|ESC&<br>~~ee~~<br>~~Po~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|
||ESC%<br>~~ee~~<br>~~Po~~<br>~~**P**o~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|
|Bit Image<br>Graphics<br>~~Po~~<br>~~**P**~~<br>~~Po~~<br>~~Po~~|ESCK<br>~~Po~~<br>~~**P**o~~|OK|OK|OK|OK|OK|OK|OK|OK<br>~~ee~~|OK|OK|OK|
||ESC L<br>~~**P**o~~|OK|OK|OK|OK|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|OK<br>~~O~~|
||ESC k<br>~~Po~~<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|
||ESCX<br>~~Po~~<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
|Logo<br>~~Po~~<br>~~Po~~<br>~~Po~~<br>~~**P**~~|ESC FSq<br>~~Po~~<br>~~Po~~<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC FSp<br>~~Po~~<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC RS L<br>~~Po~~<br>~~**P**o~~|NO|NO|NO|NO|NO|NO|Spec. A<br>for Ver.<br>1.2 or<br>Spec. B<br>for Ver.<br>1.3 or<br>later.|Spec. B|Spec. B|Spec. B|Spec. B|
|Bar Codes<br>~~**P**~~|ESC b<br>~~**P**o~~|Spec. A|Spec. A|Spec. A|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|
|Cutter Control<br>~~**P**~~|ESC d<br>~~**P**o~~|OK|OK|OK|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-6 

|**Class**<br>~~ee~~<br>~~**p**~~|**Commands**<br>~~cree~~<br>~~**p**C~~|**Model Name**<br>~~PT~~<br>~~creereeeeecececereeeeeeseeeeeeeeee~~|**Model Name**<br>~~PT~~<br>~~creereeeeecececereeeeeeseeeeeeeeee~~|**Model Name**<br>~~PT~~<br>~~creereeeeecececereeeeeeseeeeeeeeee~~|**Model Name**<br>~~PT~~<br>~~creereeeeecececereeeeeeseeeeeeeeee~~|**Model Name**<br>~~PT~~<br>~~creereeeeecececereeeeeeseeeeeeeeee~~|**Model Name**<br>~~PT~~<br>~~creereeeeecececereeeeeeseeeeeeeeee~~|**Model Name**<br>~~PT~~<br>~~creereeeeecececereeeeeeseeeeeeeeee~~|**Model Name**<br>~~PT~~<br>~~creereeeeecececereeeeeeseeeeeeeeee~~|**Model Name**<br>~~PT~~<br>~~creereeeeecececereeeeeeseeeeeeeeee~~|**Model Name**<br>~~PT~~<br>~~creereeeeecececereeeeeeseeeeeeeeee~~|**Model Name**<br>~~PT~~<br>~~creereeeeecececereeeeeeseeeeeeeeee~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~PT~~<br>~~cree~~|**TSP700**<br>~~PT~~<br>~~ree~~|**TSP600**<br>~~PT~~<br>~~eee~~|**TUP900**<br>~~PT~~<br>~~cece~~|**TSP1000**<br>~~PT~~<br>~~cere~~|**TSP828L**<br>~~PT~~<br>~~eee~~|**TSP700II**<br>~~PT~~<br>~~ees~~|**TSP650**<br>~~PT~~<br>~~eee~~|**TUP500**<br>~~PT~~<br>~~eee~~|**TSP800II**<br>~~PT~~<br>~~ee~~|**FVP10**<br>~~PT~~<br>~~ee~~|
|External device<br>drive<br>~~ee~~<br>~~**p**~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~pC~~|ESC BEL<br>~~cree~~<br>~~**p**C~~|OK<br>~~PT~~<br>~~cree ~~|OK<br>~~PT~~<br> ~~ree ~~|OK<br>~~PT~~<br> ~~eee ~~|NO<br>~~PT~~<br> ~~cece ~~|NO<br>~~PT~~<br> ~~cere ~~|NO<br>~~PT~~<br> ~~eee ~~|OK<br>~~PT~~<br> ~~ees ~~|OK<br>~~PT~~<br> ~~eee ~~|NO<br>~~PT~~<br> ~~eee ~~|OK<br>~~PT~~<br> ~~ee ~~|OK<br>~~PT~~<br> ~~ee~~|
||BEL<br>~~**p**C~~<br>~~po~~|OK|OK|OK|NO|NO<br>~~o~~|NO<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|NO<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|
||FS<br>~~po~~<br>~~po~~|OK|OK|OK|NO|NO|NO|OK|OK|NO|OK|OK|
||SUB<br>~~po~~<br>~~po~~<br>~~po~~|OK|OK|OK|NO|NO|NO|OK|OK|NO|OK|OK|
||EM<br>~~po~~<br>~~po~~<br>~~Rs~~|OK<br>~~ee~~|OK<br>~~es~~|OK<br>~~eeGe~~|NO<br>~~eeGe~~|NO<br>~~ee~~|NO<br>~~ee~~|OK|OK|NO|OK|OK|
||ESC GS BEL<br>~~po~~<br>~~Rs~~|NO<br>~~ee~~|Ver. 5.0<br>or later<br>~~es~~|NO<br>~~eeGe~~|NO<br>~~eeGe~~|OK<br>~~ee~~|NO<br>~~ee~~|OK|OK|NO|OK|OK|
||ESC GS EM DC1<br>~~Rs ~~<br>~~Ge~~<br>~~pC~~|NO<br> ~~ee ~~<br>~~Ge ~~|NO<br> ~~es ~~<br> ~~GG~~|NO<br> ~~eeGe~~<br>~~GG~~|NO<br>~~eeGe ~~<br>~~GG~~|NO<br> ~~ee~~|NO<br>~~ee~~|Ver. 1.3<br>or later|OK|NO|OK|OK|
||ESC GS EM DC2<br>~~pC~~|NO|NO|NO|NO|NO|NO|Ver. 1.3<br>or later|OK|NO|OK|OK|
|Print Setting<br>~~pC~~|ESC RS d<br>~~pC~~|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. B|Spec. B|
||ESC RS r|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. B|Spec. A|Spec. A|
|Status<br>~~-po~~<br>~~**p**~~<br>~~po~~<br>~~po~~|ESC RS a<br>~~po~~|Spec. A|Spec. A|Spec. A|Spec. A<br>Ver. 1.2 or<br>earlier<br>Spec. B<br>Ver. 1.2 or<br>later|Spec. B|Spec. B|Spec. B V.<br>2.0 or<br>earlier<br>Spec. C V.<br>2.0 or later|Spec. B V.<br>2.0 or<br>earlier<br>Spec. C V.<br>2.0 or later|Spec. C|Spec. C|Spec. C|
||ESC ACK SOH<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ENQ<br>~~po~~<br>~~**p**o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||EOT<br>~~po~~<br>~~**p**o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC ASK CAN<br>~~po~~<br>~~**p**o~~<br>~~po~~|NO|NO|NO|NO|NO<br>~~o~~|NO<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|
||ETB<br>~~po~~<br>~~po~~<br>~~po~~|Spec. A|Spec. A|Spec. A|Spec. B|Spec. B<br>~~o~~|Spec. B<br>~~o~~|Spec. B<br>~~o~~|Spec. B<br>~~o~~|Spec. B<br>~~o~~|Spec. B<br>~~o~~|Spec. B<br>~~o~~|
||ESC RS E<br>~~po~~<br>~~po~~<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC GS ETX<br>~~po~~<br>~~po~~<br>~~ee~~|NO<br>~~ee ~~|NO<br> ~~Ge~~|NO<br>~~Ge~~|NO<br>~~OG~~|NO<br>~~OG~~|NO<br>~~OG~~|Ver. 2.0<br>or later<br>~~OG~~|Ver. 2.0<br>or later<br>~~OG~~|Ver. 2.0<br>or later<br>~~OG~~|OK<br>~~OG~~|OK<br>~~OG~~|
|Kanji character<br>~~-~~<br>~~**p**~~<br>~~po~~<br>~~Po~~<br>~~**P**~~<br>||ESCp<br>~~**p**o~~|OK<br>~~o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC q<br>~~**p**o~~|OK<br>~~o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC$ ~~**p**o~~<br>~~po~~|OK<br>~~o~~|OK|OK|OK|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|
||ESC s<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC t<br>~~po~~<br>~~Po~~<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|
||ESC r<br>~~Po~~<br>~~**P**o~~|Spec. A|Spec. A|Spec. A|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|
|Others<br>~~Po~~<br>~~**P**~~<br>||CAN<br>~~Po~~<br>~~**P**o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC @<br>~~**P**o~~<br>~~EPR~~|OK<br>~~EPR~~|OK<br>~~EPR ~~|OK<br> ~~RRR~~|OK<br>~~RRR~~|OK<br>~~RRR~~|OK<br>~~RRR~~|OK<br>~~RRR~~|OK<br>~~RRR~~|OK<br>~~RRR~~|OK<br>~~RRR~~|OK<br>~~RRR~~|
||ESC GS # m<br>~~**P**o~~|Spec. A<br>Ver. 3.0 or<br>later|Ver. 3.0 or<br>Spec. A|Spec. A|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|
||ESC ?<br>~~**P**o~~|OK|OK|OK|OK|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-7 

• Raster Related Commands 

||~~a~~|~~eeeere~~|~~eeeere~~|~~eeeere~~|~~eeeere~~|~~eeeere~~|~~eeeere~~|~~eeeere~~|~~eeeere~~|~~eeeere~~|~~eeeere~~|~~eeeere~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Class**<br>~~eee~~|**Commands**<br>~~eee~~<br>~~a~~<br>~~a~~|**Model Name**<br>~~eee~~<br>~~eeeere~~|||||||||||
|||**TSP800**<br>~~eee~~<br>~~es~~<br>|**TSP700**<br>~~eee~~<br>~~es~~|**TSP600**<br>~~eee~~<br>~~ee~~|**TUP900**<br>~~eee~~<br>~~ee~~|**TSP1000**<br>~~eee~~<br>~~ee~~|**TSP828L**<br>~~eee~~<br>~~sf~~|**TSP700II**<br>~~eee~~<br>~~eee~~<br>~~sf~~|**TSP650**<br>~~eee~~<br>~~eee~~|**TUP500**<br>~~eee~~<br>~~eeeere~~|**TSP800II**<br>~~eee~~<br>~~ere~~|**FVP10**<br>~~eee~~<br>~~ere~~|
|Raster|ESC * r R<br>~~a~~<br>~~a~~<br>~~a~~|Ver. 2.0 or<br>later<br>~~es~~<br>~~i~~|OK<br>~~es~~<br>~~es~~|OK<br>~~ee~~<br>~~es~~|OK<br>~~ee~~<br>~~es~~|OK<br>~~ee~~<br>~~es~~|OK<br>~~sf~~<br>~~es~~|OK<br>~~eee~~<br>~~sf~~|OK<br>~~eee~~|OK<br>~~eee ere~~|OK<br>~~ere~~|OK<br>~~ere~~|
||ESC * r A<br>~~a~~<br>~~a~~<br>~~es~~|Ver. 2.0 or<br>later<br>~~es~~<br>~~i~~<br>~~**e**s~~|OK<br>~~es~~<br>~~es~~<br>~~se~~|OK<br>~~ee~~<br>~~es~~<br>~~se~~|OK<br>~~ee~~<br>~~es~~<br>~~ee~~|OK<br>~~ee~~<br>~~es~~<br>~~ee~~|OK<br>~~sf~~<br>~~es~~<br>~~es~~|OK<br>~~sf~~|OK|OK|OK|OK|
||ESC * r B<br>~~a ~~<br>~~a~~<br>~~es~~|Ver. 2.0 or<br>later<br>~~es ~~<br> ~~i~~<br>~~**e**s~~<br>~~e~~|OK<br> ~~es ~~<br>~~es~~<br>~~se~~<br>~~es~~|OK<br> ~~ee~~<br>~~es~~<br>~~se~~<br>~~ee~~|OK<br>~~ee~~<br>~~es~~<br>~~ee~~<br>~~ee~~|OK<br>~~ee ~~<br>~~es~~<br>~~ee~~<br>~~es~~|OK<br> ~~sf~~<br>~~es~~<br>~~es~~|OK<br>~~sf~~|OK|OK|OK|OK|
||ESC * r C<br> <br>~~a~~<br>~~es~~|Ver. 2.0 or<br>later<br> ~~i~~<br>~~**e**s~~<br>~~e~~|OK<br>~~es ~~<br>~~se~~<br>~~es~~|OK<br> ~~es~~<br>~~se~~<br>~~ee~~|OK<br>~~es~~<br>~~ee~~<br>~~ee~~|OK<br>~~es~~<br>~~ee~~<br>~~es~~|OK<br>~~es~~<br>~~es~~|OK|OK|OK|OK|OK|
||ESC * r D<br>~~es~~|Ver. 2.0 or<br>later<br>~~**e**s ~~<br>~~e ~~|OK<br> ~~se~~<br> ~~es ~~|OK<br>~~se~~<br> ~~ee~~|OK<br>~~ee~~<br>~~ee~~|OK<br>~~ee ~~<br>~~es~~|OK<br> ~~es~~|OK|OK|OK|OK|OK|
||ESC * r E<br>~~a~~|Spec. A<br>Ver. 2.0 or<br>later<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK|OK|OK|OK|
||ESC * r F<br>~~es~~|Spec. A<br>Ver. 2.0 or<br>later<br>~~es~~|OK<br>~~es~~|OK<br>~~es~~|OK<br>~~es~~|OK<br>~~ss~~|OK<br>~~ss~~|OK<br>~~es~~|OK|OK|OK|OK|
||ESC * r P<br>~~es~~<br>~~a~~|Ver. 2.0 or<br>later<br>~~es~~<br>~~i~~|OK<br>~~es~~<br>~~es~~|OK<br>~~es~~<br>~~es~~|OK<br>~~es~~<br>~~es~~|OK<br>~~ss~~<br>~~es~~|OK<br>~~ss~~<br>~~es~~|OK<br>~~es~~|OK|OK|OK|OK|
||ESC * r Q<br>~~es ~~<br>~~a~~<br>~~a~~|Ver. 2.0 or<br>later<br> ~~es~~<br>~~i~~<br>~~es~~|OK<br>~~es ~~<br>~~es~~<br>~~se~~|OK<br> ~~es~~<br>~~es~~<br>~~se~~|OK<br>~~es ~~<br>~~es~~<br>~~ee~~|OK<br> ~~ss~~<br>~~es~~<br>~~ee~~|OK<br>~~ss ~~<br>~~es~~<br>~~es~~|OK<br> ~~es~~|OK|OK|OK|OK|
||ESC * r m l<br>~~a ~~<br>~~a~~<br>~~es~~|Ver. 2.0 or<br>later<br> ~~i~~<br>~~es~~<br>~~ee~~|OK<br>~~es ~~<br>~~se~~<br>~~es~~|OK<br> ~~es~~<br>~~se~~<br>~~ee~~|OK<br>~~es~~<br>~~ee~~<br>~~ee~~|OK<br>~~es~~<br>~~ee~~<br>~~es~~|OK<br>~~es~~<br>~~es~~|OK|OK|OK|OK|OK|
||ESC * r m r<br>~~a~~<br>~~es~~<br>~~es~~|Ver. 2.0 or<br>later<br>~~es ~~<br>~~ee~~<br>~~es~~|OK<br> ~~se~~<br>~~es~~<br>~~es~~|OK<br>~~se~~<br>~~ee~~<br>~~es~~|OK<br>~~ee~~<br>~~ee~~<br>~~es~~|OK<br>~~ee ~~<br>~~es~~<br>~~ss~~|OK<br> ~~es~~<br>~~ss~~|OK<br>~~es~~|OK|OK|OK|OK|
||ESC * r T<br>~~es ~~<br>~~es~~<br>~~a~~|Ver. 2.0 or<br>later<br> ~~ee ~~<br>~~es~~<br>~~i~~|OK<br> ~~es ~~<br>~~es~~<br>~~es~~|OK<br> ~~ee~~<br>~~es~~<br>~~es~~|OK<br>~~ee~~<br>~~es~~<br>~~es~~|OK<br>~~es~~<br>~~ss~~<br>~~es~~|OK<br>~~ss~~<br>~~es~~|OK<br>~~es~~|OK|OK|OK|OK|
||ESC * r K<br>~~es ~~<br>~~a~~<br>~~a~~|Ver. 2.0 or<br>later<br> ~~es~~<br>~~i~~<br>~~es~~|OK<br>~~es ~~<br>~~es~~<br>~~se~~|OK<br> ~~es~~<br>~~es~~<br>~~se~~|OK<br>~~es ~~<br>~~es~~<br>~~ee~~|OK<br> ~~ss~~<br>~~es~~<br>~~ee~~|OK<br>~~ss ~~<br>~~es~~<br>~~es~~|OK<br> ~~es~~|OK|OK|OK|OK|
||b n1 n2 d1...dk<br>~~a ~~<br>~~a~~<br>~~es~~|Ver. 2.0 or<br>later<br> ~~i~~<br>~~es~~<br>~~ee~~|OK<br>~~es ~~<br>~~se~~<br>~~es~~|OK<br> ~~es~~<br>~~se~~<br>~~ee~~|OK<br>~~es~~<br>~~ee~~<br>~~ee~~|OK<br>~~es~~<br>~~ee~~<br>~~es~~|OK<br>~~es~~<br>~~es~~|OK|OK|OK|OK|OK|
||k n1 n2 d1...dk<br>~~a~~<br>~~es~~<br>~~es~~|Ver. 2.0 or<br>later<br>~~es ~~<br>~~ee~~<br>~~es~~|OK<br> ~~se~~<br>~~es~~<br>~~es~~|OK<br>~~se~~<br>~~ee~~<br>~~es~~|OK<br>~~ee~~<br>~~ee~~<br>~~es~~|OK<br>~~ee ~~<br>~~es~~<br>~~ss~~|OK<br> ~~es~~<br>~~ss~~|OK<br>~~es~~|OK|OK|OK|OK|
||ESC * r Y<br>~~es ~~<br>~~es~~<br>~~a~~|Ver. 2.0 or<br>later<br> ~~ee ~~<br>~~es~~<br>~~es~~|OK<br> ~~es ~~<br>~~es~~<br>~~es~~|OK<br> ~~ee~~<br>~~es~~|OK<br>~~ee~~<br>~~es~~|OK<br>~~es~~<br>~~ss~~|OK<br>~~ss~~|OK<br>~~es~~|OK|OK|OK|OK|
||ESC FF NUL<br>~~es ~~<br>~~a~~<br>~~a~~|Ver. 2.0 or<br>later<br> ~~es~~<br>~~es~~<br>~~es~~|OK<br>~~es ~~<br>~~es~~|OK<br> ~~es~~<br>~~ee~~|OK<br>~~es ~~<br>~~ee~~|OK<br> ~~ss~~<br>~~ee~~|OK<br>~~ss ~~<br>~~es~~|OK<br> ~~es~~|OK|OK|OK|OK|
||ESC FF EOT<br>~~a~~<br>~~a~~<br>~~es~~|Ver. 2.0 or<br>later<br>~~es ~~<br>~~es~~<br>~~ee~~|OK<br> ~~es~~<br>~~es~~|OK<br>~~ee~~<br>~~ee~~|OK<br>~~ee~~<br>~~ee~~|OK<br>~~ee~~<br>~~es~~|OK<br>~~es~~|OK|OK|OK|OK|OK|
||ESC * r N<br>~~a~~<br>~~es~~<br>~~es~~|NO<br>~~es~~<br>~~ee~~<br>~~es~~|NO<br>~~es~~<br>~~es~~|NO<br>~~ee~~<br>~~ee~~<br>~~es~~|NO<br>~~ee~~<br>~~ee~~<br>~~es~~|NO<br>~~ee ~~<br>~~es~~<br>~~ss~~|NO<br> ~~es~~<br>~~ss~~|Ver. 1.3 or<br>later<br>~~es~~|OK|OK|OK|OK|
||ESC * r V<br>~~es ~~<br>~~es~~|NO<br> ~~ee ~~<br>~~es~~|NO<br> ~~es ~~<br>~~es~~|NO<br> ~~ee~~<br>~~es~~|NO<br>~~ee~~<br>~~es~~|NO<br>~~es~~<br>~~ss~~|NO<br>~~ss~~|Ver. 1.3 or<br>later<br>~~es~~|OK|OK|OK|OK|
||ESC* re<br>~~es ~~<br>~~a~~|NO<br> ~~es~~|NO<br>~~es ~~<br>~~DC~~|NO<br> ~~es~~<br>~~DC~~|NO<br>~~es ~~<br>~~DC~~|NO<br> ~~ss~~<br>~~GC~~|NO<br>~~ss ~~<br>~~GC~~|NO<br> ~~es~~<br>~~GC~~|NO|NO|NO|OK|
||ESC * r S<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|OK<br>~~ee~~|
||ESC * r s 0<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|OK<br>~~ee~~|
||ESC* rs1<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO|NO|OK|
||ESC * r s 2<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee ~~|NO<br> ~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO|NO|OK|
||ESC * r s 3<br>~~PT~~|NO<br>~~PT~~|NO<br>~~PT~~|NO<br>~~PT~~|NO<br>~~PT~~|NO<br>~~PT~~|NO<br>~~PT~~|NO<br>~~PT~~|NO<br>~~PT~~|NO<br>~~PT~~|NO<br>~~PT~~|OK<br>~~PT~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-8 

• Black Mark Related Commands 

||• Black Mark Related Commands|
|---|---|
||**Class**<br>**Commands**<br>**Model Name**<br>~~Ce~~|
||**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**|
||Black Mark<br>ESC d<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>Related<br>FF<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>Commands<br>ESC C<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>ESC C 0<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>VT<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>ESC B<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>~~SSS~~<br>~~**P**o~~<br>~~o~~<br>~~Po~~<br>~~a~~<br>~~GG~~<br>~~GG~~<br>~~OO~~<br>~~Pe~~|
||• 2-Color PrintingRelated Commands|
|**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**<br>2-Color Printing ESC RS c<br>Ver. 4.0<br>Ver. 2.0<br>Ver. 2.0<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>~~Ce~~<br>~~Ce~~<br>~~uyeyaeao—_—_—_}_ IN~~||
||or later<br>or later<br>or later|
||Related<br>Commands<br>ESC RS C<br>Spec. A<br>Ver. 4.0<br>or later<br>Spec. A<br>Ver. 2.0<br>or later<br>Spec. A<br>Ver. 2.0<br>or later<br>Spec. B<br>Spec. B<br>Spec. B<br>Spec. A<br>Spec. A<br>Spec. C<br>Spec. C<br>Spec. C<br>ESC<br>4<br>(Not<br>Recommended)<br>Ver. 4.0<br>or later<br>Ver. 2.0<br>or later<br>Ver. 2.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>OK<br>NO<br>ESC<br>5<br>(Not<br>Recommended)<br>Ver. 4.0<br>or later<br>Ver. 2.0<br>or later<br>Ver. 2.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>OK<br>NO<br>ESC FS q<br>Ver. 4.0<br>or later<br>Ver. 2.0<br>or later<br>Ver. 2.0<br>or later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>ESC FS p<br>Ver. 4.0<br>or later<br>Ver. 2.0<br>or later<br>Ver. 2.0<br>or later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>~~ee~~<br>~~eeeee~~<br>~~is es ee es~~<br>~~es ee es ee es~~<br>~~es~~<br>~~ee~~<br>~~es ee es ee es~~<br>~~es se~~<br>~~ee~~<br>~~eseseeesse~~|



|• Presenter Related Commands|
|---|
|**Class**<br>**Commands**<br>**Model Name**|
|**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**|
|Presenter<br>ESC SYN0<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>Related<br>ESC SYN 1<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>Commands<br>ESC SYN 3<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>ESC SYN 4<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>ESC GS SUB DC1<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>ESC GS SUB DC2<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>ESC GS SUB DC3<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>~~a COG~~<br>~~GG~~<br>~~Po~~<br>~~Rs QQ GGG~~<br>~~GQ~~<br>~~QQ GG GG~~<br>~~Po~~<br>Q~~=SSS======——~~<br>~~Po~~|
|• Mark Commands|
|**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**<br>Mark<br>Commands<br>ESC GS * 0<br>NO<br>Ver. 4.0<br>or later<br>NO<br>Ver. 3.0<br>or later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>ESC GS * 1<br>NO<br>Ver. 4.0<br>or later<br>NO<br>Ver. 3.0<br>or later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>ESC GS * 2<br>NO<br>Ver. 4.0<br>or later<br>NO<br>Ver. 3.0<br>or later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>ESC GS * W<br>NO<br>Ver. 4.0<br>or later<br>NO<br>Ver. 3.0<br>or later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>ESC GS * C<br>NO<br>Ver. 4.0<br>or later<br>NO<br>Ver. 3.0<br>or later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>~~Ce~~<br>~~C—OOOOO~~<br>~~es ee es es~~<br>~~ee ee~~<br>~~ee i~~<br>~~ee es~~<br>~~ee ee~~<br>~~es es ee ss~~<br>~~se~~<br>~~es ee Qs~~<br>~~eseseeeseeee~~|



• Auto Logo Commands 

|**Class**<br>~~C—O~~|**Commands**<br>~~Ce~~<br>~~C—O~~<br>~~es~~|**Model Name**<br>~~Ce~~<br>~~C—OOO~~|**Model Name**<br>~~Ce~~<br>~~C—OOO~~|**Model Name**<br>~~Ce~~<br>~~C—OOO~~|**Model Name**<br>~~Ce~~<br>~~C—OOO~~|**Model Name**<br>~~Ce~~<br>~~C—OOO~~|**Model Name**<br>~~Ce~~<br>~~C—OOO~~|**Model Name**<br>~~Ce~~<br>~~C—OOO~~|**Model Name**<br>~~Ce~~<br>~~C—OOO~~|**Model Name**<br>~~Ce~~<br>~~C—OOO~~|**Model Name**<br>~~Ce~~<br>~~C—OOO~~|**Model Name**<br>~~Ce~~<br>~~C—OOO~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~Ce~~<br>~~C—O~~<br>~~es~~|**TSP700**<br>~~C—O~~<br>~~es~~|**TSP600**<br>~~C—O~~<br>~~ee~~|**TUP900**<br>~~C—O~~<br>~~ss~~|**TSP1000**<br>~~C—O~~<br>~~ss~~|**TSP828L**<br>~~C—O~~<br>~~ss~~|**TSP700II**<br>~~C—O~~<br>~~Gs~~|**TSP650**<br>~~OO~~<br>~~Gs~~|**TUP500**<br>~~OO~~|**TSP800II**<br>~~OO~~|**FVP10**<br>~~OO~~|
|Auto Logo<br>Commands ESC GS / C<br>~~C—O~~|ESC GS / W<br>~~C—O~~<br>~~es~~<br>~~is~~|NO<br>~~C—O~~<br>~~es~~<br>~~is~~|Ver. 4.0<br>or later<br>~~C—O~~<br>~~es~~<br>~~es~~|NO<br>~~C—O~~<br>~~ee~~<br>~~ee~~|NO<br>~~C—O~~<br>~~ss~~<br>~~es~~|NO<br>~~C—O~~<br>~~ss~~|NO<br>~~C—O~~<br>~~ss~~|OK<br>~~C—O ~~<br>~~Gs~~|OK<br> ~~OO~~<br>~~Gs~~|NO<br>~~OO~~|OK<br>~~OO~~|OK<br>~~OO~~|
||Commands ESC GS / C<br>~~es ~~<br>~~is~~<br>~~es~~|NO<br> ~~es ~~<br>~~is~~<br>~~ee~~|Ver. 4.0<br>or later<br> ~~es ~~<br>~~es~~<br>~~es~~|NO<br> ~~ee ~~<br>~~ee~~<br>~~ee~~|NO<br> ~~ss~~<br>~~es~~<br>~~es~~|NO<br>~~ss~~<br>~~es~~|NO<br>~~ss~~<br>~~ee~~|OK<br>~~Gs~~<br>~~ee~~|OK<br>~~Gs~~|NO|OK|OK|
||ESC GS / 1<br>~~is~~<br>~~es~~<br>~~es~~|NO<br>~~is ~~<br>~~ee~~<br>~~ee~~|Ver. 4.0<br>or later<br> ~~es ~~<br>~~es~~<br>~~es~~|NO<br> ~~ee ~~<br>~~ee~~<br>~~ee~~|NO<br> ~~es~~<br>~~es~~<br>~~es~~|NO<br>~~es~~<br>~~es~~|NO<br>~~ee~~<br>~~se~~|OK<br>~~ee~~<br>~~se~~|OK|NO|OK|OK|
||ESC GS / 2<br>~~es ~~<br>~~es~~<br>~~ee~~|NO<br> ~~ee ~~<br>~~ee~~<br>~~es~~|Ver. 4.0<br>or later<br> ~~es ~~<br>~~es~~<br>~~ee es~~|NO<br> ~~ee ~~<br>~~ee~~<br>~~es~~|NO<br> ~~es~~<br>~~es~~<br>~~es~~|NO<br>~~es~~<br>~~es~~|NO<br>~~ee~~<br>~~se~~|OK<br>~~ee~~<br>~~se~~|OK|NO|OK|OK|
||ESC GS / 3<br>~~es ~~<br>~~ee~~<br>~~is~~|NO<br> ~~ee ~~<br>~~es~~<br>~~is~~|Ver. 4.0<br>or later<br> ~~es ~~<br>~~ee es~~<br>~~es~~|NO<br> ~~ee ~~<br>~~es~~<br>~~ee~~|NO<br> ~~es~~<br>~~es~~<br>~~es~~|NO<br>~~es ~~|NO<br> ~~se~~|OK<br>~~se~~|OK|NO|OK|OK|
||ESC GS / 4<br>~~ee ~~<br>~~is~~<br>~~es~~|NO<br> ~~es ~~<br>~~is~~<br>~~ee~~|Ver. 4.0<br>or later<br> ~~ee es~~<br>~~es~~<br>~~es~~|NO<br>~~es~~<br>~~ee~~<br>~~ee~~|NO<br>~~es~~<br>~~es~~<br>~~es~~|NO<br>~~es~~|NO<br>~~ee~~|OK<br>~~ee~~|OK|NO|OK|OK|
||ESC GS / 5<br>~~is~~<br>~~es~~<br>~~es~~|NO<br>~~is ~~<br>~~ee~~<br>~~ee~~|Ver. 4.0<br>or later<br> ~~es ~~<br>~~es~~<br>~~es~~|NO<br> ~~ee ~~<br>~~ee~~<br>~~ee~~|NO<br> ~~es~~<br>~~es~~<br>~~es~~|NO<br>~~es~~<br>~~es~~|NO<br>~~ee~~<br>~~se~~|OK<br>~~ee~~<br>~~se~~|OK|NO|OK|OK|
||ESC GS / 6<br>~~es ~~<br>~~es~~|NO<br> ~~ee ~~<br>~~ee~~|Ver. 4.0<br>or later<br> ~~es ~~<br>~~es~~|NO<br> ~~ee ~~<br>~~ee~~|NO<br> ~~es~~<br>~~es~~|NO<br>~~es~~<br>~~es~~|NO<br>~~ee~~<br>~~se~~|OK<br>~~ee~~<br>~~se~~|OK|NO|OK|OK|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-9 

• PDF417 Commands 

|**Class**<br>~~ee~~|**Commands**<br>~~ee~~<br>~~ee~~|**Model Name**<br>~~ee~~|**Model Name**<br>~~ee~~|**Model Name**<br>~~ee~~|**Model Name**<br>~~ee~~|**Model Name**<br>~~ee~~|**Model Name**<br>~~ee~~|**Model Name**<br>~~ee~~|**Model Name**<br>~~ee~~|**Model Name**<br>~~ee~~|**Model Name**<br>~~ee~~|**Model Name**<br>~~ee~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~ee~~<br>~~Ge~~|**TSP700**<br>~~ee~~<br>~~Ge~~|**TSP600**<br>~~ee~~<br>~~Ge~~|**TUP900**<br>~~ee~~<br>~~GG~~|**TSP1000**<br>~~ee~~<br>~~GG~~|**TSP828L**<br>~~ee~~<br>~~eG~~|**TSP700II**<br>~~ee~~<br>~~eG~~|**TSP650**<br>~~ee~~<br>~~eG~~|**TUP500**<br>~~ee~~<br>~~eG~~|**TSP800II**<br>~~ee~~|**FVP10**<br>~~ee~~|
|PDF417<br>Commands ESC GS x S 1|ESC GS x S 0<br>~~ee~~<br>~~ee~~|NO<br>~~Ge~~<br>~~ee~~|NO<br>~~Ge~~<br>~~ee~~|NO<br>~~Ge~~<br>~~Ge~~|Ver. 3.1<br>or later<br>~~GG~~<br>~~GG~~|OK<br>~~GG~~<br>~~GG eG~~|OK<br>~~eG~~<br>~~eG~~|OK<br>~~eG~~<br>~~eG~~|NO<br>~~eG~~<br>~~eG~~|OK<br>~~eG~~<br>~~eG~~|OK<br>~~eG~~|OK<br>~~eG~~|
||Commands ESC GS x S 1<br>~~ee ~~<br>~~ee~~<br>~~ee~~|NO<br> ~~Ge~~<br>~~ee~~<br>~~ee~~|NO<br>~~Ge~~<br>~~ee~~<br>~~ee~~|NO<br>~~Ge~~<br>~~Ge~~<br>~~Ge~~|Ver. 3.1<br>or later<br>~~GG~~<br>~~GG~~<br>~~df~~|OK<br>~~GG ~~<br>~~GG eG~~<br>~~df~~|OK<br> ~~eG~~<br>~~eG~~<br>~~eG~~|OK<br>~~eG~~<br>~~eG~~<br>~~eG~~|NO<br>~~eG~~<br>~~eG~~<br>~~eG~~|OK<br>~~eG~~<br>~~eG~~<br>~~eG~~|OK<br>~~eG~~|OK<br>~~eG~~|
||ESC GS x S 2<br>~~ee ~~<br>~~ee~~<br>~~Rs~~|NO<br> ~~ee ~~<br>~~ee~~<br>~~re~~|NO<br> ~~ee~~<br>~~ee~~<br>~~ee~~|NO<br>~~Ge~~<br>~~Ge~~<br>~~Gs~~|Ver. 3.1<br>or later<br>~~GG~~<br>~~df~~<br>~~Ge~~|OK<br>~~GG eG~~<br>~~df~~<br>~~ee~~|OK<br>~~eG~~<br>~~eG~~<br>~~ee~~|OK<br>~~eG~~<br>~~eG~~<br>~~ee~~|NO<br>~~eG~~<br>~~eG~~<br>~~GG~~|OK<br>~~eG~~<br>~~eG~~<br>~~GG~~|OK<br>~~eG~~|OK<br>~~eG~~|
||ESC GS x S 3<br>~~ee~~<br>~~Rs~~<br>~~Re~~|NO<br>~~ee ~~<br>~~re~~<br>~~ee~~|NO<br> ~~ee~~<br>~~ee~~<br>~~ee~~|NO<br>~~Ge ~~<br>~~Gs~~<br>~~Gs~~|Ver. 3.1<br>or later<br> ~~df~~<br>~~Ge~~<br>~~Gee~~|OK<br>~~df ~~<br>~~ee~~<br>~~Gee~~|OK<br> ~~eG~~<br>~~ee~~|OK<br>~~eG~~<br>~~ee~~<br>~~GQ~~|NO<br>~~eG~~<br>~~GG~~<br>~~GQ~~|OK<br>~~eG~~<br>~~GG~~<br>~~GQ~~|OK|OK|
||ESC GS x D<br>~~Rs ~~<br>~~Re~~<br>~~ee~~|NO<br> ~~re~~<br>~~ee~~<br>~~ee~~|NO<br>~~ee~~<br>~~ee~~<br>~~ee~~|NO<br>~~Gs~~<br>~~Gs~~<br>~~Ge~~|Ver. 3.1<br>or later<br>~~Ge ~~<br>~~Gee~~<br>~~GG~~|OK<br> ~~ee~~<br>~~Gee~~<br>~~GG eG~~|OK<br>~~ee~~<br>~~eG~~|OK<br>~~ee~~<br>~~GQ~~<br>~~eG~~|NO<br>~~GG~~<br>~~GQ~~<br>~~eG~~|OK<br>~~GG~~<br>~~GQ~~<br>~~eG~~|OK<br>~~eG~~|OK<br>~~eG~~|
||ESC GS x P<br>~~Re ~~<br>~~ee~~|NO<br> ~~ee~~<br>~~ee~~|NO<br>~~ee~~<br>~~ee~~|NO<br>~~Gs~~<br>~~Ge~~<br>~~Ge~~|Ver. 3.1<br>or later<br>~~Gee~~<br>~~GG~~<br>~~dG~~|OK<br>~~Gee~~<br>~~GG eG~~<br>~~dG~~|OK<br>~~eG~~|OK<br>~~GQ~~<br>~~eG~~|NO<br>~~GQ~~<br>~~eG~~|OK<br>~~GQ~~<br>~~eG~~|OK<br>~~eG~~|OK<br>~~eG~~|
||ESC GS x I<br>~~ee ~~<br>~~Ge~~|NO<br> ~~ee ~~<br>~~Ge~~|NO<br> ~~ee~~<br>~~Ge~~|NO<br>~~Ge~~<br>~~Ge~~<br>~~Ge~~|Ver. 3.1<br>or later<br>~~GG~~<br>~~Ge~~<br>~~dG~~|OK<br>~~GG eG~~<br>~~Ge~~<br>~~dG~~|OK<br>~~eG~~<br>~~Ge~~|OK<br>~~eG~~<br>~~Ge~~|NO<br>~~eG~~<br>~~Ge~~|OK<br>~~eG~~<br>~~Ge~~|OK<br>~~eG~~<br>~~Ge~~|OK<br>~~eG~~<br>~~Ge~~|



## • Print Start Trigger Control Commands 

|**Class**|**Commands**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**|**TSP700**|**TSP600**|**TUP900**|**TSP1000**|**TSP828L**|**TSP700II**|**TSP650**|**TUP500**|**TSP800II**|**FVP10**|
|Print Start<br>Trigger<br>Control|ESC GS g 0|NO|NO|NO|NO|Ver. 1.1<br>or later|OK|OK|OK|OK|OK|OK|
||ESC GS g 1|NO|NO|NO|NO|Ver. 1.1<br>or later|OK|OK|OK|OK|OK|OK|



|**Class**<br>~~eR~~|**Commands**<br>~~eR~~<br>~~ee~~|**Model Name**<br>~~eR~~|**Model Name**<br>~~eR~~|**Model Name**<br>~~eR~~|**Model Name**<br>~~eR~~|**Model Name**<br>~~eR~~|**Model Name**<br>~~eR~~|**Model Name**<br>~~eR~~|**Model Name**<br>~~eR~~|**Model Name**<br>~~eR~~|**Model Name**<br>~~eR~~|**Model Name**<br>~~eR~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~eR~~<br>~~ee~~|**TSP700**<br>~~eR~~<br>~~Ge~~|**TSP600**<br>~~eR~~<br>~~Ge~~|**TUP900**<br>~~eR~~<br>~~dG~~|**TSP1000**<br>~~eR~~<br>~~dG eG~~|**TSP828L**<br>~~eR~~<br>~~eG~~|**TSP700II**<br>~~eR~~<br>~~eG~~|**TSP650**<br>~~eR~~<br>~~eG~~|**TUP500**<br>~~eR~~<br>~~eG~~|**TSP800II**<br>~~eR~~<br>~~eG~~|**FVP10**<br>~~eR~~<br>~~eG~~|
|QR Code|ESC GS y S 0<br>~~ee~~<br>~~ee~~|NO<br>~~ee~~<br>~~ee~~|NO<br>~~Ge~~<br>~~ee~~|NO<br>~~Ge~~<br>~~Ge~~|NO<br>~~dG~~<br>~~dG~~|Ver. 1.2<br>or later<br>~~dG eG~~<br>~~dG~~|OK<br>~~eG~~<br>~~eG~~|OK<br>~~eG~~<br>~~eG~~|NO<br>~~eG~~<br>~~eG~~|OK<br>~~eG~~<br>~~eG~~|OK<br>~~eG~~|OK<br>~~eG~~|
||ESC GS y S 1<br>~~ee~~<br>~~ee~~<br>~~ee~~|NO<br>~~ee~~<br>~~ee~~<br>~~ee~~|NO<br>~~Ge~~<br>~~ee~~<br>~~ee~~|NO<br>~~Ge ~~<br>~~Ge~~<br>~~Gs~~|NO<br> ~~dG~~<br>~~dG~~<br>~~Ge~~|Ver. 1.2<br>or later<br>~~dG eG~~<br>~~dG~~<br>~~Ge~~|OK<br>~~eG~~<br>~~eG~~<br>~~Ge~~|OK<br>~~eG~~<br>~~eG~~|NO<br>~~eG~~<br>~~eG~~<br>~~eG~~|OK<br>~~eG~~<br>~~eG~~<br>~~eG~~|OK<br>~~eG~~|OK<br>~~eG~~|
||ESC GS y S 2<br>~~ee ~~<br>~~ee~~<br>~~Rs~~|NO<br> ~~ee~~<br>~~ee~~<br>~~re~~|NO<br>~~ee~~<br>~~ee~~<br>~~ee~~|NO<br>~~Ge ~~<br>~~Gs~~<br>~~Gs~~|NO<br> ~~dG~~<br>~~Ge~~<br>~~Ge~~|Ver. 1.2<br>or later<br>~~dG ~~<br>~~Ge~~<br>~~ee~~|OK<br> ~~eG~~<br>~~Ge~~<br>~~ee~~|OK<br>~~eG~~<br>~~ee~~|NO<br>~~eG~~<br>~~eG~~<br>~~GG~~|OK<br>~~eG~~<br>~~eG~~<br>~~GG~~|OK|OK|
||ESC GS y D 1<br>~~ee ~~<br>~~Rs~~<br>~~Re~~|NO<br> ~~ee~~<br>~~re~~<br>~~ee~~|NO<br>~~ee~~<br>~~ee~~<br>~~ee~~|NO<br>~~Gs ~~<br>~~Gs~~<br>~~Gs~~|NO<br> ~~Ge~~<br>~~Ge~~<br>~~Gee~~|Ver. 1.2<br>or later<br>~~Ge~~<br>~~ee~~<br>~~Gee~~|OK<br>~~Ge~~<br>~~ee~~|OK<br>~~ee~~<br>~~GQ~~|NO<br>~~eG~~<br>~~GG~~<br>~~GQ~~|OK<br>~~eG~~<br>~~GG~~<br>~~GQ~~|OK|OK|
||ESC GS y D 2<br>~~Rs ~~<br>~~Re~~<br>~~ee~~|NO<br> ~~re~~<br>~~ee~~<br>~~ee~~|NO<br>~~ee~~<br>~~ee~~<br>~~ee~~|NO<br>~~Gs~~<br>~~Gs~~<br>~~Gs~~|NO<br>~~Ge ~~<br>~~Gee~~<br>~~dQ~~|Ver. 1.2<br>or later<br> ~~ee~~<br>~~Gee~~<br>~~dQ~~|OK<br>~~ee~~<br>~~ee~~|OK<br>~~ee~~<br>~~GQ~~<br>~~ee~~|NO<br>~~GG~~<br>~~GQ~~<br>~~eG~~|OK<br>~~GG~~<br>~~GQ~~<br>~~eG~~|OK|OK|
||ESC GS y P<br>~~Re ~~<br>~~ee~~|NO<br> ~~ee~~<br>~~ee~~|NO<br>~~ee~~<br>~~ee~~|NO<br>~~Gs~~<br>~~Gs~~<br>~~Ge~~|NO<br>~~Gee~~<br>~~dQ~~<br>~~ed~~|Ver. 1.2<br>or later<br>~~Gee~~<br>~~dQ~~<br>~~ed~~|OK<br>~~ee~~<br>~~ee~~|OK<br>~~GQ~~<br>~~ee~~<br>~~ee~~|NO<br>~~GQ~~<br>~~eG~~|OK<br>~~GQ~~<br>~~eG~~|OK|OK|
||ESC GS y I<br>~~ee~~<br>~~ee~~|NO<br>~~ee ~~<br>~~ee~~|NO<br> ~~ee~~<br>~~ee~~|NO<br>~~Gs ~~<br>~~ee~~<br>~~Ge~~|NO<br> ~~dQ~~<br>~~ee~~<br>~~ed~~|Ver. 1.2<br>or later<br>~~dQ ~~<br>~~ee~~<br>~~ed~~|OK<br> ~~ee~~<br>~~ee~~<br>~~ee~~|OK<br>~~ee~~<br>~~ee~~<br>~~ee~~|NO<br>~~eG~~<br>~~ee~~|OK<br>~~eG~~<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|



## • Reduced Printing Function Commands 

|**Class**<br>~~-~~|**Commands**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**|**TSP700**|**TSP600**|**TUP900**|**TSP1000**<br>~~GO~~|**TSP828L**<br>~~GO~~|**TSP700II**<br>~~GO~~|**TSP650**<br>~~(OO~~|**TUP500**<br>~~(OO~~|**TSP800II**<br>~~(OO~~|**FVP10**|
|Page Mode<br>~~-~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~Po~~|ESC GS P 0<br>~~GO~~|No<br>~~GO~~|No<br>~~GO~~|No<br>~~GO~~|No<br>~~GO~~|No<br>~~GO~~<br>~~GO~~|No<br>~~GO~~<br>~~GO~~|No<br>~~GO~~<br>~~GO~~|No<br>~~GO~~<br>~~(OO~~|No<br>~~GO~~<br>~~(OO~~|No<br>~~GO~~<br>~~(OO~~|Yes<br>~~GO~~|
||ESC GS P 1<br>~~po~~|No|No|No|No|No<br>~~GO~~|No<br>~~GO~~|No<br>~~GO~~|No<br>~~(OO~~|No<br>~~(OO~~|No<br>~~(OO~~|Yes|
||ESC GS P 2<br>~~po~~<br>~~po~~|No|No|No|No|No<br>~~GO~~<br>~~(OO~~|No<br>~~GO~~<br>~~(OO~~|No<br>~~GO~~<br>~~(OO~~|No<br>~~(OO~~<br>~~(OO~~|No<br>~~(OO~~<br>~~(OO~~|No<br>~~(OO~~<br>~~(OO~~|Yes|
||ESC GS P 3<br>~~po~~<br>~~GO~~<br>~~po~~|No<br>~~GO~~|No<br>~~GO~~|No<br>~~GO~~|No<br>~~GO~~|No<br>~~GO~~<br>~~GO~~<br>~~(OO~~|No<br>~~GO~~<br>~~GO~~<br>~~(OO~~|No<br>~~GO~~<br>~~GO~~<br>~~(OO~~|No<br>~~(OO~~<br>~~GO~~<br>~~(OO~~|No<br>~~(OO~~<br>~~GO~~<br>~~(OO~~|No<br>~~(OO~~<br>~~GO~~<br>~~(OO~~|Yes<br>~~GO~~|
||ESC GS P 4<br>~~po~~<br>~~po~~|No|No|No|No|No<br>~~GO~~<br>~~(OO~~|No<br>~~GO~~<br>~~(OO~~|No<br>~~GO~~<br>~~(OO~~|No<br>~~(OO~~<br>~~(OO~~|No<br>~~(OO~~<br>~~(OO~~|No<br>~~(OO~~<br>~~(OO~~|Yes|
||ESC GS P 5<br>~~po~~<br>~~po~~<br>~~po~~|No|No|No|No|No<br>~~GO~~<br>~~(OO~~|No<br>~~GO~~<br>~~(OO~~|No<br>~~GO~~<br>~~(OO~~|No<br>~~(OO~~<br>~~(OO~~|No<br>~~(OO~~<br>~~(OO~~|No<br>~~(OO~~<br>~~(OO~~|Yes|
||ESC GS P 6<br>~~po~~<br>~~po~~<br>~~po~~|No|No|No|No|No<br>~~GO~~|No<br>~~GO~~|No<br>~~GO~~|No<br>~~(OO~~|No<br>~~(OO~~|No<br>~~(OO~~|Yes|
||ESC GS P 7<br>~~po~~<br>~~po~~<br>~~Po~~|No|No|No|No|No<br>~~GO~~|No<br>~~GO~~|No<br>~~GO~~|No<br>~~(OO~~|No<br>~~(OO~~|No<br>~~(OO~~|Yes|
||ESC GS P 8<br>~~po~~<br>~~Po~~|No|No|No|No|No<br>~~GO~~|No<br>~~GO~~|No<br>~~GO~~|No<br>~~(OO~~|No<br>~~(OO~~|No<br>~~(OO~~|Yes|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-10 

|• Text Search Commands|
|---|
|**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP800II**<br>**FVP10**<br>Text Search<br>ESC GS)B(fn = 48)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS)B(fn = 49)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS)B(fn = 50)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS)B(fn = 64)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS)B(fn = 65)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS)B(fn = 80)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS)B(fn = 81)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS)B(fn = 96)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS)B(fn = 97)<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>• Audio Commands<br>**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP800II**<br>**FVP10**<br>Audio<br>ESC GS s O<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS s P<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS s R<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS s I<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS s U<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>ESC GS s T<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>No<br>Yes<br>~~Ce~~<br>~~eee~~<br>~~Po~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~GO~~<br>~~(OO~~<br>~~(OO~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~Po Ce~~<br>~~a~~<br>~~(~~<br>~~Ww~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~GO~~<br>~~GO~~<br>~~(OO~~<br>~~po~~<br>~~Poff~~|



- In USB printer class, the status request command is ignored for the following models. 

- TSP800, TSP700, TSP600, TUP900, TSP1000, TSP828L, TSP700II, TSP650 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-11 

## **6.3. USB I/F (Ver1.0)  • Ethernet I/F (Silex Ver1.0)** 

|**Class**<br>~~es~~<br>~~Po~~|**Commands**<br>~~es~~<br>~~Po~~|**Model Name**<br>~~PO~~<br>~~esreeeeeee~~<br>~~eeee~~|**Model Name**<br>~~PO~~<br>~~esreeeeeee~~<br>~~eeee~~|**Model Name**<br>~~PO~~<br>~~esreeeeeee~~<br>~~eeee~~|**Model Name**<br>~~PO~~<br>~~esreeeeeee~~<br>~~eeee~~|**Model Name**<br>~~PO~~<br>~~esreeeeeee~~<br>~~eeee~~|**Model Name**<br>~~PO~~<br>~~esreeeeeee~~<br>~~eeee~~|**Model Name**<br>~~PO~~<br>~~esreeeeeee~~<br>~~eeee~~|**Model Name**<br>~~PO~~<br>~~esreeeeeee~~<br>~~eeee~~|**Model Name**<br>~~PO~~<br>~~esreeeeeee~~<br>~~eeee~~|**Model Name**<br>~~PO~~<br>~~esreeeeeee~~<br>~~eeee~~|**Model Name**<br>~~PO~~<br>~~esreeeeeee~~<br>~~eeee~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~PO~~<br>~~es~~|**TSP700**<br>~~PO~~<br>~~re~~|**TSP600**<br>~~PO~~<br>~~ee~~|**TUP900**<br>~~PO~~<br>~~ee~~|**TSP1000**<br>~~PO~~<br>~~ee~~|**TSP828L**<br>~~PO~~<br>~~ee~~|**TSP700II**<br>~~PO~~<br>~~ee~~|**TSP650**<br>~~PO~~<br>~~ee~~|**TUP500**<br>~~PO~~|**TSP800II**<br>~~PO~~|**FVP10**<br>~~PO~~|
|Font Style<br>and<br>Character<br>Set<br>~~es~~<br>~~Po~~<br>~~—~~<br>~~po~~<br>~~**p**~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~Po~~|ESC RS F<br>~~es~~<br>~~Po~~|NO<br>~~es ~~|NO<br> ~~re ~~|NO<br> ~~ee ~~|NO<br> ~~ee ~~|NO<br> ~~ee~~|NO<br>~~ee ~~|NO<br> ~~ee~~|NO<br>~~ee~~|NO|NO|NO|
||ESC GS t<br>~~Po~~<br>~~—~~<br>~~|~~|OK<br>~~|~~|OK<br>~~|~~|OK<br>~~tp~~|OK<br>~~tp~~|NO<br>~~tpfp~~|NO<br>~~fp~~<br>~~|~~|NO<br>~~ft~~|NO<br>~~ft~~|NO|NO|NO|
||ESC GS =<br>~~—~~<br>~~|~~<br>~~po~~|Ver. 3.0 or<br>later<br>(*)<br>~~|~~|Ver. 3.0 or<br>Spec. A<br>(*)<br>~~|~~|Spec. A<br>(*)<br>~~tp~~|Spec. A<br>(*)<br>~~tp~~|NO<br>~~tpfp~~|NO<br>~~fp~~<br>~~|~~|NO<br>~~ft~~|NO<br>~~ft~~|NO|NO|NO|
||ESCR<br>~~—~~<br>~~|~~<br>~~po~~<br>~~**p**o~~|OK<br>~~|~~|OK<br>~~|~~|OK<br>~~tp~~|OK<br>~~tp~~|NO<br>~~tpfp~~|NO<br>~~fp~~<br>~~|~~|NO<br>~~ft~~|NO<br>~~ft~~|NO|NO|NO|
||ESC /<br>~~—~~<br>~~|~~<br>~~po~~<br>~~**p**o~~|OK<br>~~|~~|OK<br>~~|~~|OK<br>~~tp~~|OK<br>~~tp~~|NO<br>~~tp fp~~|NO<br>~~fp~~<br>~~|~~|NO<br>~~ft~~|NO<br>~~ft~~|NO|NO|NO|
||ESC SP<br>~~**p**o~~<br>~~po~~|OK|OK|OK|OK|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ESCM<br>~~po~~<br>~~po~~|OK|OK|OK|OK|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ESC P<br>~~po~~<br>~~po~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||ESC :<br>~~po~~<br>~~po~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||ESC<br>p<br>(Not<br>recommended)<br>~~po~~<br>~~po~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||ESC g<br>~~po~~<br>~~po~~<br>~~Po~~|Spec. A|Spec. A|Spec. A|Spec. B|NO|NO|NO|NO|NO|NO|NO|
|Character<br>expansion<br>settings<br>~~po~~<br>~~Po~~<br>~~**p**~~<br>~~**p**~~<br>~~po~~<br>~~Po~~|ESC i<br>~~po~~<br>~~Po~~<br>~~**p**o~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||ESC W<br>~~Po~~<br>~~**p**o~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||ESCh<br>~~**p**o~~|OK|OK|OK|OK|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||SO<br>~~po~~<br>~~**p**o~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|
||DC4<br>~~po~~<br>~~**p**o~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|
||ESC SO<br>~~**p**o~~<br>~~po~~|OK|OK|OK|OK|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ESC DC4<br>~~po~~<br>~~Po~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
|Print Mode<br>~~po~~<br>~~Po~~<br>~~po~~<br>~~**p**~~<br>~~**p**~~<br>~~po~~<br>~~po~~|ESC E<br>~~po~~<br>~~Po~~<br>~~po~~|Spec. A|Spec. A|Spec. A|Spec. A|NO|NO|NO|NO|NO|NO|NO|
||ESCF<br>~~Po~~<br>~~po~~<br>~~**p**o~~|Spec. A|Spec. A|Spec. A|Spec. A|NO|NO|NO|NO|NO|NO|NO|
||ESC -<br>~~po~~<br>~~**p**o~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||ESC_<br>~~**p**o~~<br>~~**p**o~~|OK<br>~~o~~|OK|OK|OK|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ESC4<br>~~**p**o~~|OK<br>~~o~~|OK|OK|OK|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ESC 5<br>~~**p**o~~<br>~~po~~|OK<br>~~o~~|OK|OK|OK|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||SI<br>~~po~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||DC2<br>~~po~~<br>~~Po~~<br>~~po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|
|Line spacing LF<br>~~po~~<br>~~**p**~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~po~~|Line spacing LF<br>~~po~~<br>~~**p**o~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||CR<br>~~po~~<br>~~**p**o~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||ESC a<br>~~**p**o~~<br>~~po~~|OK|OK|OK|OK|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ESC z<br>~~po~~<br>~~po~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||ESC 0<br>~~po~~<br>~~po~~<br>~~po~~|OK<br>|OK<br>|OK<br>|OK<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|
||ESC J<br>~~po~~<br>~~po~~|OK<br>|OK<br>|OK<br>|OK<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|
||ESC I<br>~~poPo~~<br>~~po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|
|Page Control FF<br>~~po~~<br>~~**p**~~<br>~~po~~<br>~~Po~~<br>~~po~~|Page Control FF<br>~~po~~<br>~~**p**o~~|OK<br>~~o~~|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||ESC C<br>~~po~~<br>~~**p**o~~|OK<br>~~o~~|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||ESC C 0<br>~~**p**o~~<br>~~po~~|OK<br>~~o~~|OK|OK|OK|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||VT<br>~~po~~<br>~~Po~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||ESCB<br>~~po~~<br>~~Po~~<br>~~po~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
|Horizontal<br>direction<br>position<br>~~Po~~<br>~~po~~<br>~~**p**~~<br>~~po~~<br>~~po~~<br>~~po~~|ESC l<br>~~Po~~<br>~~po~~<br>~~**p**o~~|Spec. A|Spec. A|Spec. A|Spec. B|NO|NO|NO|NO|NO|NO|NO|
||ESCQ<br>~~po~~<br>~~**p**o~~|Spec. A|Spec. A|Spec. A|Spec. B|NO|NO|NO|NO|NO|NO|NO|
||HT<br>~~**p**o~~<br>~~po~~|OK|OK|OK|OK|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ESC D<br>~~po~~<br>~~po~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||ESC GS A<br>~~po~~<br>~~po~~<br>~~po~~|OK<br>|OK<br>|OK<br>|OK<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|
||ESC GSR<br>~~po~~<br>~~po~~|OK<br>|OK<br>|OK<br>|OK<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|
||ESC GS a<br>~~poPo~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|
|Download<br>~~ee~~<br>~~po~~<br>~~Po~~|ESC&<br>~~ee~~<br>~~po~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|
||ESC %<br>~~ee~~<br>~~po~~<br>~~Po~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|
|Bit Image<br>Graphics<br>~~po~~<br>~~Po~~<br>~~**p**~~<br>~~Po~~<br>~~Po~~|ESC K<br>~~po~~<br>~~Po~~<br>~~**p**o~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||ESC L<br>~~Po~~<br>~~**p**o~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||ESCk<br>~~**p**o~~<br>~~Po~~|OK|OK|OK|OK|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ESC X<br>~~Po~~<br>~~Po~~|OK<br>|OK<br>|OK<br>|OK<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|
|Logo<br>~~Po~~<br>~~Po~~<br>~~po~~|ESC FSq<br>~~Po~~<br>~~Po~~|OK<br>|OK<br>|OK(*)<br>|OK(*)<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|NO<br>|
||ESCFS p<br>~~Popo~~<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|
||ESC RS L<br>~~po~~|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|
|Bar Codes<br>~~po~~<br>~~PO~~|ESC b<br>~~po~~<br>~~PO~~|Spec. A<br>~~PO~~|Spec. A<br>~~PO~~|Spec. A<br>~~PO~~|Spec. B<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|
|Cutter<br>Control|ESC d|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-12 

|**Class**<br>~~By~~<br>~~**p**~~|**Commands**<br>~~By~~<br>~~**p**C~~|**Model Name**<br>~~PT~~<br>~~Byeeeee~~<br>~~—~~|**Model Name**<br>~~PT~~<br>~~Byeeeee~~<br>~~—~~|**Model Name**<br>~~PT~~<br>~~Byeeeee~~<br>~~—~~|**Model Name**<br>~~PT~~<br>~~Byeeeee~~<br>~~—~~|**Model Name**<br>~~PT~~<br>~~Byeeeee~~<br>~~—~~|**Model Name**<br>~~PT~~<br>~~Byeeeee~~<br>~~—~~|**Model Name**<br>~~PT~~<br>~~Byeeeee~~<br>~~—~~|**Model Name**<br>~~PT~~<br>~~Byeeeee~~<br>~~—~~|**Model Name**<br>~~PT~~<br>~~Byeeeee~~<br>~~—~~|**Model Name**<br>~~PT~~<br>~~Byeeeee~~<br>~~—~~|**Model Name**<br>~~PT~~<br>~~Byeeeee~~<br>~~—~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~PT~~<br>~~By~~|**TSP700**<br>~~PT~~<br>~~By~~|**TSP600**<br>~~PT~~<br>~~Byeee~~|**TUP900**<br>~~PT~~<br>~~eee~~|**TSP1000**<br>~~PT~~<br>~~eee~~|**TSP828L**<br>~~PT~~<br>~~eee~~|**TSP700II**<br>~~PT~~<br>~~eeeee~~|**TSP650**<br>~~PT~~<br>~~ee~~|**TUP500**<br>~~PT~~<br>~~—~~|**TSP800II**<br>~~PT~~|**FVP10**<br>~~PT~~|
|External<br>Device Drive<br>~~By~~<br>~~**p**~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~**p**~~<br>~~SE~~|ESC BEL<br>~~By~~<br>~~**p**C~~|OK<br>~~By~~|OK<br>~~By~~|OK<br>~~By eee~~|NO<br>~~eee~~|NO<br>~~eee~~|NO<br>~~eee~~|NO<br>~~eee ee~~|NO<br>~~ee~~|NO<br>~~—~~|NO|NO|
||BEL<br>~~**p**C~~<br>~~po~~|OK|OK|OK|NO|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||FS<br>~~po~~<br>~~po~~|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|NO|
||SUB<br>~~po~~<br>~~po~~<br>~~po~~|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|NO|
||EM<br>~~po~~<br>~~po~~<br>~~Rs~~|OK<br>~~ee~~|OK<br>~~es eeGe~~|OK<br>~~eeGe~~|NO<br>~~eeGe~~|NO<br>~~ee~~|NO<br>~~ee~~|NO|NO|NO|NO|NO|
||ESC GS BEL<br>~~po~~<br>~~Rs~~<br>~~**p**o~~|NO<br>~~ee~~|Ver. 5.0<br>or later<br>~~es eeGe~~|NO<br>~~eeGe~~|NO<br>~~eeGe~~|NO<br>~~ee~~|NO<br>~~ee~~|NO|NO|NO|NO|NO|
||ESC GS EM DC1<br>~~Rs ~~<br>~~**p**o~~|NO<br> ~~ee ~~|NO<br> ~~es eeGe~~|NO<br>~~eeGe~~|NO<br>~~eeGe ~~|NO<br> ~~ee~~|NO<br>~~ee~~|NO|NO|NO|NO|NO|
||ESC GS EM DC2<br>~~**p**o~~<br>~~E~~|NO|NO|NO|NO|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
|Print Setting EM<br>~~SEpo~~|Print Setting EM<br>~~E~~|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|NO|
||ESC RS r<br>~~Epo~~|Spec. A|Spec. A|Spec. A|Spec. A|NO|NO|NO|NO|NO|NO|NO|
|Status<br>~~SEpo~~<br>~~po~~<br>~~po~~<br>~~**p**~~<br>~~**p**~~|ESC RS a<br>~~Epo~~<br>~~po~~|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|
||ESCACKSOH<br>~~po~~<br>~~po~~<br>~~po~~|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|
||ENQ<br>~~po~~<br>~~po~~<br>~~**p**o~~|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|
||EOT<br>~~po~~<br>~~**p**o~~|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|
||ESCACKCAN<br>~~**p**o~~|NO|NO|NO|NO|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ETB<br>~~po~~|Spec. A<br>~~po~~|Spec. A<br>~~po~~|Spec. A<br>~~po~~|Spec. B<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|
||ESC RS E<br>~~po~~<br>~~Po~~<br>~~**p**C~~|OK<br>~~po~~<br>~~Po~~|OK<br>~~po~~<br>~~Po~~|OK<br>~~po~~<br>~~Po~~|OK<br>~~po~~<br>~~Po~~|NO<br>~~po~~<br>~~Po~~|NO<br>~~po~~<br>~~Po~~|NO<br>~~po~~<br>~~Po~~|NO<br>~~po~~<br>~~Po~~|NO<br>~~po~~<br>~~Po~~|NO<br>~~po~~<br>~~Po~~|NO<br>~~po~~<br>~~Po~~|
|Kanji<br>character<br>~~**p**~~<br>~~**p**~~<br>~~po~~<br>~~Po~~|ESC p<br>~~**p**C~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||ESC q<br>~~**p**C~~|OK|OK|OK|OK|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ESC$ ~~po~~<br>~~**p**o~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|
||ESC s<br>~~po~~<br>~~**p**o~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|NO<br>~~po~~|
||ESC t<br>~~**p**o~~<br>~~po~~|OK|OK|OK|OK|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ESC r<br>~~po~~<br>~~Po~~|Spec. A|Spec. A|Spec. A|Spec. B|NO|NO|NO|NO|NO|NO|NO|
|Others<br>~~po~~<br>~~Po~~<br>~~po~~<br>~~Po~~|CAN<br>~~po~~<br>~~Po~~<br>~~po~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||ESC @<br>~~Po~~<br>~~po~~|OK|OK|OK|OK|NO|NO|NO|NO|NO|NO|NO|
||ESC GS # m<br>~~po~~<br>~~Po~~|Spec. A<br>(*)<br>Ver. 3.0 or<br>later|Ver. 3.0 or<br>Spec. A<br>(*)|Spec. A<br>(*)|Spec. B<br>(*)|NO|NO|NO|NO|NO|NO|NO|
||ESC ?<br>~~Po~~|OK(*)|OK(*)|OK(*)|OK(*)|NO|NO|NO|NO|NO|NO|NO|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-13 

• Raster Related Commands 

|**Class**<br>~~a~~<br>~~PCT~~|**Commands**<br>~~PCT~~<br>~~i~~|**Model Name**<br>~~Cn~~<br>~~eae~~<br>~~&~~<br>~~PCT~~|**Model Name**<br>~~Cn~~<br>~~eae~~<br>~~&~~<br>~~PCT~~|**Model Name**<br>~~Cn~~<br>~~eae~~<br>~~&~~<br>~~PCT~~|**Model Name**<br>~~Cn~~<br>~~eae~~<br>~~&~~<br>~~PCT~~|**Model Name**<br>~~Cn~~<br>~~eae~~<br>~~&~~<br>~~PCT~~|**Model Name**<br>~~Cn~~<br>~~eae~~<br>~~&~~<br>~~PCT~~|**Model Name**<br>~~Cn~~<br>~~eae~~<br>~~&~~<br>~~PCT~~|**Model Name**<br>~~Cn~~<br>~~eae~~<br>~~&~~<br>~~PCT~~|**Model Name**<br>~~Cn~~<br>~~eae~~<br>~~&~~<br>~~PCT~~|**Model Name**<br>~~Cn~~<br>~~eae~~<br>~~&~~<br>~~PCT~~|**Model Name**<br>~~Cn~~<br>~~eae~~<br>~~&~~<br>~~PCT~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~Cn~~<br>~~PCTCT~~<br>|**TSP700**<br>~~Cn~~<br>~~CT |~~<br>|**TSP600**<br>~~Cn~~<br>~~|~~<br>|**TUP900**<br>~~Cn~~<br>~~eae~~<br>~~|~~<br>|**TSP1000**<br>~~Cn~~<br>~~eae~~<br>|**TSP828L**<br>~~Cn~~<br>~~eae~~<br>|**TSP700II**<br>~~Cn~~<br>~~eae~~<br>|**TSP650**<br>~~Cn~~<br>~~eae~~<br>|**TUP500**<br>~~Cn~~|**TSP800II**<br>~~Cn~~|**FVP10**<br>~~Cn~~<br>~~&~~|
|Raster<br>~~PCT~~<br>~~Po~~<br>~~Po~~<br>~~po~~<br>~~Po~~<br>~~po~~<br>~~Po~~|ESC * r R<br>~~PCT~~<br>~~i~~<br>~~ee~~|Ver. 2.0<br>or later<br>~~PCTCT~~<br>~~se~~<br>|OK<br>~~CT |~~<br>~~se~~<br>|OK<br>~~|~~<br>~~es~~<br>|OK<br>~~eae~~<br>~~|~~<br>~~eG~~<br>|NO<br>~~eae~~<br>~~eG~~<br>|NO<br>~~eae~~<br>~~GG~~<br>|NO<br>~~eae~~<br>~~GG~~<br>|NO<br>~~eae~~<br>~~GG~~<br>|NO|NO|NO<br>~~&~~|
||ESC * r A<br>~~PCT~~<br>~~i~~<br>~~ee~~<br>~~es~~|Ver. 2.0<br>or later<br>~~PCT CT~~<br>~~se~~<br>~~**e**s~~|OK<br>~~CT |~~<br>~~se~~<br>~~ee~~|OK<br>~~|~~<br>~~es~~<br>~~ee~~|OK<br>~~eae~~<br>~~|~~<br>~~eG~~<br>~~eG~~|NO<br>~~eae~~<br>~~eG~~<br>~~eG~~|NO<br>~~eae~~<br>~~GG~~<br>~~GG~~|NO<br>~~eae~~<br>~~GG~~<br>~~GG~~|NO<br>~~eae~~<br>~~GG~~<br>~~GG~~|NO|NO|NO<br>~~&~~|
||ESC * r B<br><br>~~i ~~<br>~~ee~~<br>~~es~~|Ver. 2.0<br>or later<br> ~~CT~~<br> ~~se~~<br>~~**e**s~~|OK<br>~~CT |~~<br>~~se~~<br>~~ee~~<br>~~e~~|OK<br>~~|~~<br>~~es~~<br>~~ee~~<br>~~es~~|OK<br>~~|~~<br>~~eG~~<br>~~eG~~<br>~~es~~|NO<br>~~eG~~<br>~~eG~~<br>~~Qe~~|NO<br>~~GG~~<br>~~GG~~<br>~~Qe~~|NO<br>~~GG~~<br>~~GG~~<br>~~eG~~|NO<br>~~GG~~<br>~~GG~~<br>~~eG~~|NO|NO|NO|
||ESC * r C<br> <br>~~ee ~~<br>~~es~~|Ver. 2.0<br>or later<br> ~~se~~<br> ~~**e**s~~|OK<br>~~se ~~<br>~~ee~~<br>~~e~~|OK<br> ~~es ~~<br>~~ee~~<br>~~es~~|OK<br> ~~eG~~<br>~~eG~~<br>~~es~~<br>~~se~~|NO<br>~~eG ~~<br>~~eG~~<br>~~Qe~~<br>~~se~~|NO<br> ~~GG~~<br>~~GG~~<br>~~Qe~~<br>~~Ge~~|NO<br>~~GG~~<br>~~GG~~<br>~~eG~~<br>~~OG~~|NO<br>~~GG~~<br>~~GG~~<br>~~eG~~<br>~~OG~~|NO|NO|NO|
||ESC * r D<br> <br>~~es~~<br>~~ee~~|Ver. 2.0<br>or later<br> ~~**e**s ~~<br>~~ee~~|OK<br> ~~ee~~<br>~~e~~<br>~~ee~~|OK<br>~~ee ~~<br>~~es~~<br>~~ee~~|OK<br> ~~eG~~<br>~~es ~~<br>~~ee~~<br>~~se~~|NO<br>~~eG ~~<br> ~~Qe~~<br>~~ee~~<br>~~se~~|NO<br> ~~GG~~<br>~~Qe ~~<br>~~ee~~<br>~~Ge~~|NO<br>~~GG~~<br> ~~eG~~<br>~~ee~~<br>~~OG~~|NO<br>~~GG~~<br>~~eG~~<br>~~ee~~<br>~~OG~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|
||ESC * r E|Spec. A<br>Ver. 2.0<br>or later|OK|OK|OK<br>~~se~~|NO<br>~~se~~|NO<br>~~Ge~~|NO<br>~~OG~~|NO<br>~~OG~~|NO|NO|NO|
||ESC * r F<br>~~i~~|Spec. A<br>Ver. 2.0<br>or later<br>|OK<br>|OK<br>|OK<br>~~se~~<br>|NO<br>~~se~~<br>|NO<br>~~Ge~~<br>|NO<br>~~OG~~<br>|NO<br>~~OG~~<br>|NO|NO|NO|
||ESC * r P<br>~~ee~~<br>~~i~~<br>~~ee~~|Ver. 2.0<br>or later<br>~~ee~~<br>~~se~~<br>|OK<br>~~ee~~<br>~~se~~<br>|OK<br>~~ee~~<br>~~es~~<br>|OK<br>~~ee~~<br>~~se~~<br>~~eG~~<br>|NO<br>~~ee~~<br>~~se~~<br>~~eG~~<br>|NO<br>~~ee~~<br>~~Ge~~<br>~~GG~~<br>|NO<br>~~ee~~<br>~~OG~~<br>~~GG~~<br>|NO<br>~~ee~~<br>~~OG~~<br>~~GG~~<br>|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|
||ESC * r Q<br>~~i ~~<br>~~ee~~<br>~~es~~|Ver. 2.0<br>or later<br> ~~se~~<br>~~**e**s~~|OK<br>~~se~~<br>~~ee~~|OK<br>~~es~~<br>~~ee~~|OK<br>~~se~~<br>~~eG~~<br>~~eG~~|NO<br>~~se~~<br>~~eG~~<br>~~eG~~|NO<br>~~Ge~~<br>~~GG~~<br>~~GG~~|NO<br>~~OG~~<br>~~GG~~<br>~~GG~~|NO<br>~~OG~~<br>~~GG~~<br>~~GG~~|NO|NO|NO|
||ESC * r m l<br> <br>~~ee~~<br>~~es~~|Ver. 2.0<br>or later<br> ~~se~~<br>~~**e**s~~|OK<br>~~se~~<br>~~ee~~<br>~~e~~|OK<br>~~es~~<br>~~ee~~<br>~~es~~|OK<br>~~eG~~<br>~~eG~~<br>~~es~~|NO<br>~~eG~~<br>~~eG~~<br>~~Qe~~|NO<br>~~GG~~<br>~~GG~~<br>~~Qe~~|NO<br>~~GG~~<br>~~GG~~<br>~~eG~~|NO<br>~~GG~~<br>~~GG~~<br>~~eG~~|NO|NO|NO|
||ESC * r m r<br> <br>~~ee ~~<br>~~es~~<br>~~i~~|Ver. 2.0<br>or later<br> ~~se~~<br> ~~**e**s~~<br>|OK<br>~~se ~~<br>~~ee~~<br>~~e~~<br>|OK<br> ~~es ~~<br>~~ee~~<br>~~es~~<br>|OK<br> ~~eG~~<br>~~eG~~<br>~~es~~<br>~~se~~<br>|NO<br>~~eG ~~<br>~~eG~~<br>~~Qe~~<br>~~se~~<br>|NO<br> ~~GG~~<br>~~GG~~<br>~~Qe~~<br>~~Ge~~<br>|NO<br>~~GG~~<br>~~GG~~<br>~~eG~~<br>~~OG~~<br>|NO<br>~~GG~~<br>~~GG~~<br>~~eG~~<br>~~OG~~<br>|NO|NO|NO|
||ESC * r T<br> <br>~~es~~<br>~~ee~~<br>~~i~~<br>~~ee~~|Ver. 2.0<br>or later<br> ~~**e**s ~~<br>~~ee~~<br>~~se~~<br>|OK<br> ~~ee~~<br>~~e~~<br>~~ee~~<br>~~se~~<br>|OK<br>~~ee ~~<br>~~es~~<br>~~ee~~<br>~~es~~<br>|OK<br> ~~eG~~<br>~~es ~~<br>~~ee~~<br>~~se~~<br>~~eG~~<br>|NO<br>~~eG ~~<br> ~~Qe~~<br>~~ee~~<br>~~se~~<br>~~eG~~<br>|NO<br> ~~GG~~<br>~~Qe ~~<br>~~ee~~<br>~~Ge~~<br>~~GG~~<br>|NO<br>~~GG~~<br> ~~eG~~<br>~~ee~~<br>~~OG~~<br>~~GG~~<br>|NO<br>~~GG~~<br>~~eG~~<br>~~ee~~<br>~~OG~~<br>~~GG~~<br>|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|
||ESC * r K<br>~~i ~~<br>~~ee~~<br>~~es~~|Ver. 2.0<br>or later<br> ~~se~~<br>~~**e**s~~|OK<br>~~se~~<br>~~ee~~|OK<br>~~es~~<br>~~ee~~|OK<br>~~se~~<br>~~eG~~<br>~~eG~~|NO<br>~~se~~<br>~~eG~~<br>~~eG~~|NO<br>~~Ge~~<br>~~GG~~<br>~~GG~~|NO<br>~~OG~~<br>~~GG~~<br>~~GG~~|NO<br>~~OG~~<br>~~GG~~<br>~~GG~~|NO|NO|NO|
||b n1 n2 d1...dk<br> <br>~~ee~~<br>~~es~~|Ver. 2.0<br>or later<br> ~~se~~<br>~~**e**s~~|OK<br>~~se~~<br>~~ee~~<br>~~e~~|OK<br>~~es~~<br>~~ee~~<br>~~es~~|OK<br>~~eG~~<br>~~eG~~<br>~~es~~|NO<br>~~eG~~<br>~~eG~~<br>~~Qe~~|NO<br>~~GG~~<br>~~GG~~<br>~~Qe~~|NO<br>~~GG~~<br>~~GG~~<br>~~eG~~|NO<br>~~GG~~<br>~~GG~~<br>~~eG~~|NO|NO|NO|
||k n1 n2 d1...dk<br> <br>~~ee ~~<br>~~es~~<br>~~ee~~|Ver. 2.0<br>or later<br> ~~se~~<br> ~~**e**s~~<br>~~ee~~|OK<br>~~se ~~<br>~~ee~~<br>~~e~~<br>|OK<br> ~~es ~~<br>~~ee~~<br>~~es~~<br>|OK<br> ~~eG~~<br>~~eG~~<br>~~es~~<br>~~s~~<br>|NO<br>~~eG ~~<br>~~eG~~<br>~~Qe~~<br>~~s~~~~**e**~~<br>|NO<br> ~~GG~~<br>~~GG~~<br>~~Qe~~<br>~~Ge~~|NO<br>~~GG~~<br>~~GG~~<br>~~eG~~<br>~~OG~~|NO<br>~~GG~~<br>~~GG~~<br>~~eG~~<br>~~OG~~|NO|NO|NO|
||ESC * r Y<br> <br>~~es~~<br>~~ee~~<br>~~ee~~|Ver. 2.0<br>or later<br> ~~**e**s ~~<br>~~ee~~<br>~~ee~~|OK<br> ~~ee~~<br>~~e~~<br>~~ee~~<br>|OK<br>~~ee ~~<br>~~es~~<br>~~ee~~<br>|OK<br> ~~eG~~<br>~~es ~~<br>~~ee~~<br>~~s~~<br>|NO<br>~~eG ~~<br> ~~Qe~~<br>~~ee~~<br>~~s~~~~**e**~~<br>|NO<br> ~~GG~~<br>~~Qe ~~<br>~~ee~~<br>~~Ge~~|NO<br>~~GG~~<br> ~~eG~~<br>~~ee~~<br>~~OG~~|NO<br>~~GG~~<br>~~eG~~<br>~~ee~~<br>~~OG~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|
||ESC FF NUL<br>~~ee~~|Ver. 2.0<br>or later<br>~~ee ~~|OK<br> ~~es~~|OK<br>~~es ~~|OK<br>~~s~~<br> ~~e~~|NO<br>~~s~~~~**e**~~<br>~~e~~|NO<br>~~Ge~~<br>~~QO~~|NO<br>~~OG~~<br>~~QO~~|NO<br>~~OG~~<br>~~QO~~|NO|NO|NO|
||ESC FF EOT<br>~~es~~<br>~~Po~~|Ver. 2.0<br>or later<br>~~es ~~|OK<br> ~~es~~|OK<br>~~es ~~|OK<br> ~~eG~~|NO<br>~~eG~~|NO<br>~~GG~~|NO<br>~~GG~~|NO<br>~~GG~~|NO|NO|NO|
||ESC* r N<br>~~Po~~<br>~~Po~~|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|
||ESC * r V<br>~~Po~~<br>~~Po~~<br>~~po~~|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|
||ESC * r e<br>~~Po~~<br>~~po~~<br>~~Po~~|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|
||ESC* rS<br>~~po~~<br>~~Po~~<br>~~a~~|NO|NO<br>~~CO~~|NO<br>~~CO~~|NO<br>~~CO~~|NO|NO<br>~~(OO~~|NO<br>~~(OO~~|NO<br>~~(OO~~|NO|NO|NO|
||ESC * r s 0<br>~~Po~~<br>~~a~~|NO|NO<br>~~CO~~|NO<br>~~CO~~|NO<br>~~CO~~|NO|NO<br>~~(OO~~|NO<br>~~(OO~~|NO<br>~~(OO~~|NO|NO|NO|
||ESC * r s 1<br>~~a~~<br>~~Po~~<br>~~po~~|NO<br>~~Po~~|NO<br>~~CO~~<br>~~Po~~|NO<br>~~CO~~<br>~~Po~~|NO<br>~~CO~~<br>~~Po~~|NO<br>~~Po~~|NO<br>~~(OO~~<br>~~Po~~|NO<br>~~(OO~~<br>~~Po~~|NO<br>~~(OO~~<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|
||ESC* rs2<br>~~po~~<br>~~Po~~|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|
||ESC * r s 3<br>~~po~~<br>~~Po~~|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-14 

|• Black Mark Related Commands|
|---|
|**Class**<br>**Commands**<br>**Model Name**<br>~~Ce~~|
|**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**|
|Black Mark<br>ESC d<br>OK<br>OK<br>OK<br>OK<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>Related<br>FF<br>OK<br>OK<br>OK<br>OK<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>Commands<br>ESC C<br>OK<br>OK<br>OK<br>OK<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC C 0<br>OK<br>OK<br>OK<br>OK<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>VT<br>OK<br>OK<br>OK<br>OK<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC B<br>OK<br>OK<br>OK<br>OK<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>• 2-Color PrintingRelated Commands<br>**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**<br>2-Color<br>ESC RS c<br>Ver. 4.0<br>Ver. 2.0<br>Ver. 2.0<br>OK<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>~~ee Se~~<br>~~**P**o~~<br>~~o~~<br>~~Pf~~<br>~~RsGG~~<br>~~CO~~<br>~~Po CT~~<br>~~en~~<br>~~yyeaaeaaoaaa_ananaaesees~~|
|Printing<br>or later<br>or later<br>or later<br>Related<br>Commands<br>ESC RS C<br>Spec. A<br>Ver. 4.0<br>or later<br>Spec. A<br>Ver. 2.0<br>or later<br>Spec. A<br>Ver. 2.0<br>or later<br>Spec. B<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC<br>4<br>(Not<br>recommended)<br>Ver. 4.0<br>or later<br>Ver. 2.0<br>or later<br>Ver. 2.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC<br>5<br>(Not<br>Ver. 4.0<br>Ver. 2.0<br>Ver. 2.0<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>~~ft Pt~~<br>~~i es es ee ee~~|
|recommended)<br>or later<br>or later<br>or later|
|ESC FS q<br>Ver. 4.0<br>or later<br>Ver. 2.0<br>or later<br>Ver. 2.0<br>or later<br>(*)<br>OK<br>(*)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC FS p<br>Ver. 4.0<br>or later<br>Ver. 2.0<br>or later<br>Ver. 2.0<br>or later<br>OK<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>~~a~~<br>~~ee ee~~<br>~~es~~<br>~~es~~<br>~~eseess~~<br>~~ss~~|



|• Presenter Related Commands|
|---|
|**Class**<br>**Commands**<br>**Model Name**<br>~~Ce~~|
|**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**|
|Presenter<br>ESC SYN0<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>Related<br>ESC SYN 1<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>Commands<br>ESC SYN 3<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC SYN 4<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS SUB DC1<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS SUB DC2<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS SUB DC3<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>@~~=====>====——~~<br>~~**P**o~~<br>~~o~~<br>~~PT~~<br>~~Rs GG~~<br>~~GG~~<br>~~Pe~~<br>~~Pe~~|
|• Mark Commands|
|**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**<br>Mark<br>Commands<br>ESC GS * 0<br>NO<br>Ver. 4.0<br>or later<br>NO<br>Ver. 3.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS * 1<br>NO<br>Ver. 4.0<br>or later<br>NO<br>Ver. 3.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS * 2<br>NO<br>Ver. 4.0<br>or later<br>NO<br>Ver. 3.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS * W<br>NO<br>Ver. 4.0<br>or later<br>NO<br>Ver. 3.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS * C<br>NO<br>Ver. 4.0<br>or later<br>NO<br>Ver. 3.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>~~|~~<br>~~OO OOOO~~<br>~~es ee ss seGe~~<br>~~a i ee rs~~<br>~~es~~<br>~~es ee~~<br>~~a i i~~<br>~~es es ee~~<br>~~es~~<br>~~es~~<br>~~es~~<br>~~es~~<br>~~es~~<br>~~es~~|
|• Auto Logo Commands|
|**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TS{800II**<br>**FVP10**<br>~~Ce~~<br>~~SS~~|
|Auto Logo<br>ESC GS / W<br>NO<br>Ver. 4.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>Commands ESC GS / C<br>NO<br>Ver. 4.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS / 1<br>NO<br>Ver. 4.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS / 2<br>NO<br>Ver. 4.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS / 3<br>NO<br>Ver. 4.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS / 4<br>NO<br>Ver. 4.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS / 5<br>NO<br>Ver. 4.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS / 6<br>NO<br>Ver. 4.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>~~es i~~<br>~~ss eeee~~<br>~~i ee es es ee~~<br>~~a i eeee ee~~<br>~~ee~~<br>~~es es~~<br>~~es~~<br>~~es~~<br>~~es ssGe~~<br>~~es es~~<br>~~es es ssQsOs~~<br>~~i ee es es ee~~<br>~~a i eeee ee~~<br>~~ee~~<br>~~PoEEe~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-15 

|**Class**<br>~~ee~~|**Commands**<br>~~ee~~<br>~~es~~|**Model Name**<br>~~ee eae~~<br>~~o—~—$<o—>X—£&Z&Q~~|**Model Name**<br>~~ee eae~~<br>~~o—~—$<o—>X—£&Z&Q~~|**Model Name**<br>~~ee eae~~<br>~~o—~—$<o—>X—£&Z&Q~~|**Model Name**<br>~~ee eae~~<br>~~o—~—$<o—>X—£&Z&Q~~|**Model Name**<br>~~ee eae~~<br>~~o—~—$<o—>X—£&Z&Q~~|**Model Name**<br>~~ee eae~~<br>~~o—~—$<o—>X—£&Z&Q~~|**Model Name**<br>~~ee eae~~<br>~~o—~—$<o—>X—£&Z&Q~~|**Model Name**<br>~~ee eae~~<br>~~o—~—$<o—>X—£&Z&Q~~|**Model Name**<br>~~ee eae~~<br>~~o—~—$<o—>X—£&Z&Q~~|**Model Name**<br>~~ee eae~~<br>~~o—~—$<o—>X—£&Z&Q~~|**Model Name**<br>~~ee eae~~<br>~~o—~—$<o—>X—£&Z&Q~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~ee eae~~<br>~~es~~|**TSP700**<br>~~eae~~<br>~~ee~~|**TSP600**<br>~~eae~~<br>~~Ge~~|**TUP900**<br>~~eae~~<br>~~Qe~~|**TSP1000**<br>~~eae~~<br>~~Qe~~|**TSP828L**<br>~~eae~~<br>~~Ge~~|**TSP700II**<br>~~GO~~|**TSP650**<br>~~GO~~|**TUP500**<br>~~o—~—$<o—>X—£&Z&Q~~<br>~~GO~~|**TSP800II**<br>~~o—~—$<o—>X—£&Z&Q~~|**FVP10**<br>~~o—~—$<o—>X—£&Z&Q~~|
|PDF417<br>Commands ESC GS x S 1<br>~~ee~~<br>~~PCF~~|ESC GS x S 0<br>~~ee~~<br>~~es~~<br>~~Re~~|NO<br>~~ee eae~~<br>~~es~~<br>~~ee~~|NO<br>~~eae~~<br>~~ee~~<br>~~ee~~|NO<br>~~eae~~<br>~~Ge~~<br>~~Ge~~|Ver. 3.1<br>or later<br>~~eae~~<br>~~Qe~~<br>~~Ge~~|NO<br>~~eae~~<br>~~Qe~~<br>~~Ge~~|NO<br>~~eae~~<br>~~Ge~~<br>~~Ge~~|NO<br>~~GO~~<br>~~OO~~|NO<br>~~GO~~<br>~~OO~~|NO<br>~~o—~—$<o—>X—£&Z&Q~~<br>~~GO~~|NO<br>~~o—~—$<o—>X—£&Z&Q~~|NO<br>~~o—~—$<o—>X—£&Z&Q~~|
||Commands ESC GS x S 1<br>~~es~~<br>~~Re~~<br>~~PCF~~|NO<br>~~es ~~<br>~~ee~~<br>~~PCFCE~~|NO<br> ~~ee~~<br>~~ee~~<br>~~CE|~~|NO<br>~~Ge ~~<br>~~Ge~~<br>~~|~~|Ver. 3.1<br>or later<br> ~~Qe~~<br>~~Ge~~|NO<br>~~Qe~~<br>~~Ge~~|NO<br>~~Ge ~~<br>~~Ge~~|NO<br> ~~GO~~<br>~~OO~~|NO<br>~~GO~~<br>~~OO~~|NO<br>~~GO~~|NO|NO|
||ESC GS x S 2<br>~~Re ~~<br>~~PCF~~<br>~~es~~|NO<br> ~~ee~~<br>~~PCFCE~~<br>~~ee~~|NO<br>~~ee~~<br>~~CE|~~<br>~~GeGe~~|NO<br>~~Ge ~~<br>~~|~~<br>~~GeGe~~|Ver. 3.1<br>or later<br> ~~Ge~~<br>~~ee~~|NO<br>~~Ge~~<br>~~ee~~|NO<br>~~Ge ~~<br>~~ee~~|NO<br> ~~OO~~|NO<br>~~OO~~|NO|NO|NO|
||ESC GS x S 3<br>~~PCF~~<br>~~es~~<br>~~Re~~|NO<br>~~PCF CE~~<br>~~ee~~<br>~~ee~~|NO<br>~~CE |~~<br>~~GeGe~~<br>~~ee~~|NO<br>~~|~~<br>~~GeGe~~<br>~~Oe~~|Ver. 3.1<br>or later<br>~~ee~~<br>~~ee~~|NO<br>~~ee~~<br>~~ee~~|NO<br>~~ee~~|NO|NO|NO|NO|NO|
||ESC GS x D<br>~~es ~~<br>~~Re~~<br>~~Re~~|NO<br> ~~ee~~<br>~~ee~~<br>~~ee~~|NO<br>~~GeGe~~<br>~~ee~~<br>~~ee~~|NO<br>~~GeGe ~~<br>~~Oe~~<br>~~Ge~~|Ver. 3.1<br>or later<br> ~~ee~~<br>~~ee~~<br>~~Ge~~|NO<br>~~ee~~<br>~~ee~~<br>~~Ge~~|NO<br>~~ee~~<br>~~Ge~~|NO<br>~~OO~~|NO<br>~~OO~~|NO|NO|NO|
||ESC GS x P<br>~~Re ~~<br>~~Re~~<br>~~Re~~|NO<br> ~~ee~~<br>~~ee~~<br>~~es~~|NO<br>~~ee~~<br>~~ee~~<br>~~es~~|NO<br>~~Oe ~~<br>~~Ge~~<br>~~Ge~~|Ver. 3.1<br>or later<br> ~~ee~~<br>~~Ge~~<br>~~se~~|NO<br>~~ee~~<br>~~Ge~~<br>~~se~~|NO<br>~~Ge~~|NO<br>~~OO~~|NO<br>~~OO~~|NO|NO|NO|
||ESC GS x I<br>~~Re ~~<br>~~Re~~|NO<br> ~~ee~~<br>~~es~~|NO<br>~~ee~~<br>~~es~~|NO<br>~~Ge ~~<br>~~Ge~~|Ver. 3.1<br>or later<br> ~~Ge~~<br>~~se~~|NO<br>~~Ge~~<br>~~se~~|NO<br>~~Ge ~~|NO<br> ~~OO~~|NO<br>~~OO~~|NO|NO|NO|



## • Print Start Trigger Control Commands 

|• Print Start Trigger Control Commandsgger Control Commandser Control Commands||||||
|---|---|---|---|---|---|
|**Class**<br>**Commands**||**Model Name**||||
|**TSP800**<br>**TSP700**<br>**TSP600**|**TUP900**|**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**|**TSP800II**||**FVP10**|
|Print Start<br>ESC GS g 0<br>NO<br>NO<br>NO|NO|NO<br>NO<br>NO<br>NO<br>NO|NO||NO|
|Trigger<br>ESC GS g 1<br>NO<br>NO<br>NO|NO|NO<br>NO<br>NO<br>NO<br>NO|NO||NO|
|Control||||||
|• QR Commands||||||
|**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**<br>QR Code<br>ESC GSyS 0<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS y S1<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GSyS 2<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GSyD 1<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS yD 2<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GSyP<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GSyI<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>~~a~~<br>~~Le~~<br>~~mljELEW~~<br>S~~==========——~~<br>~~eG~~<br>~~(OO~~<br>~~OO~~<br>~~po~~<br>~~GG~~<br>~~OO~~<br>~~DG~~<br>~~OO~~<br>~~OO~~<br>~~OO~~<br>~~a GG~~<br>~~(GO~~<br>~~Po~~||||||
|• Page Function Commands||||||
|**Class**<br>**Commands**||**Model Name**||||
|**TSP800**<br>**TSP700**<br>**TSP600**|**TUP900**|**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**|**TSP800II**||**FVP10**|
|Page<br>ESC GSh0<br>NO<br>NO<br>NO|NO|NO<br>NO<br>NO<br>NO<br>NO|NO||NO|
|Function<br>ESC GS h 1<br>NO<br>NO<br>NO|NO|NO<br>NO<br>NO<br>NO<br>NO|NO||NO|



## • Reduced Printing Function Commands 

|**Class**|**Commands**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**|**TSP700**|**TSP600**|**TUP900**|**TSP1000**|**TSP828L**|**TSP700II**|**TSP650**|**TUP500**|**TSP800II**|**FVP10**|
|Reduced<br>Printing<br>Function|ESC GS c|x|x|x|x|x|x|x|x|x|x|○|



• Page Mode Commands 

|**Class**<br>~~ee~~<br>~~Po~~|**Commands**<br>~~ee~~<br>~~Po~~|**Model Name**<br>~~re~~|**Model Name**<br>~~re~~|**Model Name**<br>~~re~~|**Model Name**<br>~~re~~|**Model Name**<br>~~re~~|**Model Name**<br>~~re~~|**Model Name**<br>~~re~~|**Model Name**<br>~~re~~|**Model Name**<br>~~re~~|**Model Name**<br>~~re~~|**Model Name**<br>~~re~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~re~~|**TSP700**<br>~~re~~|**TSP600**<br>~~re~~|**TUP900**<br>~~re~~|**TSP1000**<br>~~re~~|**TSP828L**<br>~~re~~|**TSP700II**<br>~~re~~|**TSP650**<br>~~re~~|**TUP500**<br>~~re~~|**TSP800II**<br>~~re~~|**FVP10**<br>~~re~~|
|Page Mode<br>~~ee~~<br>~~Po~~<br>~~po~~<br>§~~>S==S==S====~~<br>~~po~~<br>~~Po~~<br>~~Po~~|ESC GS P 0<br>~~ee ~~<br>~~Po~~<br>~~po~~<br>~~>S==S==S====~~|x<br> ~~re~~<br><br>~~>S==S==S====~~|x<br>~~re~~<br><br>~~>S==S==S====~~|x<br>~~re~~<br><br>~~>S==S==S====~~|x<br>~~re~~<br><br>~~>S==S==S====~~|x<br>~~re~~<br><br>~~>S==S==S====~~|x<br>~~re~~<br><br>~~>S==S==S====~~|x<br>~~re~~<br><br>~~>S==S==S====~~|x<br>~~re~~<br><br>~~>S==S==S====~~|x<br>~~re~~<br><br>~~>S==S==S====~~|x<br>~~re~~<br><br>~~>S==S==S====~~|○<br>~~re~~<br><br>~~>S==S==S====~~|
||ESC GS P 1<br>~~Po~~<br>~~po~~<br>~~>S==S==S====~~|x<br><br>~~>S==S==S====~~|x<br><br>~~>S==S==S====~~|x<br><br>~~>S==S==S====~~|x<br><br>~~>S==S==S====~~|x<br><br>~~>S==S==S====~~|x<br><br>~~>S==S==S====~~|x<br><br>~~>S==S==S====~~|x<br><br>~~>S==S==S====~~|x<br><br>~~>S==S==S====~~|x<br><br>~~>S==S==S====~~|○<br><br>~~>S==S==S====~~|
||ESC GS P 2<br>~~poPo~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|○<br>~~Po~~<br>~~>S==S==S====~~|
||ESC GS P 3<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|x<br>~~Po~~<br>~~>S==S==S====~~|○<br>~~Po~~<br>~~>S==S==S====~~|
||ESC GS P 4<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|○<br>~~>S==S==S====~~|
||ESC GS P 5<br>~~>S==S==S====~~<br>~~Po~~<br>~~po~~|x<br>~~>S==S==S====~~<br>~~Po~~|x<br>~~>S==S==S====~~<br>~~Po~~|x<br>~~>S==S==S====~~<br>~~Po~~|x<br>~~>S==S==S====~~<br>~~Po~~|x<br>~~>S==S==S====~~<br>~~Po~~|x<br>~~>S==S==S====~~<br>~~Po~~|x<br>~~>S==S==S====~~<br>~~Po~~|x<br>~~>S==S==S====~~<br>~~Po~~|x<br>~~>S==S==S====~~<br>~~Po~~|x<br>~~>S==S==S====~~<br>~~Po~~|○<br>~~>S==S==S====~~<br>~~Po~~|
||ESC GS P 6<br>~~>S==S==S====~~<br>~~po~~<br>~~Po~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|○<br>~~>S==S==S====~~|
||ESC GS P 7<br>~~>S==S==S====~~<br>~~po~~<br>~~Po~~<br>~~Po~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|○<br>~~>S==S==S====~~|
||ESC GS P 8<br>~~>S==S==S====~~<br>~~Po~~<br>~~Po~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|x<br>~~>S==S==S====~~|○<br>~~>S==S==S====~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-16 

• Text Search Commands 

|**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP800II**<br>**FVP10**<br>Text Search<br>ESC GS)B(fn = 48)<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>○<br>ESC GS)B(fn = 49)<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>○<br>ESC GS)B(fn = 50)<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>○<br>ESC GS)B(fn = 64)<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>○<br>ESC GS)B(fn = 65)<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>○<br>ESC GS)B(fn = 80)<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>○<br>ESC GS)B(fn = 81)<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>○<br>ESC GS)B(fn = 96)<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>○<br>~~Ce~~<br>~~ieee~~<br>~~a~~<br>~~GO~~<br>~~GO~~<br>~~po~~<br>~~a~~<br>~~DO~~<br>~~GOO~~<br>~~(GO~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~po~~|
|---|
|ESC GS)B(fn = 97)<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>○<br>~~Po~~|
|• Audio Commands|
|**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP800II**<br>**FVP10**<br>Audio<br>ESC GS s O<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>○<br>ESC GS s P<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>○<br>ESC GS s R<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>○<br>ESC GS s I<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>○<br>ESC GS s U<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>○<br>ESC GS s T<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>x<br>○<br>~~CT~~<br>~~a~~<br>~~eae~~<br>~~w&g~~<br>~~**P**o~~<br>~~o~~<br>~~a~~<br>~~CO~~<br>~~(OO~~<br>~~Po~~<br>~~po~~<br>~~Po~~|



(*) It is necessary to turn the printer from off to on, because the printer hangs up after resetting the printer. 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-17 

## **6.4. Ethernet I/F / Wireless LAN I/F** 

|**Class**<br>~~ieee~~|**Commands**<br>~~ieee~~|**Model Name**<br>~~|~~<br>~~ieee~~|**Model Name**<br>~~|~~<br>~~ieee~~|**Model Name**<br>~~|~~<br>~~ieee~~|**Model Name**<br>~~|~~<br>~~ieee~~|**Model Name**<br>~~|~~<br>~~ieee~~|**Model Name**<br>~~|~~<br>~~ieee~~|**Model Name**<br>~~|~~<br>~~ieee~~|**Model Name**<br>~~|~~<br>~~ieee~~|**Model Name**<br>~~|~~<br>~~ieee~~|**Model Name**<br>~~|~~<br>~~ieee~~|**Model Name**<br>~~|~~<br>~~ieee~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~|~~<br>~~ieee~~|**TSP700**<br>~~|~~<br>~~ieee~~|**TSP600**<br>~~|~~<br>~~ieee~~|**TUP900**<br>~~|~~<br>~~ieee~~|**TSP1000**<br>~~|~~<br>~~ieee~~|**TSP828L**<br>~~|~~<br>~~ieee~~|**TSP700II**<br>~~|~~<br>~~ieee~~|**TSP650**<br>~~|~~<br>~~ieee~~|**TUP500**<br>~~|~~<br>~~ieee~~|**TSP800II**<br>~~|~~<br>~~ieee~~|**FVP10**<br>~~|~~<br>~~ieee~~|
|Font Style<br>and<br>Character<br>Set<br>~~Po~~<br>~~po~~<br>~~po~~<br>~~Po~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~Po~~|ESC RS F<br>~~Po~~<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|
||ESC GS t<br>~~Po~~<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|
||ESC GS =<br>~~Po~~<br>~~po~~|Ver. 3.0 or<br>later<br>Spec. A|Ver. 3.0 or<br>Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|
||ESCR<br>~~po~~<br>~~po~~|OK<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC /<br>~~po~~<br>~~po~~<br>~~Po~~|OK<br>~~po~~<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC SP<br>~~po~~<br>~~Po~~<br>~~po~~|OK<br>~~po~~<br>~~Po~~<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESCM<br>~~Po~~<br>~~po~~<br>~~po~~|OK<br>~~Po~~<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC P<br>~~po~~<br>~~po~~<br>~~po~~|OK<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC :<br>~~po~~<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC<br>p<br>(Not<br>recommended)<br>~~po~~<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC g<br>~~po~~<br>~~Po~~|Spec. A|Spec. A|Spec. A|Spec. B|Spec. B|Spec. B|Spec. A|Spec. A|Spec. B|Spec. A|Spec. A|
|Character<br>expansion<br>settings<br>~~po~~<br>~~Po~~<br>~~po~~<br>~~Po~~<br>~~Po~~<br>~~**p**~~|ESC i<br>~~po~~<br>~~Po~~<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC W<br>~~Po~~<br>~~po~~<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESCh<br>~~po~~<br>~~Po~~<br>~~Po~~|OK<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||SO<br>~~Po~~<br>~~Po~~<br>~~**p**o~~|OK<br>~~Po~~<br>~~o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||DC4<br>~~Po~~<br>~~**p**o~~|OK<br>~~Po~~<br>~~o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC SO<br>~~**p**o~~|OK<br>~~o~~|OK|OK|OK|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|
||ESC DC4<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|
|Print Mode<br>~~po~~<br>~~Po~~<br>~~**p**~~<br>~~po~~<br>~~Po~~|ESC E|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A<br>V. 2.0 or<br>earlier<br>Spec. B V.<br>2.0 or later|Spec. A<br>V. 2.0 or<br>earlier<br>Spec. B V.<br>2.0 or later|Spec. A<br>V. 2.0 or<br>earlier<br>Spec. B V.<br>2.0 or later|Spec. B|Spec. B|
||ESC F<br>~~po~~|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A|Spec. A<br>V. 2.0 or<br>earlier<br>Spec. B V.<br>2.0 or later|Spec. A<br>V. 2.0 or<br>earlier<br>Spec. B V.<br>2.0 or later|Spec. A<br>V. 2.0 or<br>earlier<br>Spec. B V.<br>2.0 or later|Spec. B|Spec. B|
||ESC -<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC _<br>~~po~~<br>~~Po~~<br>~~Po~~|OK<br>~~Po~~<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|
||ESC 4<br>~~Po~~<br>~~**p**o~~|OK<br>~~Po~~<br>~~o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC 5<br>~~Po~~<br>~~**p**o~~|OK<br>~~Po~~<br>~~o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||SI<br>~~**p**o~~<br>~~po~~|OK<br>~~o~~|OK|OK|OK|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|
||DC2<br>~~po~~<br>~~Po~~|OK<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
|Line spacing LF<br>~~po~~<br>~~Po~~<br>~~po~~<br>~~po~~<br>~~Po~~<br>~~po~~<br>~~**p**~~<br>~~Po~~|Line spacing LF<br>~~po~~<br>~~Po~~<br>~~po~~|OK<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||CR<br>~~Po~~<br>~~po~~<br>~~po~~|OK<br>~~Po~~<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC a<br>~~po~~<br>~~po~~<br>~~Po~~|OK<br>~~po~~<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC z<br>~~po~~<br>~~Po~~<br>~~po~~|OK<br>~~po~~<br>~~Po~~<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC 0<br>~~Po~~<br>~~po~~<br>~~**p**o~~|OK<br>~~Po~~<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC J<br>~~po~~<br>~~**p**o~~|OK<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC I<br>~~**p**o~~<br>~~Po~~|OK|OK|OK|OK|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|
|Page Control FF<br>~~Po~~<br>~~Po~~<br>~~**p**~~<br>~~Po~~|Page Control FF<br>~~Po~~<br>~~Po~~|OK<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC C<br>~~Po~~<br>~~Po~~<br>~~**p**o~~|OK<br>~~Po~~<br>~~o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC C 0<br>~~Po~~<br>~~**p**o~~|OK<br>~~Po~~<br>~~o~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||VT<br>~~**p**o~~|OK<br>~~o~~|OK|OK|OK|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|OK<br>~~o~~|
||ESC B<br>~~po~~<br>~~Po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|
|Horizontal<br>direction<br>position<br>~~Po~~<br>~~po~~<br>~~po~~<br>~~Po~~<br>~~po~~<br>~~**p**~~<br>~~P~~|ESC l<br>~~Po~~<br>~~po~~|Spec. A|Spec. A|Spec. A|Spec. B|Spec. B|Spec. B|Spec. A|Spec. A|Spec. B|Spec. A|Spec. A|
||ESC Q<br>~~Po~~<br>~~po~~<br>~~po~~|Spec. A<br>~~po~~|Spec. A|Spec. A|Spec. B|Spec. B|Spec. B|Spec. A|Spec. A|Spec. B|OK|OK|
||HT<br>~~po~~<br>~~po~~<br>~~Po~~|OK<br>~~po~~<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC D<br>~~po~~<br>~~Po~~<br>~~po~~|OK<br>~~po~~<br>~~Po~~<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC GSA<br>~~Po~~<br>~~po~~<br>~~**p**o~~|OK<br>~~Po~~<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC GS R<br>~~po~~<br>~~**p**o~~|OK<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC GS a<br>~~**p**o~~<br>~~-—f~~|OK<br>~~-—f——f~~|OK<br>~~——f~~|OK<br>~~——f—f~~|OK<br>~~—f—}~~|OK<br>~~o~~<br>~~—}—_f+—_~~|OK<br>~~o~~<br>~~—_f+—_ ++~~|OK<br>~~o~~<br>~~++~~|OK<br>~~o~~<br>~~++~~|OK<br>~~o~~<br>~~+~~<br>~~}+—_~~|OK<br>~~o~~<br>~~}+—_~~|OK<br>~~o~~|
|Download<br>~~P~~<br>~~Po~~<br>~~Po~~|ESC &<br>~~-—f~~<br>~~Po~~|OK<br>~~-—f——f~~<br>~~Po~~|OK<br>~~——f~~|OK<br>~~——f—f~~|OK<br>~~—f—}~~|OK<br>~~—}—_f+—_~~|OK<br>~~—_f+—_ ++~~|OK<br>~~++~~|OK<br>~~++~~|OK<br>~~+~~<br>~~}+—_~~|OK<br>~~}+—_~~|OK|
||ESC%<br>~~-—f~~<br>~~Po~~<br>~~Po~~|OK<br>~~-—f——f~~<br>~~Po~~<br>~~Po~~|OK<br>~~——f~~|OK<br>~~——f—f~~|OK<br>~~—f—}~~|OK<br>~~—}—_f+—_~~|OK<br>~~—_f+—_ ++~~|OK<br>~~++~~|OK<br>~~++~~|OK<br>~~+~~<br>~~}+—_~~|OK<br>~~}+—_~~|OK|
|Bit Image<br>Graphics<br>~~P~~<br>~~Po~~<br>~~Po~~<br>~~po~~<br>~~Po~~<br>~~po~~|ESC K<br>~~-—f~~<br>~~Po~~<br>~~Po~~|OK<br>~~-—f ——f~~<br>~~Po~~<br>~~Po~~|OK<br>~~——f~~|OK<br>~~——f —f~~|OK<br>~~—f —}~~|OK<br>~~—} —_f+—_~~|OK<br>~~—_f+—_ ++~~|OK<br>~~++~~|OK<br>~~++ ~~|OK<br> ~~+~~<br>~~}+—_~~|OK<br>~~}+—_~~|OK|
||ESCL<br>~~Po~~<br>~~po~~<br>~~po~~|OK<br>~~Po~~<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|OK<br>~~po~~|
||ESC k<br>~~po~~<br>~~Po~~|OK<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC X<br>~~po~~<br>~~Po~~<br>~~po~~|OK<br>~~Po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
|Logo<br>~~Po~~<br>~~po~~<br>~~po~~|ESCFS q<br>~~Po~~<br>~~po~~<br>~~po~~|OK<br>~~Po~~<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|
||ESC FSp<br>~~po~~<br>~~po~~|OK<br>~~po~~|OK|OK|OK|OK|OK|OK|OK|OK|||
||ESC RS L<br>~~po~~|NO<br>~~po~~|NO|NO|NO|NO|NO|Ver. 1.2 or<br>later Spec.<br>A Ver. 1.3<br>or later<br>Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|
|Bar Codes|ESC b|Spec. A|Spec. A|Spec. A|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|Spec. B|
|Cutter<br>Control<br>~~|~~|ESC d<br>~~|~~|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|OK|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-18 

**==> picture [489 x 340] intentionally omitted <==**

**----- Start of picture text -----**<br>
Class Commands Ce Model Name<br>TSP800  TSP700 TSP600 TUP900 TSP1000 TSP828L TSP700II  TSP650  TUP500  TSP800II FVP10<br>| oo OOOO<br>External   po ESC BEL   OK  OK  OK  NO NO NO OK  OK  NO NO NO<br>device drive  P BEL  o OK  OK  OK  NO  NO  NO  OK  OK  NO  NO  NO<br>FS  OK  OK  OK  NO  NO  o NO  OK  OK  NO  NO  NO<br>GG SUB  OK  OK  OK  NO NO NO OK  OK  NO NO NO<br>a EM  OK  OK  OK  NO  GG NO  NO  OK  CC OK  NO  NO  NO<br>ESC GS BEL  NO  Ver. 5.0  NO  NO  OK  NO  OK  OK  NO  OK  OK<br>or later<br>es ESC GS EM DC1  NO  GG NO  NO  NO  GG NO  NO  Ver. 1.3  OC OK  NO  OK  OK<br>or later<br>ee ESC GS EM DC2  ee NO  es NO  ee NO  NO  es NO  es NO  se Ver. 1.3  OK  NO<br>a es ee es or later<br>Print Setting ESC RS d   i Spec. A  Sp es ec. A  ee Spec. A Spec. A ss Spec. A Spec. A es Spec. A  Spec. A  Spec. B Spec. B Spec. B<br>ESC RS r   Spec. A  Spec. A Spec. A Spec. A Spec. A Spec. A Spec. A  Spec. A  Spec. B Spec. A Spec. A<br>Status  ESC RS a   NO  NO  NO  NO  NO  NO  Spec. C  Spec. C  Spec. C Spec. C Spec. C<br>V. 2.0 or  V. 2.0 or  V. 2.0 or<br>later  later  later<br>ESC ACK SOH  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>a ENQ OK  GG OK  OK  OK  GG OK  OK  OK  OC OK  OK  OK  OK<br>Pp EOT  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>P ESC ACK CAN  o OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>ETB  Spec. A  Spec. A Spec. A Spec. B Spec. B o Spec. B Spec. B  Spec. B  Spec. B Spec. B Spec. B<br>Po ESC RS E  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>ESC GS ETX  NO  NO  NO  NO  NO  NO  Ver. 2.0  Ver. 2.0  OK  OK  OK<br>7 ee eeeee or later  or later<br>Kanji  ee ESC p  OK  es OK  es es OK  OK  OK  OK  OK  OK  OK  OK  OK<br>character<br>GG ESC q OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>a ESC $ OK  GG OK  OK  OK  GG OK  OK  OK  CO OK  C OK  OK  OK<br>Pf ESC s   OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>Po ESC t OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>— =========—=—Po ESC r   Spec. A  Spec. A Spec. A Spec. B Spec. B Spec. B Spec. B  Spec. B  Spec. B Spec. B Spec. B<br>Others  CAN  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>ESC @ OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>ESC GS # m  Spec. A  Spec. A Spec. A Spec. B Spec. B Spec. B Spec. B  Spec. B  Spec. B Spec. C Spec. C<br>VER. 3.0<br>OR<br>LATER<br>| P ESC ?   PF PPPoe OK  OK  OK  OK  OK  OK  OK  OK  OK  OK  OK<br>**----- End of picture text -----**<br>


――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-19 

||~~a~~|~~eee~~|~~eee~~|~~eee~~|~~eee~~|~~eee~~|~~eee~~|~~eee~~|~~eee~~|~~eee~~|~~eee~~|~~eee~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Class**<br>~~ere~~|**Commands**<br>~~ere~~<br>~~a~~<br>~~a~~|**Model Name**<br>~~ere~~<br>~~eee~~|||||||||||
|||**TSP800**<br>~~ere~~<br>~~ee~~|**TSP700**<br>~~ere~~<br>~~ee~~|**TSP600**<br>~~ere~~<br>~~ee~~|**TUP900**<br>~~ere~~<br>~~se~~|**TSP1000**<br>~~ere~~<br>~~se~~|**TSP828L**<br>~~ere~~|**TSP700II**<br>~~ere~~|**TSP650**<br>~~ere~~<br>~~eee~~|**TUP500**<br>~~ere~~<br>~~eee~~|**TSP800II**<br>~~ere~~<br>~~eee~~|**FVP10**<br>~~ere~~<br>~~eee~~|
|Raster|ESC * r R<br>~~a~~<br>~~a~~<br>~~a~~|Ver. 2.0 or<br>later<br>~~ee~~<br>~~es~~<br>|OK<br>~~ee~~<br>~~es~~<br>|OK<br>~~ee~~<br>~~ee~~|OK<br>~~se~~<br>~~ss~~|OK<br>~~se~~<br>~~ss~~|OK<br>~~ss~~|OK<br>~~es ee~~|OK<br>~~eee~~<br>~~ee~~|OK<br>~~eee~~<br>~~ee~~|OK<br>~~eee~~|OK<br>~~eee~~|
||ESC * r A<br>~~a~~<br>~~a~~<br>~~es~~|Ver. 2.0 or<br>later<br>~~ee~~<br>~~es~~<br>~~a~~<br>|OK<br>~~ee~~<br>~~es~~<br>~~a~~<br>|OK<br>~~ee~~<br>~~ee~~<br>~~e~~<br>|OK<br>~~se~~<br>~~ss~~<br>~~e~~~~**s**~~<br>|OK<br>~~se~~<br>~~ss~~<br>~~**e**e~~|OK<br>~~ss~~<br>~~es~~|OK<br>~~es ee~~<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK|OK|
||ESC * r B<br>~~a~~<br>~~a~~<br>~~es~~|Ver. 2.0 or<br>later<br>~~ee~~<br>~~es~~<br>~~a~~<br>~~es~~|OK<br>~~ee ~~<br>~~es~~<br>~~a~~<br>~~ee~~|OK<br> ~~ee ~~<br>~~ee~~<br>~~e~~<br>~~e~~|OK<br> ~~se~~<br>~~ss~~<br>~~e~~~~**s**~~<br>~~e~~|OK<br>~~se~~<br>~~ss~~<br>~~**e**e~~|OK<br>~~ss~~<br>~~es~~<br>~~s~~|OK<br>~~es ee~~<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK|OK|
||ESC * r C<br>~~a ~~<br>~~es~~|Ver. 2.0 or<br>later<br>~~es~~<br> ~~a~~<br>~~es~~|OK<br>~~es ~~<br>~~a~~<br>~~ee~~|OK<br> ~~ee ~~<br>~~e~~<br>~~e~~|OK<br> ~~ss~~<br>~~e~~~~**s**~~<br>~~e~~|OK<br>~~ss~~<br>~~**e**e~~|OK<br>~~ss ~~<br>~~es~~<br>~~s~~|OK<br> ~~es ee~~<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK|OK|
||ESC * r D<br> <br>~~es ~~<br>~~|~~|Ver. 2.0 or<br>later<br> ~~a~~<br> ~~es ~~<br>||OK<br>~~a~~<br> ~~ee ~~<br>~~|~~|OK<br>~~e~~<br> ~~e~~<br>~~te~~|OK<br>~~e~~~~**s** ~~<br>~~e~~<br>~~teft~~|OK<br> ~~**e**e~~<br>~~ftte~~|OK<br>~~es ~~<br>~~s~~<br>~~tett~~|OK<br> ~~ee~~<br>~~tt~~|OK<br>~~tt~~|OK|OK|OK|
||ESC * r E<br>~~|~~|Spec. A<br>Ver. 2.0 or<br>later<br>||OK<br>~~|~~|OK<br>~~te~~|OK<br>~~teft~~|OK<br>~~ftte~~|OK<br>~~tett~~|OK<br>~~tt~~|OK<br>~~tt~~|OK|OK|OK|
||ESC * r F<br>~~|~~<br>~~Rs~~|Spec. A<br>Ver. 2.0 or<br>later<br>|<br>~~ee~~|OK<br>~~|~~<br>~~es~~|OK<br>~~te~~<br>~~es~~|OK<br>~~te ft~~<br>~~es~~|OK<br>~~ft te~~<br>~~ss~~|OK<br>~~te tt~~<br>~~ss~~|OK<br>~~tt~~|OK<br>~~tt~~|OK|OK|OK|
||ESC * r P<br>~~Rs~~<br>~~a~~|Ver. 2.0 or<br>later<br>~~ee~~<br>~~es~~|OK<br>~~es~~<br>~~es~~|OK<br>~~es~~<br>~~ee~~|OK<br>~~es~~<br>~~se~~|OK<br>~~ss~~<br>~~se~~|OK<br>~~ss~~<br>~~es~~|OK|OK|OK|OK|OK|
||ESC * r Q<br>~~Rs ~~<br>~~a~~<br>~~a~~|Ver. 2.0 or<br>later<br> ~~ee ~~<br>~~es~~|OK<br> ~~es ~~<br>~~es~~<br>~~es~~|OK<br> ~~es~~<br>~~ee~~<br>~~es~~|OK<br>~~es ~~<br>~~se~~<br>~~es~~|OK<br> ~~ss~~<br>~~se~~<br>~~es~~|OK<br>~~ss~~<br>~~es~~<br>~~es~~|OK<br>~~ee~~|OK<br>~~ee~~|OK|OK|OK|
||ESC * r m l<br>~~a~~<br>~~a~~<br>~~es~~|Ver. 2.0 or<br>later<br>~~es~~<br>~~es~~|OK<br>~~es ~~<br>~~es~~<br>~~ee~~|OK<br> ~~ee ~~<br>~~es~~<br>~~es~~|OK<br> ~~se~~<br>~~es~~<br>~~es~~|OK<br>~~se ~~<br>~~es~~<br>~~es~~|OK<br> ~~es~~<br>~~es~~<br>~~es~~|OK<br>~~ee~~|OK<br>~~ee~~|OK|OK|OK|
||ESC * r m r<br>~~a~~<br>~~es~~<br>~~Rs~~|Ver. 2.0 or<br>later<br>~~es~~<br>~~ee~~|OK<br>~~es~~<br>~~ee~~<br>~~es~~|OK<br>~~es~~<br>~~es~~<br>~~es~~|OK<br>~~es ~~<br>~~es~~<br>~~es~~|OK<br> ~~es~~<br>~~es~~<br>~~ss~~|OK<br>~~es ~~<br>~~es~~<br>~~ss~~|OK<br> ~~ee~~|OK<br>~~ee~~|OK|OK|OK|
||ESC * r T<br>~~es ~~<br>~~Rs~~<br>~~a~~|Ver. 2.0 or<br>later<br> ~~es ~~<br>~~ee~~<br>~~es~~|OK<br> ~~ee ~~<br>~~es~~<br>~~es~~|OK<br> ~~es~~<br>~~es~~<br>~~ee~~|OK<br>~~es ~~<br>~~es~~<br>~~ss~~|OK<br> ~~es~~<br>~~ss~~<br>~~ss~~|OK<br>~~es~~<br>~~ss~~<br>~~ss~~|OK<br>~~es~~|OK<br>~~ee~~|OK<br>~~ee~~|OK|OK|
||ESC * r K<br>~~Rs ~~<br>~~a~~<br>~~a~~|Ver. 2.0 or<br>later<br> ~~ee ~~<br>~~es~~<br>~~a~~|OK<br> ~~es ~~<br>~~es~~<br>~~a~~|OK<br> ~~es~~<br>~~ee~~<br>~~es~~|OK<br>~~es ~~<br>~~ss~~<br>~~es~~|OK<br> ~~ss~~<br>~~ss~~<br>~~ee~~|OK<br>~~ss~~<br>~~ss~~<br>~~es~~|OK<br>~~es~~<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|OK|OK|
||b n1 n2<br>d1...dk<br>~~a~~<br>~~a~~<br>~~es~~|Ver. 2.0 or<br>later<br>~~es~~<br>~~a~~<br>~~es~~|OK<br>~~es ~~<br>~~a~~<br>~~ee~~|OK<br> ~~ee ~~<br>~~es~~<br>~~es~~|OK<br> ~~ss~~<br>~~es~~<br>~~es~~|OK<br>~~ss~~<br>~~ee~~<br>~~es~~|OK<br>~~ss ~~<br>~~es~~<br>~~es~~|OK<br> ~~es ~~<br>~~ee~~|OK<br> ~~ee~~|OK<br>~~ee~~|OK|OK|
||k n1 n2<br>d1...dk<br>~~a ~~<br>~~es~~<br>~~Rs~~|Ver. 2.0 or<br>later<br> ~~a~~<br>~~es~~<br>~~ee~~|OK<br>~~a~~<br>~~ee~~<br>~~es~~|OK<br>~~es~~<br>~~es~~<br>~~es~~|OK<br>~~es ~~<br>~~es~~<br>~~es~~|OK<br> ~~ee~~<br>~~es~~<br>~~ss~~|OK<br>~~es ~~<br>~~es~~<br>~~ss~~|OK<br> ~~ee~~|OK|OK|OK|OK|
||ESC * r Y<br>~~es ~~<br>~~Rs~~<br>~~a~~|Ver. 2.0 or<br>later<br> ~~es ~~<br>~~ee~~<br>|OK<br> ~~ee ~~<br>~~es~~<br>|OK<br> ~~es~~<br>~~es~~|OK<br>~~es ~~<br>~~es~~<br>~~es~~|OK<br> ~~es~~<br>~~ss~~<br>~~ee~~|OK<br>~~es~~<br>~~ss~~<br>~~es~~|OK<br>~~es~~|OK<br>~~ee~~|OK<br>~~ee~~|OK|OK|
||ESC FF NUL<br>~~Rs ~~<br>~~es~~<br>~~a~~<br>~~es~~|Ver. 2.0 or<br>later<br> ~~ee ~~<br>~~es~~<br>~~a~~<br>|OK<br> ~~es ~~<br>~~es~~<br>~~a~~<br>|OK<br> ~~es~~<br>~~es~~<br>~~es~~<br>|OK<br>~~es ~~<br>~~es~~<br>~~es~~<br>~~es~~<br>|OK<br> ~~ss~~<br>~~es~~<br>~~ee~~<br>~~es~~<br>|OK<br>~~ss~~<br>~~es~~<br>~~es~~<br>~~es~~<br>|OK<br>~~es~~<br>~~es~~<br>~~ee~~|OK<br>~~es~~<br>~~ee~~|OK<br>~~es~~<br>~~ee~~|OK<br>~~es~~|OK<br>~~es~~|
||ESC FF EOT<br>~~a ~~<br>~~es~~<br>~~Rs~~|Ver. 2.0 or<br>later<br> ~~a~~<br>~~es~~<br>|OK<br>~~a~~<br>~~ee~~<br>|OK<br>~~es~~<br>~~**es**~~|OK<br>~~es ~~<br>~~es~~<br>~~**es**~~|OK<br> ~~ee ~~<br>~~es~~<br>~~e~~|OK<br> ~~es ~~<br>~~es~~<br>~~e~~~~**s**~~|OK<br> ~~es ~~<br>~~ee~~|OK<br> ~~ee~~|OK<br>~~ee~~|OK|OK|
||ESC * r N<br> <br>~~es~~<br>~~Rs~~<br>~~a~~|NO<br> ~~a~~<br>~~es~~<br>~~ee~~|NO<br>~~a~~<br>~~ee~~<br>~~es~~|NO<br>~~es~~<br>~~**es**~~|NO<br>~~es~~<br>~~**es**~~|NO<br>~~es~~<br>~~e~~<br>~~s~~|NO<br>~~es~~<br>~~e~~~~**s**~~<br>~~s~~|Ver. 1.3 or<br>later<br>~~ee~~|OK|OK|OK|OK|
||ESC * r V<br> <br>~~es ~~<br>~~Rs~~<br>~~a~~|NO<br> ~~a~~<br> ~~es~~<br>~~ee~~|NO<br>~~a~~<br>~~ee~~<br>~~es~~|NO<br>~~es~~<br>~~**es**~~|NO<br>~~es ~~<br>~~**es**~~|NO<br> ~~es~~<br>~~e~~<br>~~s~~|NO<br>~~es ~~<br>~~e~~~~**s**~~<br>~~s~~|Ver. 1.3 or<br>later<br> ~~ee~~|OK|OK|OK|OK|
||ESC* re<br> <br>~~Rs ~~<br>~~a~~|NO<br> ~~es ~~<br> ~~ee ~~<br>~~DG~~|NO<br> ~~ee ~~<br> ~~es~~<br>~~DG~~|NO<br> ~~**es**~~|NO<br>~~**es** ~~|NO<br> ~~e~~<br>~~s~~|NO<br>~~e~~~~**s**~~<br>~~s~~|NO|NO|NO|NO|OK|
||ESC * r S<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|OK<br>~~a~~|
||ESC * r s 0<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|NO<br>~~a~~|OK<br>~~a~~|
||ESC* rs1<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|OK<br>~~se~~|
||ESC * r s 2<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|OK<br>~~se~~|
||ESC * r s 3<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|OK<br>~~Po~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-20 

|• Black Mark Related Commands|
|---|
|**Class**<br>**Commands**<br>**Model Name**<br>~~Ce~~|
|**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**|
|Black Mark<br>ESC d<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>NO<br>OK<br>OK<br>OK<br>Related<br>FF<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>NO<br>OK<br>OK<br>OK<br>Commands<br>ESC C<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>NO<br>OK<br>OK<br>OK<br>ESC C 0<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>NO<br>OK<br>OK<br>OK<br>VT<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>NO<br>OK<br>OK<br>OK<br>ESC B<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>NO<br>OK<br>OK<br>OK<br>~~See~~<br>~~Pe~~<br>~~po~~<br>~~Rs~~~~**GG**~~<br>~~CG~~<br>~~Rs~~<br>~~CG~~<br>~~Pe~~|
|• 2-Color PrintingRelated Commands|
|**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**<br>2-Color<br>ESC RS c<br>Ver. 4.0<br>Ver. 2.0<br>Ver. 2.0<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>~~OOOOOO~~|
|Printing<br>or later<br>or later<br>or later<br>Related<br>Commands<br>ESC RS C<br>Spec. A<br>Ver. 4.0<br>or later<br>Spec. A<br>Ver. 2.0<br>or later<br>Spec. A<br>Ver. 2.0<br>or later<br>Spec. B<br>Spec. B<br>Spec. B<br>Spec. C<br>Spec. A<br>Spec. C<br>Spec. C<br>Spec. C<br>ESC<br>4<br>(Not<br>recommended)<br>Ver. 4.0<br>or later<br>Ver. 2.0<br>or later<br>Ver. 2.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>OK<br>NO<br>ESC<br>5<br>(Not<br>recommended)<br>Ver. 4.0<br>or later<br>Ver. 2.0<br>or later<br>Ver. 2.0<br>or later<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>OK<br>NO<br>ESC FS q<br>Ver. 4.0<br>or later<br>Ver. 2.0<br>or later<br>Ver. 2.0<br>or later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>ESC FS p<br>Ver. 4.0<br>or later<br>Ver. 2.0<br>or later<br>Ver. 2.0<br>or later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>~~ft~~<br>~~|~~<br>~~a i eeee ee~~<br>~~ee~~<br>~~es es~~<br>~~es~~<br>~~es~~<br>~~es ssGe~~<br>~~es es~~<br>~~es es ssQsOs~~<br>~~ieese~~<br>~~ee~~|



|• Presenter Related Commands|
|---|
|**Class**<br>**Commands**<br>**Model Name**|
|**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**|
|Presenter<br>ESC SYN0<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>Related<br>ESC SYN 1<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>Commands<br>ESC SYN 3<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>ESC SYN 4<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>ECS GS SUB DC1<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>ECS GS SUB DC2<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>ECS GS SUB DC3<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>~~a~~<br>~~GC~~<br>~~GG~~<br>~~CC~~<br>~~Po~~<br>~~RsGG~~<br>~~**C**C~~<br>~~RseG~~<br>~~CO GG~~<br>~~(O~~<br>~~Po~~<br>=~~=====>=====~~<br>~~Po~~|
|• Mark Commands|
|**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**<br>Mark<br>Commands<br>ESC GS * 0<br>NO<br>Ver. 4.0<br>or later<br>NO<br>Ver. 3.0<br>or later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>ESC GS * 1<br>NO<br>Ver. 4.0<br>or later<br>NO<br>Ver. 3.0<br>or later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>ESC GS * 2<br>NO<br>Ver. 4.0<br>or later<br>NO<br>Ver. 3.0<br>or later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>ESC GS * W<br>NO<br>Ver. 4.0<br>or later<br>NO<br>Ver. 3.0<br>or later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>ESC GS * C<br>NO<br>Ver. 4.0<br>or later<br>NO<br>Ver. 3.0<br>or later<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>OK<br>~~ce~~<br>~~vyeauyaeauaea_nasa——aaaes~~<br>~~i ee es es ee~~<br>~~a i eeee ee~~<br>~~ee~~<br>~~es es~~<br>~~es~~<br>~~es~~<br>~~es ssGe~~<br>~~es es~~<br>~~es es ssQsOs~~<br>~~ieese~~<br>~~ee~~|



• Auto Logo Commands 

|**Class**<br>~~OO~~|**Commands**<br>~~OO~~<br>~~i~~|**Model Name**<br>~~OOOOOO~~|**Model Name**<br>~~OOOOOO~~|**Model Name**<br>~~OOOOOO~~|**Model Name**<br>~~OOOOOO~~|**Model Name**<br>~~OOOOOO~~|**Model Name**<br>~~OOOOOO~~|**Model Name**<br>~~OOOOOO~~|**Model Name**<br>~~OOOOOO~~|**Model Name**<br>~~OOOOOO~~|**Model Name**<br>~~OOOOOO~~|**Model Name**<br>~~OOOOOO~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~OO~~<br>~~i~~|**TSP700**<br>~~OO~~<br>~~ee~~|**TSP600**<br>~~OO~~<br>~~es~~|**TUP900**<br>~~OO~~<br>~~es~~|**TSP1000**<br>~~OO~~<br>~~ee~~|**TSP828L**<br>~~OO~~|**TSP700II**<br>~~OO~~|**TSP650**<br>~~OOOO~~|**TUP500**<br>~~OOOO~~|**TSP800II**<br>~~OOOO~~|**FVP10**<br>~~OOOO~~|
|Auto Logo<br>Commands ESC GS / C<br>~~OO~~|ESC GS / W<br>~~OO~~<br>~~i~~<br>~~a~~|NO<br>~~OO~~<br>~~i~~<br>~~i~~|Ver. 4.0<br>or later<br>~~OO~~<br>~~ee~~<br>~~ee~~|NO<br>~~OO~~<br>~~es~~<br>~~ee~~|NO<br>~~OO~~<br>~~es~~<br>~~ee~~|NO<br>~~OO~~<br>~~ee~~<br>~~ee~~|NO<br>~~OO~~<br>~~ee~~|OK<br>~~OO~~<br>~~ee~~|OK<br>~~OOOO~~<br>~~ee~~|NO<br>~~OOOO~~<br>~~ee~~|OK<br>~~OOOO~~|OK<br>~~OOOO~~|
||Commands ESC GS / C<br>~~i~~<br>~~a~~<br>~~es~~|NO<br>~~i ~~<br>~~i~~<br>~~es~~|Ver. 4.0<br>or later<br> ~~ee ~~<br>~~ee~~<br>~~es~~|NO<br> ~~es ~~<br>~~ee~~<br>~~es~~|NO<br> ~~es ~~<br>~~ee~~<br>~~es~~|NO<br> ~~ee~~<br>~~ee~~<br>~~ss~~|NO<br>~~ee~~<br>~~ss~~|OK<br>~~ee~~<br>~~Ge~~|OK<br>~~ee~~|NO<br>~~ee~~|OK|OK|
||ESC GS / 1<br>~~a ~~<br>~~es~~<br>~~es~~|NO<br> ~~i ~~<br>~~es~~<br>~~es~~|Ver. 4.0<br>or later<br> ~~ee~~<br>~~es~~<br>~~es~~|NO<br>~~ee~~<br>~~es~~<br>~~es~~|NO<br>~~ee ~~<br>~~es~~<br>~~ss~~|NO<br> ~~ee~~<br>~~ss~~<br>~~ss~~|NO<br>~~ee~~<br>~~ss~~<br>~~Qs~~|OK<br>~~ee~~<br>~~Ge~~<br>~~Os~~|OK<br>~~ee~~<br>~~Os~~|NO<br>~~ee~~|OK|OK|
||ESC GS / 2<br>~~es ~~<br>~~es~~<br>~~i~~|NO<br> ~~es~~<br>~~es~~<br>~~i~~|Ver. 4.0<br>or later<br>~~es~~<br>~~es~~<br>~~ee~~|NO<br>~~es~~<br>~~es~~<br>~~es~~|NO<br>~~es ~~<br>~~ss~~<br>~~es~~|NO<br> ~~ss~~<br>~~ss~~<br>~~ee~~|NO<br>~~ss~~<br>~~Qs~~|OK<br>~~Ge~~<br>~~Os~~|OK<br>~~Os~~|NO|OK|OK|
||ESC GS / 3<br>~~es ~~<br>~~i~~<br>~~a~~|NO<br> ~~es~~<br>~~i~~<br>~~i~~|Ver. 4.0<br>or later<br>~~es ~~<br>~~ee~~<br>~~ee~~|NO<br> ~~es ~~<br>~~es~~<br>~~ee~~|NO<br> ~~ss~~<br>~~es~~<br>~~ee~~|NO<br>~~ss~~<br>~~ee~~<br>~~ee~~|NO<br>~~Qs~~<br>~~ee~~|OK<br>~~Os~~<br>~~ee~~|OK<br>~~Os~~<br>~~ee~~|NO<br>~~ee~~|OK|OK|
||ESC GS / 4<br>~~i~~<br>~~a~~<br>~~es~~|NO<br>~~i ~~<br>~~i~~<br>~~es~~|Ver. 4.0<br>or later<br> ~~ee ~~<br>~~ee~~<br>~~es~~|NO<br> ~~es ~~<br>~~ee~~<br>~~es~~|NO<br> ~~es ~~<br>~~ee~~<br>~~es~~|NO<br> ~~ee~~<br>~~ee~~<br>~~ss~~|NO<br>~~ee~~<br>~~ss~~|OK<br>~~ee~~<br>~~Ge~~|OK<br>~~ee~~|NO<br>~~ee~~|OK|OK|
||ESC GS / 5<br>~~a ~~<br>~~es~~<br>~~es~~|NO<br> ~~i ~~<br>~~es~~<br>~~es~~|Ver. 4.0<br>or later<br> ~~ee~~<br>~~es~~<br>~~es~~|NO<br>~~ee~~<br>~~es~~<br>~~ee~~|NO<br>~~ee ~~<br>~~es~~<br>~~ss~~|NO<br> ~~ee~~<br>~~ss~~<br>~~ss~~|NO<br>~~ee~~<br>~~ss~~<br>~~Gs~~|OK<br>~~ee~~<br>~~Ge~~<br>~~sd~~|OK<br>~~ee~~<br>~~sd~~|NO<br>~~ee~~|OK|OK|
||ESC GS / 6<br>~~es ~~<br>~~es~~|NO<br> ~~es~~<br>~~es~~|Ver. 4.0<br>or later<br>~~es~~<br>~~es~~|NO<br>~~es~~<br>~~ee~~|NO<br>~~es ~~<br>~~ss~~|NO<br> ~~ss~~<br>~~ss~~|NO<br>~~ss~~<br>~~Gs~~|OK<br>~~Ge~~<br>~~sd~~|OK<br>~~sd~~|NO|OK|OK|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-21 

• PDF417 Commands 

|**Class**<br>~~eee~~|**Commands**<br>~~eee~~<br>~~Re~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~eee~~<br>~~se~~|**TSP700**<br>~~eee~~<br>~~se~~|**TSP600**<br>~~eee~~<br>~~Qe~~|**TUP900**<br>~~eee~~|**TSP1000**<br>~~eee~~<br>~~Ge~~|**TSP828L**<br>~~eee~~<br>~~Ge~~|**TSP700II**<br>~~eee~~<br>~~Ge~~|**TSP650**<br>~~eee~~<br>~~GO~~|**TUP500**<br>~~eee~~<br>~~GO~~|**TSP800II**<br>~~eee~~<br>~~GO~~|**FVP10**<br>~~eee~~|
|PDF417<br>Command<br>s<br>~~PCE~~|ESC GS x S 0<br>~~Re~~<br>~~Re~~|NO<br>~~se~~<br>|NO<br>~~se~~<br>|NO<br>~~Qe~~<br>~~Ge~~<br>|Ver. 3.1<br>or later<br>|OK<br>~~Ge~~<br>~~Ge~~|OK<br>~~Ge~~<br>~~Ge~~|OK<br>~~Ge~~<br>~~GG~~|NO<br>~~GO~~<br>~~GG~~|OK<br>~~GO~~<br>~~GG~~|OK<br>~~GO~~<br>~~GG~~|OK|
||ESC GS x S 1<br>~~Re ~~<br>~~se~~<br>~~Re~~<br>~~es~~|NO<br> ~~se~~<br>~~se~~<br>~~ee~~<br>|NO<br>~~se~~<br>~~se~~<br>~~ee~~<br>|NO<br>~~Qe~~<br>~~se~~<br>~~Ge~~<br>~~Ge~~<br>|Ver. 3.1<br>or later<br>~~se~~<br><br>|OK<br>~~Ge~~<br>~~se~~<br>~~Ge~~<br>~~ee~~<br>|OK<br>~~Ge~~<br>~~se~~<br>~~Ge~~<br>~~ee~~|OK<br>~~Ge ~~<br>~~se~~<br>~~GG~~<br>~~QO~~|NO<br> ~~GO~~<br>~~se~~<br>~~GG~~<br>~~QO~~|OK<br>~~GO~~<br>~~se~~<br>~~GG~~<br>~~QO~~|OK<br>~~GO~~<br>~~se~~<br>~~GG~~|OK<br>~~se~~|
||ESC GS x S 2<br>~~se~~<br>~~Re~~<br>~~es~~<br>~~Re~~|NO<br>~~se~~<br>~~ee~~<br>~~**e**e~~|NO<br>~~se~~<br>~~ee~~<br>~~**e**e~~|NO<br>~~se~~<br>~~Ge~~<br>~~Ge~~<br>~~**Ge**~~|Ver. 3.1<br>or later<br>~~se~~<br><br>~~G~~~~**eOe**~~|OK<br>~~se~~<br>~~Ge~~<br>~~ee~~<br>~~**eOe**~~|OK<br>~~se~~<br>~~Ge~~<br>~~ee~~|OK<br>~~se~~<br>~~GG~~<br>~~QO~~|NO<br>~~se~~<br>~~GG~~<br>~~QO~~|OK<br>~~se~~<br>~~GG~~<br>~~QO~~|OK<br>~~se~~<br>~~GG~~|OK<br>~~se~~|
||ESC GS x S 3<br>~~Re ~~<br>~~es~~<br>~~Re~~|NO<br> ~~ee~~<br>~~**e**e~~|NO<br>~~ee~~<br>~~**e**e~~|NO<br>~~Ge ~~<br>~~Ge~~<br>~~**Ge**~~|Ver. 3.1<br>or later<br> <br>~~G~~~~**eOe**~~<br>~~O~~|OK<br> ~~Ge~~<br>~~ee~~<br>~~**eOe**~~|OK<br>~~Ge~~<br>~~ee~~<br>~~ee~~|OK<br>~~GG~~<br>~~QO~~<br>~~ee~~|NO<br>~~GG~~<br>~~QO~~<br>~~ee~~|OK<br>~~GG~~<br>~~QO~~|OK<br>~~GG~~|OK|
||ESC GS x D<br> <br>~~es ~~<br>~~Re~~<br>~~PCE~~|NO<br> ~~ee~~<br> ~~**e**e~~<br>~~PCE~~|NO<br>~~ee~~<br>~~**e**e~~<br>|NO<br>~~Ge~~<br>~~**Ge**~~<br>~~Ge~~<br>|Ver. 3.1<br>or later<br>~~G~~~~**eOe**~~<br>~~O~~<br>|OK<br>~~ee~~<br>~~**eOe**~~<br>~~Ge~~|OK<br>~~ee~~<br>~~ee~~<br>~~Ge~~|OK<br>~~QO~~<br>~~ee~~<br>~~GG~~|NO<br>~~QO~~<br>~~ee~~<br>~~GG~~|OK<br>~~QO~~<br>~~GG~~|OK<br>~~GG~~|OK|
||ESC GS x P<br> <br>~~Re~~<br>~~se~~<br>~~PCE~~|NO<br> ~~**e**e ~~<br>~~se~~<br>~~PCE~~|NO<br> ~~**e**e~~<br>~~se~~<br>|NO<br>~~**Ge**~~<br>~~se~~<br>~~Ge~~<br>|Ver. 3.1<br>or later<br>~~G~~~~**eOe**~~<br>~~O~~<br>~~se~~<br>|OK<br>~~**eOe**~~<br>~~se~~<br>~~Ge~~|OK<br>~~ee~~<br>~~se~~<br>~~Ge~~|OK<br>~~ee~~<br>~~se~~<br>~~GG~~|NO<br>~~ee~~<br>~~se~~<br>~~GG~~|OK<br>~~se~~<br>~~GG~~|OK<br>~~se~~<br>~~GG~~|OK<br>~~se~~|
||ESC GS x I<br>~~PCE~~|NO<br>~~PCEEE~~|NO<br>~~EE~~|NO<br>~~Ge~~<br>~~EE~~|Ver. 3.1<br>or later<br>|OK<br>~~Ge~~|OK<br>~~Ge~~|OK<br>~~GG~~|NO<br>~~GG~~|OK<br>~~GG~~|OK<br>~~GG~~|OK|



## • Print Start Trigger Control Commands 

|**Class**|**Commands**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**|**TSP700**|**TSP600**|**TUP900**|**TSP1000**|**TSP828L**|**TSP700II**|**TSP650**|**TUP500**|**TSP800II**|**FVP10**|
|Print Start<br>Trigger<br>Control|ESC GS g 0|NO|NO|NO|NO|Ver. 1.1<br>or later|OK|OK|OK|OK|OK|OK|
||ESC GS g 1|NO|NO|NO|NO|Ver. 1.1<br>or later|OK|OK|OK|OK|OK|OK|



|**Class**<br>~~eee~~|**Commands**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|**Model Name**<br>~~eee~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~eee~~|**TSP700**<br>~~eee~~|**TSP600**<br>~~eee~~|**TUP900**<br>~~eee~~|**TSP1000**<br>~~eee~~|**TSP828L**<br>~~eee~~|**TSP700II**<br>~~eee~~|**TSP650**<br>~~eee~~|**TUP500**<br>~~eee~~|**TSP800II**<br>~~eee~~|**FVP10**<br>~~eee~~|
|QR Code<br>~~Pp~~|ESC GS y S 0<br>~~ee~~<br>~~ee~~|NO<br>~~ee~~<br>~~se~~|NO<br>~~ee~~<br>~~se~~|NO<br>~~se~~|NO<br>~~se~~|Ver. 1.2<br>or later<br>~~Qe~~<br>~~Ge~~|OK<br>~~Qe~~<br>~~QO~~|OK<br>~~OG~~<br>~~QO~~|OK<br>~~OG~~<br>~~QO~~|OK|OK|OK|
||ESC GS y S 1<br>~~ee ~~<br>~~ee~~<br>~~Re~~|NO<br> ~~ee~~<br>~~se~~<br>~~ee~~|NO<br>~~ee~~<br>~~se~~<br>~~ee~~|NO<br>~~se~~<br>~~se~~|NO<br>~~se~~<br>~~se~~|Ver. 1.2<br>or later<br>~~Qe~~<br>~~Ge~~<br>~~Ge~~|OK<br>~~Qe~~<br>~~QO~~<br>~~GG~~|OK<br>~~OG~~<br>~~QO~~<br>~~GG~~|OK<br>~~OG~~<br>~~QO~~<br>~~GG~~|OK<br>~~GG~~|OK|OK|
||ESC GS y S 2<br>~~ee ~~<br>~~Re~~<br>~~es~~|NO<br> ~~se~~<br>~~ee~~<br>~~ee~~|NO<br>~~se ~~<br>~~ee~~<br>~~ee~~|NO<br> ~~se~~<br>~~se~~<br>~~es~~|NO<br>~~se~~<br>~~se~~<br>~~es~~|Ver. 1.2<br>or later<br>~~Ge ~~<br>~~Ge~~<br>~~Qe~~|OK<br> ~~QO~~<br>~~GG~~<br>~~Qe~~|OK<br>~~QO~~<br>~~GG~~<br>~~eG~~|OK<br>~~QO~~<br>~~GG~~<br>~~eG~~|OK<br>~~GG~~|OK|OK|
||ESC GS y D 1<br>~~Re ~~<br>~~es~~|NO<br> ~~ee~~<br>~~ee~~|NO<br>~~ee ~~<br>~~ee~~|NO<br> ~~se~~<br>~~es~~|NO<br>~~se~~<br>~~es~~<br>~~se~~|Ver. 1.2<br>or later<br>~~Ge ~~<br>~~Qe~~<br>~~se~~|OK<br> ~~GG~~<br>~~Qe~~<br>~~Ge~~|OK<br>~~GG~~<br>~~eG~~<br>~~OG~~|OK<br>~~GG~~<br>~~eG~~<br>~~OG~~|OK<br>~~GG~~|OK|OK|
||ESC GS y D 2<br>~~es ~~<br>~~ee~~<br>~~Pp~~|NO<br> ~~ee~~<br>~~ee~~|NO<br>~~ee~~<br>~~ee~~|NO<br>~~es~~<br>~~ee~~<br>~~se~~|NO<br>~~es ~~<br>~~ee~~<br>~~se~~<br>~~se~~|Ver. 1.2<br>or later<br> ~~Qe~~<br>~~ee~~<br>~~se~~<br>~~Ge~~|OK<br>~~Qe ~~<br>~~ee~~<br>~~Ge~~<br>~~QQ~~|OK<br> ~~eG~~<br>~~ee~~<br>~~OG~~<br>~~QQ~~|OK<br>~~eG~~<br>~~ee~~<br>~~OG~~<br>~~QQ~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|
||ESC GS y P<br>~~ee~~<br>~~Pp~~<br>~~CUE~~|NO<br>~~ee~~<br>~~CUECE~~|NO<br>~~ee~~<br>~~CE|~~|NO<br>~~ee~~<br>~~se~~<br>~~|~~|NO<br>~~se~~<br>~~ee~~<br>~~se~~<br>~~|~~|Ver. 1.2<br>or later<br>~~se~~<br>~~ee~~<br>~~Ge~~|OK<br>~~Ge~~<br>~~ee~~<br>~~QQ~~|OK<br>~~OG~~<br>~~ee~~<br>~~QQ~~|OK<br>~~OG~~<br>~~ee~~<br>~~QQ~~|OK<br>~~ee~~|OK<br>~~ee~~|OK<br>~~ee~~|
||ESC GS y I<br>~~Pp~~<br>~~CUE~~|NO<br>~~CUECE~~|NO<br>~~CE|~~|NO<br>~~se~~<br>~~|~~|NO<br>~~se~~<br>~~|~~|Ver. 1.2<br>or later<br>~~Ge~~|OK<br>~~QQ~~|OK<br>~~QQ~~|OK<br>~~QQ~~|OK|OK|OK|



## • Reduced Printing Function Commands 

|**Class**|**Commands**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**|**TSP700**|**TSP600**|**TUP900**|**TSP1000**|**TSP828L**|**TSP700II**|**TSP650**|**TUP500**|**TSP800II**|**FVP10**|
|Reduced<br>Printing<br>Function|ESC GS c|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|



• Page Mode Commands **Class Commands Model Name TSP800 TSP700 TSP600 TUP900 TSP1000 TSP828L TSP700II TSP650 TUP500 TSP800II FVP10** Page Mode ~~Po~~ ESC GS P 0 NO NO NO NO NO NO NO NO NO NO YES ~~po~~ ESC GS P 1 NO NO NO NO NO NO NO NO NO NO YES ~~Po~~ ESC GS P 2 NO NO NO NO NO NO NO NO NO NO YES ~~Po~~ ESC GS P 3 NO NO NO NO NO NO NO NO NO NO YES ESC GS P 4 NO NO NO NO NO NO NO NO NO NO YES ~~Po~~ ESC GS P 5 NO NO NO NO NO NO NO NO NO NO YES ~~po~~ ESC GS P 6 NO NO NO NO NO NO NO NO NO NO YES ~~Po~~ ESC GS P 7 NO NO NO NO NO NO NO NO NO NO YES § ~~>S==S==S====Po~~ ESC GS P 8 NO NO NO NO NO NO NO NO NO NO YES ――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-22 

|• Text Search Commands|
|---|
|**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP800II**<br>**FVP10**<br>Text Search<br>ESC GS)B(fn = 48)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>ESC GS)B(fn = 49)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>ESC GS)B(fn = 50)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>ESC GS)B(fn = 64)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>ESC GS)B(fn = 65)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>ESC GS)B(fn = 80)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>ESC GS)B(fn = 81)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>ESC GS)B(fn = 96)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>ESC GS)B(fn = 97)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>• Audio Commands<br>**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP828L**<br>**TSP800II**<br>**FVP10**<br>Audio<br>ESC GS s O<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>ESC GS s P<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>ESC GS s R<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>ESC GS s I<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>ESC GS s U<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>ESC GS s T<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>OK<br>~~Cn~~<br>~~ee~~<br>~~cere eee ces ees eee eee~~<br>~~ees eee eee ee eee~~<br>~~GO~~<br>~~(OO~~<br>~~Po~~<br>~~a~~<br>~~CO~~<br>~~(OO~~<br>~~Po~~<br>~~po~~<br>~~Po~~<br>~~poPo~~<br>~~Po CT~~<br>~~a~~<br>~~eae~~<br>~~w&g~~<br>~~**P**o~~<br>~~o~~<br>~~a~~<br>~~CO~~<br>~~(OO~~<br>~~Po~~<br>~~po~~<br>~~Po~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-23 

## **6.5. W ireless LAN I/F** 

|**Class**<br>~~yyy~~|**Commands**<br>~~yyy~~|**Model Name**<br>~~PT~~<br>~~yyyeee~~|**Model Name**<br>~~PT~~<br>~~yyyeee~~|**Model Name**<br>~~PT~~<br>~~yyyeee~~|**Model Name**<br>~~PT~~<br>~~yyyeee~~|**Model Name**<br>~~PT~~<br>~~yyyeee~~|**Model Name**<br>~~PT~~<br>~~yyyeee~~|**Model Name**<br>~~PT~~<br>~~yyyeee~~|**Model Name**<br>~~PT~~<br>~~yyyeee~~|**Model Name**<br>~~PT~~<br>~~yyyeee~~|**Model Name**<br>~~PT~~<br>~~yyyeee~~|**Model Name**<br>~~PT~~<br>~~yyyeee~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~PT~~<br>~~yyy~~|**TSP700**<br>~~PT~~<br>~~yyy~~|**TSP600**<br>~~PT~~<br>~~yyy~~|**TUP900**<br>~~PT~~<br>~~yyy~~|**TSP1000**<br>~~PT~~<br>~~eee~~|**TSP800L**<br>~~PT~~<br>~~eee~~|**TSP700II**<br>~~PT~~<br>~~eee~~|**TSP650**<br>~~PT~~<br>~~eee~~|**TUP500**<br>~~PT~~<br>~~eee~~|**TSP800II**<br>~~PT~~<br>~~eee~~|**FVP10**<br>~~PT~~|
|Font Style<br>and Character<br>Set<br>~~yyy~~<br>~~—~~<br>~~**P**~~<br>~~**P**~~<br>~~**P**~~|ESC RS F<br>~~yyy~~<br>~~PT~~|NO<br>~~yyy~~<br>~~PT~~|NO<br>~~yyy~~<br>~~PT~~|NO<br>~~yyy~~<br>~~PT~~|NO<br>~~yyy ~~<br>~~PT~~|OK<br> ~~eee~~<br>~~PT~~|NO<br>~~eee~~<br>~~PT~~|OK<br>~~eee~~<br>~~PT~~|NO<br>~~eee~~<br>~~PT~~|NO<br>~~eee~~<br>~~PT~~|NO<br>~~eee~~<br>~~PT~~|NO<br>~~PT~~|
||ESC GS t<br>~~PT~~<br>~~—~~<br>~~|~~|OK<br>~~PT~~<br>~~|~~|OK<br>~~PT~~<br>~~|~~|NO<br>~~PT~~<br>~~|~~|NO<br>~~PT~~<br>~~|~~|OK<br>~~PT~~<br>~~Pe~~|NO<br>~~PT~~<br>~~Pe~~|OK<br>~~PT~~<br>~~Petf~~|NO<br>~~PT~~<br>~~tf~~|NO<br>~~PT~~<br>~~tf~~|NO<br>~~PT~~|NO<br>~~PT~~|
||ESC GS =<br>~~—~~<br>~~|~~<br>~~**P**o~~|Ver. 3.0 or<br>later<br>Spec. A.<br>~~|~~|Spec. A.<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|Spec. A.<br>~~Pe~~|NO<br>~~Pe~~|Spec. B.<br>~~Petf~~|NO<br>~~tf~~|NO<br>~~tf~~|NO|NO|
||ESC R<br>~~—~~<br>~~|~~<br>~~**P**o~~|OK<br>~~|~~|OK<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|OK<br>~~Pe~~|NO<br>~~Pe~~|OK<br>~~Petf~~|NO<br>~~tf~~|NO<br>~~tf~~|NO|NO|
||ESC /<br>~~—~~<br>~~|~~<br>~~**P**o~~|OK<br>~~|~~|OK<br>~~|~~|NO<br>~~|~~|NO<br>~~| ~~|OK<br> ~~Pe~~<br>~~o~~|NO<br>~~Pe~~<br>~~o~~|OK<br>~~Pe tf~~<br>~~o~~|NO<br>~~tf~~<br>~~o~~|NO<br>~~tf~~<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ESC SP<br>~~PO~~<br>~~**P**o~~|OK<br>~~PO~~<br>~~o~~|OK<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|OK<br>~~PO~~|NO<br>~~PO~~|OK<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|
||ESC M<br>~~PO~~<br>~~**P**o~~|OK<br>~~PO~~<br>~~o~~|OK<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|OK<br>~~PO~~|NO<br>~~PO~~|OK<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|
||ESC P<br>~~**P**o~~|OK<br>~~o~~|OK|NO|NO|OK<br>~~o~~|NO<br>~~o~~|OK<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ESC :|OK|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
||ESC<br>p<br>(Not<br>recommended)<br>~~eG~~<br>~~**P**o~~|OK<br>~~eG~~<br>~~o~~|OK<br>~~eG~~|NO<br>~~ee~~|NO<br>~~ee~~|OK<br>~~ee~~|NO<br>~~GG~~|OK<br>~~GG~~|NO<br>~~GG~~|NO<br>~~GG~~|NO<br>~~GG~~|NO<br>~~GG~~|
||ESCg<br>~~eG~~<br>~~**P**o~~|Spec. A.<br>~~eG~~<br>~~o~~|Spec. A.<br>~~eG~~|NO<br>~~ee~~|NO<br>~~ee~~|Spec. B.<br>~~ee~~|NO<br>~~GG~~|Spec. A.<br>~~GG~~|NO<br>~~GG~~|NO<br>~~GG~~|NO<br>~~GG~~|NO<br>~~GG~~|
|Character<br>expansion<br>settings<br>~~**P**~~<br>~~**P**~~|ESCｉ<br>~~**P**o~~<br>~~**P**o~~|OK<br>~~o~~<br>~~o~~|OK|NO|NO|OK<br>~~o~~|NO<br>~~o~~|OK<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ESC W<br>~~**P**o~~|OK<br>~~o~~|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
||ESC h<br>~~**P**o~~|OK<br>~~o~~|OK|NO|NO|OK<br>~~o~~|NO<br>~~o~~|OK<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||SO<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|OK<br>~~PO~~|NO<br>~~PO~~|OK<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|
||DC4<br>~~PO~~<br>~~Po~~|OK<br>~~PO~~<br>~~Po~~|OK<br>~~PO~~<br>~~Po~~|NO<br>~~PO~~<br>~~Po~~|NO<br>~~PO~~<br>~~Po~~|OK<br>~~PO~~<br>~~Po~~|NO<br>~~PO~~<br>~~Po~~|OK<br>~~PO~~<br>~~Po~~|NO<br>~~PO~~<br>~~Po~~|NO<br>~~PO~~<br>~~Po~~|NO<br>~~PO~~<br>~~Po~~|NO<br>~~PO~~<br>~~Po~~|
||ESC SO<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|OK<br>~~Po~~|NO<br>~~Po~~|OK<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|
||ESC DC4|OK|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
|Print mode<br>~~Po~~<br>~~Po~~<br>~~**P**~~<br>~~**P**~~|ESC E|Spec. A.|Spec. A.|NO|NO|Spec. A.|NO|Spec. A.<br>Ver. 2.0 or<br>earlier<br>Spec. B.<br>Ver. 2.0 or<br>later|NO|NO|NO|NO|
||ESC F|Spec. A.|Spec. A.|NO|NO|Spec. A.|NO|Spec. A.<br>Ver. 2.0 or<br>earlier<br>Spec. B.<br>Ver. 2.0 or<br>later|NO|NO|NO|NO|
||ESC -<br>~~Po~~<br>~~Po~~|OK<br>~~Po~~<br>~~Po~~|OK<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|OK<br>~~Po~~|NO<br>~~Po~~|OK<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|
||ESC_<br>~~Po~~<br>~~Po~~|OK<br>~~Po~~|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
||ESC 4<br>~~Po~~<br>~~Po~~<br>~~**P**o~~|OK<br>~~Po~~|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
||ESC 5<br>~~Po~~<br>~~**P**o~~|OK|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
||SＩ<br>~~**P**o~~|OK|OK|NO|NO|OK<br>~~o~~|NO<br>~~o~~|OK<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||DC2<br>~~PT~~<br>~~**P**o~~|OK<br>~~PT~~|OK<br>~~PT~~|NO<br>~~PT~~|NO<br>~~PT~~|OK<br>~~PT~~|NO<br>~~PT~~|OK<br>~~PT~~|NO<br>~~PT~~|NO<br>~~PT~~|NO<br>~~PT~~|NO<br>~~PT~~|
|Line spacing<br>~~**P**~~<br>~~**P**~~<br>~~**P**~~|LF<br>~~**P**o~~|OK|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
||CR<br>~~**P**o~~<br>~~**P**o~~|OK<br>~~o~~|OK|NO|NO|OK<br>~~o~~|NO<br>~~o~~|OK<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ESC a<br>~~**P**o~~|OK<br>~~o~~|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
||ESC z<br>~~**P**o~~|OK<br>~~o~~|OK|NO|NO|OK<br>~~o~~|NO<br>~~o~~|OK<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ESC 0<br>~~PO~~|OK<br>~~PO~~|OK<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|OK<br>~~PO~~|NO<br>~~PO~~|OK<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|NO<br>~~PO~~|
||ESC J<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|OK<br>~~Po~~|NO<br>~~Po~~|OK<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|
||ESC I<br>~~PT~~<br>~~**P**o~~|OK<br>~~PT~~<br>~~o~~|OK<br>~~PT~~|NO<br>~~PT~~|NO<br>~~PT~~|OK<br>~~PT~~|NO<br>~~PT~~|OK<br>~~PT~~|NO<br>~~PT~~|NO<br>~~PT~~|NO<br>~~PT~~|NO<br>~~PT~~|
|Page Control<br>~~**P**~~<br>~~**P**~~|FF<br>~~**P**o~~|OK<br>~~o~~|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
||ESC C<br>~~**P**o~~<br>~~**P**o~~|OK<br>~~o~~|OK|NO|NO|OK<br>~~o~~|NO<br>~~o~~|OK<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ESC C 0<br>~~**P**o~~|OK|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
||VT<br>~~**P**o~~|OK|OK|NO|NO|OK<br>~~o~~|NO<br>~~o~~|OK<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|NO<br>~~o~~|
||ESC B<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|OK<br>~~Po~~|NO<br>~~Po~~|OK<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-24 

|**Class**<br>~~a,~~<br>~~7~~|**Commands**<br>~~a,~~|**Model Name**<br>~~CT~~<br>~~oom~~<br>~~ww&U~~|**Model Name**<br>~~CT~~<br>~~oom~~<br>~~ww&U~~|**Model Name**<br>~~CT~~<br>~~oom~~<br>~~ww&U~~|**Model Name**<br>~~CT~~<br>~~oom~~<br>~~ww&U~~|**Model Name**<br>~~CT~~<br>~~oom~~<br>~~ww&U~~|**Model Name**<br>~~CT~~<br>~~oom~~<br>~~ww&U~~|**Model Name**<br>~~CT~~<br>~~oom~~<br>~~ww&U~~|**Model Name**<br>~~CT~~<br>~~oom~~<br>~~ww&U~~|**Model Name**<br>~~CT~~<br>~~oom~~<br>~~ww&U~~|**Model Name**<br>~~CT~~<br>~~oom~~<br>~~ww&U~~|**Model Name**<br>~~CT~~<br>~~oom~~<br>~~ww&U~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**<br>~~CT~~|**TSP700**<br>~~CT~~|**TSP600**<br>~~CT~~<br>~~oom~~|**TUP900**<br>~~CT~~<br>~~oom~~|**TSP1000**<br>~~CT~~<br>~~oom~~|**TSP800L**<br>~~CT~~<br>~~oom~~|**TSP700II**<br>~~CT~~<br>~~oom~~|**TSP650**<br>~~CT~~<br>~~oom~~|**TUP500**<br>~~CT~~<br>~~oom~~|**TSP800II**<br>~~CT~~|**FVP10**<br>~~CT~~<br>~~ww&U~~|
|Horizontal<br>direction position<br>~~a,~~<br>~~7~~<br>~~Po~~<br>~~Po~~<br>~~Po~~<br>~~ee~~|ESC I<br>~~a,~~<br>~~Re~~|Spec. A.<br>~~CT~~|Spec. A.<br>~~CT~~<br>~~GG~~|NO<br>~~CT~~<br>~~oom~~<br>~~GG~~|NO<br>~~CT~~<br>~~oom~~<br>~~GG~~|Spec. B.<br>~~CT~~<br>~~oom~~<br>~~GGG~~|NO<br>~~CT~~<br>~~oom~~<br>~~GGG~~|Spec. A.<br>~~CT~~<br>~~oom~~<br>~~GGG~~|NO<br>~~CT~~<br>~~oom~~<br>~~(GO~~|NO<br>~~CT~~<br>~~oom~~<br>~~(GO~~|NO<br>~~CT~~<br>~~(GO~~|NO<br>~~CT~~<br>~~ww&U~~|
||ESCQ<br>~~Re~~<br>~~Po~~|Spec. A.<br>~~Po~~|Spec. A.<br>~~GG~~|NO<br>~~oom~~<br>~~GG~~|NO<br>~~oom~~<br>~~GG~~|Spec. B.<br>~~oom~~<br>~~GGG~~|NO<br>~~oom~~<br>~~GGG~~|Spec. A.<br>~~oom~~<br>~~GGG~~|NO<br>~~oom~~<br>~~(GO~~|NO<br>~~oom~~<br>~~(GO~~|NO<br>~~(GO~~|NO<br>~~ww&U~~|
||HT<br>~~Re~~<br>~~Po~~<br>~~Po~~|OK<br>~~Po~~|OK<br>~~GG~~|NO<br>~~oom~~<br>~~GG~~|NO<br>~~oom~~<br>~~GG ~~|OK<br>~~oom~~<br> ~~GGG~~<br>~~GO~~|NO<br>~~oom~~<br>~~GGG~~<br>~~GG~~|OK<br>~~oom~~<br>~~GGG ~~<br>~~GG~~|NO<br>~~oom~~<br> ~~(GO~~<br>~~GG~~|NO<br>~~oom~~<br>~~(GO~~<br>~~GG~~|NO<br>~~(GO~~|NO<br>~~ww&U~~|
||ESC D<br>~~Po~~<br>~~GG~~<br>~~Po~~|OK<br>~~Po~~<br>~~GG~~|OK<br>~~GG~~|NO<br>~~oom~~<br>~~GG~~|NO<br>~~oom~~<br>~~GG~~|OK<br>~~oom~~<br>~~GG~~<br>~~GO~~|NO<br>~~oom~~<br>~~GG~~<br>~~GG~~|OK<br>~~oom~~<br>~~GG~~<br>~~GG~~|NO<br>~~oom~~<br>~~GG~~<br>~~GG~~|NO<br>~~oom~~<br>~~GG~~<br>~~GG~~|NO<br>~~GG~~|NO<br>~~ww&U~~<br>~~GG~~|
||ESC GS A<br>~~Po~~<br>~~Po~~|OK|OK|NO<br>~~oom~~|NO<br>~~oom~~|OK<br>~~oom~~<br>~~GO~~|NO<br>~~oom~~<br>~~GG~~|OK<br>~~oom~~<br>~~GG~~|NO<br>~~oom~~<br>~~GG~~|NO<br>~~oom~~<br>~~GG~~|NO|NO<br>~~ww&U~~|
||ESC GS R<br>~~Po~~<br>~~Po~~<br>~~Ss~~|OK<br>~~Ss~~|OK<br>~~CO~~|NO<br>~~oom~~<br>~~CO~~|NO<br>~~oom~~|OK<br>~~oom~~<br>~~GO ~~<br>~~(OO~~|NO<br>~~oom~~<br> ~~GG~~<br>~~(OO~~|OK<br>~~oom~~<br>~~GG ~~<br>~~(OO~~|NO<br>~~oom~~<br> ~~GG~~<br>~~(GO~~|NO<br>~~oom~~<br>~~GG~~<br>~~(GO~~|NO<br>~~(GO~~|NO<br>~~ww&U~~|
||ESC GS a<br>~~Po~~<br>~~Ss~~<br>~~ee~~|OK<br>~~Ss~~<br>~~ee~~|OK<br>~~CO~~<br>~~ee~~|NO<br>~~oom~~<br>~~CO~~<br>~~ee~~|NO<br>~~oom~~<br>~~ee~~|OK<br>~~oom~~<br>~~(OO~~<br>~~ee~~|NO<br>~~oom~~<br>~~(OO~~<br>~~ee~~|OK<br>~~oom~~<br>~~(OO~~<br>~~ee~~|NO<br>~~oom~~<br>~~(GO~~<br>~~ee~~|NO<br>~~oom~~<br>~~(GO~~<br>~~ee~~|NO<br>~~(GO~~<br>~~ee~~|NO<br>~~ww&U~~<br>~~ee~~|
|Download<br>~~7~~<br>~~ee~~<br>~~Po~~|ESC &<br>~~Ss~~<br>~~ee~~|OK<br>~~Ss~~<br>~~ee~~|OK<br>~~CO~~<br>~~ee~~|NO<br>~~oom~~<br>~~CO~~<br>~~ee~~|NO<br>~~oom~~<br>~~ee~~|OK<br>~~oom~~<br>~~(OO~~<br>~~ee~~|NO<br>~~oom~~<br>~~(OO~~<br>~~ee~~|OK<br>~~oom~~<br>~~(OO~~<br>~~ee~~|NO<br>~~oom~~<br>~~(GO~~<br>~~ee~~|NO<br>~~oom~~<br>~~(GO~~<br>~~ee~~|NO<br>~~(GO~~<br>~~ee~~|NO<br>~~ww&U~~<br>~~ee~~|
||ESC %<br>~~ee~~<br>~~Po~~|OK<br>~~ee~~|OK<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|OK<br>~~ee~~|NO<br>~~ee~~|OK<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|
|Bit Image<br>graphics<br>~~ee~~<br>~~Po~~<br>~~Po~~<br>~~eS~~<br>~~Po~~<br>~~Po~~<br>~~PF~~|ESC K<br>~~ee~~<br>~~Po~~<br>~~Po~~<br>~~eS~~|OK<br>~~ee~~<br>~~eS~~|OK<br>~~ee~~<br>~~eS~~|NO<br>~~ee~~<br>~~eS~~|NO<br>~~ee~~|OK<br>~~ee~~<br>~~SS~~|NO<br>~~ee~~<br>~~SS~~|OK<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|NO<br>~~ee~~|
||ESC L<br>~~Po~~<br>~~Po~~<br>~~eS~~|OK<br>~~eS~~|OK<br>~~eS~~|NO<br>~~eS~~|NO|OK<br>~~SS~~|NO<br>~~SS~~|OK|NO|NO|NO|NO|
||ESC k<br>~~Po~~<br>~~eS~~<br>~~Po~~|OK<br>~~eS~~|OK<br>~~eS~~|NO<br>~~eS~~|NO|OK<br>~~SS~~|NO<br>~~SS~~|OK|NO|NO|NO|NO|
||ESC X<br>~~eS~~<br>~~Po~~<br>~~Po~~<br>~~PFTTTTi~~|OK<br>~~eS~~<br>~~TTTTi~~|OK<br>~~eS~~<br>~~TTTTi~~|NO<br>~~eS~~<br>~~TTTTi~~|NO<br>~~TTTTi~~|OK<br>~~SS~~<br>~~TTTTift~~|NO<br>~~SS~~<br>~~ft Tf{it~~|OK<br>~~Tf{it~~|NO<br>~~Tf{it~~|NO<br>~~Tf{it~~|NO<br>~~Tf{it~~|NO<br>~~Tf{it~~|
|Logo<br>~~Po~~<br>~~Po~~<br>~~PF~~<br>~~pO~~|ESC FSq<br>~~Po~~<br>~~Po~~<br>~~PFTTTTi~~|OK<br>~~TTTTi~~|OK<br>~~TTTTi~~|NO<br>~~TTTTi~~|NO<br>~~TTTTi~~|OK<br>~~TTTTift~~|NO<br>~~ft Tf{it~~|OK<br>~~Tf{it~~|NO<br>~~Tf{it~~|NO<br>~~Tf{it~~|NO<br>~~Tf{it~~|NO<br>~~Tf{it~~|
||ESC FSp<br>~~Po~~<br>~~PFTTTTi~~|OK<br>~~TTTTi~~|OK<br>~~TTTTi~~|NO<br>~~TTTTi~~|NO<br>~~TTTTi~~|OK<br>~~TTTTift~~|NO<br>~~ft Tf{it~~|OK<br>~~Tf{it~~|NO<br>~~Tf{it~~|NO<br>~~Tf{it~~|NO<br>~~Tf{it~~|NO<br>~~Tf{it~~|
||ESC RS L<br>~~PFTTTTi~~|NO<br>~~TTTTi~~|NO<br>~~TTTTi~~|NO<br>~~TTTTi~~|NO<br>~~TTTTi~~|NO<br>~~TTTTift~~|NO<br>~~ft Tf{it~~|Ver. 1.2 or<br>earlier<br>Spec. A.<br>Ver. 1.3 or<br>later<br>Spec. B.<br>~~Tf{it~~|NO<br>~~Tf{it~~|NO<br>~~Tf{it~~|NO<br>~~Tf{it~~|NO<br>~~Tf{it~~|
|Bar Codes<br>~~PF~~<br>~~pO~~<br>~~po~~|ESC b<br>~~PF TTTTi~~<br>~~|~~|Spec. A.<br>~~TTTTi~~<br>~~|~~|Spec. A.<br>~~TTTTi~~<br>~~|~~|NO<br>~~TTTTi~~<br>~~|~~|NO<br>~~TTTTi~~<br>~~|~~|Spec.<br>.<br>B<br>~~TTTTi ft~~<br>~~|~~|NO<br>~~ft Tf{it~~<br>~~|~~|Spec.<br>.<br>B<br>~~Tf{it~~<br>~~f~~|NO<br>~~Tf{it~~<br>~~|~~|NO<br>~~Tf{it~~<br>~~|~~|NO<br>~~Tf{it~~<br>~~|~~|NO<br>~~Tf{it~~<br>~~|~~|
|Cutter Control<br>~~pO~~<br>~~po~~|ESC d<br>~~|~~|OK<br>~~|~~|OK<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|OK<br>~~|~~|NO<br>~~|~~|OK<br>~~f~~|NO<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|
|External device<br>drive<br>~~po~~<br>~~Po~~<br>~~Po~~<br>~~—~~|ESC BEL<br>~~|~~<br>~~Po~~|OK<br>~~|~~|OK<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|OK<br>~~f~~|NO<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|
||BEL<br>~~|~~<br>~~Po~~|OK<br>~~|~~|OK<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~<br>~~GO~~|NO<br>~~|~~<br>~~GG~~|OK<br>~~f~~<br>~~GG~~|NO<br>~~|~~<br>~~GG~~|NO<br>~~|~~<br>~~GG~~|NO<br>~~|~~|NO<br>~~|~~|
||FS<br>~~Po~~<br>~~GG~~|OK<br>~~GG~~|OK<br>~~GG~~|NO<br>~~GG~~|NO<br>~~GG~~|NO<br>~~GG~~<br>~~GO~~|NO<br>~~GG~~<br>~~GG~~|OK<br>~~GG~~<br>~~GG~~|NO<br>~~GG~~<br>~~GG~~|NO<br>~~GG~~<br>~~GG~~|NO<br>~~GG~~|NO<br>~~GG~~|
||SUB<br>~~Po~~<br>~~Po~~|OK<br>~~Po~~|OK<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|NO<br>~~GO ~~<br>~~Po~~|NO<br> ~~GG~~<br>~~Po~~|OK<br>~~GG ~~<br>~~Po~~|NO<br> ~~GG~~<br>~~Po~~|NO<br>~~GG~~<br>~~Po~~|NO<br>~~Po~~|NO<br>~~Po~~|
||EM<br>~~Po~~<br>~~|~~|OK<br>~~|~~|OK<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|OK<br>~~Ff~~|NO<br>~~Ff~~<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|
||ESC GS BEL<br>~~Po~~<br>~~|~~|NO<br>~~|~~|Ver. 5.0 or<br>later<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|OK<br>~~|~~|NO<br>~~|~~|OK<br>~~Ff~~|NO<br>~~Ff~~<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|
||ESC GS EM DC1<br>~~|~~<br>~~|~~<br>~~—~~<br>~~|~~|NO<br>~~|~~<br>|<br>~~|~~|NO<br>~~|~~<br>|<br>~~|~~|NO<br>~~|~~<br>|<br>~~|~~|NO<br>~~|~~<br>|<br>~~|~~|NO<br>~~|~~<br>|<br>~~|~~|NO<br>~~|~~<br>|<br>~~|~~|Ver. 1.3 or<br>later<br>~~Ff~~<br>f<br>~~Jf~~|NO<br>~~Ff~~<br>~~|~~<br>|<br>~~Jf~~<br>~~|~~|NO<br>~~|~~<br>|<br>~~|~~|NO<br>~~|~~<br>|<br>~~|~~|NO<br>~~|~~<br>|<br>~~|~~|
||ESC GS EM DC2<br>~~—~~<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|Ver. 1.3 or<br>later<br>~~Jf~~|NO<br>~~Jf~~<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|
|Print Setting<br>~~—~~<br>~~en~~<br>~~Po~~|ESC RS d<br>~~—~~<br>~~|~~<br>~~en~~|Spec. A.<br>~~|~~<br>~~en~~|Spec. A.<br>~~|~~<br>~~en~~|NO<br>~~|~~<br>~~en~~|NO<br>~~|~~<br>~~en~~|Spec. A.<br>~~|~~<br>~~ee~~|NO<br>~~|~~<br>~~ee~~|Spec. A.<br>~~Jf~~<br>~~ee~~|NO<br>~~Jf~~<br>~~|~~<br>~~ee a~~|NO<br>~~|~~<br>~~a~~|NO<br>~~|~~|NO<br>~~|~~|
||ESC RS r<br>~~en~~<br>~~Po~~|Spec. A.<br>~~en~~|Spec. A.<br>~~en~~|NO<br>~~en~~|NO<br>~~en ~~|Spec. A.<br> ~~ee~~|NO<br>~~ee~~|Spec. A.<br>~~ee~~|NO<br>~~ee a~~|NO<br>~~a~~|NO|NO|
|Status<br>~~Po~~<br>~~Po~~<br>~~Po~~<br>~~Po~~<br>~~Po~~<br>| <br>~~Po~~|ESC RS a<br>~~Po~~<br>~~Po~~<br>~~Po~~<br>~~SS~~|NO<br>~~SS~~|NO<br>~~SS SSS~~|NO<br>~~SSS~~|NO<br>~~SSS~~|NO<br>~~SSS~~|NO<br>~~SSS~~|NO<br>~~SSS~~|NO<br>~~SSS S==~~|NO<br>~~S==~~|NO<br>~~S==~~|NO<br>~~S==~~|
||ESC ACK SOH<br>~~Po~~<br>~~Po~~<br>~~es~~<br>~~Po~~<br>~~SS~~|OK<br>~~es~~<br>~~SS~~|OK<br>~~SS SSS~~|NO<br>~~GG~~<br>~~SSS~~|NO<br>~~GG~~<br>~~SSS~~|OK<br>~~GG~~<br>~~SSS~~|NO<br>~~GG~~<br>~~SSS~~|OK<br>~~GO~~<br>~~SSS~~|NO<br>~~(GO~~<br>~~SSS S==~~|NO<br>~~(GO~~<br>~~S==~~|NO<br>~~(GO~~<br>~~S==~~|NO<br>~~S==~~|
||ENQ<br>~~Po~~<br>~~es~~<br>~~Po~~<br>~~Po~~<br>~~SS~~|OK<br>~~es~~<br>~~SS~~|OK<br>~~SS SSS~~|NO<br>~~GG~~<br>~~SSS~~|NO<br>~~GG~~<br>~~SSS~~|OK<br>~~GG~~<br>~~SSS~~|NO<br>~~GG~~<br>~~SSS~~|OK<br>~~GO~~<br>~~SSS~~|NO<br>~~(GO~~<br>~~SSS S==~~|NO<br>~~(GO~~<br>~~S==~~|NO<br>~~(GO~~<br>~~S==~~|NO<br>~~S==~~|
||EOT<br>~~es~~<br>~~Po~~<br>~~Po~~<br>~~Po~~<br>~~SS~~|OK<br>~~es~~<br>~~SS~~|OK<br>~~SS SSS~~|NO<br>~~GG~~<br>~~SSS~~|NO<br>~~GG~~<br>~~SSS~~|OK<br>~~GG~~<br>~~SSS~~|NO<br>~~GG~~<br>~~SSS~~|OK<br>~~GO~~<br>~~SSS~~|NO<br>~~(GO~~<br>~~SSS S==~~|NO<br>~~(GO~~<br>~~S==~~|NO<br>~~(GO~~<br>~~S==~~|NO<br>~~S==~~|
||ESC ACK CAN<br>~~Po~~<br>~~Po~~<br>~~Po~~<br>~~SS~~|NO<br>~~SS~~|NO<br>~~SS SSS~~|NO<br>~~SSS~~|NO<br>~~SSS~~|NO<br>~~SSS~~|NO<br>~~SSS~~|OK<br>~~SSS~~|NO<br>~~SSS S==~~|NO<br>~~S==~~|NO<br>~~S==~~|NO<br>~~S==~~|
||ETB<br>~~Po~~<br>~~Po~~<br>~~SS~~|Spec. A.<br>~~SS~~|Spec. A.<br>~~SS SSS~~|NO<br>~~SSS~~|NO<br>~~SSS~~|Spec. B.<br>~~SSS~~|NO<br>~~SSS~~|Spec. B.<br>~~SSS~~|NO<br>~~SSS S==~~|NO<br>~~S==~~|NO<br>~~S==~~|NO<br>~~S==~~|
||ESC RS E<br>~~Po~~<br>~~SS~~<br>~~|~~|OK<br>~~SS~~<br>~~|~~|OK<br>~~SS SSS~~<br>~~|~~|NO<br>~~SSS~~<br>~~|~~|NO<br>~~SSS~~<br>~~|~~|OK<br>~~SSS~~<br>~~|~~|NO<br>~~SSS~~<br>~~|~~|OK<br>~~SSS~~<br>~~Ff~~|NO<br>~~SSS S==~~<br>~~Ff~~<br>~~|~~|NO<br>~~S==~~<br>~~|~~|NO<br>~~S==~~<br>~~|~~|NO<br>~~S==~~<br>~~|~~|
||ESC GS ETX<br>~~Po~~<br> ~~SS~~<br>~~|~~<br>~~Po~~|NO<br>~~SS~~<br>~~|~~|NO<br>~~SS SSS~~<br>~~|~~|NO<br>~~SSS~~<br>~~|~~|NO<br>~~SSS~~<br>~~|~~|NO<br>~~SSS ~~<br>~~|~~|NO<br> ~~SSS~~<br>~~|~~|Ver. 2.0 or<br>later<br>~~SSS~~<br>~~Ff~~|NO<br>~~SSS S==~~<br>~~Ff~~<br>~~|~~|NO<br>~~S==~~<br>~~|~~|NO<br>~~S==~~<br>~~|~~|NO<br>~~S==~~<br>~~|~~|
|Chinese Character <br>~~Po~~<br>~~Po~~<br>~~Po~~<br>~~Po~~<br>~~Po~~<br>~~Po~~<br>||ESCp<br>~~|~~<br>~~Po~~<br>~~Po~~|OK<br>~~|~~<br>~~Po~~|OK<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|OK<br>~~|~~|NO<br>~~|~~|OK<br>~~Ff~~|NO<br>~~Ff~~<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|NO<br>~~|~~|
||ESCq<br>~~Po~~<br>~~Po~~<br>~~Po~~|OK<br>~~Po~~|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
||ESC$ ~~Po~~<br>~~Po~~|OK<br>~~Po~~|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
||ESC s<br>~~Po~~<br>~~Po~~|OK|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
||ESC t<br>~~Po~~<br>~~Po~~|OK|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
||ESC r<br>~~Po~~<br>~~Po~~<br>~~Po~~|Spec.<br>A.|Spec. A.|NO|NO|Spec. B.|NO|Spec. B.|NO|NO|NO|NO|
|Others<br>~~Po~~<br>~~Po~~<br>|<br>~~Po~~|CAN<br>~~Po~~<br>~~Po~~|OK|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
||ESC@<br>~~Po~~<br>~~Ferree~~|OK<br>~~Ferree~~|OK<br>~~Ferree~~|NO<br>~~Ferree~~|NO<br>~~Ferree~~|OK<br>~~Ferree~~|NO<br>~~Ferree ~~|OK<br> ~~eee~~|NO<br>~~eee~~|NO<br>~~eee~~|NO<br>~~eee~~|NO<br>~~eee~~|
||ESC GS # m<br>~~Po~~<br>~~Po~~|Spec. A.<br>Ver. 3.0 or<br>later|Spec. A.|NO|NO|Spec. B.|NO|Spec. B.|NO|NO|NO|NO|
||ESC ?<br>~~Po~~<br>~~Po~~|OK|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|



――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-25 

• Raster related commands 

**==> picture [489 x 509] intentionally omitted <==**

**----- Start of picture text -----**<br>
|||||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Class|Commands|Model Name|
|a|Cn|TSP800|TSP700|TSP600|eee]|TUP900|TSP1000|TSP828L|TSP700II|TSP650|TUP500|TSP800II|FVP10|
|Raster|ESC * r R|Ver. 2.0 or|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
|later|
|es|ESC * r A|Ver. 2.0 or|ee|OK|NO|eG|NO|OK|QQ|NO|OK|NO|GO|NO|NO|NO|
|later|
|es|ESC * r B|Ver. 2.0 or|ee|OK|NO|ee|Ge|NO|OK|Qe|NO|GG|OK|NO|NO|NO|NO|
|later|
|se|ESC * r C|Ver. 2.0 or|OK|ee|NO|Ge|NO|OK|Qe|NO|GO|OK|NO|NO|NO|NO|
|later|
|Re|ESC * r D|Ver. 2.0 or|ee|OK|es|NO|se|NO|Ge|OK|NO|OK|NO|NO|NO|NO|
|later|
|ee|ESC * r E|Spec. A.|ee|OK|NO|ee|NO|GeGe|OK|NO|OK|NO|NO|NO|NO|
|Ver. 2.0 or|
|later|
|ESC * r F|Spec. A.|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
|Ver. 2.0 or|
|later|
|ESC * r P|Ver. 2.0 or|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
|later|
|ee|ESC * r Q|Ver. 2.0 or|ee|OK|NO|ee|NO|GeGe|OK|NO|OK|NO|NO|NO|NO|
|later|
|es|ESC * r m l|Ver. 2.0 or|ee|OK|NO|ee|Ge|NO|OK|Qe|NO|GG|OK|NO|NO|NO|NO|
|later|
|se|ESC * r m r|Ver. 2.0 or|OK|ee|NO|Ge|NO|OK|Qe|NO|GO|OK|NO|NO|NO|NO|
|later|
|Re|ESC * r T|Ver. 2.0 or|ee|OK|es|NO|se|NO|Ge|OK|NO|OK|NO|NO|NO|NO|
|later|
|ee|ESC * r K|Ver. 2.0 or|ee|OK|NO|ee|NO|GeGe|OK|NO|OK|NO|NO|NO|NO|
|later|
|es|b n1 n2 d1...dk|Ver. 2.0 or|ee|OK|NO|ee|Ge|NO|OK|Qe|NO|GG|OK|NO|NO|NO|NO|
|later|
|se|k n1 n2 d1...dk|Ver. 2.0 or|OK|ee|NO|Ge|NO|OK|Qe|NO|GO|OK|NO|NO|NO|NO|
|later|
|Re|ESC * r Y|Ver. 2.0 or|ee|OK|es|NO|se|NO|Ge|OK|NO|OK|NO|NO|NO|NO|
|later|
|ee|ESC FF NUL|Ver. 2.0 or|ee|OK|NO|ee|NO|GeGe|OK|NO|OK|NO|NO|NO|NO|
|later|
|se|ESC FF EOT|Ver. 2.0 or|es|OK|NO|ee|Ge|NO|OK|Ge|NO|GG|OK|NO|NO|NO|NO|
|es|later|
|ESC * r N|NO|NO|NO|NO|NO|NO|Ver. 1.3 or|NO|NO|NO|NO|
|later|
|Re|ESC * r V|ee|NO|NO|es|NO|es|e|NO|Ge|NO|Qe|NO|GG|Ver. 1.3 or|NO|NO|NO|NO|
|later|
|eeI|ESC * r e|NO|ee|NO|NO|ee|NO|GeGe|NO|NO|NO|NO|NO|NO|NO|
|I|ESC * r S|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|
|a|ESC * r s 0|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|
|a|ESC * r s 1|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|
|a|ESC * r s 2|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|
|Po|ESC * r s 3|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|
|• Black mark related commands|
|Class|Commands|fC|Model Name|
|TSP800|TSP700|TSP600|TUP900|TSP1000|TSP800L|TSP700II|TSP650|TUP500|TSP800II|FVP10|
|Black Mark|ESC d|OK|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
|Related|FF|SS|OK|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
|Commands|I|ESC C|OK|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
|I|ESC C 0|OK|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
|I|VT|OK|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|
|2|aI|ESC B|a|OK|OK|NO|NO|OK|NO|OK|NO|NO|NO|NO|

**----- End of picture text -----**<br>


**==> picture [489 x 139] intentionally omitted <==**

**----- Start of picture text -----**<br>
||||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|• 2-Color Printing Related Commands|
|Class|Commands|Model Name|
|a|Cn|TSP800|TSP700|TSP600|eee|TUP900|TSP1000|TSP800L|TSP700II|TSP650|TUP500|TSP800II|/g3>|FVP10|
|2-Color Printing|ESC RS c|Ver. 4.0 or|Ver. 2.0 or|NO|NO|OK|NO|OK|NO|NO|NO|NO|
|Related|ee|ESC RS C|Spec. A.later|Spec. A.later|ee|NO|NO|ee|Spec. B.|GQ|NO|Spec. C.|NO|NO|NO|NO|
|Ver. 4.0 or|Ver. 2.0 or|
|later|later|
|Commands|ESC|4|(Not|Ver. 4.0 or|Ver. 2.0 or|NO|NO|x|NO|OK|NO|NO|NO|NO|
|recommended)|later|later|
|ee|ESC|5|(Not|Ver. 4.0 or|Ver. 2.0 or|ee|NO|NO|ee|x|Ge|NO|OK|Ge|NO|NO|NO|NO|
|eee|recommended)|later|later|
|ESC FS q|Ver. 4.0 or|Ver. 2.0 or|NO|NO|OK|NO|OK|NO|NO|NO|NO|
|later|later|
|es|ESC FS p|Ver. 4.0 or|Ver. 2.0 or|NO|NO|ee|OK|GQ|NO|OK|NO|NO|NO|NO|
|later|later|
|es|ee|e|eee|e|e|ee|

**----- End of picture text -----**<br>


――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― 

STAR Line Mode Command Specifications 

6-26 

• Presenter Related Commands 

|**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP800L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**<br>Presenter<br>ESC SYN 0<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>Related<br>ESC SYN 1<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>Commands<br>ESC SYN 3<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC SYN 4<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC  GS  SUB  DC1<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC  GS  SUB  DC2<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC  GS  SUB  DC3<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>• Mark Commands<br>**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP800L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**<br>Mark Commands ESC GS * 0<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>NO<br>OK<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>ESC GS * 1<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>NO<br>OK<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>ESC GS * 2<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>NO<br>OK<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>ESC GS * W<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>NO<br>OK<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>ESC GS * C<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>NO<br>OK<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>~~Cn~~<br>~~a~~<br>~~eae~~<br>~~&~~<br>@~~==========——~~<br>~~Po~~<br>~~a~~<br>~~CO~~<br>~~(OO~~<br>~~Po~~<br>~~po~~<br>~~Po~~<br>~~Po Cn~~<br>~~a~~<br>~~eeeellOE—E~~<br>~~es ee ee ee~~<br>~~ee ee eeGe Ge~~<br>~~eee~~<br>~~eeGQ~~<br>~~es e~~~~**e** ee ~~~~**e**e ~~~~**ee**~~<br>~~es e~~<br>~~e~~|
|---|
|• Auto Logo Commands|
|**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP800L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**<br>Auto Logo<br>ESC GS / W<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>Commands<br>ESC GS / C<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>ESC GS / 1<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>ESC GS / 2<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>ESC GS / 3<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>ESC GS / 4<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>ESC GS / 5<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>ESC GS / 6<br>NO<br>Ver. 4.0 or<br>later<br>NO<br>NO<br>NO<br>NO<br>OK<br>NO<br>NO<br>NO<br>NO<br>~~fC~~<br>~~a~~<br>~~eee~~<br>~~/]g&3Z~~<br>~~—~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~[|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~JT~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~fT~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~—~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~fF~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~a ee ee ee~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~JT~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~fT~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~—~~<br>~~{|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~fF~~<br>~~|~~<br>~~|~~<br>~~|~~<br>~~|~~|



## • PDF417 Commands 

**Class Commands Model Name** ~~a EefC~~ **TSP800 TSP700 TSP600 TUP900** ~~eeeeeeeeeiIgE7~~ **TSP1000 TSP800L TSP700II TSP650 TUP500 TSP800II FVP10** PDF417 ~~Rs~~ ESC GS x S 0 ~~OO~~ NO NO NO NO OK NO OK NO NO NO NO Commands ~~PO~~ ESC GS x S 1 NO NO NO NO OK NO OK NO NO NO NO ~~Po~~ ESC GS x S 2 NO NO NO NO OK NO OK NO NO NO NO ~~OOO~~ ESC GS x S 3 NO NO NO NO OK NO OK NO NO NO NO ESC GS x D NO NO NO NO OK NO OK NO NO NO NO ~~OO~~ ESC GS x P NO NO NO NO OK NO OK NO NO NO NO . ~~==========——Po~~ ESC GS x I NO NO NO NO OK NO OK NO ~~OO~~ NO NO NO • Print Start Trigger Control Commands **Class Commands Model Name TSP800 TSP700 TSP600 TUP900 TSP1000 TSP800L TSP700II TSP650 TUP500 TSP800II FVP10** Print Start ESC GS g 0 NO NO NO NO Ver. 1.1 or NO OK NO NO NO NO later Trigger Control ESC GS g 1 NO NO NO NO Ver. 1.1 or NO OK NO NO NO NO later 

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――― STAR Line Mode Command Specifications 6-27 

## • QR Code Commands 

|||~~eee~~<br>~~/g3>~~|~~eee~~<br>~~/g3>~~|~~eee~~<br>~~/g3>~~|~~eee~~<br>~~/g3>~~|~~eee~~<br>~~/g3>~~|~~eee~~<br>~~/g3>~~|~~eee~~<br>~~/g3>~~|~~eee~~<br>~~/g3>~~|~~eee~~<br>~~/g3>~~|~~eee~~<br>~~/g3>~~|~~eee~~<br>~~/g3>~~|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Class**<br>~~a~~|**Commands**<br>~~ee~~|**Model Name**<br>~~Cn~~<br>~~eee~~<br>~~/g3>~~|||||||||||
|||**TSP800**<br>~~Cn~~<br>~~ee~~|**TSP700**<br>~~Cn~~<br>|**TSP600**<br>~~Cn~~<br>~~ee~~<br>|**TUP900**<br>~~Cn~~<br>~~eee~~<br>~~ee~~<br>|**TSP1000**<br>~~Cn~~<br>~~eee~~<br>~~ee~~<br>|**TSP800L**<br>~~Cn~~<br>~~eee~~<br>~~GQ~~<br>|**TSP700II**<br>~~Cn~~<br>~~eee~~<br>~~GQ~~<br>|**TSP650**<br>~~Cn~~<br>~~eee~~<br>~~GQ~~<br>|**TUP500**<br>~~Cn~~<br>~~eee~~<br>~~GQ~~|**TSP800II**<br>~~Cn~~<br>~~/g3>~~|**FVP10**<br>~~Cn~~<br>~~/g3>~~|
|Print QR code|ESC GS y S 0<br>~~ee~~<br>~~ee~~|NO<br>~~ee~~<br>~~ee~~|NO<br>~~ee~~<br>~~ee~~|NO<br>~~ee~~<br>~~ee~~<br>~~ee~~|NO<br>~~eee~~<br>~~ee~~<br>~~ee~~<br>~~ee~~|Ver. 1.2 or<br>later<br>~~eee~~<br>~~ee~~<br>~~ee~~<br>~~ee~~|NO<br>~~eee~~<br>~~ee~~<br>~~GQ~~<br>~~Ge~~|OK<br>~~eee~~<br>~~ee~~<br>~~GQ~~<br>~~Ge~~|NO<br>~~eee~~<br>~~ee~~<br>~~GQ~~<br>~~Ge~~|NO<br>~~eee~~<br>~~ee~~<br>~~GQ~~|NO<br>~~/g3>~~<br>~~ee~~|NO<br>~~/g3>~~<br>~~ee~~|
||ESC GS y S 1<br>~~ee~~<br>~~es~~|NO<br>~~ee~~<br>|NO<br>~~ee~~<br>|NO<br>~~ee~~<br>~~ee~~<br>|NO<br>~~ee~~<br>~~ee~~<br>~~ee~~<br>|Ver. 1.2 or<br>later<br>~~ee~~<br>~~ee~~<br>~~ee~~<br>|NO<br>~~GQ~~<br>~~Ge~~<br>~~GQ~~|OK<br>~~GQ~~<br>~~Ge~~<br>~~GQ~~|NO<br>~~GQ~~<br>~~Ge~~<br>~~GQ~~|NO<br>~~GQ~~|NO|NO|
||ESC GS y S 2<br>~~ee~~<br>~~eee~~<br>~~es~~<br>~~es~~|NO<br>~~ee ~~<br>~~eee~~<br>~~**ee**~~|NO<br> ~~ee~~<br>~~eee~~<br>~~**ee**~~|NO<br>~~ee ~~<br>~~ee ~~<br>~~eee~~<br>~~ee~~|NO<br> ~~ee~~<br> ~~ee~~<br>~~eee~~<br>~~ee~~<br>~~ee~~|Ver. 1.2 or<br>later<br>~~ee~~<br>~~ee~~<br>~~eee~~<br>~~ee~~<br>~~ee~~|NO<br>~~GQ~~<br>~~Ge ~~<br>~~eee~~<br>~~GQ~~|OK<br>~~GQ~~<br> ~~Ge~~<br>~~eee~~<br>~~GQ~~|NO<br>~~GQ~~<br>~~Ge~~<br>~~eee~~<br>~~GQ~~|NO<br>~~GQ~~<br>~~eee~~|NO<br>~~eee~~|NO<br>~~eee~~|
||ESC GS y D 1<br>~~eee~~<br>~~es~~<br>~~es~~|NO<br>~~eee~~<br>~~**ee**~~|NO<br>~~eee~~<br>~~**ee**~~|NO<br>~~eee~~<br>~~ee~~<br>~~ee~~|NO<br>~~eee~~<br>~~ee~~<br>~~ee~~<br>~~ee~~|Ver. 1.2 or<br>later<br>~~eee~~<br>~~ee~~<br>~~ee~~|NO<br>~~eee~~<br>~~GQ~~|OK<br>~~eee~~<br>~~GQ~~|NO<br>~~eee~~<br>~~GQ~~|NO<br>~~eee~~|NO<br>~~eee~~|NO<br>~~eee~~|
||ESC GS y D 2<br>~~es ~~<br>~~es~~<br>~~ee~~|NO<br> ~~**ee**~~<br>~~ee~~|NO<br>~~**ee**~~<br>~~ee~~|NO<br>~~ee~~<br>~~ee~~<br>~~ee~~|NO<br>~~ee~~<br>~~ee~~<br>~~ee~~<br>~~ee~~|Ver. 1.2 or<br>later<br>~~ee~~<br>~~ee~~<br>~~ee~~|NO<br>~~GQ~~<br>~~Ge~~|OK<br>~~GQ~~<br>~~Ge~~|NO<br>~~GQ~~<br>~~Ge~~|NO|NO|NO|
||ESC GS y P<br> <br>~~es~~<br>~~ee~~|NO<br> ~~**ee** ~~<br>~~ee~~|NO<br> ~~**ee** ~~<br>~~ee~~|NO<br> ~~ee ~~<br>~~ee~~<br>~~ee~~<br>~~ee~~|NO<br> ~~ee~~<br>~~ee~~<br>~~ee~~<br>~~ee~~|Ver. 1.2 or<br>later<br>~~ee~~<br>~~ee~~<br>~~ee~~|NO<br>~~Ge~~<br>~~Ge~~|OK<br>~~Ge~~<br>~~GG~~|NO<br>~~Ge~~<br>~~GG~~|NO<br>~~GG~~|NO|NO|
||ESC GS y I<br>~~ee~~<br>~~ee~~|NO<br>~~ee ~~<br>~~ee~~|NO<br> ~~ee~~<br>~~ee~~|NO<br>~~ee ~~<br>~~ee~~<br>~~ee~~|NO<br> ~~ee~~<br>~~ee~~<br>~~ee~~|Ver. 1.2 or<br>later<br>~~ee~~<br>~~ee~~<br>~~ee~~|NO<br>~~Ge ~~<br>~~ee~~<br>~~Ge~~|OK<br> ~~Ge~~<br>~~ee~~<br>~~GG~~|NO<br>~~Ge~~<br>~~ee~~<br>~~GG~~|NO<br>~~ee~~<br>~~GG~~|NO<br>~~ee~~|NO<br>~~ee~~|



## • Page Function Commands 

|**Class**|**Commands**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**|**TSP700**|**TSP600**|**TUP900**|**TSP1000**|**TSP800L**|**TSP700II**|**TSP650**|**TUP500**|**TSP800II**|**FVP10**|
|Page function|ESC GS h 0|NO|NO|NO|NO|NO|NO|OK|NO|NO|NO|NO|
||ESC GS h 1|NO|NO|NO|NO|NO|NO|OK|NO|NO|NO|NO|



## • Reduced Printing Function Commands 

|**Class**|**Commands**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|**Model Name**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**TSP800**|**TSP700**|**TSP600**|**TUP900**|**TSP1000**|**TSP800L**|**TSP700II**|**TSP650**|**TUP500**|**TSP800II**|**FVP10**|
|Reduced Printing<br>Function|ESC GS c|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|NO|



|• Page Mode Commands|
|---|
|**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP800L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**<br>Page Mode<br>ESC GS P 0<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS P 1<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS P 2<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS P 3<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS P 4<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS P 5<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS P 6<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS P 7<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS P 8<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>• Text Search Commands<br>**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP800L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**<br>~~fC~~<br>~~a~~<br>~~mow~~<br>~~Po~~<br>~~§>=S==S===S===~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~Po~~<br>~~po~~<br>~~po~~<br>~~PofC~~<br>~~a~~<br>~~OO eee~~|
|Text Search<br>ESC GS)B(fn = 48)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS)B(fn = 49)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS)B(fn = 50)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS)B(fn = 64)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS)B(fn = 65)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS)B(fn = 80)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS)B(fn = 81)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS)B(fn = 96)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS)B(fn = 97)<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>• Audio Commands<br>**Class**<br>**Commands**<br>**Model Name**<br>**TSP800**<br>**TSP700**<br>**TSP600**<br>**TUP900**<br>**TSP1000**<br>**TSP800L**<br>**TSP700II**<br>**TSP650**<br>**TUP500**<br>**TSP800II**<br>**FVP10**<br>Audio<br>ESC GS s O<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS s P<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS s R<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS s I<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS s U<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>ESC GS s T<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>NO<br>~~GG~~<br>~~OO~~<br>~~GO OO~~<br>~~po~~<br>~~Po~~<br>~~poPo~~<br>~~Po~~<br>~~§>=S==S==S====~~<br>~~Po~~<br>~~Po fC~~<br>~~ee~~<br>~~nn~~<br>~~ee~~<br>~~po~~<br>~~po~~<br>~~po~~<br>~~po~~<br>B~~= =S=S5=S====~~<br>~~Po~~|
|―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――|
|STAR Line Mode Command Specifications<br>6-28|

## **SPECIAL PRODUCTS DIVISION STAR MICRONICS CO., LTD.** 

536 Nanatsushinya, Shimizu-ku, Shizuoka, 424-0066 Japan Tel: (int+81)-54-347-0112 Fax: (int+81)-54-347-0409 

Please access the following URL http://www.star-m.jp/eng/dl/dl02.htm for the latest revision of the manual. 

## **OVERSEAS SUBSIDIARY COMPANIES STAR MICRONICS AMERICA, INC.** 

1150 King Georges Post Road, Edison, NJ 08837-3729 U.S.A. Tel: (int+1)-732-623-5555, Fax: (int+1)-732-623-5590 

## **STAR MICRONICS EUROPE LTD.** 

Star House, Peregrine Business Park, Gomm Road, High Wycombe, Bucks, HP13 7DL, U.K. Tel: (int+44)-1494-471111, Fax: (int+44)-1494-473333 

## **STAR MICRONICS ASIA LTD.** 

Rm. 1901-5, 19/F., Enterprise Square Two, 3 Sheung Yuet Road, Kowloon Bay, Hong Kong Tel : (int+852)-2796-2727,  Fax : (int+852)-2799-9344 

Rev. 1.12  2010.05.10 Printed in Japan, 80874577 
