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
