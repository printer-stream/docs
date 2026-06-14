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
