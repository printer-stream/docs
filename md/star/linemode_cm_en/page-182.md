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
