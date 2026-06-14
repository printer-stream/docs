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
