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
