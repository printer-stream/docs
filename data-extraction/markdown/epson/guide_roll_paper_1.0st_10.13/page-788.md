## C O N F I D E N T I A L

## Program Example 2

PRINT #1, CHR$(&amp;H1D);"L";CHR$(24);CHR$(0); ← Set left margin PRINT #1, CHR$(&amp;H1D);"W";CHR$(104);CHR$(1); ← Print area width (30 columns) PRINT #1, CHR$(&amp;H1D);"(M";CHR$(2);CHR$(0);CHR$(1);CHR$(1); ← &lt;Function 1&gt; PRINT #1, CHR$(&amp;H1D);"(M";CHR$(2);CHR$(0);CHR$(3);CHR$(1); ← &lt;Function 3&gt; PRINT #1, CHR$(&amp;H1D);"L";CHR$(0);CHR$(0); ← Set left margin PRINT #1, CHR$(&amp;H1D);"W";CHR$(120);CHR$(0); ← Print area width (10 columns) PRINT #1, "AAAAAAAAAAAAAAAAAAAA"; CHR$(&amp;HA); ← Execute 20-column printing PRINT #1, CHR$(&amp;H1B);"@"; ← Initialize printer PRINT #1, "BBBBBBBBBBBBBBBBBBBB"; CHR$(&amp;HA); ← Execute 20-column printing

## TM-J2000/J2100

## GS ( M affects the following commands:

| Category of function   | Command                                                                                                |
|------------------------|--------------------------------------------------------------------------------------------------------|
| Line spacing           | ESC 2, ESC 3                                                                                           |
| Print character        | ESC SP, ESC !, ESC -, ESC E, ESC G, ESC M, ESC R, ESC V, ESC r, ESC t, ESC {, GS !, GS ( N, GS B, GS b |
| Panel switch           | ESC c 5                                                                                                |
| Paper sensor           | ESC c 3, ESC c 4                                                                                       |
| Print position         | ESC D, ESC T, ESC a, GS L, GS W                                                                        |
| Bit image              | FS ( L Function 49                                                                                     |
| Status                 | GS j, GS a                                                                                             |
| Bar code               | GS H, GS f, GS h, GS w                                                                                 |
| Macro function         | GS :                                                                                                   |
| Mech control           | ESC U                                                                                                  |
| Kanji control          | FS !, FS &, FS ( A, FS -, FS ., FS C, FS S, FS W                                                       |
| Miscellaneous function | GS ( D, GS ( K, GS P                                                                                   |

AAAAAAAAAA

AAAAAAAAAA

BBBBBBBBBBBBBBBBBBBB

## Print Sample 2
