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
