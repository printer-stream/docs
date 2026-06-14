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
